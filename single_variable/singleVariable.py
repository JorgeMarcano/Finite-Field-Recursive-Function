w = int(input())
functionList = []

f = open("ring" + str(w) + ".txt", "w")

def pwrX(x, power):
    # x^n = x*(x^n-1) = x*y
    if (power == 0):
        return [1]

    z = []
    for i in range(0, w):
        z.append(0)

    #given (x+2)(x2+2x+1) = x*y
    y = pwrX(x, power-1)
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            coefficient = (x[i] * y[j]) % w
            #x0*x0=x0
            #x1*x0=x1
            #x1*x1=x2
            #x2*x1=x3=x1
            #x2*x2=x4=x2
            degree = i + j
            
            while (degree >= w):
                degree = degree - w + 1
                
            z[degree] += coefficient
            z[degree] %= w

    return z

def addTerms(x, y):
    z = []
    for i in range(0, w):
        z.append(0)

    for i in range(0, len(x)):
        z[i] += x[i]
        z[i] %= w

    for i in range(0, len(y)):
        z[i] += y[i]
        z[i] %= w

    return z

def multiply(x, scalar):
    z = []

    for i in range(0, w):
        z.append(0)
    
    for i in range(0, len(x)):
        z[i] = (x[i] * scalar) % w

    return z

def function(fct, x):
    #fct    x2+2x+1 mapped [1,2,1]
    #x      2a+1    mapped [1,2,0]
    #for each nomial in the polynomial
    temp = []
    for i in range(0, len(fct)):
        z = pwrX(x, i)
        z = multiply(z, fct[i])
        temp = addTerms(z, temp)

    return temp

def isInPrev(prev, z):
    for i in prev:
        if len(i) == len(z):
            isSame = True
            for j in range(0, len(i)):
                if i[j] != z[j]:
                    isSame = False

            if isSame:
                return True

    return False

def printAndSave(fct, index, z, i):
    #print("For fct: ", fct[::-1])
    f.write("For fct: " + str(fct[::-1]) + "\n")
    #print("    c = ", i - index, "n")
    f.write("    c = " + str(i - index) + "n" + "\n")
    tempStr = ""
    if (index != 0):
        tempStr = "n"
    #print("    k = ", index, tempStr)
    f.write("    k = " + str(index) + tempStr + "\n")

def printAndCSV(fct, index, z, i):
    #print("For fct: ", fct[::-1])
    fctNb = ""
    for j in fct[::-1]:
        fctNb += str(j)
    f.write(fctNb)
    #print("    c = ", i - index, "n")
    f.write(", " + str(i - index))
    #print("    k = ", index, tempStr)
    f.write(", " + str(index) + "\n")

#create all the functions
for i in range(0, w**w):
    tempList = []
    for j in range(0, w):
        tempList.append(int(i/(w**j)) % w)
    functionList.append(tempList)

#for each function created
f.write("fct nb, c, k\n")
for fct in functionList:
    #save prev f(x) and then loop to see if current f(x) is there
    prev = []
    #since single variable fcts,
    #just test n=1 then multiply by n
    #do 10 tries just for lols
    #set first trie to z = a
    z = []
    for i in range(0, w):
        z.append(0)

    z[1] = i
    i = 0
    while not (z in prev):
        prev.append(z)
        i += 1
        z = function(fct, z)

    
    index = prev.index(z)
    #printAndSave(fct, index, z, i)
    printAndCSV(fct, index, z, i)

f.close()
