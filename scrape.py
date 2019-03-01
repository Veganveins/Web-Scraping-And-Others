from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup
import requests
import time
import csv
from datetime import timedelta, date

basic_url = "https://www.nytimes.com/crosswords/game/mini/"
links = []
start_date = date(2018, 7, 1)
end_date = date(2019, 1, 23)

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

for single_date in daterange(start_date, end_date):
    links.append(basic_url + single_date.strftime("%Y/%m/%d"))

times = []

browser = webdriver.Firefox() #replace with .Firefox(), or with the browser of your choice
url = "https://myaccount.nytimes.com/auth/login?URI=https%3A%2F%2Fwww.nytimes.com%2Fcrosswords"
browser.get(url) #navigate to the page

username = browser.find_element_by_id("username") #username form field
password = browser.find_element_by_id("password") #password form field

# username.send_keys("danjplunkett@gmail.com")
# time.sleep(5)
# password.send_keys("Jplunkett1!")
# time.sleep(5)
username.send_keys("waltz22r@mtholyoke.edu")
password.send_keys("March151995")



submitButton = browser.find_element_by_id("submitButton") 
submitButton.click() 
time.sleep(120)

for link in links:
	browser.get(link)
	solution_time = browser.find_element_by_css_selector('div.timer-count')
	print(solution_time.text, link[-10:])
	times.append(solution_time.text)


myFyle = open("rose2.csv",'w')
wr = csv.writer(myFyle, dialect='excel')
for time in times:
	wr.writerow(time)
