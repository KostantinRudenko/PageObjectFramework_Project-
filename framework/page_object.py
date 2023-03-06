from time import sleep

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
    
    def find_title_game(self, link_number): # This function find game in steam

        steam_button = self.find_block('xpath', '//*[@id="logo_holder"]/a/img')
        steam_button.click()

        game_names = ['Grand Theft Auto V', 'Portal 2', 'Rust', 'Half-Life 2', 'RimWorld', 'Fallout 4']
        
        game_name = game_names[link_number]
        search_field = self.find_block('id', 'store_nav_search_term')
        search_field.send_keys(game_name)
        search_field.send_keys(Keys.RETURN)
        first_game = self.find_block('xpath', "//div[@class='col search_name ellipsis']/span[1]")
        first_game.click()

        assert_elements = [(game_names[link_number]), (self.browser.title)]

        return assert_elements
    
    def generate_link_numbers(self, limit, link_amount):
        link_numbers = [str(link) for link in range(limit, link_amount - 1)]
        return link_numbers

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