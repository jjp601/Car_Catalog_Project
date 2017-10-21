from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    picture = Column(String(250))


class Dealership(Base):
    __tablename__ = 'dealer'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    address = Column(String(50))
    phone = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'address': self.address,
            'phone': self.phone,
        }


class Car(Base):
    __tablename__ = 'car'

    make = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    id = Column(Integer, primary_key=True)
    year = Column(String(4), nullable=False)
    color = Column(String(50))
    mileage = Column(String(50))
    price = Column(String(10))
    image = Column(String(250))
    dealer_id = Column(Integer, ForeignKey('dealer.id'))
    dealer = relationship(Dealership)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'make': self.make,
            'model': self.model,
            'id': self.id,
            'price': self.price,
            'mileage': self.mileage,
            'year': self.year,
            'color': self.color,
            'image': self.image,
        }

engine = create_engine('sqlite:///car_catalog.db')


Base.metadata.create_all(engine)
