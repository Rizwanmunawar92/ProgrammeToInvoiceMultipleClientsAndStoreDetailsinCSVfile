import time

file_name ="invoice_log.csv"
client_totals = {} # This is our empty Dictionary

print("\n" +"="*40)
print("    OFFICIAL REVENUE REPORT")

try:
    with open(file_name, "r") as file:
        for line in file:
            parts=line.strip().split(",")

            if len(parts)== 5:
                name = parts[1]
                amount = float(parts[4])

                if name in client_totals:
                    client_totals[name] += amount
                
                else:
                    client_totals[name] = amount
                

    for name, total in client_totals.items():
        print(f"Clinet: {name:15} | Total: £{total:>8.2f}")

    print ("="*48)
    print(f"GRAND TOTAL REVENUE: £ {sum(client_totals.values()):.2f}")

except FileNotFoundError:
    print("No data found to summarize.")





