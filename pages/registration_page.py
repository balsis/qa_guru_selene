import allure
from selene import browser, command, have, be

from data.paths import image_path


class RegistrationPage:
    @allure.step("Открытие страницы регистрации")
    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    @allure.step("Заполнение имени: {value}")
    def fill_firstname(self, value):
        browser.element('#firstName').type(value)

    @allure.step("Заполнение фамилии: {value}")
    def fill_lastname(self, value):
        browser.element("#lastName").type(value)

    @allure.step("Заполнение email: {value}")
    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    @allure.step("Выбор пола: {value}")
    def select_user_gender(self, value):
        browser.element(f'[name="gender"][value={value}]').perform(command.js.click)

    @allure.step("Заполнение номера телефона: {value}")
    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)

    @allure.step("Выбор даты рождения: {day}-{month}-{year}")
    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(f'option[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click().element(f'option[value="{year}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    @allure.step("Выбор хобби: {values}")
    def select_hobby(self, *values):
        for value in values:
            browser.all('[for^="hobbies-checkbox"]').element_by(have.text(value)).click()

    @allure.step("Выбор предметов: {values}")
    def select_subject(self, *values):
        for value in values:
            browser.element('#subjectsInput').type(value).press_enter()

    def upload_picture(self, value):
        browser.element('#uploadPicture').type(image_path(value))

    @allure.step("Заполнение текущего адреса: {value}")
    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    @allure.step("Выбор штата: {value}")
    def select_state(self, value):
        browser.element('#state').click().all('[id^=react-select-3-option]').element_by(have.text(value)).click()

    @allure.step("Выбор города: {value}")
    def select_city(self, value):
        browser.element('#city').click().all('[id^=react-select-4-option]').element_by(have.text(value)).click()

    @allure.step("Нажатие на кнопку отправки")
    def submit_button(self):
        browser.element('#submit').click()

    @allure.step("Проверка данных зарегистрированного пользователя")
    def should_registered_user_with_data(self, *values):
        browser.all("//div[@class='table-responsive']//td[2]").should(
            have.exact_texts(values))

    @allure.step("Проверка, что кнопка закрытия кликабельна")
    def close_button_should_be_clickable(self):
        browser.element('#closeLargeModal').should(be.clickable).click()

    @allure.step("Проверка  сообщения об успешной отправке формы")
    def should_thanks_message(self):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
