#1
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылк
# MyAccountMenu=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']").click()
# User=driver.find_element_by_id("username").send_keys("gorbach1166@mail.ru")
# password=driver.find_element_by_id("password").send_keys("Team1166aaa")
# login=driver.find_element_by_name("login").click()
# shop=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/shop/']").click()
# html5=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product/html5-forms/']").click()
# element = driver.find_element_by_css_selector("[itemprop='name']") # нашли элемент по составному селектору
# element_get_text = element.text # получили текст элемента с помощью .text
# assert element_get_text == "HTML5 Forms"
# print ("заголовок книги назвается: HTML5 Forms")
#driver.close
#2
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылк
# MyAccountMenu=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']").click()
# User=driver.find_element_by_id("username").send_keys("gorbach1166@mail.ru")
# password=driver.find_element_by_id("password").send_keys("Team1166aaa")
# login=driver.find_element_by_name("login").click()
# shop=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/shop/']").click()
# Html=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product-category/html/']").click()
# items=driver.find_elements_by_class_name("price")
# if len(items) == 3:
#     print ("На странице три товара")
# else:
#     print("нет")
# 3
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылк
# MyAccountMenu=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']").click()
# User=driver.find_element_by_id("username").send_keys("gorbach1166@mail.ru")
# password=driver.find_element_by_id("password").send_keys("Team1166aaa")
# login=driver.find_element_by_name("login").click()
# shop=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/shop/']").click()
# sort1 = driver.find_element_by_css_selector("[name='orderby']")
# sort1_check = sort1.get_attribute("value")
# if sort1_check == "menu_order":
#   print("сортировка по умолчанию")
# else:
#    print("сортировка по не умолчанию")
# from selenium.webdriver.support.select import Select # импортируем класс Select или библиотеки webdriver
# element = driver.find_element_by_css_selector("[class='orderby']")
# select = Select(element)
# select.select_by_value("price-desc")
# sort2 = driver.find_element_by_css_selector("[name='orderby']")
# sort2_check = sort2.get_attribute("value")
# if sort2_check == "price-desc":
#   print("ссортировка по цене от большей к меньшей")
# else:
#    print("Nooo")
# 4
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылк
# driver.implicitly_wait(10)
# driver.maximize_window()
# MyAccountMenu=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']").click()
# User=driver.find_element_by_id("username").send_keys("gorbach1166@mail.ru")
# password=driver.find_element_by_id("password").send_keys("Team1166aaa")
# login=driver.find_element_by_name("login").click()
# shop=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/shop/']").click()
# start=driver.find_element_by_css_selector("[title='Android Quick Start Guide']").click()
# old_price = driver.find_element_by_css_selector(".price > del > span")
# old_price_get_text = old_price.text
# assert old_price_get_text == "₹600.00"
# new_price = driver.find_element_by_css_selector(".price > ins > span")
# new_price_get_text = new_price.text # получили текст элемента с помощью .text
# assert new_price_get_text == "₹450.00" # добавили проверку что содержимое равно ожидаемому
# bookcover = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# bookcover=driver.find_element_by_class_name("images").click()
# close=WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# close=driver.find_element_by_class_name("pp_close").click()

