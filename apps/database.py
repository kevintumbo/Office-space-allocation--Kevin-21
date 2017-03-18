from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


engine = create_engine('sqlite:///dojo.db')
Base = declarative_base()


class People(Base):

    """ creates people table """

    __tablename__ = 'people'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    role = Column(String(250), nullable=False)
    accomodation = Column(String(1))
    office_allocated = Column(String(250))
    living_space_allocated = Column(String(250))


class Room(Base):

    """ creates Room table """

    __tablename__ = 'room'
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_name = Column(String(250), nullable=False)
    room_type = Column(String(250), nullable=False)
    maximum_occupants = Column(Integer, nullable=False)
    current_occupants = Column(Integer, nullable=False)


Base.metadata.create_all(engine)
