from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
#link = "http://suninjuly.github.io/registration2.html"

from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(link)

nameInput = browser.find_element_by_css_selector(".first_class [placeholder='Введите имя']")
nameInput.send_keys("Гоша")

lastnameInput = browser.find_element_by_css_selector(".second_class [placeholder='Введите фамилию']")
lastnameInput.send_keys("Гошар")

emailInput = browser.find_element_by_css_selector(".third_class [placeholder='Введите Email']")
emailInput.send_keys("baks@bk.com")

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text

assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
#browser.close()