import os

from selene import browser, have, be, command


def test_validate_registration_form():
    browser.open("/automation-practice-form")
    browser.element('#firstName').type('Ivan')
    browser.element("#lastName").type('Ivanov')
    browser.element('#userEmail').type('test@test.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('7911111111')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="11"]').click()
    browser.element('.react-datepicker__year-select').click().element("option[value='2011']").click()
    browser.element('.react-datepicker__day--011').click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#subjectsInput').type("Math").press_enter()
    browser.element('#uploadPicture').type(f"{os.path.dirname(os.getcwd())}/resources/avatar.png")
    browser.element('#currentAddress').type("Pushkina street, Kolotushkina house")
    browser.element('#state').perform(command.js.scroll_into_view).click().element('#react-select-3-option-2').click()
    browser.element('#city').click().element('#react-select-4-option-1').click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.all("//div[@class='table-responsive']//td[2]").should(
        have.exact_texts('Ivan Ivanov', 'test@test.com', 'Male', '7911111111', '11 December,2011', 'Maths', 'Sports', 'avatar.png',
                         'Pushkina street, Kolotushkina house', 'Haryana Panipat'))
    browser.element('#closeLargeModal').should(be.clickable).click()
