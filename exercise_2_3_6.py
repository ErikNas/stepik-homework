import time
import math
import os 

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def pass_capcha():
    #robot_check_box = browser.find_element_by_css_selector("#robotCheckbox")
    #robot_check_box.click()

    #robot_radio = browser.find_element_by_css_selector("#robotsRule")
    #robot_radio.click()

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_css_selector(".btn.btn-primary").click()
    #ActionChains(browser).click(btn).perform()
    

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Chrome()

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
browser.get("http://suninjuly.github.io/redirect_accept.html")

browser.find_element_by_css_selector(".trollface.btn.btn-primary").click()

first_window = browser.window_handles[0]
new_window = browser.window_handles[1]

browser.switch_to.window(new_window)

pass_capcha()

# После выполнения всех действий мы не должны забыть закрыть окно браузера
#browser.quit()
