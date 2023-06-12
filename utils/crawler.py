from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils import capcha

_LOGIN_URL = 'https://webap.nkust.edu.tw/nkust/index_main.html'


def set_webdriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    return webdriver.Chrome(options=chrome_options)


def not_empty(browser):
    try:
        element = browser.find_element(By.ID, "verifyCode")
    except NoSuchElementException:
        return False
    return element.get_attribute("src") != ''


def get_capcha_image(browser):
    image = None
    try:
        WebDriverWait(browser, 5).until(not_empty)
        capcha_image = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, "verifyCode"))
        )
        image = capcha_image.screenshot_as_png
    except Exception as error:
        print("get capcha error:", error)
    return image


def login(username, password):
    browser = set_webdriver()
    count = 0
    state = 500
    department = ""
    while count < 3:
        try:
            browser.get(_LOGIN_URL)
            capcha_img = get_capcha_image(browser)
            capcha_code = capcha.identify_capcha(capcha_img)
            element_username = browser.find_element(By.ID, "uid")
            element_password = browser.find_element(By.ID, "pwd")
            element_captcha = browser.find_element(By.ID, "etxt_code")

            element_username.send_keys(username)
            element_password.send_keys(password)
            element_captcha.send_keys(capcha_code)

            submit_button = browser.find_element(By.ID, "chk")
            submit_button.click()

            state = browser.page_source
            department = get_department(browser)
            break
        except Exception as error:
            state = str(error)
            if retry(state):
                browser.refresh()
                count += 1
            else:
                print(error)
                count += 1

    http_code = http_code_parser(state)
    browser.quit()

    return http_code, department


"""
Http code
200: 登入成功

400: 參數錯誤
無此帳號或密碼不正確 帳號不可空白 密碼不可空白

500: 伺服器問題
網頁繁忙 未知錯誤
"""


def http_code_parser(state):
    switch = {"f_index.html": 200, 'f_head.jsp': 200, '無此帳號或密碼不正確': 400, '帳號不可空白': 400,
              '密碼不可空白': 400, '繁忙': 500}

    for key in switch:
        if key in state:
            return switch[key]
    return 500


def retry(state):
    return '驗證碼錯誤' in state or '更改密碼' in state


def get_department(browser):
    lmenu_element = browser.find_element(By.NAME, "Lmenu")
    browser.switch_to.frame(lmenu_element)
    browser.execute_script("of_display('AG003')")
    browser.switch_to.default_content()

    main_element = browser.find_element(By.NAME, "Main")
    browser.switch_to.frame(main_element)

    start = '科　　系：'
    end = '</td>'
    start_index = browser.page_source.find(start) + len(start)
    end_index = browser.page_source.find(end, start_index)

    department = browser.page_source[start_index:end_index]
    return department
