from models import Todos, Users
from sqlalchemy import StaticPool, create_engine, text
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from database import Base
from main import app
import pytest
from routers.auth import bcrypt_context, authenticate_user,create_access_token, SECRET_KEY, ALGORITHM
from jose import jwt
from datetime import timedelta

SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {'username': 'Shreyash', 'id': 1, 'user_role': 'admin'}        

client = TestClient(app)

@pytest.fixture
def test_todo():
   
    todo = Todos(
        title="Learn pytest",
        description="Need to learn everyday",
        priority=5,
        complete=False,
        owner_id=1
    )
    db = TestingSessionLocal() 
    db.add(todo)
    db.commit() 
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()

@pytest.fixture
def test_user():
    user = Users(
        username="Shreyash",
        email="shreyasgupta55@gmail.com",
        first_name="Shreyash",
        last_name="Gupta",
        hashed_password=bcrypt_context.hash("pass12"),
        role="admin",
        phone_number="9264922625"
    )
    db=TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()