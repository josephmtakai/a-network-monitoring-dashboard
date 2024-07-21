import psutil
import scapy.all as scapy

def get_network_stats():
    return {
        'bytes_sent': psutil.net_io_counters().bytes_sent,
        'bytes_recv': psutil.net_io_counters().bytes_recv,
        'packets_sent': psutil.net_io_counters().packets_sent,
        'packets_recv': psutil.net_io_counters().packets_recv
    }

def scan_network():
    # Example network scanning function
    scapy.arping("192.168.1.1/24")

if __name__ == "__main__":
    print(get_network_stats())
    scan_network()
