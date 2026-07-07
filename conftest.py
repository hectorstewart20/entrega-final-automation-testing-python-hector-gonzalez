import pytest


@pytest.fixture
def posts_data():
    return {
        "title": "Post acerca de la IA y el testing",
        "body": "LA IA revolucionando toda la tecnología que hasta hoy existía",
        "userId": 1
    }


@pytest.fixture
def users_data():
    return {
        "name": "Hector Gonzalez",
        "username": "hgonzalez",
        "email": "gonzalez.hector.83@gmail.com"
    }


@pytest.fixture
def user_id():
    return 1


# def pytest_html_report_title(report):
#     report.title = "API JSONPLACEHOLDER"