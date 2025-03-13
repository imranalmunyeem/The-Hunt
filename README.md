📌 Automated Information Gathering Tool
🚀 An advanced OSINT tool for Active & Passive reconnaissance, integrating APIs like Shodan, VirusTotal, and Have I Been Pwned.
🔍 Built with Python & Streamlit for an intuitive UI and modular scanning framework.

📖 Table of Contents
Introduction
Features
Project Structure
Installation
Usage
Scanners & Functionalities
Configuration (API Keys)
Future Enhancements
Contributing
License
📌 Introduction
This tool automates information gathering for ethical hackers, penetration testers, and security researchers.
It provides both Active and Passive reconnaissance techniques, allowing users to scan domains, IPs, emails, and websites efficiently.

✅ OSINT-focused reconnaissance tool
✅ APIs integration with Shodan, VirusTotal, Have I Been Pwned
✅ Modular design (easy to add new scanners)
✅ Built using Python & Streamlit

🌟 Features
✅ Active Information Gathering

WHOIS Lookup
DNS Records Retrieval
IP & Hosting Information
Website Vulnerability Scanning
Shodan Open Ports & Services Check
✅ Passive Information Gathering

Email Harvesting
Social Media Profile Discovery
Website Technology Stack Identification
VirusTotal Domain Reputation Check
Data Breach Lookup via Have I Been Pwned
GitHub Leaks Discovery
✅ Streamlit Web UI

Simple & user-friendly interface for easy scanning
Select multiple scan types at once
✅ Modular Structure

Easy to extend with new scanning modules
Implements OOP best practices with a BaseScanner class
📂 Project Structure
bash
Copy
Edit
info_gathering_tool/
│── main.py  # Streamlit UI
│── modules/
│   │── base_scanner.py  # Base class for scanners
│   │── active_scanner.py
│   │── passive_scanner.py
│   │── scanners/
│   │   │── whois_scanner.py
│   │   │── dns_scanner.py
│   │   │── ip_scanner.py
│   │   │── email_scanner.py
│   │   │── social_media_scanner.py
│   │   │── tech_stack_scanner.py
│   │   │── vulnerability_scanner.py
│   │   │── shodan_scanner.py
│   │   │── virustotal_scanner.py
│   │   │── hibp_scanner.py
│   │   │── github_leak_scanner.py
│── config.py  # Stores API keys
│── requirements.txt
│── README.md
⚡ Installation
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/your-username/info-gathering-tool.git
cd info-gathering-tool
2️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Add API Keys (For Advanced Scanners)
Edit config.py and add your API keys.
python
Copy
Edit
SHODAN_API_KEY = "your_shodan_api_key"
VIRUSTOTAL_API_KEY = "your_virustotal_api_key"
HIBP_API_KEY = "your_hibp_api_key"
🛠 Usage
Running the Tool
sh
Copy
Edit
streamlit run main.py
Using the UI
Select Active or Passive Information Gathering
Choose the types of scans
Enter a target (Domain/IP/URL/Email)
Click "Start Gathering"
View results directly in Streamlit UI
🔍 Scanners & Functionalities
Scanner	Description	Type
WHOIS Lookup	Fetches WHOIS information of a domain	Active
DNS Records	Retrieves A, MX, NS, TXT, CNAME records	Active
IP & Hosting Info	Fetches the IP address of a domain	Active
Website Vulnerabilities	Checks for basic website security flaws	Active
Shodan Scan	Finds open ports & vulnerabilities using Shodan API	Active
Email Harvesting	Extracts emails from a website	Passive
Social Media Presence	Finds social media profiles of a target	Passive
Tech Stack Identification	Identifies website technologies (CMS, Frameworks)	Passive
VirusTotal Check	Checks if a domain is blacklisted	Passive
HIBP Breach Check	Finds breached emails from Have I Been Pwned API	Passive
GitHub Leaks	Searches GitHub for leaked credentials	Passive
⚙️ Configuration (API Keys)
Some features require API keys. Register for free at:

Shodan
VirusTotal
Have I Been Pwned
Once obtained, add them to config.py:

python
Copy
Edit
SHODAN_API_KEY = "your_key_here"
VIRUSTOTAL_API_KEY = "your_key_here"
HIBP_API_KEY = "your_key_here"
🚀 Future Enhancements
✅ PDF/HTML Reporting - Generate structured reports of findings
✅ Real-Time Alerts - Send alerts via Telegram/Slack
✅ AI-based Risk Analysis - Use OpenAI API for threat scoring
✅ Database Logging - Store scan results for later analysis

📝 Contributing
Want to improve this tool? 🎯
Contributions are welcome! Follow these steps:

Fork the repo 🍴
Create a feature branch (git checkout -b new-feature)
Commit changes (git commit -m "Added new feature")
Push to GitHub (git push origin new-feature)
Create a Pull Request! 🚀
📜 License
📄 This project is licensed under the MIT License – free to use and modify.

🔗 Author: Your Name
🔗 GitHub: Your Profile

🚀 Final Thoughts
This Automated Information Gathering Tool is an advanced OSINT solution, ideal for cybersecurity professionals, pentesters, and researchers.

✅ Fast, Modular, and Scalable
✅ OSINT-focused & API-powered
✅ Security Automation for Ethical Hackers

🎯 Want to add new features? Fork the repo and start contributing!

⭐ Found this project useful? Give it a star on GitHub! 🚀🌟

🔗 Links
Shodan API Key → Get Here
VirusTotal API Key → Get Here
Have I Been Pwned API Key → Get Here