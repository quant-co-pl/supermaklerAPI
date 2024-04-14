from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import yaml

# URL where the form will be submitted
URL = 'https://pkosupermakler.pl/web/'

def login() -> str:
    """
    Logs user in using credentials defined in the config.yml file + SMS.
    Returns session cookie.
    """
    with open('config.yml', 'r') as f:
        config = yaml.safe_load(f)

    with webdriver.Chrome() as driver:
        driver.get(URL)
        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login-email-input')))
            myElem = WebDriverWait(driver,  5).until(EC.presence_of_element_located((By.ID, 'login-password-input')))
            myElem = WebDriverWait(driver,  5).until(EC.presence_of_element_located((By.ID, 'nxl-login-button')))
        except TimeoutException as e:
            print("Loading login page took too much time!")
        driver.find_element("name","email").send_keys(config['credentials']['login'])
        driver.find_element("name","password").send_keys(config['credentials']['password'])
        driver.find_element("name","nxl-login-button").click()
        try:
            # sms verification by user happens here
            myElem = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'toolbar-myWalletValue')))
        except TimeoutException as e:
            print("SMS verification took too much time!")

        cookies=driver.get_cookies()
        for cookie in cookies:
            if cookie['name']=='JSESSIONID':
                return cookie['value']
    return ''
