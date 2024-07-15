from .utils import * 
from routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db]=override_get_db
app.dependency_overrides[get_current_user]=override_get_current_user

def test_return_user(test_user):
    response= client.get("/users/")
    assert response.status_code ==status.HTTP_200_OK
    assert response.json()['username'] == 'Shreyash'
    assert response.json()['email'] == 'shreyasgupta55@gmail.com'
    assert response.json()['first_name'] == 'Shreyash'
    assert response.json()['last_name'] == 'Gupta'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '9264922625'

def test_change_password(test_user):
    response= client.put("/users/password", json={"password":"pass12","new_password":"test12"})
    assert response.status_code==status.HTTP_204_NO_CONTENT

def test_passqord_error(test_user):
    response = client.put("/users/password", json={"password":"password","new_password":"passss"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail':'Error on password change'}

def test_phone_change(test_user):
    response= client.put("/users/phonenumber/9264922625")
    assert response.status_code == status.HTTP_204_NO_CONTENT

