import requests
import time
from colorama import init, Fore

# Initialize colorama
init()

def get_location(ip):
    try:
        response = requests.get(f"https://ip-api.com/json/{ip}")
        data = response.json()
        if data["status"] == "success":
            return data
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

def matrix_display(text, delay=0.01):
    colors = [Fore.RED, Fore.LIGHTRED_EX]  # Define colors
    lines = text.split('\n')
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != ' ':
                color = colors[(i+j) % len(colors)]
                print(color + char, end='', flush=True)
            else:
                print(' ', end='', flush=True)
            time.sleep(delay)
        print()

def main():
    ip = input("Please enter an IP address: ")
    location_data = get_location(ip)
    if location_data:
        print("IP:", location_data["query"])
        print("Country:", location_data["country"])
        print("City:", location_data["city"])
        print("Latitude:", location_data["lat"])
        print("Longitude:", location_data["lon"])
        print("ISP:", location_data["isp"])
        
        # Matrix display
        text = """\
          M   M    TTTTTTT
          MM MM       T
          M M M       T
          M   M       T
        """
        matrix_display(text)
    else:
        print("Unable to retrieve location data for the provided IP.")

if __name__ == "__main__":
    main()

