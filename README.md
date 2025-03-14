# 🔍 The-Hunt ➜ (Automated Information Gathering Tool)
🚀 An advanced OSINT tool for Active & Passive reconnaissance.
<br>
<br>

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
<br>

## 📌 Introduction
##### This tool automates information gathering for ethical hackers, penetration testers, and security researchers.
##### It provides both Active and Passive reconnaissance techniques, allowing users to scan domains, IPs, emails, and websites efficiently.

##### ✅ OSINT-focused reconnaissance tool
##### ✅ APIs integration with Shodan, VirusTotal, Have I Been Pwned
##### ✅ Modular design (easy to add new scanners)
##### ✅ Built using Python & Streamlit
<br>


## 🛠️ Tools & Libraries Used
[![Python](https://img.shields.io/badge/Python-17202C?style=for-the-badge&logo=python&logoColor=yellow)](https://www.python.org/) 
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)

| 📦 Library / Tool       | 🔍 Purpose                                                       |
|------------------------|----------------------------------------------------------------|
| 🌐 socket             | Fetches IP addresses of domains.                               |
| 🔍 re                 | Uses Regular Expressions for parsing emails, URLs, etc.       |
| 📄 json               | Handles API responses and data serialization.                 |
| 🖥️ os                 | Interacts with system commands (if needed).                   |
| 🌍 requests           | Sends HTTP requests to websites and APIs.                     |
| 🏗️ BeautifulSoup      | Extracts information from HTML pages.                         |
| 🕷️ Scrapy             | (Optional) For advanced web crawling.                         |
| 📡 python-whois       | Retrieves WHOIS information for domains.                      |
| 🌍 dnspython          | Resolves DNS records (A, MX, TXT, NS, CNAME).                 |
| 🔎 Shodan            | Finds open ports, services, vulnerabilities.                   |
| 🛡️ VirusTotal        | Checks if a domain/IP is blacklisted.                         |
| 🔐 Have I Been Pwned (HIBP) | Checks if emails are in data breaches.                |
| 🌍 crt.sh            | Finds subdomains using certificate transparency logs.          |
| 🔄 ViewDNS.info      | Performs reverse IP lookups.                                   |
| 📱 Selenium          | Scrapes social media profiles.                                |
| 🛠️ GitHub API        | Finds leaked credentials in public repositories.              |
| 📊 Streamlit        | Creates an interactive web-based UI.                           |
| 📑 pandas            | Processes and formats scanned data.                           |
| 📄 pdfkit            | (Optional) Converts reports to PDF.                           |
| 📊 csv               | Saves results in CSV format.                                  |

<br>

## 🌟 Features  

| 🚀 Feature                         | 🔍 Description                                                                                  |
|------------------------------------|----------------------------------------------------------------------------------------------|
| ✅ Active Information Gathering    | Performs direct interaction-based reconnaissance, retrieving real-time data from the target. |
| ✅ Passive Information Gathering   | Collects publicly available data without directly interacting with the target, ensuring stealth. |
| ✅ WHOIS Lookup                    | Fetches domain ownership details, registration dates, and contact information.              |
| ✅ DNS Records Retrieval           | Extracts A, MX, NS, TXT, and CNAME records to analyze domain configurations.               |
| ✅ IP & Hosting Information        | Resolves the domain’s IP address and provides hosting provider details.                     |
| ✅ Website Vulnerability Scanning  | Identifies exposed directories, outdated software, and misconfigurations.                   |
| ✅ Shodan Open Ports Check         | Uses the Shodan API to detect publicly exposed ports and running services.                  |
| ✅ Email Harvesting                | Extracts email addresses from the target’s website and indexed pages.                       |
| ✅ Social Media Profile Discovery  | Searches for associated social media accounts using OSINT techniques.                      |
| ✅ Website Technology Detection    | Identifies CMS, JavaScript frameworks, web servers, and third-party services.              |
| ✅ VirusTotal Domain Check         | Verifies if a domain/IP is flagged for malware, phishing, or abuse reports.                |
| ✅ Data Breach Lookup (HIBP)       | Checks if emails linked to the domain have been exposed in past breaches.                   |
| ✅ GitHub Leaks Discovery          | Searches for leaked credentials, API keys, and sensitive data in public GitHub repositories. |
| ✅ Streamlit Web UI                 | Provides an intuitive, user-friendly interface for seamless scanning.                       |
| ✅ Modular & Scalable Architecture | Implements an Object-Oriented design, allowing easy extension with additional scanners.    |

<br>

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
<br>

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
<br>

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
<br>

## 🔍 Scanners & Functionalities 
| 🛠️ Scanner                  | 🔎 Description                                             | 📌 Type   |
|-----------------------------|----------------------------------------------------------|-----------|
| 🏷️ WHOIS Lookup             | Fetches WHOIS information of a domain                   | Active    |
| 🌐 DNS Records              | Retrieves A, MX, NS, TXT, CNAME records                 | Active    |
| 📌 IP & Hosting Info        | Fetches the IP address of a domain                      | Active    |
| 🛡️ Website Vulnerabilities  | Checks for basic website security flaws                 | Active    |
| 🔎 Shodan Scan             | Finds open ports & vulnerabilities using Shodan API     | Active    |
| 📧 Email Harvesting        | Extracts emails from a website                          | Passive   |
| 🔗 Social Media Presence   | Finds social media profiles of a target                 | Passive   |
| 🏗️ Tech Stack Identification | Identifies website technologies (CMS, Frameworks)    | Passive   |

<br>

## ⚙️ Configuration (API Keys)
#### Edit 'Config.py' and Add API Keys (For Advanced Scanners)

  ```bash
  SHODAN_API_KEY = "your_shodan_api_key"
  VIRUSTOTAL_API_KEY = "your_virustotal_api_key"
  HIBP_API_KEY = "your_hibp_api_key"
  ```
<br>

## 🚀 Future Enhancements
<br>

## 📝 Contributing
#### Step 1 ➜ Fork the repo 🍴

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
<br>

## 🎯 Found this project useful? Give it a ⭐ on GitHub! 🚀🌟
