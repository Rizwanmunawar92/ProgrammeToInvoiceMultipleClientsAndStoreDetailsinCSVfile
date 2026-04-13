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
            if len(parts) == 5:

                date = parts[0]
                client = parts[1]
                hours = parts[2]
                amount = parts[4]

                # parts[1] is the Client Name
                # parts[4] is the Total Money

                if client.lower() == search_name.lower():
                    print(f"Date: {parts[0]} | Hours Work: {parts[2]} |Amount : £ {parts[4]}")
                
                    try:
                        grand_total +=float(parts[4])
                    except ValueError:
                        print(f"Skipping a row because the amount'{amount}' is not a number.")

            else: # If a line has fewer than 5 parts, 'continue' skips to the next line
                  continue
    


    print("=" * 50)
    print("\n")
    print(f"LIFETIME TOTAL FOR {search_name.upper()} : £ {grand_total}")
    print("\n")

    print("=" * 50)

except FileNotFoundError:
    print ("Error: No invoice file found yet. Go create some first!")



