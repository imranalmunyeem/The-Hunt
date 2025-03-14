# 🔍 The-Hunt ➡ (Automated Information Gathering Tool)
🚀 An advanced OSINT tool for Active & Passive reconnaissance.
 
## 📖 Table of Contents
- [Introduction](#📌-introduction)
- [Tools & Libraries Used](#🛠️-tools--libraries-used)
- [Features](#🌟-features)
- [Project Structure](#📂-project-structure)
- [Installation](#⚡-installation)
- [Usage](#🛠-usage)
- [Scanners & Functionalities](#🔍-scanners--functionalities)
- [Configuration (API Keys)](#⚙️-configuration-api-keys)
- [Future Enhancements](#🚀-future-enhancements)
- [Contributing](#📝-contributing)
- [License](#📜-license)

## 📌 Introduction
This tool automates information gathering for ethical hackers, penetration testers, and security researchers.
It provides both Active and Passive reconnaissance techniques, allowing users to scan domains, IPs, emails, and websites efficiently.

✅ OSINT-focused reconnaissance tool
✅ APIs integration with Shodan, VirusTotal, Have I Been Pwned
✅ Modular design (easy to add new scanners)
✅ Built using Python & Streamlit

## 🛠️ Tools & Libraries Used

[![Python](https://img.shields.io/badge/Python-17202C?style=for-the-badge&logo=python&logoColor=yellow)](https://www.python.org/) 
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)

### 1️⃣ Core Python Libraries ➡️
##### 🌐 socket ➜ Fetches IP addresses of domains  
##### 🔍 re ➜ Regular expressions for parsing emails, URLs, etc.  
##### 📄 json ➜ Handles API responses and data serialization  
##### 🖥️ os ➜ Interacts with system commands (if needed)  
<br>

### 2️⃣ Web Scraping & HTTP Requests ➡️
##### 🌍 requests ➜ Sends HTTP requests to websites and APIs
##### 🏗️ BeautifulSoup ➜ Extracts information from HTML pages
##### 🕷️ Scrapy ➜ (Optional) For advanced web crawling
<br>

### 3️⃣ DNS & WHOIS Lookup ➡️
##### 📡 python-whois ➜ Retrieves WHOIS information for domains
##### 🌍 dnspython ➜ Resolves DNS records (A, MX, TXT, NS, CNAME)
<br>

### 4️⃣ OSINT & Cybersecurity APIs ➡️
##### 🔎 Shodan ➜ Finds open ports, services, vulnerabilities
##### 🛡️ VirusTotal ➜ Checks if a domain/IP is blacklisted
##### 🔐 Have I Been Pwned (HIBP) ➜ Checks if emails are in data breaches
##### 🌍 crt.sh ➜ Finds subdomains using certificate transparency logs
##### 🔄 ViewDNS ➜ Performs reverse IP lookups
<br>

### 5️⃣ Social Media & GitHub Intelligence ➡️
##### 📱 Selenium ➜ Scrapes social media profiles
##### 🛠️ GitHub API ➜ Finds leaked credentials in public repositories
<br>

### 6️⃣ Web Framework & UI ➡️
##### 📊 Streamlit ➜ Creates an interactive web-based UI
<br>

### 7️⃣ Reporting & Export ➡️
##### 📑 pandas ➜ Processes and formats scanned data
##### 📄 pdfkit ➜ (Optional) Converts reports to PDF
##### 📊 csv ➜ Saves results in CSV format

## 🌟 Features
##### ✅ Active Information Gathering – Performs direct interaction-based reconnaissance, retrieving real-time data from the target.
##### ✅ Passive Information Gathering – Collects publicly available data without directly interacting with the target, ensuring stealth.
##### ✅ WHOIS Lookup – Fetches domain ownership details, registration dates, and contact information for domain intelligence.
##### ✅ DNS Records Retrieval – Extracts A, MX, NS, TXT, and CNAME records to analyze domain configurations.
##### ✅ IP & Hosting Information – Resolves the domain’s IP address and provides hosting provider details for footprint analysis.
##### ✅ Website Vulnerability Scanning – Identifies exposed directories, outdated software, and misconfigurations for security assessment.
##### ✅ Shodan Open Ports & Services Check – Leverages the Shodan API to detect publicly exposed ports and running services.
##### ✅ Email Harvesting – Extracts email addresses from the target’s website and indexed pages for contact enumeration.
##### ✅ Social Media Profile Discovery – Searches for associated social media accounts using OSINT techniques.
##### ✅ Website Technology Stack Identification – Detects CMS, JavaScript frameworks, web server details, and third-party services.
##### ✅ VirusTotal Domain Reputation Check – Verifies if a domain or IP is flagged for malware, phishing, or abuse reports.
##### ✅ Data Breach Lookup via Have I Been Pwned – Checks if emails linked to the domain have been exposed in past breaches.
##### ✅ GitHub Leaks Discovery – Searches for leaked credentials, API keys, and sensitive data in public GitHub repositories.
##### ✅ Streamlit Web UI – Provides an intuitive, user-friendly interface for seamless scanning and results visualization.
##### ✅ Modular & Scalable Architecture – Implements an Object-Oriented design, allowing easy extension with additional scanners.


## 📂 Project Structure
```
|-- info_gathering_tool
|     |-- modules                                  # Core scanning modules
|          |-- base_scanner.py                     # Parent class for all scanners
|          |-- active_scanner.py                   # Manages active information gathering
|          |-- passive_scanner.py                  # Manages passive information gathering
|          |-- scanners                            # Individual scanners for different tasks
|               |-- whois_scanner.py               # WHOIS lookup scanner
|               |-- dns_scanner.py                 # DNS records scanner
|               |-- ip_scanner.py                  # IP & hosting information scanner
|               |-- email_scanner.py               # Email harvesting scanner
|               |-- social_media_scanner.py        # Social media profile scanner
|               |-- tech_stack_scanner.py          # Technology stack detection scanner
|               |-- vulnerability_scanner.py       # Website vulnerability scanner
|               |-- shodan_scanner.py              # Shodan API scanner (open ports, services)
|               |-- virustotal_scanner.py          # VirusTotal API scanner (domain reputation)
|               |-- hibp_scanner.py                # HIBP API scanner (breach check)
|               |-- github_leak_scanner.py         # GitHub leaks scanner (sensitive data)
|     |-- config.py                                # Stores API keys for Shodan, VirusTotal, HIBP, etc.
|     |-- main.py                                  # Streamlit UI for interactive scanning
|-- .gitignore                                     # Excludes unnecessary files from version control
|-- requirements.txt                               # Lists all dependencies for the project
|-- README.md                                      # Project documentation
```

## ⚡ Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/imranalmunyeem/The-Hunt.git
   ```

2. Navigate to the project directory:

   ```bash
   cd The-Hunt
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Edit 'Config.py' and Add API Keys (For Advanced Scanners)

  ```bash
  SHODAN_API_KEY = "your_shodan_api_key"
  VIRUSTOTAL_API_KEY = "your_virustotal_api_key"
  HIBP_API_KEY = "your_hibp_api_key"
  ```

## 🛠 Usage
####   Running the tool
  ```bash
streamlit run main.py
  ```

## 🔍 Scanners & Functionalities

## ⚙️ Configuration (API Keys)

## 🚀 Future Enhancements

## 📝 Contributing

## 📜 License


## 📌 Introduction
This repository contains a Test Automation Framework, built using Cypress and Javascript for automated testing for this site: https://www.saucedemo.com/




## 🚀 Key Features
This Cypress project is designed for robust end-to-end testing, incorporating best practices and advanced features to enhance test automation efficiency.
- ✅ Page Object Model (POM) – Organized test structure using reusable page classes to improve maintainability.
- ✅ Data-Driven Testing – Uses external test data for login credentials and other scenarios, ensuring flexibility and scalability.
- ✅ Custom Commands – Encapsulates frequently used actions like login to reduce redundancy and improve readability.
- ✅ Advanced Module Integrations:
   - XPath Support – Enables selecting elements using XPath.
   - Cross-Environment Configuration – Allows testing across multiple environments (e.g., production & development) by dynamically setting the base URL.
   - Screenshots & Videos – Automatically captures test evidence for debugging and reporting.
   - Retries on Failures – Configured retries to improve test stability.
   - Test Grouping with Grep – Supports running specific test groups using Cypress grep.
- ✅ Custom Scripts – Optimized package.json scripts for running tests across different browsers, environments, and headless modes.
- ✅ Mochawesome Reporting – Generates detailed, interactive HTML reports with screenshots and logs for better test analysis.
- ✅ CI/CD Integration with GitHub Actions:
   - Runs tests automatically on every push & pull request.
   - Scheduled execution Monday to Friday at noon (UTC).
   - Supports manual test execution triggers via GitHub Actions workflow.

## 🛠️ Prerequisites

- [![Node.js](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/) (v18.16.1 or higher recommended)
- [![npm](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)](https://www.npmjs.com/) (v9.5.1 or higher recommended)

## ▶️ Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/imranalmunyeem/saucedemo-e2e-cypress.git
   ```

2. Navigate to the project directory:

   ```bash
   cd saucedemo-e2e-cypress
   ```

3. Install dependencies:

   ```bash
   npm install
   ```

## 🚀 Running Tests

  ```bash
  npm test
  ```

## 📁 Project Structure

The tests follow a modular and maintainable structure:

```
|-- .github
|     |-- workflows
|          |-- cypress-tests.yml                # GitHub Actions CI/CD workflow
|-- cypress
|     |-- e2e
|          |-- SauceDemo
|                |-- login.spec.js              # Login test cases
|                |-- product.spec.js            # Product page test cases
|     |-- fixtures
|           |-- request-body
|                |-- login_credentials.json     # Test data
|     |-- reports                               # Stores test execution reports
|     |-- support
|          |-- pages
|                |-- LoginPage.js               # Page Object Model for Login page
|                |-- ProductPage.js             # Page Object Model for Product page
|          |-- commands.js                      # Custom Cypress commands
|          |-- e2e.js                           # Global test configurations
|-- .gitignore
|-- cypress.config.js                           # Cypress configuration settings
|-- package.json                                # Project dependencies and custom scripts
```

- `cypress/e2e`: Contains the actual test files. You can organize your tests into subdirectories as needed. 
- `cypress/fixtures`: Contains external files (example: user create/update data) that can be used to mock data during tests.
- `cypress/reports`: Contains the report for tests (Logs are attached).
- `cypress/support`: Contains custom commands and global configuration.
- `cypress/support/utils`: Contains the Utilities that provides methods for asserting different conditions on web elements, handling requests and responses.

## ⚙️ Configuration

- Modify `cypress.config.json` for Cypress configuration settings.
- Customize `commands.js` and other files in `cypress/support` for reusable commands.

## 🔄 Continuous Integration

This project is configured for CI using Github Actions. Check the configurations in `.github/workflows/*.yml`.

## 📊 Reporting

Mochawesome report (Logs are attached) is stored in the `cypress/reports` directory.
