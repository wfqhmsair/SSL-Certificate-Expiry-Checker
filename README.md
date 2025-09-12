# SSL Certificate Expiry Checker

A simple Python script to check the expiry date of a website's SSL certificate.

## Features

- Connects to any HTTPS website and retrieves the SSL certificate expiry date.
- Prints the exact expiry date and the number of days left until expiry.
- Warns if the certificate is about to expire or has already expired.

## Usage

1. **Clone this repository or download the script.**
2. **Run the script using Python 3:**

    ```sh
    python check_ssl_expiry.py <hostname>
    ```

    Example:
    ```sh
    python check_ssl_expiry.py example.com
    ```

3. **Output Example:**

    ```
    SSL certificate for example.com expires on: 2025-06-14 12:00:00
    Days until expiry: 275
    ```

    If the certificate is close to expiry (less than 30 days) or expired, a warning will be displayed.

## Requirements

- Python 3.x

No external dependencies needed; uses only Python's standard library.

## License

This project is provided under the MIT License.
