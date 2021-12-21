from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt
import time

PATH = 'C:/Program Files (x86)/chromedriver.exe'


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(executable_path=PATH, options=options)
    driver.get('https://automated.pythonanywhere.com/login/')
    return driver


def clean_text(text):
    """Extracts only the temperature from the text"""
    return float(text.split(': ')[1])


def write_file(text):
    """Write input text into a file"""
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, 'w') as f:
        f.write(text)


def main():
    driver = get_driver()
    driver.find_element(by='id', value='id_username').send_keys('automated')
    driver.find_element(by='id', value='id_password').send_keys(
        'automatedautomated' + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by='xpath', value='/html/body/nav/div/a').click()

    while True:
        time.sleep(2)
        element = driver.find_element(
            by='xpath', value='/html/body/div[1]/div/h1[2]')
        text = str(clean_text(element.text))
        write_file(text)


print(main())
