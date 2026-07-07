from behave import given, when,then
from api_client import get_users, login , create_user


# ==================
#    BACKGROUND
# ==================

@given("que realizo un login valido")
def step_login(contex):

    response = login(
        "eve.holt@reqres.in",
        "cityslicka"
    )

    assert response.status_code == 200

    contex.token = response.json()["token"]

    
# ==================
#    llamado a usuarios
# ==================
@when("consulto la lista de usuarios")
def step_validar_usuarios( context ):
    context.response = get_users()

@then("la lista de usuarios no debe estar vacia")
def step_validar_lista(context):

    body = context.response.json()

    assert "data" in body
    assert len(body["data"]) > 0

# =========================
#    CREACION DE un USUARIO
# =========================

@when("creo un usuario con los siguientes datos")
def step_create_user_table(context):

    row = context.table[0]

    context.response = create_user(
        row["name"],
        row["job"]
    )

@then('el nombre debe ser "{name}"')
def step_validar_name(context, name):

    body = context.response.json()

    assert body["name"] == name 

@then('el trabajo debe ser "{job}"')
def step_validar_job(context, job):

    body = context.response.json()

    assert body["job"] == job 





















# ==============================
#    STATUS GENERICO DE CODIGOS
# ==============================
@then("la respuesta debe ser 200")
def step_status_code_200(context):
    assert context.response.status_code == 200

@then("la respuesta debe ser 201")
def step_status_code_201(context):
    assert context.response.status_code == 201