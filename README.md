```markdown
# Selenium Data-Driven Tests with MySQL

This project demonstrates **data-driven testing** using **Selenium WebDriver** and **pytest**, with test data stored in a **MySQL database**. It also includes a **GitHub Actions workflow** to run tests automatically in CI.

---

## Project Structure

```

.
├── create\_mysql\_data.py        # Script to create DB and insert test data
├── conftest.py                 # Pytest fixtures for Selenium and MySQL
├── test\_login\_mysql.py         # Data-driven Selenium tests
└── .github/workflows/
└── python-selenium.yml    # GitHub Actions CI workflow

````

---

## Prerequisites

- Python 3.13+
- MySQL server
- Google Chrome (or ChromeDriver for local runs)
- pip packages:
  ```bash
  pip install selenium mysql-connector-python pytest
````

---

## Setup MySQL Test Data

Run the script to create the database, table, and insert test credentials:

```bash
python create_mysql_data.py
```

This creates:

* Database: `selenium_tests`
* Table: `login_data` with columns:

  * `id` (INT, AUTO\_INCREMENT)
  * `username` (VARCHAR)
  * `password` (VARCHAR)
* Sample test data:

  * `tomsmith / SuperSecretPassword!`
  * `invalid_user / SuperSecretPassword!`
  * `tomsmith / invalid_password`

---

## Running Tests Locally

Run pytest with verbose output:

```bash
pytest -v
```

* The `conftest.py` fixture provides:

  * Headless Selenium Chrome WebDriver
  * Test data fetched from MySQL

* Tests navigate to [The Internet Login Page](https://the-internet.herokuapp.com/login) and verify login attempts.

---

## GitHub Actions CI

* Workflow file: `.github/workflows/python-selenium.yml`
* Features:

  * Runs on `ubuntu-latest`
  * Installs Python, Chrome, ChromeDriver
  * Starts MySQL service
  * Runs `create_mysql_data.py` to populate DB
  * Executes `pytest` tests automatically on push or pull request to `main`

---

## Notes

* Ensure MySQL root password matches `create_mysql_data.py` and workflow.
* Selenium runs **headless** in CI, so no GUI is required.
* You can expand tests with more data in the MySQL table.

---

## License

MIT License


