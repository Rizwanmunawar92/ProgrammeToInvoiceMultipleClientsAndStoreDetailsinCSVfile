#To search invoices in the database

import time

file_name = "Invoice_log.csv"

search_name =input("Enter the client name you want to search for:")
grand_total = 0

print(f"\n Search Results for : {search_name}---")

try: 
    with open(file_name, "r") as file:
        for line in file:
            clean_line = line.strip() # Step 1: Clean the line (remove the \n at the end)

            parts = clean_line.split(",") # Step 2: Split the line into a list of 5 pieces

            # parts[1] is the Client Name
            # parts[4] is the Total Money

            if parts[1].lower() == search_name.lower():
                print(f"Date: {parts[0]} | Amount : £{parts[4]}")
                grand_total +=float(parts[4])


    print("=" * 50)
    print("\n")
    print(f"LIFETIME TOTAL FOR {search_name.upper()} : £{grand_total}")
    print("\n")

    print("=" * 50)

except FileNotFoundError:
    print ("Error: No invoice file found yet. Go create some first!")



