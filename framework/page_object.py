import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from framework.config import *
from framework.exceptions import *
class PageObject:
    def __init__(self): # This function open Steam's webside
        "ChromeDriverManager().install()"
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(URL)
        self.search_field = self.find_block('id', 'store_nav_search_term')
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
    '''def change_title(self):
        self.browser.title = 'ILovePython'
        return self.browser.title'''
    def steam_login(self): # This function log in to steam
        self.browser.get('https://store.steampowered.com/login/?redir=&redir_ssl=1&snr=1_4_4__global-header')
        name_field = self.find_block('xpath', "//div/input/class='newlogindialog_TextInput_2eKVn'[@type='text']")
        name_field.send_keys(username)
        password_field = self.find_block('xpath', "//div/input/[class='newlogindialog_TextInput_2eKVn'][@type='password']")
        password_field.send_keys(password)
        login_end_button = self.find_block('xpath', "//div[@class='newlogindialog_SubmitButton_2QgFE']")
        login_end_button.click()
        self.browser.get('https://steamcommunity.com/profiles/76561199476469925/home/')
        result = self.find_block('xpath', "//div[@id='hello']")
        return result
    def change_language(self, language): # This function change language
        language_list = ['polish', 'english']
        language_choice_button = self.find_block('id', 'language_pulldown')
        language_choice_button.click()
        if language in language_list:
            result_language = self.find_block('xpath', f"//div/a[@href='?l={language}']") 
            result_language.click()
            time.sleep(3)
            return self.browser.title
        else:
            raise LanguageNotFoundError
    def close_browser(self): # This function close browser
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