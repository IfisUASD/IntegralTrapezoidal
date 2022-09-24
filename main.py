import os
import argparse
from graph import Graph
from intTrap import intTrap
from readFile import readFile

def main():

	parser = argparse.ArgumentParser(description='Description of your program')
	parser.add_argument('-f','--path', help='Path for the data file', required=True)
	parser.add_argument('-g','--graph', help='Optional argument for graphing points', required=False)
	args = vars(parser.parse_args())

	print("La integral resulta:", intTrap(readFile(args['path'])[0], readFile(args['path'])[1]))
	
	if args['graph'] == 'y':
		Graph(args['path'])

	#main function

if __name__ == '__main__':
	main()
