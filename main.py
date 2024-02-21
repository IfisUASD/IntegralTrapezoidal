import os
import argparse
from graph import Graph
from intTrap import intTrap
from readFile import readFile

def main():
	parser = argparse.ArgumentParser(description='Description of your program')
	parser.add_argument('-f','--path', help='Path for the data file', required=True)
	parser.add_argument('-p','--phi', help='Phi', required=False)
	parser.add_argument('-T','--Temp', help='Temp', required=False)
	parser.add_argument('-g','--graph', help='Optional argument for graphing points', required=False)
	args = vars(parser.parse_args())

	print("La integral resulta:", intTrap(readFile(args['path'])[0], readFile(args['path'])[1]))
	#print(readFile(float(args['phi']), float(args['Temp']), args['path']))
	if args['graph'] == 'y':
		Graph(args['path'], intTrap(readFile(args['path'])[0], readFile(args['path'])[1]))

	#main function

if __name__ == '__main__':
	main()
