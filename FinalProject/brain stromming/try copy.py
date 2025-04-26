products = [
    ["product_id", "product_name", "product_category", "production_date", "expire_date", "number_of_stocks", "supplier", "price", "shelf_location", "barcode"],
    ["5400CD101", "Coca Cola", "Cold Drink", "20-04-2025", "25-04-2025", 100, "Tesco Warehouse", 1.50, "Aisle 1, Shelf B", "1234567890123"],
    # ... more rows ...
]

format_str = "{:<12}\t| {:<15}\t| {:<15}\t|  {:<15}\t|  {:<15}\t|  {:<17}\t|  {:<18}\t|  {:<7}\t|  {:<17}\t|  {:<13}\n"

with open("product_data.txt", "w") as f:
    for row in products:
        f.write(format_str.format(*row))
