from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from constants import PROMISED_DOWN, PROMISED_UP, TWITTER_PASSWORD, TWITTER_USERNAME


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
          
          
        # attributes that will save the internet speed information  
        self.up = 0
        self.down = 0
        
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
            sleep(47)
            
            #In these variables, we store the speed data obtained from the speed website
            self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            
            sleep(2)
            
            self.down = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
      
            
            print()
            print(f"the internet speed is down {self.down} and up {self.up}")
            print()
            
        except Exception as err:
            print(f"Error occurred while finding the 'Go button' cookie element:  {err}")     
            
                    
    def tweet_at_provider(self):
        """This method login in to twitter an include the up/downs speeds got before and the promises speeds and send the tweet"""
        
        #get the twitter website
        self.driver.get(url="https://twitter.com/")
        try:
            #wait 
            sleep(3)
            
            sign_in=self.down=self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
            sign_in.click()
            
            
        except Exception as err:
            print(f"Error occurred while finding the 'sign in button':  {err}")       
            #wait 
        
        try: 
            
            sleep(4)
               
            #get the email  input box
            email=self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
            
            #send my email to the   input box
            email.send_keys(TWITTER_USERNAME, Keys.ENTER)
            
            
        except Exception as err:
            
            print(f"Error occurred while entering the email :  {err}")      
            
            
            
        try: 
            sleep(4)
            
            #get the password  input box    
            password=self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
            
            #send my password to the  input box
            password.send_keys(TWITTER_PASSWORD, Keys.ENTER)
            
            sleep(2)
            
            
        except Exception as err:
            print(f"Error occurred while entering the password :  {err}")  
          

        #I close the pop-up window that says 'boosts your account security'  
        try: 
            sleep(3)
            
            #get the password  input box    
            self.driver.find_element(By.CSS_SELECTOR, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div/svg').click()
    
            
            sleep(2)
            
            
        except Exception as err:
            print(f"Error occurred when try to close the 'boosts your account security' window :  {err}")  
            
            pass
        
        
        try:
            print(f"the internet speed is down {self.down} and up {self.up}")
            
            
            sleep(4)
            
            #get the twitter text box
            twitter_text_box=self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span')
            
        except Exception as err:
            
            print(f"Error occurred when try to get the 'twitter  text box' :  {err}")     
            sleep(3)
        
        try:    
            #get and click in the button "post" 
            sleep(3)
            
            post=self.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]')
            
            post.click()   
             
        except Exception as err:
            
            print(f"Error occurred when try to get the 'post button' :  {err}")     
            sleep(3)
            # sleep(10)
            # #close the browser
            # self.driver.quit()
        
            
        
        
            
    def run_script(self):
        self.cookies()
        self.get_internet_speed()
        self.tweet_at_provider()
        
        
bot=InternetSpeedTwitterBott()
bot.run_script()


# <div class="public-DraftEditorPlaceholder-inner" id="placeholder-7snnt" style="white-space: pre-wrap;">What is happening?!</div>