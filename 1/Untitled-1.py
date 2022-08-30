
#from selenium.webdriver.chrome.service import Service
s=Service('/Users/betul.kul/Desktop/teleskop/chromedriver')
browser = webdriver.Chrome(service=s)
url='https://www.facebook.com/KaracabeyBel'
browser.get(url)




Items = driver.find_elements(By.CLASS_NAME, "wkznzc2l")



from webdriver_manager.chrome import ChromeDriverManager
#like = driver.find_element_by_id('toplamSatışAdedi').text
#ib=driver.find_element_by_class_name("pcp91wgn")
#print (ib)
Items = driver.find_elements_by_css_selector("span.l9j0dhe7")
Items = driver.find_elements_by_css_selector("span.l9j0dhe7")
#like=driver.find_element_by_id('<span aria-hidden="true" class="bzsjyuwj ni8dbmo4 stjgntxs ltmttdrg gjzvkazv"><span><span class="pcp91wgn">168</span></span></span>')
#comment = driver.find_element_by_id('<div class="gtad4xkn"><span class="tojvnm2t a6sixzi8 abs2jz4q a8s20v7p t1p8iaqh k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y iyyx5f41"><div aria-expanded="true" class="oajrlxb2 gs1a9yip mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o tgvbjcpo hpfvmrgz esuyzwwr f1sip0of n00je7tq arfg74bv qs9ysxi8 k77z8yql pq6dq46d btwxx1t3 abiwlrkh lzcic4wl dwo3fsh8 g5ia77u1 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv gmql0nx0 kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h du4w35lb gpro0wi8" id="jsc_c_12d" role="button" tabindex="0"><span class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d9wwppkn iv3no6db jq4qci2q a3bd9o3v b1v8xokw m9osqain" dir="auto">22 Yorum</span></div></span></div>').text
#share = driver.find_element_by_id('<div class="gtad4xkn"><span class="tojvnm2t a6sixzi8 abs2jz4q a8s20v7p t1p8iaqh k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y iyyx5f41"><div class="oajrlxb2 gs1a9yip mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o tgvbjcpo hpfvmrgz esuyzwwr f1sip0of n00je7tq arfg74bv qs9ysxi8 k77z8yql pq6dq46d btwxx1t3 abiwlrkh lzcic4wl dwo3fsh8 g5ia77u1 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv gmql0nx0 kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h du4w35lb gpro0wi8" role="button" tabindex="0"><span class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d9wwppkn iv3no6db jq4qci2q a3bd9o3v b1v8xokw m9osqain" dir="auto">25 Paylaşım</span></div></span></div>')
#print(m)
#print(comment)
#<span class="pcp91wgn">3</span>
#//*[@id="mount_0_0_xg"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[1]