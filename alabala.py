import json
import random
from datetime import datetime, timedelta
import os
import pandas as pd


# Sample data
departure_addresses = [
    "bul Iskarsko shose",
    "bul Tsarigradsko shose 133",
    "bul Ovcha kupel 55A",
    "zh.k Mladost 3 blok 115",
    "bul Maria Luiza",
    "zh.k Sveta Troitsa",
    "ul 3ti Mart",
    "ul Vasil Levski",
    "zh.k Boyana",
    "bul Ovcha kupel 7"
]

arrival_addresses = [
    "bul Ovcha kupel 7",
    "bul Tsarigradsko shose 133",
    "bul Vitosha 89B",
    "zh.k Lulin 9 - 115",
    "bul Iskarsko shose",
    "zh.k Musagenitsa",
    "zh.k Dragalevski Hills",
    "zh.k Simeonovo ul Vazrazhdane",
    "bul James Bourchier",
    "ul Tsarigradsko shose"
]

sender_receiver_ids = list(range(1, 51))  # Assuming sender and receiver IDs are from 1 to 50
employee_ids = list(range(1, 41))  # Assuming employee IDs are from 1 to 40
courier_ids = list(range(43, 51))  # Assuming courier IDs are from 43 to 50

# Generate shipments
num_shipments = 10
shipments = []

for _ in range(num_shipments):
    departure_address = random.choice(departure_addresses)
    arrival_address = random.choice(arrival_addresses)
    weight = random.randint(50, 200)
    sender_id = random.choice(sender_receiver_ids)
    receiver_id = random.choice(sender_receiver_ids)
    employee_id = random.choice(employee_ids)
    sent_date = datetime.now() - timedelta(days=random.randint(1, 10))
    courier_id = random.choice(courier_ids)

    shipment = {
        "departureAddress": departure_address,
        "arrivalAddress": arrival_address,
        "weight": weight,
        "senderId": sender_id,
        "receiverId": receiver_id,
        "employeeId": employee_id,
        "sentDate": sent_date.strftime("%Y-%m-%dT%H:%M:%S"),
        "courierId": courier_id
    }

    shipments.append(shipment)

# Print shipments
for idx, shipment in enumerate(shipments, start=1):
    print(f"Shipment {idx}:")
    print(json.dumps(shipment, indent=4))
    print()

# Write shipments to a JSON file
output_file = "shipments.json"
output_path = os.path.join(os.getcwd(), output_file)

with open(output_path, "w") as file:
    json.dump(shipments, file, indent=4)

print(f"Shipments saved to: {output_path}")



# Read the JSON file
json_data = pd.read_json("shipments.json")

# Convert to an Excel file
json_data.to_excel("output.xlsx", index=False)