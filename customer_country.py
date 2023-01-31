infile = open('customers.csv', 'r')
copyfile = open('customer_country.csv', 'w')

for i in infile:
    b = i.split(',')
    copyfile.write(f"{b[1]},{b[2]},{b[4]}\n")
