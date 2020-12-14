from selenium import webdriver
import time
import urllib
import urllib2

x=raw_input("www.fflatest.xyz")
refreshrate=raw_input("15")
refreshrate=int(refreshrate)
driver = webdriver.Firefox()
driver.get("http://"+x)
while True:
    time.sleep(refreshrate)
    driver.refresh()
