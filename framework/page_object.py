from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from framework.config import *
class PageObject:
    def __init__(self): # This function open Steam's webside
        "ChromeDriverManager().install()"
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(URL)
        self.search_field = self.find_block('id', 'store_nav_search_term')
        self.account = self.find_block('class', 'menuitem supernav username persona_name_text_content')
    def get_title_url(self):
        return self.browser.current_url
    
    def find_block(self, search_type, block):# This function find block on steam
        if search_type == 'xpath':
            result = self.browser.find_element(By.XPATH, block)
        elif search_type == 'class':
            result = self.browser.find_element(By.CLASS_NAME, block)
        elif search_type == 'id':
            result = self.browser.find_element(By.ID, block)
        return result
    def find_title_game(self, name_game): # This function find game in steam
        self.search_field.send_keys(name_game)
        self.search_field.send_keys(Keys.RETURN)
        first_game = self.find_block('xpath', "//div[@class='col search_name ellipsis']/span[1]")
        first_game.click()
        return self.browser.title
    def steam_login(self): # This function log in to steam
        community_button = self.find_block("class", 'menuitem supernav')
        community_button.click()
        login_start_button = self.find_block("class", 'btn_green_white_innerfade btn_medium')
        login_start_button.click()
        name_field = self.find_block('xpath', "//input[@class='newlogindialog_TextInput_2eKVn']")
        name_field.send_keys(name)
        password_field = self.find_block('xpath', "//input[@class='newlogindialog_TextInput_2eKVn']")
        password_field.send_keys(password)
        login_end_button = self.find_block('class', 'newlogindialog_SubmitButton_2QgFE')
        login_end_button.click()
        self.account.click()
        result = self.find_block('id', 'hello')
        return result
    def close_browser(self): # This function close Chrome
        self.browser.close()

    '''
    TODO:
    1. Расписать документацию (О автоматизации, о тестировании, документацию проекта)
    2. Составить тест-план (~15 тестов)
    3. Доработать фреймворк:
       - функция, которая будет искать текст
       - Дописать config (Логин и пароль)
    4. Написать функцию, которая будет входить в стим
    5. Выполнить все TODO
    6. Залить изменения (add -> commit -> push) в ветку TT0001
    '''