import csv

with open("products.csv", newline='') as file:
    reader = csv.DictReader(file)
    data = list(reader)


print("All Products:")
for row in data:
    print(f"{row['id']} - {row['name']} | {row['category']} | Price: {row['price']} | Qty: {row['quantity']}")


print("\nTotal rows:", len(data))


above_500 = [p for p in data if float(p['price']) > 500]
print("Products priced above 500:", len(above_500))


avg_price = sum(float(p['price']) for p in data) / len(data)
print("Average price:", avg_price)

cat = input("Enter category: ")
cat_products = [p for p in data if p['category'].lower() == cat.lower()]
print(f"\nProducts in '{cat}' category:")
for p in cat_products:
    print(p['name'])

total_qty = sum(int(p['quantity']) for p in data)
print("\nTotal quantity in stock:", total_qty)
