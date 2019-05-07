'''
As an avid crossword puzzler, I subscribed to the new york times in July of 2018 to gain access to the daily puzzles. As a 

subscriber I also gain the benefit of keeping a historical log of my times for each mini puzzle I complete. I wondered how the 

subscription had affected my overall mini times. My hypothesis was, after subscribing and therefore completing more daily puzzles,

my overall "crossword IQ" if you will would go up, resulting in a faster average completion time. To test this hypothesis, I would

need the data. So I built a hacky webscraper in Python to hit the nytimes crossword, login with my credentials, and pull the 

times for each day a puzzle was completed. With the values stored in a Python list I could easily write them to a file for

some exploratory EDA in R. As an added bonus, I hassled a few friends into giving me their login credentials so I could scrape

their data as well and tell the story of who, truly, was the crossword puzzle champion.

Yes, I realize I am a humongous nerd. Sorry.
'''


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

# username.send_keys("xxxxxxxxxx@gmail.com")
# time.sleep(5)
# password.send_keys("supersecretpassword")
# time.sleep(5)
username.send_keys("your-nytimes-account-login-goes-here")
password.send_keys("your-nytimes-account-password-goes-here")



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
