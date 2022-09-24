import numpy as np
import matplotlib.pyplot as plt
from readFile import readFile

def Graph(fileName):
    plt.plot(readFile(fileName)[0], readFile(fileName)[1], 'bo', label="Data")
    plt.legend()
    plt.show()
    #plt.savefig()
    

