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
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.set_window_size(1336,800)
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
            game_name_1 = self.find_block('xpath', f'//*[@id="tab_newreleases_content"]/a[{link_number}]/div[3]/div[1]').text
            # name of the game on its main page
            actions = ActionChains(self.browser)
            game_block = self.find_block('xpath', f'//*[@id="tab_newreleases_content"]/a[{link_number}]')
            actions.move_to_element(game_block).perform()
            time.sleep(2)
            game_name_2 = self.find_block('xpath', f"//div[@class='tab_preview focus']/h2").text
            all_games_names = [game_name_1, game_name_2]
            return all_games_names
        except TypeError:
            raise ElementNotStrError
        
    def check_prices(self, link_number) -> list: # This function check prices of ten popular games
        steam_button = self.find_block('xpath', '//*[@id="logo_holder"]/a/img')
        steam_button.click()
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
    
    def generate_link_numbers(self, __limit, __link_amount):
        link_numbers = [str(link) for link in range(__limit, __link_amount + 1)]
        return link_numbers

    def find_genre_name(self, link_number, language='english'): # This function check genre names
        self.browser.get(URL)
        
        title = self.browser.title
        if title != 'Welcome to Steam':
            language_choice_button = self.find_block('id', 'language_pulldown')
            language_choice_button.click()
        
            result_language = self.find_block('xpath', f"//div/a[@href='?l={language}']") 
            result_language.click()
        
            time.sleep(3)

        genre_button = self.find_block('xpath', f'//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div[2]/a[{link_number}]')
        genre_name = genre_button.text
        genre_button.click()
        genre_name = genre_name.upper()

        genre_main_page_text = self.find_block('xpath', '//*[@class="contenthubmaincarousel_ContentHubTitle_9tb4j ContentHubTitle"]').text
        names = [genre_name, genre_main_page_text]
        return names

    def find_price_less_80(self, link_number, symbol='₴') -> int:
        # This function saves and returns prices of games, that are relevant to the content "Under 80"
        self.browser.get(URL)
        self.browser.execute_script('window.scrollBy(0, 3900)') # This function scroll down page
        time.sleep(2)

        game = self.find_block('xpath', f'//div[@class="carousel_container paging_capsules specials_under10"]/div/div/a[{link_number}]')
        game.click()
        
        game_price = None

        try:
            discount = self.find_block('xpath', '//div[@class="game_purchase_action"]/div[1]/div[1]/div[1]').is_displayed()
            discount_2 = self.find_block('xpath','//div[@class="discount_block game_purchase_discount"]/div[2]').is_displayed()
            if discount == True:
                game_price = self.find_block('xpath', '//div[@class="discount_final_price"][1]')
            elif discount_2 == True:
                game_price = self.find_block('xpath', '//div[@class="game_purchase_price price"]')
            else:
                raise PriceNotFoundError
        except:
            game_price = self.find_block('xpath', '//*[@class="game_purchase_action"]/div/div[1]')
        return int(game_price.text.replace(symbol, ''))
    
    def click_category(self, link_number, language='english') -> str:
        self.browser.get(URL)

        title = self.browser.title
        if title != 'Welcome to Steam':
            language_choice_button = self.find_block('id', 'language_pulldown')
            language_choice_button.click()
        
            result_language = self.find_block('xpath', f"//div/a[@href='?l={language}']") 
            result_language.click()
        
            time.sleep(3)

        category = self.find_block('xpath',
        f"//div[@class='carousel_items store_capsule_container responsive_scroll_snap_ctn']/div/a[{link_number}]")
        category_name = self.find_block('xpath',
        f'//*[@id="responsive_page_template_content"]/div[1]/div[2]/div[5]/div/div[2]/div/div[1]/div[1]/a[{link_number}]/div[2]/span').text
        
        category.click()

        main_category_page_name = self.find_block('xpath', '//*[@class="contenthubmaincarousel_ContentHubTitleCtn_61ECB ContentHubTitleCtn"]/div').text

        return [category_name.upper(), main_category_page_name.upper()]
    
    def check_streams(self, link_nnumber, language='english'):
        self.browser.get(URL)

        title = self.browser.title
        if title != 'Welcome to Steam':
            language_choice_button = self.find_block('id', 'language_pulldown')
            language_choice_button.click()

            result_language = self.find_block('xpath', f"//div/a[@href='?l={language}']") 
            result_language.click()
        
            time.sleep(3)
        
        self.browser.execute_script('window.scrollBy(0, 3900)') # This function scroll down page
        time.sleep(2)
        
        stream_game_name = self.find_block('xpath',
                                           f'//*[@id="live_streams_carousel"]/div/div/a[{link_nnumber}]/div[2]/span[1]')
        stream_game_link = self.find_block('xpath',
                                           f'//*[@id="live_streams_carousel"]/div/div/a[{link_nnumber}]')
        stream_game_link.click()
        
        cur_url = self.get_title_url()
        if 'agecheck' in cur_url:
            return True

        time.sleep(4)

        self.browser.execute_script('window.scrollBy(0, 3000)') # This function scroll down page
        time.sleep(1)

        game_main_page_name = self.find_block('xpath', '//*[@id="genresAndManufacturer"]/b[1]').text

        return [stream_game_name.text, game_main_page_name]

    def close_browser(self) -> None: # This function close Chrome

        self.browser.close()