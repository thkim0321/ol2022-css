
def AND(x1,x2):
    w1 = 0.5
    w2 = 0.5
    b = -0.7
    sum = x1*w1 + x2*w2 + b
    if sum <= 0:
        return 0
    else:
        return 1



def NAND(x1,x2):
    w1 = -0.5
    w2 = -0.5
    b = 0.7
    sum = x1*w1 + x2*w2 + b
    if sum <= 0:
        return 0
    else:
        return 1

def OR(x1,x2):
    w1 = 0.5
    w2 = 0.5
    b = -0.2
    sum = x1*w1 + x2*w2 + b
    if sum <= 0:
        return 0
    else:
        return 1


def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y




