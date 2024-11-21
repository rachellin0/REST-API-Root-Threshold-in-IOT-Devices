# REST-API-Root-Threshold-in-IOT-Devices
Open a terminal or command prompt:
pip install requests
pip install datetime
from iot_devices import numDevices
statusQuery = "STOPPED"
threshold = 45
dateStr = "04-2019"

result = numDevices(statusQuery, threshold, dateStr)
print(f"Number of matching devices: {result}")
