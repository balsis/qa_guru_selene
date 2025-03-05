import allure

from pages.registration_page import RegistrationPage


@allure.feature("Форма регистрации")
@allure.story("Проверка успешного заполнения формы регистрации")
@allure.suite("Форма регистрации")
@allure.title("Заполнение формы регистрации пользователя валидными данными")
def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_firstname("Ivan")
    registration_page.fill_lastname("Ivanov")
    registration_page.fill_email("test@test.com")
    registration_page.select_user_gender("Male")
    registration_page.fill_phone_number("7911111111")
    registration_page.fill_date_of_birth(day = 11, month = 11, year = 2011)
    registration_page.select_hobby("Sports", "Music")
    registration_page.select_subject("Math", "History")
    registration_page.upload_picture("avatar.png")
    registration_page.fill_current_address("Pushkina street, Kolotushkina house")
    registration_page.select_state("Haryana")
    registration_page.select_city("Panipat")
    registration_page.submit_button()
    registration_page.should_thanks_message()
    registration_page.should_registered_user_with_data('Ivan Ivanov', 'test@test.com', 'Male', '7911111111', '11 December,2011', 'Maths, History',
                                                       'Sports, Music',
                                                       'avatar.png',
                                                       'Pushkina street, Kolotushkina house', 'Haryana Panipat')
    registration_page.close_button_should_be_clickable()


