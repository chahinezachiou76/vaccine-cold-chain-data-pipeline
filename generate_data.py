import random
import csv
from datetime import datetime

# إنشاء ملف البيانات
with open("temperature_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # أسماء الأعمدة
    writer.writerow(["timestamp", "sensor_id", "temperature"])

    # توليد 50 قراءة حرارة
    for i in range(50):
        timestamp = datetime.now()
        sensor_id = "S01"
        temperature = round(random.uniform(2, 10), 2)

        writer.writerow([timestamp, sensor_id, temperature])

print("Data generated!")
