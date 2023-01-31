with open("sales.csv", "r") as infile:
    header = infile.readline()
    sales = {}
    for line in infile:
        data = line.strip().split(",")
        customer_id = data[0]
        sales_amount = float(data[3])

        if customer_id in sales:
            sales[customer_id]["total_sales"] += sales_amount
        else:
            sales[customer_id] = {
                "num_orders": 1,
                "total_sales": sales_amount
            }

with open("sales_report.csv", "w") as outfile:
    outfile.write("CustomerID TotalSales\n")
    for customer_id, data in sales.items():
        outfile.write(f"{customer_id} {data['total_sales']:.2f}\n")
