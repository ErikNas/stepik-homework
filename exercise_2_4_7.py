import time
import math
import os 

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def pass_capcha():
    
    time.sleep(1)

    x = browser.find_element_by_css_selector("#input_value").text
    print(x)
   
    y = calc(x)

    browser.find_element_by_css_selector("#answer").send_keys(y)
    btn = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()
   
    #browser.execute_script("return checkAnswer(arguments[0], 2408);", y)
    #ActionChains(browser).click(btn).perform()
    

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Chrome()

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

browser.find_element_by_id("book").click()


#browser.find_element_by_css_selector(".trollface.btn.btn-primary").click()

#first_window = browser.window_handles[0]
#new_window = browser.window_handles[1]

#browser.switch_to.window(new_window)

pass_capcha()

#alert = browser.switch_to.alert
#print(alert.text)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
#browser.quit()
