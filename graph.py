import numpy as np
import matplotlib.pyplot as plt
from readFile import readFile

def Graph():
    plt.plot(readFile()[0], readFile()[1], 'bo', label="Data")
    plt.legend()
    plt.show()
    #plt.savefig()
    

Graph()