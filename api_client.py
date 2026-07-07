import requests

BASE_URL = "https://reqres.in/api"

HEADERS = {
    "x-api-key": "free_user_3DlMlTJEai0AWD9gw6DvADtOxi6"
}

def get_users():
    return requests.get(
        f"{BASE_URL}/users",
        headers=HEADERS
    )


def create_user(name, job):
    data = {
        "name": name,
        "job": job
    }

    return requests.post(
        f"{BASE_URL}/users",
        json=data,
        headers=HEADERS
    )


def update_user(user_id, name, job):
    data = {
        "name": name,
        "job": job
    }

    return requests.put(
        f"{BASE_URL}/users/{user_id}",
        json=data,
        headers=HEADERS
    )


def delete_user(user_id):
    return requests.delete(
        f"{BASE_URL}/users/{user_id}",
        headers=HEADERS
    )


def login(email, password):

    data = {
        "email": email,
        "password": password
    }

    return requests.post(
        f"{BASE_URL}/login",
        json=data,
        headers=HEADERS
    )