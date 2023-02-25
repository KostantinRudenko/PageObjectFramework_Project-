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
        elif search_type == 'css_sel':
            result = self.browser.find_element(By.CSS_SELECTOR)
        return result    

    def get_title(self):
        return self.browser.title
    
    def find_title_game(self, name_game): # This function find game in steam
        self.search_field.send_keys(name_game)
        self.search_field.send_keys(Keys.RETURN)
        first_game = self.find_block('xpath', "//div[@class='col search_name ellipsis']/span[1]")
        first_game.click()
        return self.browser.title

    def change_language(self, language): # This function change language
        language_list = ['polish', 'english', 'italian', 'german', 'french']
        language_choice_button = self.find_block('id', 'language_pulldown')
        language_choice_button.click()
        if language in language_list:
            result_language = self.find_block('xpath', f"//div/a[@href='?l={language}']") 
            result_language.click()
            time.sleep(3)
            return self.browser.title
        else:
            raise LanguageNotFoundError
    
    def category_select(self, column, row, title): # This function select category
        category_panel_button = self.find_block('id', 'genre_tab')
        category_panel_button.click()
        while title not in self.browser.title:
            category_button = self.find_block('xpath', f'//*[@id="genre_flyout"]/div/div[{column}]/div[{row}]')
            category_button.click()
        time.sleep(3)
        page_main_text = self.find_block('xpath', '//*[@id="SaleSection_56339"]/div/div')
        return page_main_text
    
    def text_to_search_field(self, text):
        search_field = self.find_block('id', 'store_nav_search_term')
        search_field.send_keys(text)
        search_field.send_keys(Keys.RETURN)
        find_results = self.find_block('class', 'search_results_count')
        return find_results

    def open_popular_game(self, link_number):
        try:
            first_game_name = self.find_block('xpath', f'//*[@id="tab_newreleases_content"]/a[{link_number}]/div[3]/div[1]').text
            game_name_1 = first_game_name.__getattribute__('title')
            game_link = self.find_block('xpath', f'//*[@id="tab_newreleases_content"]/a[{link_number}]')
            game_link.click()
            url = self.get_title_url()
            if "agecheck" in self.get_title_url():
                submit_button = self.find_block('css_sel', str('#view_product_page_btn'))
                submit_button.click()
            # name of the game on its main page
            name_game_2 = self.find_block('css_sel', '#appHubAppName').text
            all_games_names = [str(game_name_1), str(name_game_2)]
            return all_games_names
        except TypeError:
            raise ElementNotStrError
    def close_browser(self): # This function close Chrome
        self.browser.close()

    '''
    TODO:
    1. Расписать документацию (О автоматизации, о тестировании, документацию проекта)
    2. Составить тест-план (~15 тестов)
    3. Доработать фреймворк:
       - функция, которая будет искать текст
    4. Выполнить все TODO
    5. Переписать README.md
       - Краткое описание проекта;
         а. Для чего этот проект?
         б. Что он тестирует (какой сайт)?
       - Окружение;
         а. Программное обеспечение (Программирование & Модули)
            - Python
            - selenium
            - time
            - webdriver-manager
            - pytest
         б. ОС (Винда) Пример: Windows 10 Home Edition x64
         в. Программное обеспечение:
            - Браузеры (Хром, Файрфокс);
            - Драйвер для тестирования (Хром драйвер)
        - Как это все установить? Example: https://github.com/CleverRaven/Cataclysm-DDA/blob/master/README.md
        - К кому обращаться за дополнительными вопросами 
    '''