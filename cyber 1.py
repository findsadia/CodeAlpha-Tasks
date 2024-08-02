from scapy.all import *
import sys

# Function to handle each packet
def packet_callback(packet):
    print(packet.summary())
    wrpcap('captured_packets.pcap', packet, append=True)

# Main function to start sniffing
def start_sniffing(interface, packet_filter):
    try:
        print(f"Sniffing on {interface} with filter: {packet_filter}")
        sniff(iface=interface, filter=packet_filter, prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("\nSniffing stopped")
        sys.exit(0)

if __name__ == "__main__":
    interface = input("Enter the interface to sniff on (e.g., eth0, wlan0): ")
    packet_filter = input("Enter the packet filter (e.g., tcp, udp, icmp, or leave blank for all packets): ")
    start_sniffing(interface, packet_filter)
