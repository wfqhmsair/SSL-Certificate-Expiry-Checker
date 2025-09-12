import socket
import ssl
from datetime import datetime

def get_ssl_expiry_date(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            # NotAfter format: 'Jun 14 12:00:00 2025 GMT'
            expiry_str = cert['notAfter']
            expiry_date = datetime.strptime(expiry_str, '%b %d %H:%M:%S %Y %Z')
            return expiry_date

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python check_ssl_expiry.py <hostname>")
        sys.exit(1)
    hostname = sys.argv[1]
    try:
        expiry_date = get_ssl_expiry_date(hostname)
        print(f"SSL certificate for {hostname} expires on: {expiry_date}")
        days_left = (expiry_date - datetime.utcnow()).days
        print(f"Days until expiry: {days_left}")
        if days_left < 0:
            print("Certificate has expired!")
        elif days_left < 30:
            print("Warning: Certificate will expire in less than 30 days!")
    except Exception as e:
        print(f"Error retrieving certificate: {e}")

if __name__ == "__main__":
    main()
