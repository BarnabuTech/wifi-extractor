
# Wi-Fi EXTRACTOR TOOL

Developed a tool using python programming language that extract and decode Wi-Fi network information, such as SSIDs and passwords. This tool can be used for auditing network security or retrieving lost Wi-Fi credentials.




## Step-by-Step explanation:

    1. Subprocess module:
     This will be used to run system commands in the background.

    2. Windows Command (netsh): 
    We'll utilize the netsh wlan show profile command to list the available Wi-Fi profiles (SSIDs), and then extract detailed information for each profile, including the password (if available).


## Steps for the tool:

    1. Extract Wi-Fi Profiles:
    The netsh wlan show profiles command is used to list all Wi-Fi profiles (SSIDs) saved on the machine.

    2. Fetch Password for Each Profile: 
    The netsh wlan show profile name="SSID" key=clear command is used to show the password (if stored) for each Wi-Fi profile.

    3. Extract and Display SSID and Password:
     The SSID and password are extracted from the output and displayed in a user-friendly format.


## How it works:

The script starts by running netsh wlan show profiles to get a list of all Wi-Fi profiles stored on the computer. For each profile, it runs netsh wlan show profile name="profile_name" key=clear to retrieve details, including the password (if available).
The SSID and password are then displayed in a readable format.


## Output Screenshot:


<img width="414" alt="Readme" src="https://github.com/user-attachments/assets/933e3d9a-8a41-4d00-9f8d-1d847b6cd2f0">




