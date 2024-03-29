#matrix multiplier
#by Greg Brown
#7/15/2019

import datetime

#get number of rows of matrix A from user
#error handling included to ensure input is an integer
print("A is an m by n matrix.")
m = input("m =  ")
while type(m) != type(1):
    try:
        m = int(m)
    except ValueError:
        print()
        print("error: the input was not an integer. enter an integer.")
        m = input("m =  ")

#get number of columns of matrix A from user
#error handling included to ensure input is an integer
n = input("n =  ")
while type(n) != type(1):
    try:
        n = int(n)
    except ValueError:
        print()
        print("error: the input was not an integer. enter an integer.")
        n = input("n =  ")
print()

#intial matrix A
a = []

#append each entry of matrix A
#input must be an integer
for i in range(m):
    print("enter each entry for row " + str(i + 1) + ' of matrix A:')
    row = []
    for j in range(n):
        entry = input()
        while type(entry) != type(1):
            try:
                entry = int(entry)
            except ValueError:
                print()
                print("error: the input was not an integer. enter an integer.")
                entry = input()
        row.append(int(entry))
    a.append(row)
    print()

#get number of columns of matrix B from user
#error handling included to ensure input is an integer
print("B is an n by p matrix.")
p = input("p =  ")
while type(p) != type(1):
    try:
        p = int(p)
    except ValueError:
        print()
        print("error: the input was not an integer. enter an integer.")
        p = input("n =  ")
print()

#initial matrix B
b = []

#append each entry of matrix B
#input must be an integer
for i in range(n):
    print("enter each entry for row " + str(i + 1) + ' of matrix B:')
    row = []
    for j in range(p):
        entry = input()
        while type(entry) != type(1):
            try:
                entry = int(entry)
            except ValueError:
                print()
                print("error: the input was not an integer. enter an integer.")
                entry = input()
        row.append(int(entry))
    b.append(row)
    print()
    print()

#display matrix A    
print("A = ")
for i in a:
    print(i)

#blank line
print()

#display matrix B    
print("B = ")
for i in b:
    print(i)

#blank line
#print()

#generate blank matrix for b transpose
B = [[0 for i in range(n)] for j in range(p)]

#generate b transpose
for i in range(p):
	for j in range(n):
		B[i][j] = b[j][i]				

#print b transpose		
#print()
#
#print('b transpose =')
#for i in range(len(B)):
#	print(B[i])					

#calculate product of a and b by pairing rows in a with rows in b transpose (columns of b)
product = [[sum([a * b for a, b in zip(a[i], B[j])]) for j in range(len(B))] for i in range(len(a))]

#blank line
print()

#print product matrix
print('A * B = ')
for i in product:
	print(i)
print()

#ask user to save results
s = input("enter 'save' to log the results in a text file in the current working directory. ")
if s == 'save':

        #open file and write datetime
        file = open("matrix_mult_log.txt", "a+")
        time = str(datetime.datetime.now())
        file.write("-------------------\n")
        file.write(time[0:19])
        file.write("\n")
        file.write("\n")
        
        #write matrix a to file
        file.write("A =\n")
        for i in a:
                file.write(str(i) + "\n")
        file.write("\n")

        #write matrix b to file
        file.write("B =\n")
        for i in b:
                file.write(str(i) + "\n")
        file.write("\n")

        #write product matrix to file
        file.write("A * B =\n")
        for i in product:
                file.write(str(i) + "\n")
        file.write("\n")
        file.write("\n")

        #close file
        file.close()

        print()
        print("file saved as 'matrix_mult_log.txt' in current working directory.")

