import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

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
    
    def check_discounts(self, link_number): # This function select popular sections on main page
        try:
            discount_content_button = self.find_block('xpath', '//*[@id="tab_specials_content_trigger"]/div')
            discount_content_button.click()
            discount = self.find_block('xpath', f'//*[@id="tab_specials_content"]/a[{link_number}]/div[2]/div[1]').text
            discount = int(discount.replace('%', ''))
            return discount
        except TypeError:
            raise ElemantNotIntError
    
    def text_to_search_field(self, text): # This function try to find non-existent games
        search_field = self.find_block('id', 'store_nav_search_term')
        search_field.send_keys(text)
        search_field.send_keys(Keys.RETURN)
        find_results = self.find_block('class', 'search_results_count')
        return find_results

    def open_popular_game(self, link_number): # This function check names of popular games
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
        
    def check_prices(self, link_number) -> list:
        usual_game_price = self.find_block('xpath', f'//*[@id="tab_newreleases_content"]/a[{link_number}]/div[2]/div/div').text
        discount_final_price = self.find_block('xpath', f'//div[@class="tab_content"]/a[{link_number}]/div[2]/div[2]/div[2]').text

        discount_content_elem = self.find_block('xpath', f'//div[@class="tab_content"]/a[{link_number}]/div[2]/div[2]/div[2]')
        game_link = self.find_block('xpath', f'//*[@id="tab_newreleases_content"]/a[{link_number}]')
        
        free_game_prices = ['Бесплатно', 'Free To Play', 'Free']

        price_1, price_2 = None, None

        if discount_content_elem.is_displayed():
            price_1 = discount_final_price
            game_link.click()

            price_2 = self.find_block('xpath', '//div[@class="discount_final_price"]').text

            if 'https://store.steampowered.com/agecheck/app/' in self.get_title_url():
                return None

            if usual_game_price in free_game_prices:
                free_game_price = self.find_block('xpath', '//*[@class="game_purchase_price price"]').text
                price_2 = free_game_price

        elif usual_game_price:
            price_1 = usual_game_price
            game_link.click()
        
        else:
            price_2 = self.find_block('xpath', '//*[@class="game_purchase_price price"]').text

        all_prices = [price_1, price_2]
        return all_prices
    def close_browser(self) -> None: # This function close Chrome
        self.browser.close()

    '''
    TODO:
    1. Составить тест-план (~15 тестов)
    2. Выполнить все TODO
    '''