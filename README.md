All-in-One Tool for Information Gathering
An all-in-one tool designed for efficient and comprehensive information gathering in cybersecurity. This tool automates the process of gathering crucial data, including domain information, IP details, and more, to assist penetration testers and security researchers in their activities.

Features
DNS Lookup: Get domain and subdomain information.
IP Geolocation: Retrieve geolocation data based on IP addresses.
Whois Lookup: Perform Whois queries to gather ownership details about domains and IP addresses.
Port Scanning: Detect open ports and services running on remote systems.
Banner Grabbing: Extract useful information about services running on a system.
Vulnerability Scanning: Identify known vulnerabilities associated with target IP addresses or domains.
OSINT Tools Integration: Integration with other OSINT (Open Source Intelligence) tools to gather public data from social media and websites.
Requirements
Python 3.6 or higher
Required Python libraries:
requests
beautifulsoup4
socket
python-whois
scapy
Installation
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/neeraj2234444/all-in-one-tool-for-information-gathering.git
Navigate into the project directory:

bash
Copy code
cd all-in-one-tool-for-information-gathering
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the tool using the command:

bash
Copy code
python main.py
You'll be prompted to choose an option for the information gathering you want to perform. Each option is designed to guide you through the process step-by-step, helping you collect valuable data.

Example Usage
Domain Lookup: Fetch DNS and Whois information for a domain.

bash
Copy code
Enter domain to gather information: example.com
IP Geolocation: Get the location details of an IP address.

bash
Copy code
Enter IP address to gather geolocation: 8.8.8.8
