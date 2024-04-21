from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Replace with the website URL where you enter the registration number
website_url = "https://unnportal.unn.edu.ng/putme_login"

# Replace with the ID or name of the text box where you enter the registration number
reg_number_textbox_id = "reg_no"

# Replace with the class name of the button that triggers the download
download_button_class = "rse-button"

# Path where you want to save the downloaded PDFs (replace with your desired path)
download_folder = os.getcwd()

# Replace with your list of registration numbers
registration_numbers = ["202330556803CA", "202331451080jf", "202330602126HF"]

# Open a headless Chrome browser (replace with your preferred browser if needed)
driver = webdriver.Chrome()
driver.get(website_url)

for reg_number in registration_numbers:
    try:
        # Wait for the registration number textbox to be visible
        reg_number_textbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, reg_number_textbox_id)))
        
        # Enter the registration number
        reg_number_textbox.clear()  # Clear any previous input
        reg_number_textbox.send_keys(reg_number)
        reg_number_textbox.send_keys(Keys.RETURN)  # Submit the form (adjust if needed)
        print(f"Entered registration number: {reg_number}")

        # Wait for the print button to be clickable
        putme_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, download_button_class)))
        putme_button.click()
        print("Clicked the 'Print PUTME Slip' button after waiting!")

        # Switch to the print window
        # print_window = driver.window_handles[-1]
        # driver.switch_to.window(print_window)

        # Wait for the download link to appear (adjust if needed)
        WebDriverWait(driver, 10).until(EC.url_contains(".pdf"))

        # Download the PDF using the browser's built-in capabilities
        driver.execute_script('window.print();')  # This will trigger the print dialog and download the PDF

        print(f"Downloaded PDF for registration number: {reg_number}")

    except Exception as e:
        print(f"Error processing registration number: {reg_number}")
        print(e)

    finally:
        try:
            # Close the print window
            driver.close()

            # Switch back to the main window if there are any remaining windows
            if len(driver.window_handles) > 0:
                driver.switch_to.window(driver.window_handles[0])
        except:
            pass  # Ignore any exceptions when closing windows

# Close the WebDriver session when done
driver.quit()

print("Download completed for all registration numbers (if successful).")
