# WhatsApp Status Downloader and Twitter Bot

## Introduction
This Python project aims to automate the process of checking and downloading WhatsApp status updates that have not been viewed within the last hour. Additionally, it provides the functionality to post these downloaded statuses on Twitter.

## Requirements
To run this project, ensure that you have the following:

1. Python (version 3.x) installed on your system.
2. `pip` package manager installed.

## Installation
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Configuration
Before running the project, you need to configure the necessary settings:

  - Download [ChromeDriver] that is of the same version as your Chrome browser. goto `chrome://version/` to check your Chrome Version.
  - Extract chromedriver from the zip into this folder `assest/driver`
  - Afterwards, ensure all required in the `config.py` are provided (PHONE_ID, CONTACTS and TOKEN). 
  
  See [WhatsApp Business Cloud API] for your infomations. 
  > **REMEMBER:** THE GENERATED TOKEN EXPIRES EVERY 24HOURS.
  - Then navigate to this project folder, open `main.py`.
  - Edit `driverpath` variable to your driver path.
  - Edit `timezone` variable to your location time zone.
  - Edit `options.add_argument(r'user-data-dir=YOUR-USER-DATA-DIR')`.
  - Edit `options.add_argument(r'--profile-directory=YOUR-PROFILE-DIR')`.
  - Edit the global vairable `statusUploaderName` to your desired ContactName (make sure it is exactly how it is saved on your phone(Case Sensitive)).

1. **WhatsApp Configuration:**
    You really do not need to do anything because you would login into [WhatsApp Web] when the program is ran for the first time (Scan WhatsApp Barcode to log in).

3. **Twitter Configuration:**
    Open the `main.py` and find `status_captions: Optional[Dict]`, comment out both places where found and run program to open and log in into Twitter.

## Usage

1. Run the `main.py` script to initiate the WhatsApp status checking and downloading process:
   ```
   python main.py
   ```
   This script will check a specified WhatsApp contact status every hour(1 hour by default) and download any unviewed statuses and then tweet them.

2. You can modify the frequency of status checks or customize the behavior by adjusting the settings in the `config.py` file.

## Conclusion
With this WhatsApp Status Downloader and Twitter Bot, you can effortlessly keep track of unviewed WhatsApp statuses and share them on your Twitter feed. Feel free to explore and enhance the project according to your needs and preferences. Happy downloading and tweeting!


[WhatsApp Web]: <https://web.whatsapp.com>
[Python-WhatsApp-Bot]: <https://github.com/Radi-dev/python-whatsapp-bot>
[ChromeDriver]: <https://chromedriver.chromium.org/downloads>
[WhatsApp Business Cloud API]:<https://developers.facebook.com/products/whatsapp/>
[WhatsApp Business Cloud API Dashboard]: <README.md#WhatsApp-Business-Cloud-API-Dashboard>