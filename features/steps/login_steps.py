# from behave import then, when
# from api_client import login


# @when('realizo login con email "{email}" y password "{password}"')
# def step_login(context, email, password):
#     context.response = login(
#         email,
#         password
#     )

# @then("la respuesta deber ser {status:d}")
# def step_status_code(context, status):
#     assert context.response.status_code == status

# @then("debe existir un token")
# def step_token(context):
#     body = context.response.json()

#     assert "token" in body