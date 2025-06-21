# VTU Auto Login Bot

A Python automation bot that logs into the [VTU Online Portal](https://online.vtu.ac.in/login) automatically using Selenium. This tool handles form fields, scrolls to the login button, and clicks it using JavaScript for consistent and reliable automation. It also supports packaging into a `.exe` file with a custom icon for easy, terminal-free use on Windows.

---

## 🚀 Features

- Automates login to the VTU student portal using Selenium WebDriver
- Dynamically locates form fields and login button using robust selectors
- Scrolls to and clicks the "Sign in" button using JavaScript execution
- Uses `WebDriverWait` to handle dynamic page loads
- Keeps Chrome browser open after login for manual use
- Can be converted into a `.exe` with a custom icon and no console window

---

## 🛠 Tech Stack

- **Python 3**
- **Selenium**
- **ChromeDriver**
- **PyInstaller** (for `.exe` packaging)

---

## 📦 How to Run Locally

1. **Install Selenium** (if not already installed):

   ```bash
   pip install selenium

2. Download the correct ChromeDriver that matches your Chrome version from
https://chromedriver.chromium.org/downloads

3. Update the script:

Set the path to your downloaded chromedriver.exe

Fill in your VTU email and password

4. Run the bot:
    ```bash
    python VTU_login_bot.py

## How to Convert to .exe (Optional)
To create a terminal-free .exe with a custom icon:

Save your icon as vtu_icon.ico in the same folder

Run:

    
    pyinstaller --onefile --noconsole --icon="vtu_icon.ico" VTU_login_bot.py

Your `.exe` will be created inside the dist/ folder.

✅ You can now create a desktop shortcut with the custom icon.


## ⚠️ Development Challenges Faced  

Button Click Failure: .click() didn’t work due to overlays. Solved using JavaScript click() via driver.execute_script().  
Hidden Login Button: Resolved by using scrollIntoView() before clicking.  
Browser Auto-Close: Removed input() (which crashes in .exe) and used an infinite loop (while True) to keep Chrome open after login.  
Non-console Execution: Used PyInstaller’s --noconsole option and avoided any input prompts to prevent .exe from crashing.  
Icon Embedding: Packaged with a .ico file to improve presentation and usability.  

---
📌 Notes
Built for educational purposes and to demonstrate automation skills.
Do not use automation on any platform that prohibits it.

