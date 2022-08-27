# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# other imports
import random 
import time
#import os
#import wget # to save images to computer
#from webdriver_manager.chrome import ChromeDriverManager

class Insta_bot():
    """ 1. open insta
        2. login into it
        3. search for hashtag
        4. scroll down and get links
        5. like and comment to link """

    def open_insta_bot(self):
        """just opening insta(without login)"""
        wd_path = r'C:/Users/2me41/Downloads/chromedriver_win32(1)/chromedriver.exe'
        driv = webdriver.Chrome(wd_path)

        # tell drive which url to open
        url = 'https://www.instagram.com/'
        driv.get(url)       
        self.driv = driv
    
    def login(self, user_name, pass_word):
        """Login into insta account"""
        driv = self.driv
        wd_path = r'C:/Users/2me41/Downloads/chromedriver_win32(1)/chromedriver.exe'
        driv = webdriver.Chrome(wd_path)

        # tell drive which url to open
        url = 'https://www.instagram.com/'
        driv.get(url)

        # trying to login into page (using By css selector)
        username = WebDriverWait(driv, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password = WebDriverWait(driv, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        username.clear()
        password.clear()

        username.send_keys(user_name) # your user name
        password.send_keys(pass_word) # your password

        # Clicking the login button
        WebDriverWait(driv, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        # save your login info? Not Now
        WebDriverWait(driv, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
        # turn on notification? Not Now
        WebDriverWait(driv, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

    def hash_tags(self):
        """searching the hash_tag and opening up that page"""
        driv = self.driv
        # for searching anything 
        searchbox = WebDriverWait(driv, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
        to_search_for = '#abstractart'
        searchbox.send_keys(to_search_for)
        # to click enter
        searchbox.send_keys(Keys.ENTER)

        try:
            searchbox.send_keys(Keys.ENTER)
        except:
            pass

        time.sleep(3.00 + (float('{0:.3f}'.format(random.random()*(2)))))

    def taking_links(self, all_link_list):
        """getting all the links available"""
        driv = self.driv
        some_links = WebDriverWait(driv, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="_aabd _aa8k _aanf" ]/a[@href]'))) 
        some_links = [i.get_attribute('href') for i in some_links]
        
        hover_path = '[href="' + some_links[-1][25:] + '"]'
        ele_hover = driv.find_element(By.CSS_SELECTOR, hover_path)
        time.sleep(2)
        self.action_chain_driv.move_to_element(ele_hover).perform()

        some_links = some_links[10:]
        all_link_list += some_links
    
    def my_links(self, final_link_list):
        """scroll the down to get more links"""
        driv = self.driv
        self.action_chain_driv = ActionChains(driv)
        
        final_link_list = []
        self.taking_links(final_link_list)

        driv.execute_script("window.scrollTo(0, 3700)") # scroll till 9 lines
        time.sleep(2.00 + (float('{0:.3f}'.format(random.random()*(3)))))
        driv.execute_script("window.scrollTo(3700, 5300)") # after 9 till more 5 lines
        time.sleep(2.00 + (float('{0:.3f}'.format(random.random()*(3)))))

        self.taking_links(final_link_list)

        driv.execute_script("window.scrollTo(5300, 9300)") # 4000 means more 5
        time.sleep(2.00 + (float('{0:.3f}'.format(random.random()*(3)))))
        driv.execute_script("window.scrollTo(9300, 16300)") 
        time.sleep(2.00 + (float('{0:.3f}'.format(random.random()*(3))))) # can add more lines


        self.taking_links(final_link_list)
        print(len(final_link_list))
        final_link_list = [final_link_list[i:i + 3] for i in range(0, len(final_link_list), 3)]
        return final_link_list

    def like_comment(self, my_list):
        """selecting the random link and commenting on it"""
        driv = self.driv
        sample_words = ['lovely!!', 'pretty!!', 'appealing!!', 'gorgeous!!', 'engaging!!']

        for i in my_list:
            x = random.choice(i)
            driv.get(x)
            time.sleep(float('{0:.3f}'.format(random.random()*(3))))
            WebDriverWait(driv, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="_aamw"]/button/div/span'))).click()
            WebDriverWait(driv, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[placeholder='Add a comment…']"))).click()
            WebDriverWait(driv, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[placeholder='Add a comment…']"))).send_keys(random.choice(sample_words))
            WebDriverWait(driv, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
            time.sleep(float('{0:.3f}'.format(random.random()*(3))))


bot = Insta_bot() # create object
bot.open_insta_bot() # opening insta
bot.login('riya26feb', 'w4h7@6t9e') # login into insta
bot.hash_tags() # searching
final_list_of_links = []
bot.my_links(final_list_of_links) # get all links
bot.like_comment(final_list_of_links) # like and comment

