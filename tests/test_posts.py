import pytest
import pytest_check as check
from pages.posts_api_page import PostsApi
from utils.logger import logger

api = PostsApi()

def test_get_one_post():
    logger. info("Solicitud de un post")
    logger. info(f"")
    posts_id = 2

    res = api.get_one_post(posts_id)

    check.equal(res.status_code, 200, "ESTATUS INCORRECTO")
    body = res.json()   
    check.equal(body["id"], posts_id, "ID INCORRECTO")
def test_posts():
    logger.info("Obteniendo TODOS posts")
    response = api.get_posts()

    check. equal(
        response.status_code, #201
        200,
        "STATUS INCORRECTO"
    )
    posts = response.json()

    check.is_true(
        len(posts) > 0,
        "No se obtuvieron posts"
    )

    check.is_true(
        isinstance(posts, list),
        "LA RESPUESTA NO ES UNA LISTA"
    )



def test_create_post(posts_data):
    logger. info("CREANDO POSTS")

    response = api.create_posts(
        posts_data["title"],
        posts_data["body"],
        posts_data["userId"]
    )
    check. equal(
        response. status_code,
        201,
        "NO SE CREÓ EL POST"
    )
