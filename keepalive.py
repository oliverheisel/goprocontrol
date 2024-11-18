import requests

# GoPro Configuration
gopro_serial = "C3471327959627"
lastthreeserial = gopro_serial[-3:]
gopro_ip = f"172.2{lastthreeserial[0]}.1{lastthreeserial[1:]}.51"

# Function to send keep-alive signal to the GoPro
def keep_alive(timeout_duration=10):
    url = f"http://{gopro_ip}:8080/gopro/camera/keep_alive"
    
    try:
        response = requests.get(url, timeout=timeout_duration)
        print(response.text)
        return response.text
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None

# Call the function to send keep-alive signal
keep_alive()

