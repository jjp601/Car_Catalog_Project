from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Base, Dealership, Car, User

engine = create_engine('sqlite:///car_catalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create a sample user
User1 = User(name="Jay Powell", email="jpowell@example.com",
             picture='static/blank_user.gif')
session.add(User1)
session.commit()

# Cars for Mike's Auto Dealership
dealer1 = Dealership(user_id=1, name="Mike's Auto",
                     address="Columbus NE", phone="555-5555")

session.add(dealer1)
session.commit()

car1 = Car(user_id=1, make="Chevy", model="Camaro", year="2013",
           color="Orange", mileage="50000", price="$15,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer1)

session.add(car1)
session.commit()

car2 = Car(user_id=1, make="Chevy", model="Equinox", year="2014",
           color="silver", mileage="40000", price="$17,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer1)

session.add(car2)
session.commit()

car3 = Car(user_id=1, make="Ford", model="Mustang", year="2015",
           color="blue", mileage="28000", price="$21,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer1)

session.add(car3)
session.commit()

car4 = Car(user_id=1, make="Ford", model="Fusion", year="2012",
           color="red", mileage="68000", price="$11,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer1)

session.add(car4)
session.commit()

car5 = Car(user_id=1, make="Honda", model="Civic", year="2016",
           color="white", mileage="25000", price="$22,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer1)

session.add(car5)
session.commit()

car6 = Car(user_id=1, make="Honda", model="Civic", year="2015",
           color="Black", mileage="29000", price="$18,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer1)

session.add(car5)
session.commit()

# Cars for Ernst Auto Dealership
dealer2 = Dealership(user_id=1, name="Ernst Auto",
                     address="Fremont NE", phone="555-5555")

session.add(dealer2)
session.commit()

car1 = Car(user_id=1, make="Chevy", model="Impala", year="2012",
           color="white", mileage="62000", price="$12,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer2)

session.add(car1)
session.commit()

car2 = Car(user_id=1, make="Chevy", model="Equinox", year="2014",
           color="blue", mileage="34000", price="$13,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer2)

session.add(car2)
session.commit()

car3 = Car(user_id=1, make="Ford", model="Explorer", year="2013",
           color="gray", mileage="44000", price="$11,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer2)

session.add(car3)
session.commit()

car4 = Car(user_id=1, make="Ford", model="F-150", year="2016",
           color="red", mileage="14000", price="$21,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer2)

session.add(car4)
session.commit()

car5 = Car(user_id=1, make="Kia", model="Sorento", year="2015",
           color="white", mileage="24000", price="$18,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer2)

session.add(car5)
session.commit()

car6 = Car(user_id=1, make="Kia", model="Optima", year="2017",
           color="silver", mileage="4000", price="$20000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer2)

session.add(car6)
session.commit()

# Cars for Tracy's Sportsline Dealership
dealer3 = Dealership(user_id=1, name="Tracy Sportsline",
                     address="Norfolk NE", phone="555-5555")

session.add(dealer3)
session.commit()

car1 = Car(user_id=1, make="Chevy", model="Camaro", year="2014",
           color="white", mileage="27000", price="$21,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer3)

session.add(car1)
session.commit()

car2 = Car(user_id=1, make="Chevy", model="Tahoe", year="2015",
           color="blue", mileage="34000", price="$17,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer3)

session.add(car2)
session.commit()

car3 = Car(user_id=1, make="Ford", model="Mustang", year="2015",
           color="black", mileage="34000", price="$29,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer3)

session.add(car3)
session.commit()

car4 = Car(user_id=1, make="Dodge", model="Challenger", year="2016",
           color="gray", mileage="23000", price="$31,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer3)

session.add(car4)
session.commit()

car5 = Car(user_id=1, make="Audi", model="R8", year="2016",
           color="red", mileage="17000", price="$140,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer3)

session.add(car5)
session.commit()

car6 = Car(user_id=1, make="Porsche", model="Boxter", year="2017",
           color="white", mileage="5000", price="$52000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer3)

session.add(car6)
session.commit()

# Cars for Phil Spady's Auto Dealership
dealer4 = Dealership(user_id=1, name="Phil Spady's auto",
                     address="Lincoln NE", phone="555-5555")

session.add(dealer4)
session.commit()

car1 = Car(user_id=1, make="Chevy", model="Camaro", year="2012",
           color="black", mileage="46000", price="$18,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer4)

session.add(car1)
session.commit()

car2 = Car(user_id=1, make="Chevy", model="Cruze", year="2017",
           color="red", mileage="6000", price="$18,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer4)

session.add(car2)
session.commit()

car3 = Car(user_id=1, make="Ford", model="Escape", year="2015",
           color="black", mileage="34000", price="$29,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer4)

session.add(car3)
session.commit()

car4 = Car(user_id=1, make="Ford", model="Fusion", year="2014",
           color="silver", mileage="28000", price="$20,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer4)

session.add(car4)
session.commit()

car5 = Car(user_id=1, make="Dodge", model="Avenger", year="2014",
           color="red", mileage="48000", price="$11,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer4)

session.add(car5)
session.commit()

car6 = Car(user_id=1, make="Lincoln", model="Navigator", year="2017",
           color="white", mileage="4000", price="$61000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer4)

session.add(car6)
session.commit()

# Cars for Clock Tower Auto Dealership
dealer5 = Dealership(user_id=1, name="Clock Tower Auto Mall",
                     address="Omaha NE", phone="555-5555")

session.add(dealer5)
session.commit()

car1 = Car(user_id=1, make="Dodge", model="Charger", year="2015",
           color="red", mileage="15000", price="$21,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer5)

session.add(car1)
session.commit()

car2 = Car(user_id=1, make="Chevy", model="Malibu", year="2015",
           color="silver", mileage="48000", price="$13,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer5)

session.add(car2)
session.commit()

car3 = Car(user_id=1, make="Ford", model="Focus", year="2013",
           color="Gray", mileage="42000", price="$11,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer5)

session.add(car3)
session.commit()

car4 = Car(user_id=1, make="Ford", model="Fusion", year="2017",
           color="silver", mileage="23000", price="$18,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer5)

session.add(car4)
session.commit()

car5 = Car(user_id=1, make="Subaru", model="Legacy", year="2014",
           color="Gray", mileage="33000", price="$17,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer5)

session.add(car5)
session.commit()

car6 = Car(user_id=1, make="Hyundai", model="Sonata", year="2015",
           color="white", mileage="67000", price="$12,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer5)

session.add(car6)
session.commit()

# Cars for Eagles Auto Dealership
dealer6 = Dealership(user_id=1, name="Eagles Auto Sales",
                     address="Bennington NE", phone="555-5555")

session.add(dealer6)
session.commit()

car1 = Car(user_id=1, make="Chevy", model="Equinox", year="2016",
           color="white", mileage="14000", price="17,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer6)

session.add(car1)
session.commit()

car2 = Car(user_id=1, make="Buick", model="Verano", year="2016",
           color="black", mileage="18000", price="$27,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer6)

session.add(car2)
session.commit()

car3 = Car(user_id=1, make="Chevy", model="Malibu", year="2012",
           color="blue", mileage="24000", price="$9,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer6)

session.add(car3)
session.commit()

car4 = Car(user_id=1, make="Honda", model="Civic", year="2014",
           color="silver", mileage="32000", price="$14,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer6)

session.add(car4)
session.commit()

car5 = Car(user_id=1, make="Nissan", model="Altima", year="2016",
           color="red", mileage="3000", price="$11,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer6)

session.add(car5)
session.commit()

car6 = Car(user_id=1, make="Hyundai", model="Sonata", year="2016",
           color="black", mileage="46000", price="$18,000",
           image="http://mercedesdealers.co.in/images/no_car_image.jpg",
           dealer=dealer6)

session.add(car6)
session.commit()


print "Added Dealerships and Cars"
