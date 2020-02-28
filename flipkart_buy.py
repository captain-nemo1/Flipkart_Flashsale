#Flash Sale helper made using Selenium 
#for BUY OPTION
#Needs Firefox and geckodriver installed
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

flag=True#will turn to false and stop script if item added to cart
driver = webdriver.Firefox()
#place the url here in the parenthesis
driver.get("https://www.flipkart.com/redmi-note-7-pro-neptune-blue-64-gb/p/itmfhvueapyyqn2d?pid=MOBFHUQ4WFPBGHPK&lid=LSTMOBFHUQ4WFPBGHPK6AU3AO&marketplace=FLIPKART&srno=b_1_1&otracker=hp_rhs_announcement_1_3.rhsAnnouncement.RHS_ANNOUNCEMENT_L4CTQMECKL9E&fm=neo%2Fmerchandising&iid=d6df9866-75ee-430f-8e65-89159b62212b.MOBFHUQ4WFPBGHPK.SEARCH&ppt=browse&ppn=browse&ssid=vzzv1vcrtlhvgxds1582874154172")

while flag:
    try:
        button=driver.find_element_by_class_name("_7UHT_c")#this is the class of buy button
        button.click()#click on it
        flag=False#so as to not load page again after successfully added to cart
        time.sleep(.5)
    except:
            driver.refresh()#if not added to cart then refresh page
