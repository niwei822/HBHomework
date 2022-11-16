"""Generate sales report showing total melons each salesperson sold."""


# salespeople = []
# melons_sold = []

# f = open('sales-report.txt')

# for line in f:
#     line = line.rstrip()
#     entries = line.split('|')
#     salesperson = entries[0]
#     melons = int(entries[2])

#     if salesperson in salespeople:
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons
        
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)


# for i in range(len(salespeople)):
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')

def sales_report(file_path):
    file = open(file_path)
    sales = {}
    for line in file:
       line = line.rstrip()
       entries = line.split('|')
       salesperson = entries[0]
       melons = int(entries[2])
       sales[salesperson] = sales.get(salesperson, melons) + melons
    for person, melon in sales.items():
        print(f"{person} sold {melon}")
     

    
       
    
sales_report("sales-report.txt")
            
    