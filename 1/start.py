from typing import ItemsView
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver =webdriver.Chrome('/Users/betul.kul/Desktop/teleskop/chromedriver')
driver.get('https://www.facebook.com/KaracabeyBel')


Items = driver.find_element(By.CSS_SELECTOR, "#mount_0_0_Kt > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.j83agx80.cbu4d94t.dp1hu0rb > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div.rq0escxv.d2edcug0.ecyo15nh.hv4rvrfc.dati1w0a.tr9rh885 > div > div.rq0escxv.l9j0dhe7.du4w35lb.hpfvmrgz.buofh1pr.g5gj957u.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5.gile2uim.qmfd67dx > div > div:nth-child(1) > div.du4w35lb.k4urcfbm.l9j0dhe7.sjgh65i0 > div > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(4) > div > div > div:nth-child(1) > div > div.l9j0dhe7 > div > div.bp9cbjyn.j83agx80.buofh1pr.ni8dbmo4.stjgntxs > span.bzsjyuwj.ni8dbmo4.stjgntxs.ltmttdrg.gjzvkazv > span > span")
time.sleep(5)
print ("burda333")
print (Items)
share=driver.find_elements(By.CSS_SELECTOR, ".span.d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d9wwppkn iv3no6db jq4qci2q a3bd9o3v b1v8xokw m9osqain")
print (share)
for i in Items:
    print ("burda")
    like=driver.find_element(By.CSS_SELECTOR, ".span.pcp91wgn")
    share=driver.find_element(By.CSS_SELECTOR, ".span.d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d9wwppkn iv3no6db jq4qci2q a3bd9o3v b1v8xokw m9osqain")

    print (like)

 print(begeni)
        header=self.browser.find_element(By.CSS_SELECTOR,"#mount_0_0_mC.")
        print ("header")
        print(header)
        commentcount =self.browser.find_elements(By.CSS_SELECTOR,"#jsc_c_7")
        print("comment")
        print(commentcount)
        sharecount=self.browser.find_elements(By.CSS_SELECTOR,"#mount_0_0_X0.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.dp1hu0rb.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0.rq0escxv.d2edcug0.ecyo15nh.k387qaup.r24q5c3a.hv4rvrfc.dati1w0a.tr9rh885.rq0escxv.l9j0dhe7.du4w35lb.hpfvmrgz.g5gj957u.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5.gile2uim.pwa15fzy.fhuww2h9.l9j0dhe7.bp9cbjyn.j83agx80.pfnyh3mw.p1ueia1e")
        print ("share")
        print(sharecount)
        likecount1 = self.browser.find_elements(By.CLASS_NAME,"pcp91wgn")
        element=self.browser.find_element(By.ID,"jsc_c_7")
        print("element")
        print(element)
        print ("likecount1")
        print(likecount1)
        likecount =self.browser.find_elements(By.CSS_SELECTOR,"#mount_0_0_X0.nth-child(1).rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.dp1hu0rb.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0.rq0escxv.d2edcug0.ecyo15nh.k387qaup.r24q5c3a.hv4rvrfc.dati1w0a.tr9rh885.rq0escxv.l9j0dhe7.du4w35lb.hpfvmrgz.g5gj957u.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5.gile2uim.pwa15fzy.fhuww2h9.nth-child(2).nth-child(1).nth-child(2).nth-child(4).l9j0dhe7.bp9cbjyn.j83agx80.buofh1pr.ni8dbmo4.stjgntxs.gpro0wi8.cwj9ozl2.bzsjyuwj.ja2t1vim")
       
        for like in likecount:
            print ("betul")
            print(like.text)
        
