import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.core.config import settings
from app.db.session import get_db
from app.main import app
from app.models.base import Base
from app.models.employee import Department, Position, Location, Employee


@pytest.fixture(scope="session")
def test_db_url():
    return settings.SQLALCHEMY_DATABASE_URI


@pytest.fixture(scope="session")
def engine(test_db_url):
    engine = create_engine(
        test_db_url, connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope="function")
def db_session(engine):
    connection = engine.connect()
    transaction = connection.begin()
    
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = TestingSessionLocal()
    
    session.begin_nested()
    
    yield session
    
    session.rollback()
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture(scope="function")
def test_data(db_session):
    departments = db_session.query(Department).all()
    
    positions = db_session.query(Position).all()
    
    locations = db_session.query(Location).all()
    
    employees = db_session.query(Employee).all()
    
    return {
        "departments": departments,
        "positions": positions,
        "locations": locations,
        "employees": employees
    }
