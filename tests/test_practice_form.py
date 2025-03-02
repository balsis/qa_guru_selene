from helpers.users import user
from pages.registration_page import RegistrationPage


def test_validate_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register_user(user)
    registration_page.assert_form_submission(user)
