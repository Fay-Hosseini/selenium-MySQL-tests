import mysql.connector
import os

# Connect to MySQL
conn= mysql.connector.connect(
    host ="localhost",
    user ="root",
    password=os.getenv("MYSQL_PASSWORD")
)

cursor = conn.cursor()

#Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS selenium_tests")
cursor.execute("Use selenium_tests")

#Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS login_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
)
""")

# Insert test data
cursor.executemany("""
INSERT INTO login_data (username, password) VALUES (%s, %s)
""", [
    ("tomsmith", "SuperSecretPassword!"),
    ("invalid_user", "SuperSecretPassword!"),
    ("tomsmith", "invalid_password")

])

conn.commit()
conn.close()

print("✅ MySQL test data created successfully.")