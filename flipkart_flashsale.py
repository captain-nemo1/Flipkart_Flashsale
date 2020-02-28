#Flash Sale helper made using Selenium
#Needs Firefox and geckodriver installed
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

flag=True#will turn to false and stop script if item added to cart
driver = webdriver.Firefox()
#place the url here in the parenthesis
driver.get("https://www.flipkart.com/iqoo-3-5g-tornado-black-256-gb/p/itmafb0d2484a4d9?pid=MOBFP4P2HCJBY5YN&lid=LSTMOBFP4P2HCJBY5YNLX4GEI&marketplace=FLIPKART&srno=b_1_1&otracker=browse&fm=neo%2Fmerchandising&iid=40ceba7a-a5b0-4fdf-a148-6310aa8d7689.MOBFP4P2HCJBY5YN.SEARCH&ppt=browse&ppn=browse&ssid=0qe21d7xdelbiyv41582890515687")

while flag:
    try:
        button=driver.find_element_by_class_name("_2Npkh4")#this is the class of add to cart button
        button.click()#click on it
        flag=False#so as to not load page again after successfully added to cart
        time.sleep(.5)
    except:
            driver.refresh()#if not added to cart then refresh page
