
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылк
driver.execute_script("window.scrollBy(0, 600);")
ruby=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product/selenium-ruby/']").click()
REVIEWS=driver.find_element_by_css_selector("[href='#tab-reviews']").click()
stars=driver.find_element_by_css_selector("[class='star-5']").click()
Review=driver.find_element_by_id("comment").send_keys("Nice book!")
Email=driver.find_element_by_id("email").send_keys("gorbach1166@mail.ru")
Name=driver.find_element_by_id("author").send_keys("Dima")
submit=driver.find_element_by_id("submit").click()
driver.close()