import os

from selene import browser, command, have, be

from helpers.paths import image_path


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_firstname(self, value):
        browser.element('#firstName').type(value)

    def fill_lastname(self, value):
        browser.element("#lastName").type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def select_user_gender(self, value):
        browser.element(f'[name="gender"][value={value}]').perform(command.js.click)

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(f'option[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click().element(f'option[value="{year}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def select_hobby(self, *values):
        for value in values:
            browser.all('[for^="hobbies-checkbox"]').element_by(have.text(value)).click()

    def select_subject(self, *values):
        for value in values:
            browser.element('#subjectsInput').type(value).press_enter()

    def should_registered_user_with_data(self, *values):
        browser.all("//div[@class='table-responsive']//td[2]").should(
            have.exact_texts(values))

    def close_button_should_be_clickable(self):
        browser.element('#closeLargeModal').should(be.clickable).click()

    def upload_picture(self, value):
        browser.element('#uploadPicture').type(image_path(value))

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element('#state').click().all('[id^=react-select-3-option]').element_by(have.text(value)).click()

    def select_city(self, value):
        browser.element('#city').click().all('[id^=react-select-4-option]').element_by(have.text(value)).click()

    def submit_button(self):
        browser.element('#submit').click()

    def should_thanks_message(self):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))



