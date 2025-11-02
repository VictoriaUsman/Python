from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

title = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

#Finding the Events, and date of Events Using Selenium
list = []
for number in range(1):
    initial = (title[number].text)
    for i in range(10):
        key = initial.split("\n")[i]
        list.append(key)

date = list[:10:2]
events = list[1:10:2]


#Adding to dictionary

event = [{"oras": date[i], "ganap": events[i]} for i in range(5)]
print(event)