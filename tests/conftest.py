# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DB = os.getenv("MYSQL_DB")

# --- Fixture for Selenium WebDriver (headless) ---
@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless")  # headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# --- Fixture for fetching test data from MySQL ---
@pytest.fixture(scope="session")
def login_data():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )
        cursor = conn.cursor()
        cursor.execute("SELECT username, password FROM login_data")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except mysql.connector.Error as e:
        pytest.exit(f"Database connection failed: {e}")
