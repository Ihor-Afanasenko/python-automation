from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def test_forward_to_service_page(driver):
    service_menu: WebElement = driver.find_element(By.XPATH, "//*[@class='top-navigation__item-link' and normalize-space()='SERVICES']")
    service_menu.click()
    assert driver.current_url == "https://test.io/services"


def test_forward_to_talk_to_qa_experts_page(driver):
    service_menu: WebElement = driver.find_element(By.XPATH, "//*[@class='top-navigation__item-link' and normalize-space()='SERVICES']")
    service_menu.click()
    sleep(2)
    talk_button: WebElement = driver.find_element(By.XPATH, "//*[contains(@class, 'button--teal')]")
    talk_button.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    assert driver.current_url == "https://hi.test.io/contact-us/"


def test_forward_to_talk_to_qa_experts_form_visible(driver):
    service_menu: WebElement = driver.find_element(By.XPATH, "//*[@class='top-navigation__item-link' and normalize-space()='SERVICES']")
    service_menu.click()
    sleep(2)
    talk_button: WebElement = driver.find_element(By.XPATH, "//*[contains(@class, 'button--teal')]")
    talk_button.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    form_title: WebElement = driver.find_element(By.XPATH, "//*[contains(@class,'lp-element') and @id='lp-pom-text-38']//span")
    assert form_title.text == "Learn More About Test IO"


def test_fill_learn_more_about_test_io_form_with_not_valid_email(driver):
    service_menu: WebElement = driver.find_element(By.XPATH, "//*[@class='top-navigation__item-link' and normalize-space()='SERVICES']")
    service_menu.click()
    sleep(2)
    talk_button: WebElement = driver.find_element(By.XPATH, "//*[contains(@class, 'button--teal')]")
    talk_button.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    first_name_field: WebElement = driver.find_element_by_id('first_name')
    first_name_field.send_keys('Test First Name')
    last_name_field: WebElement = driver.find_element_by_id('last_name')
    last_name_field.send_keys('Test Last Name')
    company_field: WebElement = driver.find_element_by_id('company')
    company_field.send_keys('Test Company')
    message_field: WebElement = driver.find_element_by_id('Message')
    message_field.send_keys('Test Message')
    email_field: WebElement = driver.find_element_by_id('email')
    email_field.send_keys('test_test.google.com')
    talk_to_qa_experts_button: WebElement = driver.find_element(By.XPATH, "//*[contains(@class ,'lp-pom-button')]")
    talk_to_qa_experts_button.click()
    form_title: WebElement = driver.find_element(By.XPATH, "//*[contains(@class,'lp-element') and @id='lp-pom-text-38']//span")
    assert form_title.text == "Learn More About Test IO"


def test_fill_learn_more_about_test_io_form_clear_and_return_to_service_page(driver):
    window_first = driver.window_handles[0]
    service_menu: WebElement = driver.find_element(By.XPATH, "//*[@class='top-navigation__item-link' and normalize-space()='SERVICES']")
    service_menu.click()
    sleep(2)
    talk_button: WebElement = driver.find_element(By.XPATH, "//*[contains(@class, 'button--teal')]")
    talk_button.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    first_name_field: WebElement = driver.find_element_by_id('first_name')
    first_name_field.send_keys('Test First Name')
    last_name_field: WebElement = driver.find_element_by_id('last_name')
    last_name_field.send_keys('Test Last Name')
    company_field: WebElement = driver.find_element_by_id('company')
    company_field.send_keys('Test Company')
    message_field: WebElement = driver.find_element_by_id('Message')
    message_field.send_keys('Test Message')
    email_field: WebElement = driver.find_element_by_id('email')
    email_field.send_keys('test_test.@google.com')
    first_name_field.clear()
    last_name_field.clear()
    company_field.clear()
    message_field.clear()
    email_field.clear()
    driver.switch_to.window(window_first)
    assert driver.current_url == "https://test.io/services"


def test_check_terms_and_conditions_link(driver):
    service_menu: WebElement = driver.find_element(By.XPATH, "//*[@class='top-navigation__item-link' and normalize-space()='SERVICES']")
    service_menu.click()
    sleep(2)
    talk_button: WebElement = driver.find_element(By.XPATH, "//*[contains(@class, 'button--teal')]")
    talk_button.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    terms_link: WebElement = driver.find_element(By.XPATH, "//*[contains(@id ,'lp-pom-text')]//a")
    terms_link.click()
    window_policies = driver.window_handles[2]
    driver.switch_to.window(window_policies)
    assert driver.current_url == "https://test.io/policies"


def test_scroll_page_and_check_footer_menu(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    become_tester_menu: WebElement = driver.find_element(By.XPATH, "//*[contains(@class,'footer-menu__item-link') and normalize-space()='Become a Tester']")
    assert become_tester_menu.text == "Become a Tester"


def test_scroll_page_and_forward_to_sign_in_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sign_in_menu: WebElement = driver.find_element(By.XPATH, "//*[contains(@class,'footer-menu__item-link') and normalize-space()='Sign In']")
    sleep(2)
    sign_in_menu.click()
    sign_in_page = driver.window_handles[0]
    driver.switch_to.window(sign_in_page)
    assert driver.current_url == "https://cirro.io/users/sign_in"


def test_forward_to_sign_in_page_fill_sign_in_form_check_alert_message(driver):
    sign_in_button: WebElement = driver.find_element(By.XPATH, "//*[contains(@class, 'button-cta--sign-in')]")
    sign_in_button.click()
    sleep(2)
    sign_in_page = driver.window_handles[1]
    driver.switch_to.window(sign_in_page)
    user_email_field: WebElement = driver.find_element_by_id('user_email')
    user_email_field.send_keys('test_test@gmail.com')
    password_field: WebElement = driver.find_element_by_id('user_password')
    password_field.send_keys('test_password')
    submit_button: WebElement = driver.find_element(By.XPATH, "//*[@type='submit']")
    submit_button.click()
    alert_message: WebElement = driver.find_element(By.XPATH, "//*[@class='alert-message']")
    assert alert_message.text == "Invalid Email or password."


def test_forward_to_sign_in_page_and_reset_password_page(driver):
    sign_in_button: WebElement = driver.find_element(By.XPATH, "//*[contains(@class, 'button-cta--sign-in')]")
    sign_in_button.click()
    sleep(2)
    sign_in_page = driver.window_handles[1]
    driver.switch_to.window(sign_in_page)
    reset_password_link: WebElement = driver.find_element(By.XPATH, "//*[@class='btn-link' and normalize-space()='Reset password']")
    reset_password_link.click()
    reset_header: WebElement = driver.find_element(By.XPATH, "//*[@class='heading-divider-text']/*[@class='text-heading-3']")
    assert reset_header.text == "Reset password"
