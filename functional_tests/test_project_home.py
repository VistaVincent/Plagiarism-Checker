from selenium import webdriver
from blog.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class Testprojecthome(StaticLiveServerTestCase):

    def setUp(self):
        driver_location="/usr/bin/chromedriver"
        binary_location="/usr/bin/google-chrome"
        options= webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.binary_location=binary_location
        
        self.browser=webdriver.Chrome(executable_path=driver_location, chrome_options=options)

    def tearDown(self):
        self.browser.close()
    
    def test_no_login(self):
        self.browser.get(self.live_server_url)
        #alert= self.browser.find_element
        self.browser.find_element_by_name("username").send_keys("pranay")
        self.browser.find_element_by_name("password").send_keys("noonecan@8")
        self.browser.find_element_by_name("submit").click()  
        alert=self.browser.find_element_by_class_name("form-group")
        self.assertEquals(
            alert.find_element_by_tag_name('li').text,
            "Please enter a correct username and password. Note that both fields may be case-sensitive."
        )

    def test_about(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_link_text('About').click()
        alert=self.browser.find_element_by_class_name("row")
        self.assertEquals(
            alert.find_element_by_tag_name('h1').text,
            "This is a online plagiarism and grammer checker"
        )


    def test_register(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_link_text('Register').click()
        self.browser.find_element_by_name("username").send_keys("pranay")
        self.browser.find_element_by_name("email").send_keys("jasti.pranay@gmail.com")
        self.browser.find_element_by_name("password1").send_keys("capstone@8")
        self.browser.find_element_by_name("password2").send_keys("capstone@8")
        self.browser.find_element_by_name("submit").click()
        self.browser.find_element_by_name("username").send_keys("pranay")
        self.browser.find_element_by_name("password").send_keys("capstone@8")
        self.browser.find_element_by_name("submit").click() 
        alert=self.browser.find_element_by_class_name("row")
        self.assertEquals(
            alert.find_element_by_tag_name('h2').text,
            "Proctored"
        )


    #def test_upload(self): 
      ##  self.browser.get(self.live_server_url)
       # self.browser.find_element_by_link_text('Register').click()
       # self.browser.find_element_by_name("username").send_keys("pranay")
       # self.browser.find_element_by_name("email").send_keys("jasti.pranay@gmail.com")
        #self.browser.find_element_by_name("password1").send_keys("capstone@8")
        #self.browser.find_element_by_name("password2").send_keys("capstone@8")
       # self.browser.find_element_by_name("submit").click()
       # self.browser.find_element_by_name("username").send_keys("pranay")
        #self.browser.find_element_by_name("password").send_keys("capstone@8")
        #self.browser.find_element_by_name("submit").click() 
       # self.browser.find_element_by_link_text('Upload Assignment').click()
        #self.browser.find_element_by_name("content").send_keys("test")
        #self.browser.find_element_by_id("id_document").send_keys("D:\\Users\\Pranay Chowdary\\Downloads\\pethullanaveenreddy_finalreport.docx")
        #self.browser.find_element_by_name("submit").click()
        #self.assertEquals(
         #   self.browser.find_element_by_tag_name('p').text,
          #  "test"
        #)





