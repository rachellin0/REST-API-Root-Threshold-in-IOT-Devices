# -*- coding: utf-8 -*-


#import requests
#import datetime

def numDevices(statusQuery, threshold, dateStr):
    base_url = "https://jsonmock.hackerrank.com/api/iot_devices/search"
    page = 1
    total_pages = 1
    matching_devices = 0

    # Convert dateStr to datetime object for comparison
    target_date = datetime.datetime.strptime(dateStr, "%m-%Y")

    while page <= total_pages:
        url = f"{base_url}?status={statusQuery}&page={page}"
        response = requests.get(url)
        data = response.json()

        total_pages = data['total_pages']

        for device in data['data']:
            # Check if device was added in the given month and year
            device_date = datetime.datetime.fromtimestamp(device['timestamp'] / 1000)
            if device_date.month == target_date.month and device_date.year == target_date.year:
                # Check if root threshold is greater than the given threshold
                if device['operatingParams']['rootThreshold'] > threshold:
                    matching_devices += 1

        page += 1

    return matching_devices

# Example usage
#statusQuery = "STOPPED"
#threshold = 45
#dateStr = "04-2019"

#result = numDevices(statusQuery, threshold, dateStr)
#print(result)

