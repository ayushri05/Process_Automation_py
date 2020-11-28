from selenium import webdriver
import selenium
import win32api
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def automate():
    driver = webdriver.Chrome(
        executable_path=r'C:\\Users\\Ayushri\\Downloads\\chromedriver_win32\\chromedriver')

    try:
        driver.get('https://apisandbox.zuora.com')
    except expression as er:
        win32api.MessageBox(0, 'SOmething went wrong in opening website',
                            'issue with autmated process', 0x00001000)
        driver.refresh()

    # driver.get('https://apisandbox.zuora.com')
    login_user = driver.find_element_by_xpath('//*[@id="id_username"]')
    login_user.send_keys('amit.bhokri+zu@wipro.com')

    login_pass = driver.find_element_by_xpath('//*[@id="id_password"]')
    login_pass.send_keys('Ab@123456')

    login_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/a')
    login_btn.click()

    time.sleep(15)

    workflow = driver.find_element_by_link_text('Workflow')
    # workflow.get_attribute('href')
    workflow.click()

    time.sleep(20)

    workflow1 = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "tab_workflow")))

    # workflow1 = driver.find_element_by_xpath('//*[@id="tab_workflow"]/a')
    # workflow.get_attribute('href')
    workflow1.click()

    # time.sleep(15)

    list_view = driver.find_element_by_css_selector(
        '#Workflows_view_table')
    list_view.click()

    time.sleep(10)

    # select = Select(driver.find_element_by_id('table_size'))

    #

    # select.select_by_value('25')
    w_ser = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#Workflows_search_btn")))
    # w_ser = driver.find_element_by_css_selector('#Workflows_search_btn')
    w_ser.click()

    w_name = driver.find_element_by_xpath('//*[@id="Workflows_search"]')
    # w_size.cilck()
    time.sleep(10)
    w_name = w_name.send_keys("Test Demo Blank")
    time.sleep(5)
    w_name.click()


automate()
