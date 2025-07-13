# SauceDemo Automation Project
QA Automation project for saucedemo.com using Selenium and Pytest


## Goal
Автоматизирани UI тестове на [saucedemo.com](https://www.saucedemo.com)

## Techologies
- Python 3
- Selenium Webdriver
- Pytest
- Allure Reports

## Steps for starting
```bash
pip install -r requirements.txt
pytest --alluredir=reports/
allure serve reports/
