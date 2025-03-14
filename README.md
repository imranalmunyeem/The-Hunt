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
#### Step 1 ➜ Clone the repository:

   ```bash
   git clone https://github.com/imranalmunyeem/The-Hunt.git
   ```

#### Step 2 ➜ Navigate to the project directory:

   ```bash
   cd The-Hunt
   ```

#### Step 3 ➜ Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

#### Step 4 ➜ Edit 'Config.py' and Add API Keys (For Advanced Scanners)

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
####   Using the UI
##### 1️⃣ Select Active or Passive Information Gathering
##### 2️⃣ Choose the types of scans
##### 3️⃣ Enter a target (Domain/IP/URL/Email)
##### 4️⃣ Click "Start Gathering"
##### 5️⃣ View results directly in Streamlit UI

## 🔍 Scanners & Functionalities

## ⚙️ Configuration (API Keys)
#### Edit 'Config.py' and Add API Keys (For Advanced Scanners)

  ```bash
  SHODAN_API_KEY = "your_shodan_api_key"
  VIRUSTOTAL_API_KEY = "your_virustotal_api_key"
  HIBP_API_KEY = "your_hibp_api_key"
  ```

## 🚀 Future Enhancements

## 📝 Contributing
#### Step 1 -> Fork the repo 🍴

   ```bash
   git clone https://github.com/imranalmunyeem/The-Hunt.git
   ```

#### Step 1 ➜ Create a feature branch 

   ```bash
   git checkout -b new-feature
   ```

#### Step 2 ➜ Commit changes 

   ```bash
   git commit -m "Added new feature"
   ```

#### Step 3 ➜ Push to GitHub

   ```bash
   git push origin new-feature
   ```

#### Step 4 ➜ Create a Pull Request! 🚀 


## 📜 License


