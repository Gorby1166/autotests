#rega
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылк
# MyAccountMenu=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']").click()
# Email=driver.find_element_by_id("reg_email").send_keys("gorbach1166@mail.ru")
# Pass=driver.find_element_by_id("reg_password").send_keys("Team1166aaa")
# Register=driver.find_element_by_name("register").click()
#driver.close
#login
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылк
MyAccountMenu=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']").click()
User=driver.find_element_by_id("username").send_keys("gorbach1166@mail.ru")
password=driver.find_element_by_id("password").send_keys("Team1166aaa")
login=driver.find_element_by_name("login").click()
element = driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/customer-logout/']") # нашли элемент по составному селектору
element_get_text = element.text # получили текст элемента с помощью .text
assert element_get_text == "Logout" # добавили проверку что содержимое равно ожидаемому
driver.close()