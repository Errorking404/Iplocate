import requests
from termcolor import colored
import os
import sys
platform = sys.platform                           if platform == 'win32':
    import colorama
    colorama.init()

def get_ip_location():
    ip_address = input("Enter the IP address you want to locate: ")
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    # Check if the request was successful
    if response.ok:
        data = response.json()

        if data["status"] == "success":
            print(colored("IP Location Information:", 'green'))
            print(colored("------------------------", 'green'))
            print(colored(f"IP Address: {data['query']}", 'blue'))
            print(colored(f"Country: {data['country']}", 'blue'))
            print(colored(f"Region: {data['regionName']}", 'blue'))
            print(colored(f"City: {data['city']}", 'blue'))
            print(colored(f"ISP: {data['isp']}", 'blue'))
            print(colored(f"Latitude: {data['lat']}", 'blue'))
            print(colored(f"Longitude: {data['lon']}", 'blue'))
            print(colored(f"Zip Code: {data['zip']}", 'blue'))
            print(colored(f"Time Zone: {data['timezone']}", 'blue'))
            print(colored(f"AS Number: {data['as']}", 'blue'))
            print(colored(f"Organization: {data['org']}", 'blue'))

            # Generate Google Maps link
            latitude = data['lat']
            longitude = data['lon']
            google_maps_link = f"http://www.google.com/maps/place/{latitude},{longitude}/@{latitude},{longitude},16z"
            print(colored(f"Google Maps Link: {google_maps_link}", 'blue'))

            # Open Google Maps link in default browser
            import webbrowser
            webbrowser.open(google_maps_link)

            print(colored("------------------------", 'green'))
        else:
            print(colored("Failed to retrieve location information for the IP address.", 'red'))
    else:
        print(colored("Failed to connect to the API.", 'red'))

def get_my_ip():
    url = "http://ip-api.com/json"
    response = requests.get(url)

    # Check if the request was successful
    if response.ok:
        data = response.json()

        if data["status"] == "success":
            print(colored("My IP Location Information:", 'green'))
            print(colored("------------------------", 'green'))
            print(colored(f"IP Address: {data['query']}", 'blue'))
            print(colored(f"Country: {data['country']}", 'blue'))
            print(colored(f"Region: {data['regionName']}", 'blue'))
            print(colored(f"City: {data['city']}", 'blue'))
            print(colored(f"ISP: {data['isp']}", 'blue'))
            print(colored(f"Latitude: {data['lat']}", 'blue'))
            print(colored(f"Longitude: {data['lon']}", 'blue'))
            print(colored(f"Zip Code: {data['zip']}", 'blue'))
            print(colored(f"Time Zone: {data['timezone']}", 'blue'))
            print(colored(f"AS Number: {data['as']}", 'blue'))
            print(colored(f"Organization: {data['org']}", 'blue'))

            # Generate Google Maps link
            latitude = data['lat']
            longitude = data['lon']
            google_maps_link = f"http://www.google.com/maps/place/{latitude},{longitude}/@{latitude},{longitude},16z"
            print(colored(f"Google Maps Link: {google_maps_link}", 'blue'))

            # Open Google Maps link in default browser
            import webbrowser
            webbrowser.open(google_maps_link)

            print(colored("------------------------", 'green'))
        else:
            print(colored("Failed to retrieve location information for your IP address.", 'red'))
    else:
        print(colored("Failed to connect to the API.", 'red'))

def main():
    import time
    import sys

    banner = """

   ___  ____   ____   ___   ____       ____  ____  ______  ____    ____    __  __  _
  /  _]|    \ |    \ /   \ |    \     |    ||    \|      ||    \  /    |  /  ]|  |/ ]
 /  [_ |  D  )|  D  )     ||  D  )     |  | |  o  )      ||  D  )|  o  | /  / |  ' /
|    _]|    / |    /|  O  ||    /      |  | |   _/|_|  |_||    / |     |/  /  |    \
|   [_ |    \ |    \|     ||    \      |  | |  |    |  |  |    \ |  _  /   \_ |     \
|     ||  .  \|  .  \     ||  .  \     |  | |  |    |  |  |  .  \|  |  \     ||  .  |
|_____||__|\_||__|\_|\___/ |__|\_|    |____||__|    |__|  |__|\_||__|__|\____||__|\_|


"""

    def print_banner():
        for line in banner.split('\n'):
            print(colored(line, 'green'))
            time.sleep(0.1)

    def loading_animation():
        animation = "|/-\\"
        idx = 0
        while True:
            print(colored("Loading...", 'red') + colored(animation[idx], 'red'), end='\r')
            idx = (idx + 1) % len(animation)
            time.sleep(0.1)
            if idx == 0:
                break

    print_banner()
    loading_animation()
    while True:
        # rest of your code
        print(colored("IP Tracker", 'green'))
        print(colored("------------------------", 'green'))
        print(colored("1. Track Target's IP", 'blue'))
        print(colored("2. What is my IP?", 'blue'))
        print(colored("3. Quit", 'red'))
        print(colored("------------------------", 'green'))

        choice = input("Enter your choice: ")

        if choice == "1":
            get_ip_location()
            input("Press Enter to continue...")
        elif choice == "2":
            get_my_ip ()
            input("Press Enter to continue...")
        elif choice == "3":
            print(colored("Goodbye!", 'green'))
            exit(0)
        else:
            print(colored("Invalid choice. Please try again.", 'red'))

if __name__ == "__main__":
    main()
