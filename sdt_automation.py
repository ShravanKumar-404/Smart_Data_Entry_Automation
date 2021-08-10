import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

s = requests.session()

chrome_path = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(chrome_path)

time.sleep(3)


def sign_in(drivers):
    drivers.get('http://www.smartdataentry.in/Home/Login')

    time.sleep(5)

    print('Sign in started')

    login_text = drivers.find_element_by_id('txtUserName')
    login_text.clear()
    login_text.send_keys('6281465658')

    time.sleep(1)

    password_text = drivers.find_element_by_id('txtPassword')
    password_text.clear()
    password_text.send_keys('s8r@145415')

    time.sleep(1)

    submit_login = drivers.find_element_by_xpath(
        '/html/body/div/div[2]/div/div/div/form/button')
    submit_login.click()

    print('Signed in successfully')


def sentences(driver, number):
    time.sleep(5)

    print(f'Sentence-{number} started successfully')

    sentence = driver.find_element_by_id('divSentence')

    sentence_box = driver.find_element_by_id('txtContent')
    sentence_box.clear()

    time.sleep(3)

    sentence_box.send_keys(sentence.text)

    time.sleep(3)

    detect_btn = driver.find_element_by_xpath(
        '//*[@id="divbody"]/div/div[2]/input')
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

    time.sleep(2)

    lang_code_box = driver.find_element_by_id('txtLanguageCode')
    lang_code_box.clear()
    lang_code_box.send_keys(lang_code.text)
    time.sleep(1)

    lang_name_box = driver.find_element_by_id('txtLanguageName')
    lang_name_box.clear()
    lang_name_box.send_keys(lang_name.text)
    time.sleep(1)

    probability_box = driver.find_element_by_id('txtProbability')
    probability_box.clear()
    probability_box.send_keys(probability.text)
    time.sleep(1)

    percentage_box = driver.find_element_by_id('txtPercentage')
    percentage_box.clear()
    percentage_box.send_keys(percentage.text)
    time.sleep(1)

    result_box = driver.find_element_by_id('txtReliableResult')
    result_box.clear()
    result_box.send_keys(result.text)
    time.sleep(1)

    captcha_box = driver.find_element_by_id('txtCaptcha')
    captcha_box.clear()
    captcha_box.send_keys(captcha.text)
    time.sleep(1)

    driver.find_element_by_id('txtReliableResult').click()

    time.sleep(1)

    driver.find_element_by_id('txtReliableResult').click()

    time.sleep(3)

    driver.find_element_by_id('btnSave').click()

    time.sleep(5)

    print('submitted successfully')

    work_page(driver)


def work_page(drivers):
    print('work page started')

    drivers.get('http://www.smartdataentry.in/Home/Work')

    time.sleep(3)

    sentence_number = input("Enter the 'sentence number' or type 'exit' : ")

    if sentence_number == 'exit':

        print('trying to sign out')
        time.sleep(5)
        drivers.find_element_by_xpath('//*[@id="divsignout"]/a/div').click()

        print('sign out completed successfully \n')

        time.sleep(5)
        drivers.quit()

    else:

        sentence_number_added = int(sentence_number) + 5000

        # print(f'sentence_number_added : {sentence_number_added}')

        time.sleep(2)

        print(f'Entered number : {sentence_number} \n ')

        drivers.find_element_by_xpath(
            f"//button[@onclick='ViewSentence({sentence_number_added})']").click()

        sentences(drivers, sentence_number)


sign_in(driver)

time.sleep(5)

work_page(driver)
