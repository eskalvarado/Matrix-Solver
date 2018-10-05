#Makes a nxn matrix from the data file. 
def InputMatrix(txt):
	f = open(txt,"r")
	m = []
	row = 0
	for line in f.readlines():
		m.append([])
		for i in line.split():
			try:
				m[row].append(float(i))
			except ValueError:
				pass 
		row+=1
	f.close()
	return m

# Characteristic Variables
m = InputMatrix("data.txt")
rowsize = len(m)
colsize = len(m[0])

# Prints matrix in a readable manner
def MatrixPrinter(matrix):
	i=0
	for row in matrix:
		print("%s %i" %(row, i))
		i+=1

MatrixPrinter(m)

# adds/Substracts rows to eachother by a certain amount.
def rowop(row1, row2, num, matrix):
	for colm in range(colsize):
		matrix[row1][colm] += num*matrix[row2][colm]
	# print(matrix)

# Multiplies a row by a certain number.
def rowmult(row,num,matrix):
	colsize = len(matrix[0])
	for colm in range(colsize):
		matrix[row][colm] = num * matrix[row][colm]

# A repeating set of code modularize to save space.
# Keeps or breaks the loop in the terminal.
def ContinueModule(contvar):
	while True:
		cont = input("continue current operation? ")
		if cont == "yes" or cont == "true":
			return True
			break
		elif cont == "no" or cont == "false":
			return False
			break
		else:
			print("sorry, I couldn't understand that.")
			continue
# Same thing but with different outstream to choose between the two row operations can be done.
def ContinueModule1(contvar):
	while True:
		cont = input("continue doing operations? ")
		if cont == "yes" or cont == "true":
			return True
			break
		elif cont == "no" or cont == "false":
			return False
			break
		else:
			print("sorry, I couldn't understand that.")
			continue

# The I/O function of the rowop function.
def rowopInput(m):
	i=True
	while i == True:
		rowchanged = int(input("row to change: "))
		rowchanger = int(input("row to add or subtract: "))
		mult = float(input("by how much: "))
		rowop(rowchanged, rowchanger, mult, m)
		MatrixPrinter(m)
		print("\n")
		i = ContinueModule(i)

# The I/O function of the rowmult function.
def rowmultInput(m):
	j=True
	while j == True:
		rowtochange = int(input("row to multiply: "))
		multiby =  float(input("multiply by how much: "))
		rowmult(rowtochange,multiby,m)
		MatrixPrinter(m)
		print("\n")
		j = ContinueModule(j)

# Menu for selecting which, if any, operation to run.
a=True
while a == True:
	action = input("rowop or rowmult? ")
	if action == "rowop":
		rowopInput(m)
	elif action == "rowmult":
		rowmultInput(m)
	else:
		print("sorry, I couldn't understand that.")
		continue
	a = ContinueModule1(a)

# Final Matrix	
print("final Matrix")
MatrixPrinter(m)
print("\n")

# Prints the resulting constants.
i=0
for row in m:
	print("c%i %s" %(i,row[colsize-1]))
	i+=1
# Checks if correct matrix has been solved correctly
if m[0][0] == 1 and m[1][1] == 1 and m[0][1] == 0 and m[1][0] == 0:
	print("###CORRECT CONSTANTS###")
else:
	print("###INCORRECT CONSTANTS###")