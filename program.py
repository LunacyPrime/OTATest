from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/LunacyPrime/OTATest/main/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "program.py")
ota_updater.download_and_install_update_if_available()
