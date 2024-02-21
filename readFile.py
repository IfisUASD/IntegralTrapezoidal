import numpy as np




def readFile(fileName):
    file = open("{}".format(fileName))
    x = []
    E = []
    pdos = []
    for line in file:
        #print(line)
        x.append(line.split())
        #y = x.split()


    x.pop(0)
    i = 0
    j = 0
    #print(x[0])
    while i < len(x):
        while j < 2:
            if j == 0:
                E.append(x[i][j])
            else:
                pdos.append(x[i][j])
            j = j + 1
        j = 0
        i = i + 1
    
    E = np.array(E)
    E = E.astype(float)

    pdos = np.array(pdos)
    pdos = pdos.astype(float)

   
    
    return E, pdos


