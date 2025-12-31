Project Sentinel: Automated Asset Discovery
Project Overview
Developed a network security tool designed to map active assets on a local subnet using ARP (Address Resolution Protocol). This project demonstrates a deep understanding of network layers and hybrid environment configuration.

Key Features
Custom Packet Crafting: Uses the Scapy library to manually build and broadcast Ethernet and ARP packets.

Environment Optimization: Implemented WSL2 Mirrored Networking to bypass virtual network isolation and access physical hardware.

Security Integration: Configured custom Windows Firewall rules to allow Layer 2 traffic while maintaining overall system host security.

Technologies Used
Language: Python 3.x

Core Library: Scapy

OS: Ubuntu (WSL2)

Protocols: ARP, Ethernet, TCP/IP

How to Run
Clone the repository:

Bash

git clone https://github.com/Sandeep-int/Project-Sentinel-Asset-Discovery.git
Install dependencies:

Bash

pip install -r requirements.txt
Run the scanner (Requires Sudo for raw packets):

Bash

sudo python3 mapper.py