#5
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылк
# driver.implicitly_wait(10)
# driver.maximize_window()
# shop=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/shop/']").click()
# driver.execute_script("window.scrollBy(0, 300);")
# html5dev=driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# time.sleep(2)
# basket=driver.find_element_by_id("wpmenucartli").click()
# price = driver.find_element_by_css_selector("[data-title='Price']") # нашли элемент по составному селектору
# price_get_text = price.text # получили текст элемента с помощью .text#
# assert price_get_text == "₹180.00"
# print("стоимость 180.00")
# item = driver.find_element_by_css_selector("[name='cart[4c5bde74a8f110656874902f07378009][qty]']") # нашли элемент по составному селектору
# item_check = item.get_attribute("value")
# if item_check == "1":
#     print("выбран 1 товар")
# some_element= WebDriverWait(driver, 10).until(
#   EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']"), "180.00"))
# some_element2= WebDriverWait(driver, 10).until(
#   EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='order-total']"), "183.60"))
#6

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылк
# driver.implicitly_wait(10)
# driver.maximize_window()
# shop=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/shop/']").click()
# driver.execute_script("window.scrollBy(0, 300);")
# html5dev=driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# time.sleep(2)
# jsdata=driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']").click()
# basket=driver.find_element_by_id("wpmenucartli").click()
# time.sleep(2)
# delete=driver.find_element_by_css_selector("[data-product_id='182']").click()
# time.sleep(2)
# undo=driver.find_element_by_link_text("Undo?").click()
# book1=driver.find_element_by_css_selector("[max='9809']").clear()
# #boo=driver.find_element_by_css_selector(".product-quantity>.quantity>[name='cart[4c5bde74a8f110656874902f07378009][qty]']").send_keys(3)
# book1=driver.find_element_by_css_selector(".product-quantity>.quantity>[max='9809']").send_keys("3")
# update=driver.find_element_by_css_selector("[value='Update Basket']").click()
# element = driver.find_element_by_css_selector(".product-quantity>.quantity>[max='9809']")
# element_check = element.get_attribute("value")
# assert element_check == "3" # добавили проверку что содержимое равно ожидаемому
# time.sleep(2)
# apply=driver.find_element_by_css_selector(".coupon").click()
# time.sleep(1)
# sort2 = driver.find_element_by_css_selector("[class='woocommerce-error']")
# sort2_check = sort2.get_attribute("class")
# if sort2_check == "woocommerce-error":
#    print("Please enter a coupon code.")
#7
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылк
driver.implicitly_wait(10)
driver.maximize_window()
shop=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/shop/']").click()
driver.execute_script("window.scrollBy(0, 300);")
html5dev=driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
time.sleep(2)
basket=driver.find_element_by_id("wpmenucartli").click()
PROCEED = WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, "[href='https://practice.automationtesting.in/checkout/']")))
PROCEED1=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/checkout/']").click()
name = WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='billing_first_name']")))
firstname=driver.find_element_by_id("billing_first_name").send_keys("Dima")
lastname=driver.find_element_by_css_selector("[autocomplete='family-name']").send_keys("Tretiakovskii")
email=driver.find_element_by_css_selector("[id='billing_email']").send_keys("gorbach1166@mail.ru")
phone=driver.find_element_by_css_selector("[id='billing_phone']").send_keys("89111178648")
time.sleep(1)
element = driver.find_element_by_css_selector("[id='select2-chosen-1']").click()
element1=driver.find_element_by_css_selector("[id='s2id_autogen1_search']").send_keys("Russia")
russia=driver.find_element_by_css_selector(".select2-match").click()
street=driver.find_element_by_css_selector("[placeholder='Street address']").send_keys("shaumyana")
apartment=driver.find_element_by_css_selector("[placeholder='Apartment, suite, unit etc. (optional)']").send_keys("48")
town=driver.find_element_by_css_selector("[autocomplete='address-level2']").send_keys("Saint-Peterburg")
country=driver.find_element_by_css_selector("[name='billing_state']").send_keys("Russia")
zip=driver.find_element_by_css_selector("[autocomplete='postal-code']").send_keys("245")
driver.execute_script("window.scrollBy(0, 600);")
checkpayments=driver.find_element_by_id("payment_method_cheque").click()
time.sleep(4)
placeoler=driver.find_element_by_css_selector("[value='Place order']").click()
thanks= WebDriverWait(driver, 10).until(
 EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='woocommerce-thankyou-order-received']"), "Thank you. Your order has been received."))
Check_Payments= WebDriverWait(driver, 10).until(
  EC.text_to_be_present_in_element((By.XPATH, "//td[text()='Check Payments']"), "Check Payments"))


