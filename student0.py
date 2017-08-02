import csv

with open('student.csv',newline='') as f:
    reader = csv.reader(f)
    s=''
    for row in reader:
        for c in row:
            if c==",":break
            s='%s%s'%(s,c)
        print(s)
f.close()