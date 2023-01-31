with open('EmployeePay.csv', 'r') as infile:
    with open('customer_country.csv', 'r') as details:
        infile_header = infile.readline().strip().split(',')
        emp_index = infile_header.index('EmpFName')
        salary_index = infile_header.index('Salary')

        details_header = details.readline().strip().split(',')
        fname_index = details_header.index('FirstName')
        country_index = details_header.index('Country')

        for line in details:
            customer = line.strip().split(',')
            for emp_line in infile:
                emp = emp_line.strip().split(',')
                if customer[fname_index] == emp[emp_index]:
                    print(
                        f"For customer {customer[fname_index]} {customer[details_header.index('LastName')]}, the salary is {emp[salary_index]} and they are from {customer[country_index]}")
                    break
        infile.seek(0)
