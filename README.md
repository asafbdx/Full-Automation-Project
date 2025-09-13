# 🚀 Full Automation Project

A complete automation framework for **Web, Mobile, Desktop, Electron, and API testing**, built with a focus on **modularity, readability, and maintainability**.  
The project is implemented in **Python** using **PyTest, Selenium, Appium, Allure**, and other automation tools.  

---

## 📂 Project Structure

```
project/
│── configuration/
│   └── data.xml                 # Configuration and test data file
│
│── flows/                       # Flow layer - business logic and reusable flows
│   ├── WebFlows.py              # Web flows for Grafana
│   ├── APIFlows.py              # API flows for Team Management
│   ├── DBFlows.py               # Database flows (login via DB)
│   ├── MobileFlows.py           # Mobile flows (Mortgage Calculator)
│   ├── DesktopFlows.py          # Desktop flows (Windows Calculator)
│   └── ElectronFlows.py         # Electron flows (Task App)
│
│── page_objects/                # Page Object Models for each platform
│   ├── web/ (LoginPage, MainPage, LeftMenuPage, UpperMenuPage, UsersPage, AdministrationMenuPage, NewUsersPage)
│   ├── mobile/ (CalculatorPage, SavedPage)
│   ├── desktop/ (StandardPage)
│   └── electron/ (TaskPage)
│
│── utilities/
│   ├── utils.py                 # Utility functions (get_data, read_csv, wait, enums, etc.)
│   ├── UiActions.py             # Common UI actions (click, text, hover, drag-drop)
│   ├── MobileActions.py         # Mobile-specific actions (tap, swipe, zoom, pinch)
│   ├── APIActions.py            # API actions (GET, POST, PUT, DELETE)
│   ├── DBActions.py             # Database actions (query builder, fetch results)
│   └── Verifications.py         # Assertions and validations
│
│── tests/
│   ├── Test_Web.py              # Web tests for Grafana
│   ├── Test_Web_DB.py           # Combined Web + DB tests
│   ├── Test_API.py              # API tests for Teams CRUD
│   ├── Test_Mobile.py           # Mobile tests for Mortgage Calculator
│   ├── TestDesktop.py           # Desktop tests for Windows Calculator
│   └── Test_Electron.py         # Electron app tests (Task Manager)
│
│── conftest.py                  # PyTest fixtures: drivers, DB setup, Allure, Appium
│── ManagePages.py               # Initializes Page Objects for each platform
│── requirements.txt             # Project dependencies
└── README.md
```

---

## ⚙️ Technologies & Tools
- **Language:** Python 3.x  
- **Test Framework:** PyTest  
- **Web Automation:** Selenium, WebDriverManager  
- **Mobile Automation:** Appium  
- **Desktop Automation:** WinAppDriver  
- **Electron Automation:** ChromeDriver with binary configuration  
- **API Testing:** Requests  
- **Database:** SQLite3  
- **Reporting:** Allure Reports + Screenshots on failure  

---

## ▶️ Running Tests

### Web
```bash
pytest -s -v  .\test_web.py --alluredir=../allure-results
```

### Web + Database
```bash
pytest -s -v  .\test_web_db.py --alluredir=../allure-results
```

### API
```bash
pytest -s -v  .\test_api.py --alluredir=../allure-results
```

### Mobile
```bash
pytest -s -v  .\test_mobile.py --alluredir=../allure-results
```

### Desktop
```bash
pytest -s -v  .\test_desktop.py --alluredir=../allure-results
```

### Electron
```bash
pytest -s -v  .\test_electron.py --alluredir=../allure-results
```

---

## 📊 Reports
- **Allure Reports** are generated for all test runs.  
- Includes detailed steps, screenshots (on failure), and visual test coverage.  

---

## 🎯 Purpose
This project demonstrates a **full cross-platform automation framework** capable of handling:  
- Web testing with UI flows (Grafana).  
- API CRUD validation for teams.  
- Database-driven login tests.  
- Mobile mortgage calculator flows.  
- Desktop calculator tests (Windows).  
- Electron app task management automation.  

The framework follows **Page Object Model (POM)** and separates concerns into **Actions, Flows, Utilities, and Tests** for maximum maintainability.  


---

## 📦 Requirements

The project dependencies are listed in **`requirements.txt`**.  
This file ensures that anyone running the project installs the same versions of all required packages.

### Install dependencies

Before running the tests, install the required packages by running:

```bash
pip install -r requirements.txt
```

---

## 🖥️ Grafana Setup (Required for Web Tests)

To run the **Web tests**, you need to install and run **Grafana v12.0.2** locally.

### Steps:
1. Download **Grafana v12.0.2** from the official Grafana website:  
   [https://grafana.com/grafana/download](https://grafana.com/grafana/download)

2. Extract the downloaded archive to a local folder.

3. Navigate into the extracted Grafana directory:
  
4. Enter the bin folder

5. Open the file grafana-server

6. Now run the web test with pytest -s -v  .\test_web.py --alluredir=../allure-results



---

## ⚠️ Known Issues

- Sometimes there can be conflicts between dependencies that the applications are using.


- This project is intended **for DEMO purposes only**.  
- In a real production environment, the framework should be **split into separate projects** (Web, API, Mobile, Desktop, Electron, DB) for better scalability and maintainability.  
- Nevertheless, the file **`requirements.txt`** is attached so you can install the exact same library versions and extensions to reproduce the environment on your own system and run the entire test suite consistently.


## 🎥 Demo

![Project Demo](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExczk3YWF0cHNldTZpbGcyb3VuODU1NXpmbGV6Mm9zMmNkMnZ6b3lqNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ega4KTz4LTIGFAS5uo/giphy.gif)


