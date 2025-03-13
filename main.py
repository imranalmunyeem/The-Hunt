import streamlit as st
from modules.active_scanner import ActiveScanner
from modules.passive_scanner import PassiveScanner

st.title("Automated Information Gathering Tool")

gathering_type = st.selectbox("Select Information Gathering Type", ["Active", "Passive"])

info_types = [
    "WHOIS Lookup", "DNS Records", "IP & Hosting Info",
    "Website Vulnerabilities", "Shodan Scan", "Email Harvesting",
    "Social Media Presence", "Tech Stack Identification",
    "VirusTotal Check", "HIBP Breach Check", "GitHub Leaks"
]
selected_info = st.multiselect("Select Information to Gather", info_types)

target = st.text_input("Enter Target (Domain/IP/URL)")

if st.button("Start Gathering"):
    if target:
        if gathering_type == "Active":
            scanner = ActiveScanner(target)
        else:
            scanner = PassiveScanner(target)

        results = scanner.scan(selected_info)

        st.write("### Results")
        for info, result in results.items():
            st.write(f"**{info}**: {result}")
    else:
        st.error("Please enter a target.")
