from readFile import readFile

def intTrap(x, f):
    i = 0
    I = 0
    while i < len(f) - 1:
        I = I + (f[i] + f[i + 1])*(x[i + 1] - x[i])/2
        i = i + 1
    return I



