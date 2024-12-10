Project Title: Honeypot Attacks on Telnet Service

Course: ICS344 - KFUPM
Description:
This project was developed as part of the ICS344 course at KFUPM, focusing on analyzing and simulating attacks on a Telnet service hosted on a honeypot. The goal was to implement various attack techniques, monitor their effects, and study honeypot logs for insights.

Project Workflow
Selection of Service:
We selected Telnet as the target service for our honeypot project.

Implemented Three Types of Attacks:

Caldera: Used for simulating automated adversary emulation to test Telnet vulnerabilities.
Python Brute Force Script: A custom script written to brute force Telnet credentials.
Metasploit Framework: Used the auxiliary/scanner/telnet/telnet_login module for brute force attacks.
Created a Cloud Server:
We deployed a Cowrie honeypot on a cloud server to simulate a Telnet environment, capturing logs of all interactions and attacks.

Repeated Attacks on the Honeypot:

We executed the three attacks (Caldera, Python script, Metasploit) on the honeypot.
Collected data on each attack's success and failure.
Log Analysis:

We analyzed the Cowrie honeypot logs to understand the behavior of the attacks.
Used Splunk to visualize and gain insights from the honeypot logs.
Tools and Technologies Used
Cowrie: Deployed as the honeypot to simulate Telnet.
Caldera: Used for adversary emulation.
Python: Created a brute force script for Telnet.
Metasploit Framework: Exploited Telnet vulnerabilities.
Splunk: Used for log analysis and visualization.
How to Recreate This Project
Deploy a Cowrie honeypot on a cloud server.
Simulate attacks using:
Caldera adversary emulation.
Custom Python brute force script.
Metasploit Framework.
Analyze the Cowrie honeypot logs using Splunk or similar tools.
Disclaimer
This project is for educational purposes only. Ensure you have explicit permission to perform any penetration testing or attacks in real-world scenarios.

