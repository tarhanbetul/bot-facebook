from selenium import webdriver
import time
from selenium.webdriver.common.by import By

import kullaniciBilgileri as kb

class Browser:
    def __init__(self,link):
        self.link = link
        self.browser = webdriver.Chrome('/Users/betul.kul/Desktop/teleskop/chromedriver')
        Browser.goFacebook(self)
    def goFacebook(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser.login(self)
        Browser.getlikes(self)
        Browser.getcomment(self)
    
    def getlikes(self):
        time.sleep(2)
        likecount=self.browser.find_elements(By.CSS_SELECTOR,"span.pcp91wgn")
        print(likecount)
        for a in likecount:
            print(a.text)
            time.sleep(2)
        print ("bitti")
    
    def getcomment(self):
        time.sleep(2)
        takvim=self.browser.find_elements(By.CLASS_NAME,"jpp8pzdo")
        for t in takvim:
            print(t.text)
        commentandshare=self.browser.find_elements(By.CLASS_NAME,"bp9cbjyn.j83agx80.pfnyh3mw.p1ueia1e")
        
        print(commentandshare)
        for c in commentandshare: 
            print ("betul")
            print(c.text)
            time.sleep(2)
            count1 =len(c)
            print ("dd",count1)
           
            if count1==0:
                pass
            elif c.size()==1:
                print ("cc")
                print(c.text)
            else:
                for i in c:
                    comment=i.find_element(By.CLASS_NAME,"gtad4xkn")
                    print(comment.text)

           
    def login(self):
        username=self.browser.find_element(By.NAME,"email")
        password=self.browser.find_element(By.NAME,"pass")
        username.send_keys(kb.userName)
        password.send_keys(kb.password)
        time.sleep(2)

        loginBtn = self.browser.find_element(By.CSS_SELECTOR,"#loginbutton")
        loginBtn.click()
        time.sleep(5)

        self.browser.get(self.link)
        time.sleep(5)