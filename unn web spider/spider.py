from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os

# Replace with the website URL where you enter the registration number
website_url = "https://unnportal.unn.edu.ng/putme_login"

# Replace with the ID or name of the text box where you enter the registration number
reg_number_textbox_id = "reg_no"

login_button = "login" #login button

# Replace with the ID or name of the button that triggers the download
download_button_id = "download_button"

# Path where you want to save the downloaded PDFs (replace with your desired path)
download_folder = os.getcwd()

# Replace with your list of registration numbers
registration_numbers = ["202330556803CA", "202331451080jf", "202330602126HF"]

# Open a headless Chrome browser (replace with your preferred browser if needed)
driver = webdriver.Chrome()
driver.get(website_url)

for reg_number in registration_numbers:
  # Enter the registration number
  reg_number_textbox = driver.find_element(By.ID, reg_number_textbox_id)
  reg_number_textbox.send_keys(reg_number)
  reg_number_textbox.send_keys(Keys.RETURN)  # Submit the form (adjust if needed)
  print("made it")
  # click login button
  #login_button = driver.find_element(By.ID, login_button_id)
  #login_button.click()

  # click print putme slip button
  #wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for the element to be clickable
  try:
    # Wait for the button to be clickable
    wait = WebDriverWait(driver, 10)
    putme_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "rse-button")))
    putme_button.click()
    print("Clicked the button after waiting!")

  except EnvironmentError:
    print("Error: Button not clickable after waiting 10 seconds.")

    print("Got here")

#   # Click the download button (adjust selector if needed)
#   download_button = driver.find_element(By.CLASS_NAME, "action-button")
#   download_button.click()
    
  pdf_url = driver.current_url
  response = requests.get(pdf_url)

  # Wait for download to complete (replace with a more robust method if needed)
  # This is a basic example, actual waiting time might vary
  import time
  time.sleep(10)  # Wait for 10 seconds

  filename = f"{download_folder}{reg_number}.pdf"
  with open(filename, 'wb') as f:
      f.write(response.content)

  # Clear the registration number textbox for the next iteration
  reg_number_textbox.clear()

driver.quit()

print("Download completed for all registration numbers (if successful).")
