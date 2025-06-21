from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
import time

def startBot(email, password, url):
    path = r"C:\Users\Pavanchandra Devang\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

    print("🔧 Launching Chrome browser...")
    options = Options()
    # options.add_argument("--headless")  # Optional: hide browser

    service = Service(path)
    driver = webdriver.Chrome(service=service, options=options)

    print(f"🌐 Navigating to {url}")
    driver.get(url)

    try:
        wait = WebDriverWait(driver, 15)

        print("⌛ Waiting for input fields...")
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        print("✍️  Typing email and password...")
        email_field.send_keys(email)
        password_field.send_keys(password)

        print("🔍 Locating 'Sign in' button...")
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

        print("📜 Scrolling to the button...")
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        time.sleep(1)

        print("🖱️  Clicking 'Sign in' button with JavaScript...")
        driver.execute_script("arguments[0].click();", submit_button)

        print("✅ Login click submitted.")
    except Exception as e:
        print("❌ Error during login:", e)
    # 🔁 Keeps browser open
    print("⏳ Browser will stay open. Close it manually when done.")
    while True:
        time.sleep(60)

# Secure input
print("🔐 VTU Login")
email = "pavanchandradevangl@gmail.com"
password = ""
url = "https://online.vtu.ac.in/login"

startBot(email, password, url)
