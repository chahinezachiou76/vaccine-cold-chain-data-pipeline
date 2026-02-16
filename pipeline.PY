import random
from datetime import datetime
import pyodbc

#   SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=(local);"
    "DATABASE=VaccineDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

for i in range(20):
    timestamp = datetime.now()
    sensor_id = random.choice(["S01", "S02", "S03"])
    temperature = round(random.uniform(2, 12), 2)

    # Alert
    if temperature > 8:
        print("WARNING: Temperature exceeded safe limit!")

    # Data Quality Check
    if temperature < 0 or temperature > 15:
        continue

    cursor.execute(
        "INSERT INTO Temperature_Readings (timestamp, sensor_id, temperature) VALUES (?, ?, ?)",
        timestamp, sensor_id, temperature
    )

conn.commit()
conn.close()

print("Pipeline finished!")
