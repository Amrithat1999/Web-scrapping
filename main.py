###### Import needed Libraries ######

from selenium import webdriver
import time
import chromedriver_binary
from urllib.request import urlopen
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
import pandas as pd

###### Import chrome driver ######

driver = webdriver.Chrome('chromedriver')
profile_url=driver.get("https://www.hcpcsdata.com/Codes")

###### Maximise Window ######

driver.maximize_window()
time.sleep(1)


first=[]
codes=[]
Long_des=[]
ddd=[]
for fi in range(1,6):
    p='/html/body/div[1]/div/table/tbody/tr['+str(fi)+']/td[1]/a'
    s=driver.find_elements_by_xpath(p)
    code=[]
    Long_de=[]
    dd=[]
    for ss in s:
        ss.click()
        time.sleep(3)

        a=driver.find_elements_by_class_name('identifier')
        
        try:
            for aa in a:
                code.append(aa.text)
            cod=code[:10]
            codes.append(cod)
            time.sleep(3)
        except:
            pass

        try:
            for it in range(1,11):
                des=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/table/tbody/tr['+str(it)+']/td[2]')
                Long_de.append(des.text)
            Long_des.append(Long_de)
            time.sleep(3)

        except:
            pass

        
        try:
            for it in range(1,11):
                path='/html/body/div[1]/div/div[1]/table/tbody/tr['+str(it)+']/td[2]'
                ab=driver.find_elements_by_xpath(path)
                for abc in ab:
                    abc.click()
                    s_des=driver.find_element_by_xpath('//*[@id="codeDetail"]/tbody/tr[1]/td[2]')
                    
                    time.sleep(2)
                    dd.append(s_des.text)
                    driver.back()
                    time.sleep(1)

        except:
            pass
        ddd.append(dd)

    time.sleep(1)
    driver.back()
    time.sleep(2)

f_co=[]
for i in codes:
    for j in i:
        f_co.append(j)

Long=[]
for ii in Long_des:
    for jj in ii:
        Long.append(jj)

short=[]
for iii in ddd:
    for jjj in iii:
        short.append(jjj)

###### Create Dateframe ######
dat={'Code':f_co,'Long Description':Long,'Short Description':short}
data=pd.DataFrame(dat)
data['Group']="HCPCS 'A' Codes"
data['Category']="Transportation Services Including Ambulance, Medical & Surgical Supplies"


cols = data.columns.tolist()
cols = cols[-1:] + cols[:-1]
cols = cols[-1:] + cols[:-1]

###### Create Excel file ######

data=data[cols]
data.to_excel('hcpc_data.xlsx')