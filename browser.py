from requests import post
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urlList as urlList
import kullaniciBilgileri as kb
from PIL import Image
import hashlib
import csv
import os

class Browser:
    SUM_VALUES_FOR_ALL_URLS_VALUES = "bot-facebook_202206.csv"
    
    def __init__(self,link):
        current_directory = os.getcwd()
        with open(Browser.SUM_VALUES_FOR_ALL_URLS_VALUES, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["URL", "MD5", "ToplamBegeni", "ToplamYorum", "ToplamPaylasim"])
       
        self.link = link
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        self.browser = webdriver.Chrome(current_directory+'/chromedriver',chrome_options=chrome_options)
        self.browser.maximize_window()
        Browser.goFacebook(self)
    
    def goFacebook(self):

        for url in urlList.urlList:

            self.browser.get(url)
            time.sleep(2)
            Browser.login(self)
            Browser.takeScreenShot(self,url)
            # Browser.getlikes(self)
            Browser.postInfo(self,url)
    

    def postInfo(self,url):  
        allPostsObject = []
       
        sumLikeCount = 0
        sumCommentCount = 0
        sumShareCount = 0
        SumCsvPrefixName ="bot-facebook_" 
        hashedUrl = Browser.hashMd5(url)
        fullCsvUrl = SumCsvPrefixName + hashedUrl + ".csv"
        i=0
        with open(fullCsvUrl, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Sum Like Count", "Sum Comment Count", "Sum Share Count"])
        
        while(i<=2):    
            Browser.scrolDown(self)
            time.sleep(1)
            posts = self.browser.find_elements(By.CLASS_NAME,"du4w35lb.k4urcfbm.l9j0dhe7.sjgh65i0") 
            time.sleep(1)
            for p in posts:
                if p not in allPostsObject:
                    allPostsObject.append(p) 
                    print("-----------------------------------------------")
                    try:
                        postLike = p.find_element(By.CSS_SELECTOR,"span.pcp91wgn").text
                        if postLike == '':
                            postLike = 0
                        elif "B" in postLike: 
                            postLike.replace('B', '')
                            if "," in postLike:
                                postLike.replace(',', '')
                            postLike.strip()
                            postLike+00    
                    except:
                        postLike = 0
                    try:
                        postShareAndCommentString = p.find_element(By.CLASS_NAME,"bp9cbjyn.j83agx80.pfnyh3mw.p1ueia1e").text          
                        commentcount = Browser.GetCommentCount(str(postShareAndCommentString))
                        sharecount =  Browser.GetShareCount(str(postShareAndCommentString))                      
                        time.sleep(1)
                    except:
                        commentcount = 0
                        sharecount =  0   
                    
                    # print("likeCount: " ,postLike ," ShaheAndCommentInfo: ",postShareAndCommentString )
                    # print ("commentcount" , commentcount)
                    # print ("sharecount" , sharecount) 
                    with open(fullCsvUrl, 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([postLike, commentcount, sharecount])    

                    sumLikeCount = sumLikeCount + int(postLike)
                    sumCommentCount = sumCommentCount + int(commentcount)
                    sumShareCount = sumShareCount + int(sharecount)       
                else:
                    continue  
                           
            i=i+1
        with open(Browser.SUM_VALUES_FOR_ALL_URLS_VALUES, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([url, fullCsvUrl, sumLikeCount, sumCommentCount, sumShareCount])
        
    def login(self):
        try:
            username=self.browser.find_element(By.NAME,"email")
            password=self.browser.find_element(By.NAME,"pass")

            if username != None and password != None:
                username.send_keys(kb.userName)
                password.send_keys(kb.password)
                time.sleep(2)

                loginBtn = self.browser.find_element(By.CSS_SELECTOR,"#loginbutton")
                loginBtn.click()
                time.sleep(5)      
        except:
            print("Non Login Page !")


    def scrolDown(self):
            html = self.browser.find_element(By.TAG_NAME,'html')
            html.send_keys(Keys.END)

    def takeScreenShot(self,url): 
        pngPrefixName ="bot-facebook_" 
        hashedUrl = Browser.hashMd5(url)
        fullPngName = pngPrefixName + hashedUrl
        self.browser.save_screenshot(fullPngName +".png")
        # screenshot = Image.open("ss.png")
        # screenshot.show()

    def hashMd5(plainText):
        return hashlib.md5(plainText.encode('utf-8')).hexdigest()

    def GetCommentCount(postShareAndCommentString):   
        if "Yorum" in postShareAndCommentString:
           end = postShareAndCommentString.index('Y')
           return int(postShareAndCommentString[0:end].strip())
        else:
            return 0

    def GetShareCount(postShareAndCommentString):    
        if "Paylaşım" in postShareAndCommentString:        
           if "Yorum" in postShareAndCommentString:
            splittedArray = postShareAndCommentString.split('\n')
            end = splittedArray[1].index('P')
            return int(splittedArray[1][0:end].strip())
           else:
            end = postShareAndCommentString.index('P')
            return int(postShareAndCommentString[0:end].strip())
        else:
            return 0