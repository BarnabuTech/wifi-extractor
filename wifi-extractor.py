import subprocess

def extract_wifi_info():
    # Get the profiles (SSID names)
    command = "netsh wlan show profiles"
    networks = subprocess.check_output(command, shell=True, text=True)
    
    # Filter to get the list of profiles (SSID names)
    profiles = []
    for line in networks.split('\n'):
        if "All User Profile" in line:
            profile_name = line.split(":")[1].strip()
            profiles.append(profile_name)
    
    # For each profile, extract the SSID and password (if available)
    wifi_data = []
    for profile in profiles:
        # Use netsh command to get profile details including password
        command = f'netsh wlan show profile "{profile}" key=clear'
        result = subprocess.check_output(command, shell=True, text=True)
        
        # Extract SSID and password
        ssid = profile
        password = None
        for line in result.split('\n'):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                break
        
        # Append extracted data to the wifi_data list
        wifi_data.append({"SSID": ssid, "Password": password if password else "None"})
    
    return wifi_data

def display_wifi_info(wifi_data):
    # Display the information
    print("\nWi-Fi Network Information:")
    print("-" * 40)
    for wifi in wifi_data:
        print(f"SSID: {wifi['SSID']}")
        print(f"Password: {wifi['Password']}")
        print("-" * 40)

if __name__ == "__main__":
    wifi_info = extract_wifi_info()
    display_wifi_info(wifi_info)
