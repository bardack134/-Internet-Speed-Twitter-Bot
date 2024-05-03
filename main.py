from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class InternetSpeedTwitterBott:
    
    def __init__(self):
        
        # Keep the browser open after the script has run, and expand the browser
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach", True)
                
        # Create object webdriver for Chrome and receive the parameters written before
        self.driver = webdriver.Chrome(options=chrome_options)

        #get the website to check our internet speed
        self.driver.get(url="https://www.speedtest.net/")
          
    
    def cookies(self):
        """Methods that accept the cookies"""
        
        try:
            sleep(5)
            
            # get element  after explicitly waiting for 5 seconds, and do click() on the element
            self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

        except Exception as err:
            
            # print error message if the element was not found
            print(f"Error occurred while finding the 'I accept' cookie element:  {err}")    
                    
            
    def get_internet_speed(self):
        """This method is used to get the internet speed from www.speedtest.net"""
        
        try:
            sleep(1)
            
            #get the 'Go' button and do click()
            self.driver.find_element(By.CSS_SELECTOR, "span.start-text").click()
            
        except Exception as err:
            print(f"Error occurred while finding the 'Go button' cookie element:  {err}") 
            
        try:
            #wait 1 minute while checking for internet speed
            sleep(60)
            
            #In these variables, we store the speed data obtained from the speed website
            self.up=self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            
            self.down=self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            
            print(f"the internet speed is down {self.down} and up {self.up}")
            
        except Exception as err:
            print(f"Error occurred while finding the 'Go button' cookie element:  {err}")     
            
                    
    def tweet_at_provider(self):
        pass
    
    
    def run_script(self):
        self.cookies()
        self.get_internet_speed()
        
        
bot=InternetSpeedTwitterBott()
bot.run_script()