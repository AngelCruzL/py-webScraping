import smtplib
import time

from selenium import webdriver

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
    driver.get('https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6')
    return driver


def clean_text(text):
    """Extracts only the price percentage from the text"""
    return float(text.split(' ')[0])


def get_price_percentage():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(
        by='xpath', value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span')
    return clean_text(element.text)


def send_email(price_percentage):
    import os
    from email import message

    from dotenv import load_dotenv

    load_dotenv()

    sender = os.environ['OUTLOOK']
    receiver = os.environ['GMAIL']
    password = os.environ['PASSWORD_OUTLOOK']

    message = f"""
    Subject: Stock price alert!

    Hello, this is an automated email from Python.
    Now the stock price is {price_percentage}%.
    You can check it out here: https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6
    """

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()

    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    server.quit()
    print("Email sent! 🚀")


def main():
    price_percentage = get_price_percentage()
    if price_percentage < -0.10:
        send_email(price_percentage)


main()
