#Importing necessary libraries

import wget
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

#Setting up account, password, and download location
username = 'YourUsername'  # This is the insatgram username
# ---------------------------
password = 'YourPassword'  # This is the password
# ----------------------------------
dest_loc = r'TheDestination' #Here is the Directory to install images at

# So step by step what will we do as humans ?
#Step 1 open instagram
#Step 2 loging into our account
#Step 3 Bypassing any pop ups
#Step 4 Search for the brand-name we got from slash
#Step 5 If we are seeing the products we keep scrolling that's what we will do
#Finaly Step 6 install the images into the needed directiory

# Step 1
# Opening with Firefox.
driver = webdriver.Firefox()
# ----------------------------------
driver.maximize_window()
# Opening Instagram
driver.get('https://www.instagram.com')
time.sleep(5)

#Step 2
# Locating the username input box
username_box = driver.find_element(By.XPATH, '//input[@name="username"]')
username_box.send_keys(username)  # Sending the username to the input box
username_box.send_keys(Keys.ENTER)

# Locating the password input box
password_box = driver.find_element(By.XPATH, '//input[@aria-label="Password"]')
password_box.send_keys(password)
password_box.send_keys(Keys.ENTER)
time.sleep(12)

#Step 3 "Take care of case senstivity took me some mins to figure out the problem here !"
# Handling the first pop-up (Not now)
not_now_button = driver.find_element(By.XPATH, "//div[text()='Not now']")
not_now_button.click()
time.sleep(5)

# Handling the second pop-up (Not Now for Notifications)
notifications_not_button = driver.find_element(By.XPATH, "//button[text()='Not Now']")
notifications_not_button.click()
time.sleep(5)

#Step 4
# Locating and clicking the search button
search_button = driver.find_element(By.XPATH, "(//div[@class='x1iyjqo2 xh8yej3']/div)[2]")
search_button.click()

# Locating the search box and entering the desired search query
search_box = driver.find_element(By.XPATH, '//input[@aria-label="Search input" and @placeholder="Search"]')
search_query = input('Enter the brand name : ')
search_box.send_keys(search_query)
time.sleep(5)

# Clicking on the first result of the search
first_finding_account = driver.find_element(By.XPATH, '(//div[@class="x9f619 x78zum5 xdt5ytf x1iyjqo2 x6ikm8r x1odjw0f xh8yej3 xocp1fn"]/a)[1]')
first_finding_account.click()
time.sleep(3)

#Step 5
account_images = set()
while True:
    images = driver.find_elements(By.XPATH,
                                  '//img[@class="x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3"]')
    for image in images:
        source = image.get_attribute('src')
        account_images.add(source)

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    time.sleep(3)

    number_of_images = driver.find_element(By.XPATH,
                                           "//*[contains(@class,'html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs')]").text
    int_number_of_images = int(number_of_images.replace(',', ''))
    if len(account_images) >=50:
        break


# Showing the number of links in the account_images set
print(len(account_images))

#Step 6
# Downloading the images to the specified folder
for image in account_images:
    wget.download(image, dest_loc)   # downloading the images to the specified folder (dest_loc).