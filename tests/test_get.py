from api_client import get_users , create_user, update_user,delete_user,login

def test_get_users():
    response = get_users()

    assert response.status_code == 200

    data = response.json()

    assert "data" in data
    assert len(data["data"]) > 0

def test_create_user(user_data):
    response = create_user(
        user_data["name"],
        user_data["job"]
    )
    assert response.status_code == 201
    body = response.json()

    assert body["name"] == "Brayann"
    assert body["job"] == "Developer"


def test_update_user():
    response = update_user(
        2,
        "Brayann Updated",
        "QA Automation"
    )

    assert response.status_code == 200
    body = response.json()

    assert body["name"] == "Brayann Updated"
    assert body["job"] == "QA Automation"


def test_delete_user():
    response = delete_user(2)
    assert response.status_code == 204



def test_login():
    response = login(
        "eve.holt@reqres.in",
        "cityslicka"
    )

    assert response.status_code == 200

    body = response.json()

    assert "token" in body



# @pytest.mark.get
# def test_flujo_completo():

    # login_response = login(
    #     "eve.holt@reqres.in",
    #     "cityslicka"
    # )

    # token = login_response.json()["token"]

    # create_response = create_user(
    #     "Brayann",
    #     "Developer"
    # )

    # print(create_response.json()["id"])

    # user_id = create_response.json()["id"]

    # update_response = update_user(
    #     user_id,
    #     "QA Updated",
    #     "Automation"
    # )

    # delete_response = delete_user(user_id)

    # assert delete_response.status_code == 204