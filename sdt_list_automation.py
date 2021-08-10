import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException as ENIE
from selenium.common.exceptions import NoSuchElementException as NSEE

import time

s = requests.session()

chrome_path = 'C:\Program Files (x86)\chromedriver.exe'

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument('--disable-blink-features=AutomationControlled')
options.headless = False
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1280,720")
options.add_argument('--ignore-certificate-errors')
options.add_argument('disable-infobars')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)

time.sleep(2)


def sign_in(drivers):
    print(
        '\n ************************************************************************************************************ \n')

    drivers.get('http://www.smartdataentry.in/Home/Login')

    time.sleep(8)

    print('Sign in started')

    login_text = drivers.find_element_by_id('txtUserName')
    login_text.clear()
    login_text.send_keys('6281465658')

    time.sleep(2)

    password_text = drivers.find_element_by_id('txtPassword')
    password_text.clear()
    password_text.send_keys('s8r@145415')

    time.sleep(2)

    submit_login = drivers.find_element_by_xpath('/html/body/div/div[2]/div/div/div/form/button')
    submit_login.click()

    print('Signed in successfully \n')

    print(
        '\n ************************************************************************************************************ \n')

    time.sleep(5)

    decision_making(drivers)


def sign_out(drivers):
    print(
        '\n ************************************************************************************************************ \n')

    print('trying to sign out')

    time.sleep(5)
    drivers.find_element_by_xpath('//*[@id="divsignout"]/a/div').click()

    print('sign out completed successfully \n')

    print(
        '\n ************************************************************************************************************ \n')

    time.sleep(5)


##################  DECISION MAKING #########################


def decision_making(drivers):
    print(
        '\n ************************************************************************************************************ \n')

    print('Decision making started')

    work_or_exit = input("Do you want to work or exit (type 'yes' to work or 'no' to exit) : ")

    if work_or_exit == 'yes':

        specific_or_range = input(
            "Do you want to work with specific sentences or range of sentences (type '1' for specific or '2' for range of sentences): ")

        if specific_or_range == '1':
            work_page_specific(drivers)
        elif specific_or_range == '2':
            work_page_range(drivers)
        else:
            print("Bye Bye Bad Boy")

    elif work_or_exit == 'no':
        sign_out(drivers)
    else:
        print("Bye Bye Bad Boy")


#################  WORK PAGE SPECIFIC #####################


def work_page_specific(drivers):
    print(
        '\n ************************************************************************************************************ \n')

    print('Specific Sentences Started')

    time.sleep(2)

    drivers.get('http://www.smartdataentry.in/Home/Work')

    time.sleep(5)

    list_of_sentence_numbers = input("Enter the 'specific sentence numbers' continued by 'comma': ")
    list_of_values = list(list_of_sentence_numbers.split(","))

    print(f"Entered 'Specific' Sentences Numbers : {list_of_values} \n")

    for value in list_of_values:

        print(
            '\n ************************************************************************************************************ \n')

        time.sleep(5)

        drivers.get('http://www.smartdataentry.in/Home/Work')

        time.sleep(10)

        sentence_number_added = int(value) + 5000

        # print(f'sentence_number_added : {sentence_number_added}')

        time.sleep(2)

        print(f'Entered number : {value} \n ')

        try:
            drivers.find_element_by_xpath(f"//button[@onclick='ViewSentence({sentence_number_added})']").click()
        except NSEE as exception:

            drivers.get('http://www.smartdataentry.in/Home/Work')

            time.sleep(5)

            drivers.find_element_by_xpath(f"//button[@onclick='ViewSentence({sentence_number_added})']").click()

        time.sleep(5)

        sentence_process(drivers, value)

    decision_making(drivers)


######################## WORK PROCESS ####################

