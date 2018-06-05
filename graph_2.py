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
fString = ["from Math import *\ndef f(x):\n", "\ty = " + raw_input("f(x) = "), "\n\treturn y"]
height = 40
width = 40
height = range(0, height)
width = range(0, width)
graph = []
first = raw_input("First coordinate (x,y): ")	#Coordinates of top left corner of graph
first = first[1:len(first)-1].split(",")
first = [int(first[0]), int(first[1])]
unit = float(raw_input("Unit: "))
prec = float(raw_input("Precision (a fraction of unit): "))


#	Write a file for f(x)
newProgram = open("function.py", "w")
for i in range(0,len(fString)):
	newProgram.write(fString[i])
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
