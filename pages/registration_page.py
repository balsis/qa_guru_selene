from selene import browser, command, have, be

from helpers.paths import image_path
from helpers.users import User, format_date


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def register_user(self, user: User):
        browser.element('#firstName').type(user.firstname)
        browser.element("#lastName").type(user.lastname)
        browser.element('#userEmail').type(user.email)
        browser.element(f'[name="gender"][value={user.gender}]').perform(command.js.click)
        browser.element('#userNumber').type(user.phone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(f'option[value="{user.date_of_birth.month-1}"]').click()
        browser.element('.react-datepicker__year-select').click().element(f'option[value="{user.date_of_birth.year}"]').click()
        browser.element(f'.react-datepicker__day--0{user.date_of_birth.day}').click()
        for value in user.subjects:
            browser.element('#subjectsInput').type(value).press_enter()
        for hobby in user.hobbies:
            browser.all('[for^="hobbies-checkbox"]').element_by(have.text(hobby)).click()
        browser.element('#uploadPicture').type(image_path(user.picture))
        browser.element('#currentAddress').type(user.current_address)
        browser.element('#state').click().all('[id^=react-select-3-option]').element_by(have.text(user.state)).click()
        browser.element('#city').click().all('[id^=react-select-4-option]').element_by(have.text(user.city)).click()
        browser.element('#submit').click()

    def assert_form_submission(self, user: User):
        expected_date_of_birth = format_date(user.date_of_birth.day, user.date_of_birth.month, user.date_of_birth.year)
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
        browser.all("//div[@class='table-responsive']//td[2]").should(
            have.exact_texts(
                f'{user.firstname} {user.lastname}',
                user.email,
                user.gender,
                user.phone_number,
                expected_date_of_birth,
                ", ".join(user.subjects),
                ", ".join(user.hobbies),
                user.picture,
                user.current_address,
                f'{user.state} {user.city}',
            )
        )
        browser.element('#closeLargeModal').should(be.clickable).click()
