import requests
import sys
import time

def send_requests(port=8888, n=50000):
    url = f"http://127.0.0.1:{port}"
    
    for i in range(n):
        try:
            response = requests.get(url)
            print(f"Request {i+1}: Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request {i+1} failed: {e}")
        
        # Sleep for 10 milliseconds after each request
        time.sleep(0.01)  # 0.01 seconds is 10 milliseconds

if __name__ == "__main__":
    # Default values
    port = 8888
    n = 50000

    # Read command-line arguments if provided
    if len(sys.argv) > 1:
        port = int(sys.argv[1])  # First argument is the port number
    if len(sys.argv) > 2:
        n = int(sys.argv[2])  # Second argument is the number of requests
    
    send_requests(port, n)