def sentence_process(driver, number):
    print('Sentence Process Started.......')

    time.sleep(5)

    print(f'Sentence-{number} started successfully')

    sentence = driver.find_element_by_id('divSentence')

    sentence_box = driver.find_element_by_id('txtContent')
    sentence_box.clear()

    time.sleep(10)

    sentence_box.send_keys(sentence.text)

    time.sleep(5)

    detect_btn = driver.find_element_by_xpath('//*[@id="divbody"]/div/div[2]/input')
    detect_btn.click()

    time.sleep(3)

    lang_code = driver.find_element_by_id('language_code')
    lang_name = driver.find_element_by_id('language_name')
    probability = driver.find_element_by_id('probability')
    percentage = driver.find_element_by_id('percentage')
    result = driver.find_element_by_id('reliable_result')
    captcha = driver.find_element_by_id('txtCaptchaCode')

    time.sleep(1)

    print(
        f'language-code : {lang_code.text}, language-name :{lang_name.text}, probability : {probability.text}, percentage : {percentage.text}, result : {result.text}, captcha : {captcha.text} \n ')

    time.sleep(3)

    lang_code_box = driver.find_element_by_id('txtLanguageCode')
    lang_code_box.clear()
    time.sleep(2)
    lang_code_box.send_keys(lang_code.text)
    time.sleep(3)

    lang_name_box = driver.find_element_by_id('txtLanguageName')
    lang_name_box.clear()
    time.sleep(2)
    lang_name_box.send_keys(lang_name.text)
    time.sleep(3)

    probability_box = driver.find_element_by_id('txtProbability')
    probability_box.clear()
    time.sleep(2)
    probability_box.send_keys(probability.text)
    time.sleep(3)

    percentage_box = driver.find_element_by_id('txtPercentage')
    percentage_box.clear()
    time.sleep(2)
    percentage_box.send_keys(percentage.text)
    time.sleep(3)

    result_box = driver.find_element_by_id('txtReliableResult')
    result_box.clear()
    time.sleep(2)
    result_box.send_keys(result.text)
    time.sleep(3)

    captcha_box = driver.find_element_by_id('txtCaptcha')
    captcha_box.clear()
    time.sleep(2)
    captcha_box.send_keys(captcha.text)
    time.sleep(3)

    driver.find_element_by_id('txtReliableResult').click()

    time.sleep(2)

    driver.find_element_by_id('txtReliableResult').click()

    # driver.get_screenshot_as_file("screenshot.png")

    time.sleep(5)

    try:
        driver.find_element_by_id('btnSave').click()
    except ENIE as exception:
        driver.find_element_by_id('btnUpdate').click()

    time.sleep(5)

    print('submitted successfully \n')


#################  WORK PAGE RANGE #####################

def work_page_range(drivers):
    print(
        '\n ************************************************************************************************************ \n')

    print('Range of Sentences Started')

    time.sleep(2)

    drivers.get('http://www.smartdataentry.in/Home/Work')

    time.sleep(5)

    print("Enter the 'sentence numbers' from 1 to 800 ( maximum 50 sentences ) : \n")

    first_number = int(input("Enter the first number : "))
    last_number = int(input("Enter the last number : "))
    range_of_numbers = list(range(first_number, last_number + 1))

    print(f" You have entered : {range_of_numbers} \n")

    print('work page range of sentences started')

    for value in range_of_numbers:

        time.sleep(5)

        drivers.get('http://www.smartdataentry.in/Home/Work')

        time.sleep(10)

        print(
            '\n ************************************************************************************************************ \n')

        sentence_number_added = int(value) + 5000

        # print(f'sentence_number_added : {sentence_number_added}')

        time.sleep(2)

        print(f'\n Entered number : {value} \n ')

        try:
            drivers.find_element_by_xpath(f"//button[@onclick='ViewSentence({sentence_number_added})']").click()
        except NSEE as exception:

            drivers.get('http://www.smartdataentry.in/Home/Work')

            time.sleep(5)

            drivers.find_element_by_xpath(f"//button[@onclick='ViewSentence({sentence_number_added})']").click()

        time.sleep(5)

        sentence_process(drivers, value)

    decision_making(drivers)


sign_in(driver)

time.sleep(5)
