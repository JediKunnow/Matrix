import time
import sys

try:
    N = int(sys.argv[1])
except IndexError:
    print("Usage: python matrix.py ELEMENT_COUNT")
    exit()
    
FNAME = "com_" + str(N) + "x" + str(N) + "_bMatrix.txt"
T = 2**N
A = []

print("CURRENT SETTINGS:\n")
print("T="+str(T)+" | N="+str(N)+"\n")
raw_input("Press Enter to continue...")

millis = int(round(time.time() * 1000))


with open(FNAME,'w') as F:
    for i in range(0,T):
        strVal = '{0:0{C}b}'.format(i,C=N)
        line = "[" + strVal + "]"
        F.write(line + "\n")
        print("Row dumped: " +line+ " | Data="+strVal+"\n")
    F.write("THIS IS KUNNOW's CODE!\n")
    F.close()

now = int(round(time.time() * 1000))
print("\nOutput name:" + FNAME)
print("\nMatrices count: " +str(T))
print("\nTotal computations: " +str(T*N))
print("\nDone!\t\tExecution time: " + str(now-millis) + " ms ( " + str((now-millis)*0.001) + " s)")
print("\nKUNNOW!")

