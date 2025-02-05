from selenium import webdriver
from selenium.webdriver.common.by import By


#Use Selenium to open the webpage in a browser and highlight key fields.
#Not sure if this is the best way to do this , and it might mabye not work yet.
class Visualizer:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def highlight_elements(self, elements):
        self.driver.get(self.url)
        for element in elements:
            # Use JavaScript to highlight
            self.driver.execute_script("arguments[0].style.border='2px solid red'", element)
        return self.driver

    def close(self):
        self.driver.quit()
