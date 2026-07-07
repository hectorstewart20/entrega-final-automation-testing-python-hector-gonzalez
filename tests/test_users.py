import pytest_check as check
from pages.users_api_page import UsersApi
from utils.logger import logger

api = UsersApi()


def test_get_one_user():
    logger.info("Solicitud de un usuario")
    user_id = 1

    response = api.get_one_user(user_id)

    check.equal(response.status_code, 200, "ESTATUS INCORRECTO")
    body = response.json()
    check.equal(body["id"], user_id, "ID INCORRECTO")


def test_users():
    logger.info("Obteniendo TODOS los usuarios")
    response = api.get_users()

    check.equal(response.status_code, 200, "STATUS INCORRECTO")
    users = response.json()

    check.is_true(len(users) > 0, "No se obtuvieron usuarios")
    check.is_true(isinstance(users, list), "LA RESPUESTA NO ES UNA LISTA")


def test_create_user(users_data):
    logger.info("CREANDO USUARIO")

    response = api.create_user(
        users_data["name"],
        users_data["username"],
        users_data["email"]
    )

    check.equal(response.status_code, 201, "NO SE CREÓ EL USUARIO")
