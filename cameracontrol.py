import requests

# GoPro Configuration
gopro_serial = "C3471327959627"
lastthreeserial = gopro_serial[-3:]
gopro_ip = f"172.2{lastthreeserial[0]}.1{lastthreeserial[1:]}.51"

# Function to control GoPro over wired USB
def control_wired_usb(timeout_duration=10):
    url = f"http://{gopro_ip}:8080/gopro/camera/control/wired_usb"
    #querystring = {"p": "0"} # Datenübertragung
    querystring = {"p": "2"} # steuern
    
    try:
        response = requests.get(url, params=querystring, timeout=timeout_duration)
        print(response.text)
        return response.text
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None

# Call the function to control GoPro over wired USB
control_wired_usb()
