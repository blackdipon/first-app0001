#!/usr/bin/env python3
import datetime
import time
import requests

startTime = datetime.datetime.now() # get Current time
upTime = 0

# Run loop
while True:
    time.sleep(60) # sleep for 1min
    upTime = upTime + 1 # added 1min

    # Send post request
    requests.post(
        'http://first-app0001.atwebpages.com/process.php',
        data={'startTime' : startTime, 'upTime' : upTime}
    )