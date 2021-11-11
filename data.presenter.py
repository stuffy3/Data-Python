# Create a new file called data_presenter.py.

# Open the CupcakeInvoices.csv.
cupcake = open('CupcakeInvoices.csv')
# Loop through all the data and print each row.
for line in cupcake:
    print(line)
# Loop through all the data and print the type of cupcakes purchased.
cupcake.seek(0)
for line in cupcake:
    print(line.strip().split(',')[2])
# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
cupcake.seek(0)
for line in cupcake:
    q = int(line.strip().split(',')[3])
    c = float(line.strip().split(',')[4])
    print (q * c)

# Loop through all the data, and print out the total for all invoices combined.
cupcake.seek(0)
total = 0
for line in cupcake:
    q = int(line.strip().split(',')[3])
    c = float(line.strip().split(',')[4])
    total = total + (q * c)
print (round(total))



# Close your open file.
cupcake.close()