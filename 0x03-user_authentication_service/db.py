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

    def add_user(self, email: str, hashed_password: str) -> User:
        """ saves a user to the database and returns the user object
        """
        obj = User(email=email, hashed_password=hashed_password)
        self._session.add(obj)
        self._session.commit()
        return obj

    def find_user_by(self, **filters) -> User:
        """ returns user depending on search filters
        """
        # checking for valid column names
        columns = [col.name for col in User.__table__.columns]
        for key in filters.keys():
            if key not in columns:
                raise InvalidRequestError()

        obj = self._session.query(User).filter_by(**filters).first()

        # checking if object was returned
        if obj is None:
            raise NoResultFound()
        return obj

    def update_user(self, user_id: int, **fields) -> None:
        """updates a user with key value arguments"""
        column_names = [col.name for col in User.__table__.columns]
        session = self._session
        user = self.find_user_by(id=user_id)
        for k, v in fields.items():
            if k not in column_names:
                raise ValueError
            setattr(user, k, v)
        session.commit()
