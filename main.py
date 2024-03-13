import requests
import random

def change_ip():
    proxies = [
        {
            'http': 'http://proxy1.example.com:8000',
            'https': 'https://proxy1.example.com:8000'
        },
        {
            'http': 'http://proxy2.example.com:8000',
            'https': 'https://proxy2.example.com:8000'
        },
        # Add more proxy configurations here...
    ]

    proxy = random.choice(proxies)
    try:
        requests.get('https://api.ipify.org', proxies=proxy)
        print(f'Changed IP address. New IP: {proxy}')
    except requests.exceptions.RequestException:
        print('Failed to change IP address.')

while True:
    change_ip()