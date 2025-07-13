import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    options = webdriver.ChromeOptions()

    # 🧼 Използваме чист профил (временна папка)
    user_data_dir = os.path.abspath("tmp/test-profile")
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # 🔕 Изключваме warning за пароли
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    # 💡 Флагове за избягване на Chrome security интервенции
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    options.add_argument("--start-maximized")

    # 🧪 Премахва "Chrome is being controlled..." съобщение
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver
