print("--- Freelance Billing System v1.0 ---")

import time 

all_invoices = []

file_name = "Invoice_log.csv"
while True:
    client = input("\n Enter Client Name (or type 'quit' to exit):")
    if client.lower() == 'quit':
        print("Closing System ... Good luck wiht your hustle!")
        break

    hours = float(input(f"How many hours did you work for {client}? "))
    rate = float(input(f"What is hourly rate £ for {client}? "))

    total = hours * rate
    all_invoices.append(total)

    with open(file_name,"a") as file:
        file.write(f"{time.ctime()},{client},{hours},{rate},{total}\n")

    print ("\n")    
    print ("-"*50)


    print (f"INVOICE Generated: {client} | Time: {time.ctime()} | Total: £{total}")
    print ("-"*50)

    
print ("\n" + "="*30)
print("  DAILY PROFIT REPORT")
print ("\n" + "="*30)
print(f"Total Invoices: {len(all_invoices)}")
print(f"Grand Total:  £ {sum(all_invoices)}")



                   