from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://github.com/LunacyPrime/OTATest/new/main/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "program.py")

ota_updater.download_and_install_update_if_available()
