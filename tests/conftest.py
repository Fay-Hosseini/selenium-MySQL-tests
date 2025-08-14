# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import mysql.connector
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env (for local development)
load_dotenv()

# MySQL connection info from environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
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
    if not all([MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB]):
        pytest.exit(
            "Missing MySQL environment variables. Make sure MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, and MYSQL_DB are set."
        )

    # Retry connection a few times in case the MySQL container is still starting
    for attempt in range(10):
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
            if attempt < 9:
                time.sleep(2)  # wait before retrying
            else:
                pytest.exit(f"Database connection failed after retries: {e}")
