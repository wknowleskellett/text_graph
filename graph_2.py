#	William Knowles-Kellett
#	08/18/17
#	

#	Define function

def toint(q):
	q = str(round(q))
	return int(q[0:len(q)-2])

#	Define constants
print "Enter function in python notation.\tx^2 => x**2\tsin(x) => sin(x)"

#	f(x) program as a list of strings
funcString = ["from math import *\ndef f(x):\n", "\ty = " + raw_input("f(x) = "), "\n\treturn y"]

height = 40
width = 40
h_range = range(0, height)
w_range = range(0, width)
graph = []

#       Process input
first_co_str = raw_input("First coordinate (x,y): (")	#Coordinates of top left corner of graph
first_co_li = first_co_str[:-1].split(",")
first = [int(first_co_li[0].strip()), int(first_co_li[1].strip())]
unit = float(raw_input("Scale (size of a unit): "))
prec = float(raw_input("Precision (a decimal within unit - essentially epsilon): "))

#	Write a file for f(x)
newProgram = open("function.py", "w")

for i in range(0,len(funcString)):
	newProgram.write(funcString[i])
newProgram.close()

#	import the user-entered f(x) from the new file
from function import f


#	Establish graph with axis
for i in height:
	y = first[1] - unit*i
	graph.append([])
	for j in width:
		x = unit*j + first[0]
		if (y==0):
			if (x==0):
				graph[i].append("+ ")
			else:
				graph[i].append("- ")
		elif (x==0):
			graph[i].append("| ")
		else:
			graph[i].append(". ")


#	Write over graph given y=f(x)
jay = 0
x = first[0]
while (jay + 0.5*unit < len(width)):
	j = toint(jay)
	y = f(x)
	i = toint((first[1]-y)/unit)
	if (i >= 0 and i < len(height)):
		graph[i][j] = "O "
	jay = jay + prec
	x = jay*unit + first[0]


#	Display graph
for i in range(0, len(graph)):
	strand = str(first[1]-unit*i) + "\t"
	for j in range(0, len(graph[i])):
		strand = strand + graph[i][j]
	print strand
