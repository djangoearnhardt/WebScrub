# This script accesses sensitive information, so I've intentionally omitted components and marked then with ***
# Make sure  to install selenium for python and download the chrome driver executable. can install selenium pip3 install -u selenium
# Import lists: os for file management, selenium for web driving, time for pausing between navigation, datetime for recording time of submission
import os
import csv
import selenium
import time
import datetime
from time import gmtime, strftime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#define chromedriver location
#reference https://selenium-python.readthedocs.io/installation.html#drivers
local = '/Users/***/Desktop/chromedriver'
driver = webdriver.Chrome(local)
driver.maximize_window()

# Define start time
start = time.time()

# Open Otix Login
driver.get(***)
time.sleep(1)
# Find the email box
id_box = driver.find_element_by_name('j_username')
# Send email information
id_box.send_keys(***)
# Find the password box
pass_box = driver.find_element_by_name('j_password')
# Send password
pass_box.send_keys(***)
# Find login button
login_button = driver.find_element_by_id('btnLogin')
# Click login
login_button.click()
time.sleep(1)

# Find Season from Drop Down Menu
production_drop = driver.find_element_by_xpath('//*[@id="top_row"]/span[1]/select')
production_drop.click()
# Select AMFS Season
select = Select(production_drop)
select.select_by_index(1)

# Define Patron Names and Patron ID
tup = (***)
# Select a patron from tup, and cycle through these results
x = 0
for tu in tup:
  search = str(tup[x][0])
  print(search)
  # Find Patron Search
  patron_link = driver.find_element_by_id('top_search')
  # Click Patron Search
  search_click = patron_link.click()
  # Find First Name Box
  first_name_box = driver.find_element_by_name('firstName')
  # Send Patron Name
  first_name_box.send_keys(search)
  # Submit Patron Name
  first_name_box.submit()
  # The results are too low to find, so this scrolls to the bottom of the page. Very useful fix.
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  #patron_link = driver.find_element_by_link_text('Test')
  patron_link = driver.find_element_by_link_text(search)
  patron_link.click()
  # Switch to iframe with our information
  iframe1 = driver.find_element_by_id('subApplicationIframe')
  driver.switch_to.frame(iframe1)
  time.sleep(2)
  #sell_link = driver.find_element_by_partial_link_text('Sell tickets')
  sell_link = driver.find_element_by_xpath('//*[@id="myContent"]/div[3]/div/div[3]/div[1]/a/div')
  sell_link.click()
  production_drop = driver.find_element_by_id('production')
  select = Select(production_drop)
  # Select an event for current patron, and cycle through all events
  # Choose two points to log out and back in to keep the script running
  re_log_points = set((20,70))
  y = 0
  sel = select.options
  for se in sel:
    print(y)
    print(len(sel))
    # Otix will go to sleep under selenium. This will log you back in after half the events are gone through.
    if y in re_log_points:
      exit = driver.find_element_by_xpath('//*[@id="home"]')
      exit.click()
      re_log = driver.find_element_by_link_text('[log out]')
      re_log.click()
      id_box = driver.find_element_by_name('j_username')
      # Send email information
      id_box.send_keys(***)
      # Find the password box
      pass_box = driver.find_element_by_name('j_password')
      # Send password
      pass_box.send_keys(***)
      # Find login button
      login_button = driver.find_element_by_id('btnLogin')
      # Click login
      login_button.click()
      time.sleep(1)
      # Find Season from Drop Down Menu
      production_drop = driver.find_element_by_xpath('//*[@id="top_row"]/span[1]/select')
      production_drop.click()
      # Select AMFS Season
      select = Select(production_drop)
      select.select_by_index(1)
      patron_link = driver.find_element_by_id('top_search')
      # Click Patron Search
      search_click = patron_link.click()
      # Find First Name Box
      first_name_box = driver.find_element_by_name('firstName')
      # Send Patron Name
      first_name_box.send_keys(search)
      # Submit Patron Name
      first_name_box.submit()
      # The results are too low to find, so this scrolls to the bottom of the page. Very useful fix.
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      #patron_link = driver.find_element_by_link_text('Test')
      patron_link = driver.find_element_by_link_text(search)
      patron_link.click()
      # Switch to iframe with our information
      iframe1 = driver.find_element_by_id('subApplicationIframe')
      driver.switch_to.frame(iframe1)
      time.sleep(2)
      #sell_link = driver.find_element_by_partial_link_text('Sell tickets')
      sell_link = driver.find_element_by_xpath('//*[@id="myContent"]/div[3]/div/div[3]/div[1]/a/div')
      sell_link.click()
    production_drop = driver.find_element_by_id('production')
    production_drop.click()
    # Select Event 
    select = Select(production_drop)
    select.select_by_index(y)
    # Find Package Text for CSV file
    package = driver.find_element_by_xpath('//*[@id="priceLevelLegend"]/h2')
    p_n = package.text
    # Find A Seat. Can't be the first one since the grid isn't uniform. 12 is arbitrary but reaches open seats in smaller concerts.
    seat_2 = driver.find_elements_by_css_selector("a[class=imgLink]")
    seat_2[12].click()
    # Add Seat to Cart
    add_to_cart = driver.find_element_by_xpath('//*[@id="mainSection"]/div[2]/div[4]/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td[1]/div[2]/a')
    add_to_cart.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Expand Cart Details
    expand_cart = driver.find_element_by_css_selector("img[id*=arrow_tickets]")
    expand_cart.click()
    time.sleep(2)
    # Turn Results into Text
    cart = driver.find_element_by_xpath('//*[@id="deleteForm"]/table/tbody/tr/td/table/tbody')        
    cart_result = cart.text
    patron = driver.find_element_by_id('patronName')
    p_t = patron.text
    info = driver.find_element_by_class_name('information')
    info_result = info.text
    # Break Text Results into an Arrays
    cart_split = cart_result.split('\n')
    cart_tick = cart_split[1].split()
    p_t_split = p_t.split(', ')
    info_split = info_result.split('\n')
    time.sleep(1)

    # Clear Cart 
    clear = driver.find_element_by_xpath('//*[@id="mainSection"]/div[2]/div[5]/div[1]/div/div[2]/a[2]')
    clear.click()
    alert = driver.switch_to.alert.accept()
    time.sleep(1)
    
    # Write a csv file for our results
    with open('***.csv', mode='a') as csv_file:
      fieldnames = ['Patron', 'Package', 'Event', 'Fee', 'Ticket Value']
      writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
      if y == 0:
        writer.writeheader()
      writer.writerow({'Patron': p_t_split[1], 'Package': p_n, 'Event': cart_split[0].strip('(1) '), 'Fee': cart_split[2].strip('+ '), 'Ticket Value': cart_split[3:7]})
  # Exit Quick Sell
    if y < (len(sel) - 4):
      y += 1
    elif y == (len(sel) - 4):
  # I don't want to test the last three events
      exit = driver.find_element_by_xpath('//*[@id="home"]')
      exit.click()
      break
  x += 1
  if x == len(tup):
    break
# Print the time elapsed to run the code
end = time.time()
elapsed = end - start
print('Completed')
print(elapsed)
