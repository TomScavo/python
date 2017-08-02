import csv
with open('student.csv',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        r=row
        print(r)
        if r==['fa', 'afw']:
            print('hello')
