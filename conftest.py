from pytest import fixture
from requests import Session

@fixture
def logged_in_session():
    session = Session()

    # Mimic navigating to the landing page
    landing_page_resp = session.get(url="http://127.0.0.1:5000/")

    # Login with a POST
    login_info = {
        "email": "brandon@techstepacademy.com",
        "password": "1234"
    }

    login_resp = session.post(url="http://127.0.0.1:5000/v1/login", data=login_info)

    if login_resp.status_code != 200:
        raise ValueError(f"Expected 200, but received {login_resp.status_code}")

    return session
