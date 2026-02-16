import random
import csv
from datetime import datetime

with open("temperature_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["timestamp", "sensor_id", "temperature"])

    for i in range(50):
        timestamp = datetime.now()
        sensor_id = "S01"
        temperature = round(random.uniform(2, 10), 2)

        writer.writerow([timestamp, sensor_id, temperature])

print("Data generated!")
