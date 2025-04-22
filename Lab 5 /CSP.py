# Define products and slots
products = [
    {"id": 1, "frequency": 15, "volume": 2},
    {"id": 2, "frequency": 8, "volume": 1},
    {"id": 3, "frequency": 20, "volume": 3}
]

slots = [
    {"id": 1, "distance": 1, "capacity": 3},
    {"id": 2, "distance": 2, "capacity": 2},
    {"id": 3, "distance": 3, "capacity": 2}
]

# Sort products by highest frequency
products.sort(key=lambda x: -x["frequency"])

# Sort slots by lowest distance
slots.sort(key=lambda x: x["distance"])

# Assign products to slots
assignments = []

for product in products:
    for slot in slots:
        if product["volume"] <= slot["capacity"]:
            assignments.append((product["id"], slot["id"]))
            slot["capacity"] -= product["volume"]
            break

# Print the result
print("Assignments:")
for product_id, slot_id in assignments:
    print(f"Product {product_id} → Slot {slot_id}")
