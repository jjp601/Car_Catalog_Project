from flask import (Flask, render_template, request, redirect,
                   jsonify, url_for, flash, make_response)
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Dealership, Car, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import requests


app = Flask(__name__)


# Connect to Database and create database session
engine = create_engine('sqlite:///car_catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token

    app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (  # noqa
        app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.8/me"

    token = result.split(',')[0].split(':')[1].replace('"', '')

    url = 'https://graph.facebook.com/v2.8/me?access_token=%s&fields=name,id,email' % token  # noqa
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout
    login_session['access_token'] = token

    # Get the user's picture
    url = 'https://graph.facebook.com/v2.8/me/picture?access_token=%s&redirect=0&height=200&width=200' % token  # noqa
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']

    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '  # noqa

    flash("Now logged in as %s" % login_session['username'])
    return output


@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id, access_token)  # noqa
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# JSON APIs to view Dealership Information
@app.route('/dealer/<int:dealer_id>/cars/JSON')
def dealerCarsJSON(dealer_id):
    dealer = session.query(Dealership).filter_by(id=dealer_id).one()
    cars = session.query(Car).filter_by(
        dealer_id=dealer_id).all()
    return jsonify(Cars=[i.serialize for i in cars])


@app.route('/dealer/<int:dealer_id>/cars/<int:collection_id>/JSON')
def carJSON(dealer_id, collection_id):
    oneCar = session.query(Car).filter_by(id=collection_id).one()
    return jsonify(oneCar=oneCar.serialize)


@app.route('/dealer/JSON')
def dealersJSON():
    dealers = session.query(Dealership).all()
    return jsonify(dealers=[r.serialize for r in dealers])


# Show all dealers
@app.route('/')
@app.route('/dealer/')
def showDealerships():
    dealers = session.query(Dealership).order_by(asc(Dealership.name))
    if 'username' not in login_session:
        return render_template('publicdealers.html', dealers=dealers)
    else:
        return render_template('dealers.html', dealers=dealers)


# Create a new dealer
@app.route('/dealer/new/', methods=['GET', 'POST'])
def newDealership():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newDealership = Dealership(name=request.form['name'],
                                   address=request.form['address'],
                                   phone=request.form['phone'],
                                   user_id=login_session['user_id'])
        session.add(newDealership)
        flash('New Dealership %s Successfully Created!' % newDealership.name)
        session.commit()
        return redirect(url_for('showDealerships'))
    else:
        return render_template('newdealer.html')


# Edit a dealer
@app.route('/dealer/<int:dealer_id>/edit/', methods=['GET', 'POST'])
def editDealership(dealer_id):
    editedDealership = session.query(
        Dealership).filter_by(id=dealer_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedDealership.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to edit this dealership. Please create your own dealership in order to edit.');}</script><body onload='myFunction()''>"  # noqa
    if request.method == 'POST':
        if request.form['name']:
            editedDealership.name = request.form['name']
        if request.form['address']:
            editedDealership.address = request.form['address']
        if request.form['phone']:
            editedDealership.phone = request.form['phone']
            flash('Successfully Edited %s!' % editedDealership.name)
            return redirect(url_for('showDealerships'))
    else:
        return render_template('editdealer.html', dealer=editedDealership)


# Delete a dealer
@app.route('/dealer/<int:dealer_id>/delete/', methods=['GET', 'POST'])
def deleteDealership(dealer_id):
    dealerToDelete = session.query(
        Dealership).filter_by(id=dealer_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if dealerToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to delete this dealership. Please create your own dealer in order to delete.');}</script><body onload='myFunction()''>"  # noqa
    if request.method == 'POST':
        session.delete(dealerToDelete)
        flash('%s Successfully Deleted!' % dealerToDelete.name)
        session.commit()
        return redirect(url_for('showDealerships', dealer_id=dealer_id))
    else:
        return render_template('deletedealer.html', dealer=dealerToDelete)


# Show a dealer catalog
@app.route('/dealer/<int:dealer_id>/')
@app.route('/dealer/<int:dealer_id>/cars/')
def showCars(dealer_id):
    dealer = session.query(Dealership).filter_by(id=dealer_id).one()
    creator = getUserInfo(dealer.user_id)
    cars = session.query(Car).filter_by(
        dealer_id=dealer_id).all()
    if 'username' not in login_session or creator.id != login_session['user_id']:  # noqa
        return render_template('publiccars.html', cars=cars,
                               dealer=dealer, creator=creator)
    else:
        return render_template('cars.html', cars=cars, dealer=dealer,
                               creator=creator)


# Create a new car
@app.route('/dealer/<int:dealer_id>/cars/new/', methods=['GET', 'POST'])
def newCar(dealer_id):
    if 'username' not in login_session:
        return redirect('/login')
    dealer = session.query(Dealership).filter_by(id=dealer_id).one()
    if login_session['user_id'] != dealer.user_id:
        return "<script>function myFunction() {alert('You are not authorized to add cars to this dealership. Please create your own dealership in order to add cars.');}</script><body onload='myFunction()''>"  # noqa
    if request.method == 'POST':
        newCar = Car(make=request.form['make'], model=request.form['model'],
                     price=request.form['price'],
                     mileage=request.form['mileage'],
                     year=request.form['year'],
                     color=request.form['color'], image=request.form['image'],
                     dealer_id=dealer.id, user_id=dealer.user_id)
        session.add(newCar)
        session.commit()
        flash('New %s %s Successfully Added!' % (newCar.make, newCar.model))
        return redirect(url_for('showCars', dealer_id=dealer_id))
    else:
        return render_template('newcar.html', dealer_id=dealer_id)


# Edit a car
@app.route('/dealer/<int:dealer_id>/cars/<int:collection_id>/edit',
           methods=['GET', 'POST'])
def editCar(dealer_id, collection_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedCar = session.query(Car).filter_by(id=collection_id).one()
    dealer = session.query(Dealership).filter_by(id=dealer_id).one()
    if login_session['user_id'] != dealer.user_id:
        return "<script>function myFunction() {alert('You are not authorized to edit cars for this dealership. Please create your own dealership in order to edit cars.');}</script><body onload='myFunction()''>"  # noqa
    if request.method == 'POST':
        if request.form['make']:
            editedCar.make = request.form['make']
        if request.form['model']:
            editedCar.model = request.form['model']
        if request.form['price']:
            editedCar.price = request.form['price']
        if request.form['mileage']:
            editedCar.mileage = request.form['mileage']
        if request.form['year']:
            editedCar.year = request.form['year']
        if request.form['color']:
            editedCar.color = request.form['color']
        if request.form['image']:
            editedCar.image = request.form['image']
        session.add(editedCar)
        session.commit()
        flash('%s %s Successfully Edited!' % (editedCar.make, editedCar.model))
        return redirect(url_for('showCars', dealer_id=dealer_id))
    else:
        return render_template('editcar.html', dealer_id=dealer_id,
                               collection_id=collection_id, car=editedCar)


# Delete a car
@app.route('/dealer/<int:dealer_id>/cars/<int:collection_id>/delete',
           methods=['GET', 'POST'])
def deleteCar(dealer_id, collection_id):
    if 'username' not in login_session:
        return redirect('/login')
    dealer = session.query(Dealership).filter_by(id=dealer_id).one()
    carToDelete = session.query(Car).filter_by(id=collection_id).one()
    if login_session['user_id'] != dealer.user_id:
        return "<script>function myFunction() {alert('You are not authorized to delete cars for this dealership. Please create your own dealership in order to delete cars.');}</script><body onload='myFunction()''>"  # noqa
    if request.method == 'POST':
        session.delete(carToDelete)
        session.commit()
        flash('%s %s Successfully Deleted!' % (carToDelete.make,
              carToDelete.model))
        return redirect(url_for('showCars', dealer_id=dealer_id))
    else:
        return render_template('deletecar.html', car=carToDelete)


# Disconnect from Auth provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showDealerships'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showDealerships'))


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
