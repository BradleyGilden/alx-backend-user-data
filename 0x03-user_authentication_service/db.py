#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email, hashed_password):
        """ saves a user to the database and returns the user object
        """
        obj = User(email=email, hashed_password=hashed_password)
        self._session.add(obj)
        self._session.commit()
        return obj

    def find_user_by(self, **filters):
        """ returns user depending on search filters
        """
        # checking for valid column names
        columns = [col.name for col in User.__table__.columns]
        for key in filters.keys():
            if key not in columns:
                raise InvalidRequestError()

        obj = self.__session.query(User).filter_by(**filters).first()

        # checking if object was returned
        if obj is None:
            raise NoResultFound()
        return obj
