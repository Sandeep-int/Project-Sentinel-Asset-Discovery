import scapy.all as scapy

def scan(ip):
    # This creates an ARP packet to ask "Who has this IP address?"
    arp_request = scapy.ARP(pdst=ip)
    
    # This creates an Ethernet frame to send the shout to everyone
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # We combine them into one packet
    packet = broadcast/arp_request
    
    # We send the packet and wait 2 seconds for replies
    answered_list = scapy.srp(packet, timeout=2, verbose=False)[0]
    
    print("\n[+] LIVE DEVICES FOUND ON YOUR NETWORK:")
    print("IP Address\t\tMAC Address")
    print("-" * 45)
    for element in answered_list:
        # element[1] is the response from a device that heard us
        print(f"{element[1].psrc}\t\t{element[1].hwsrc}")

# Change this to your router's range. (Usually 172.16.44.1/24)
scan("172.16.44.1/24")
