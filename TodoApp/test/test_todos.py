from routers.auth import get_current_user
from fastapi import status
from routers.todos import get_db
from .utils import *
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

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user



def test_read_all_authenticated(test_todo):
    response = client.get("/", headers={"Authorization": "Bearer valid_token"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{'complete':False,'title':'Learn pytest','description':'Need to learn everyday','priority':5,'id':test_todo.id,'owner_id':1}]


def test_read_one(test_todo):
    response = client.get("/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'complete':False,'title':'Learn pytest','description':'Need to learn everyday','priority':5,'id':test_todo.id,'owner_id':1}

def test_read_one_authenticated_not_foud(test_todo):
    response = client.get("/todo/999")
    assert response.status_code== 404
    assert response.json() == {'detail':'item not found'}

def test_create_todo(test_todo):
    request_data={
        'title':'New Todo',
        'description':'description',
        'priority':5,
        'complete':False
    }

    response = client.post('/todo/', json= request_data)
    assert response.status_code ==201

    db= TestingSessionLocal()
    model=db.query(Todos).filter(Todos.id == 2).first()
    assert model.title == request_data.get('title')
    assert model.priority == request_data.get('priority')
    assert model.description == request_data.get('description')
    assert model.complete == request_data.get('complete')


def test_update_todo(test_todo):
    request_data={
        'title':'The title is changed',
        'description':'Need to learn everyday',
        'priority':5,
        'complete':False,
        'owner_id':1,
        'id':test_todo.id
    }

    response = client.put('/todo/1',json= request_data)
    assert response.status_code == 204

    db= TestingSessionLocal()
    model= db.query(Todos).filter(Todos.id == 1).first()
    assert model.title == 'The title is changed'

def test_update_todo(test_todo):
    request_data={
        'title':'The title is changed',
        'description':'Need to learn everyday',
        'priority':5,
        'complete':False,
        'owner_id':1,
        'id':test_todo.id
    }

    response = client.put('/todo/999',json= request_data)
    assert response.status_code == 404
    assert response.json() == {'detail':'Item not found'}

def test_delete_todo(test_todo):
    response = client.delete('/todo/1')
    assert response.status_code== 204
    db= TestingSessionLocal()
    model= db.query(Todos).filter(Todos.id == 1).first()
    assert model is None

def test_delete_not_found(test_todo):
    response = client.delete('/todo/999')
    assert response.status_code== 404
    assert response.json() == {'detail':'Item not found'}