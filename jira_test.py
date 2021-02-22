from datetime import datetime

from selenium import webdriver

from config import AppConfig


def create_driver(app_config: AppConfig):
    capabilities = {
        "browserName": app_config.SELENOID_BROWSER
    }

    if app_config.SELENOID_BROWSER_VERSION:
        capabilities = {
            "browserName": app_config.SELENOID_BROWSER,
            "browserVersion": app_config.SELENOID_BROWSER_VERSION
        }
    new_driver = webdriver.Remote(
        command_executor=app_config.SELENOID_HUB_URL,
        desired_capabilities=capabilities)
    return new_driver


def test_jira_load_ticket_seconds(app_config: AppConfig):
    driver = create_driver(app_config)
    if not driver:
        print('driver failed')
        exit(-1)

    ms1 = datetime.now()
    ms2 = None
    ms3 = None

    print('started: ' + str(ms1))

    try:
        driver.get(app_config.JIRA_CHECK_URL)
        ms2 = datetime.now()
        print('submitted: ' + str(ms2))
        driver.find_element_by_id("login-form-username").click()
        driver.find_element_by_id("login-form-username").clear()
        driver.find_element_by_id("login-form-username").send_keys(app_config.JIRA_USERNAME)
        driver.find_element_by_id("login-form-password").click()
        driver.find_element_by_id("login-form-password").clear()
        driver.find_element_by_id("login-form-password").send_keys(app_config.JIRA_PASSWORD)
        driver.find_element_by_id("login-form-password").submit()
        driver.implicitly_wait(30)
        profile = driver.find_element_by_id("view_profile")
        ms3 = datetime.now()
        if not profile:
            print('JIRA id="profile" web element was not found')
    except Exception as e:
        print(e)
    driver.quit()

    if not ms2:
        exit(-1)

    if not ms3:
        exit(-1)

    print("load page 1 " + str((ms2 - ms1).seconds))
    print("login page " + str((ms3 - ms2).seconds))

    return (ms2 - ms1).seconds, (ms3 - ms2).seconds
