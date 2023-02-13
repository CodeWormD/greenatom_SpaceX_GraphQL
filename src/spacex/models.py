from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# приходит пустой список с миссиями
# class Missions(Base):

#     __tablename__ = 'missions'

#     id = Column(Integer, primary_key=True, index=True, unique=True)
#     name = Column(String, unique=True, nullable=False)


class Rocket(Base):

    __tablename__ = 'rockets'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True, nullable=False)
    first_flight = Column(String(15), nullable=False)
    description = Column(Text, nullable=False)

    # launches = relationship('Launch', back_populates = 'rocket')


class Launch(Base):

    __tablename__ = 'launches'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    mission_name = Column(String, unique=True, nullable=False)

    # rockets = relationship('Rocket', back_populates = 'launch', lazy='select')