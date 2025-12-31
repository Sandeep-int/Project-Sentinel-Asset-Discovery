Project Sentinel: Automated Asset Discovery
Project Overview
Developed a custom network security tool designed to map active assets on a local subnet using ARP (Address Resolution Protocol). This project demonstrates an understanding of network protocol manipulation and the configuration of hybrid Windows/Linux environments for security research.

Key Features
Custom Packet Crafting: Utilizes the Scapy library to manually construct and broadcast Ethernet frames and ARP requests.

Environment Optimization: Implemented WSL2 Mirrored Networking via .wslconfig to bypass virtual network isolation and achieve Layer 2 visibility of physical hardware.

Security Integration: Configured custom Inbound Firewall Rules in Windows PowerShell to allow discovery traffic while maintaining overall system security.

Subnet Targeting: Dynamically targets specific local CIDR ranges (e.g., 172.16.44.1/24) to discover active IP and MAC addresses.

Technologies Used
Programming Language: Python 3.x

Core Library: Scapy (Packet Manipulation)

OS Environment: Ubuntu (WSL2)

System Config: Windows Firewall, .wslconfig

Project Verification
The tool's connectivity and environmental setup were verified using the Linux neighbor table (ip neigh), confirming active communication with the local gateway.

How to Run
Clone the repository:

Bash

git clone https://github.com/Sandeep-int/Project-Sentinel-Asset-Discovery.git
Install dependencies:

Bash

pip install -r requirements.txt
Run the scanner (Requires sudo for raw packet privileges):

Bash

sudo python3 mapper.py
