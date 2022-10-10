import random
import time
from datetime import datetime
while True:
    date_time = str(datetime.now())
    t = random.randint(30, 90)
    print("Temperature:",t)
    h = random.randint(30, 75)
    print("Humidity:",h)
    if t > 50:
       print( "HIGH TEMP DETECTED", date_time)
    time.sleep(3)