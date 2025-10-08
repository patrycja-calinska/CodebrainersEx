import sys
sys.stdout.reconfigure(encoding='utf-8')


from page_objects.forms.practice_form_page import PracticeFormPage
from test_data.practice_form_test_data import PracticeFormTestData

test_data = PracticeFormTestData()
practice_form_page = PracticeFormPage()


def test_submit_form_with_correct_data():
    practice_form_page.open_page()
    practice_form_page.fill_whole_practice_form(test_data)
    # prctaice_form_page.fill_first_name_input(test_data.first_name)
    # practice_form_page.fill_lsat_name_input(test_data.last_name)
    # practice_form_page.fill_user_email_input(test_data.email_address)


    input("Czy zamknac okno?: ")
    practice_form_page.driver.quit()
