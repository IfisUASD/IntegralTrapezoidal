import numpy as np
import matplotlib.pyplot as plt
from readFile import readFile

def Graph(fileName, int):
    plt.plot(readFile(fileName)[0], readFile(fileName)[1], '-r', label="Integral = {}".format(round(int, 2)))
    plt.legend()
    plt.savefig("{}.png".format(fileName))
    plt.show()
    
    

