import time
import sys

millis = int(round(time.time() * 1000))
USE_TH = True
try:
    FR = int(sys.argv[1])
    BK = int(sys.argv[2])
except IndexError:
    print("Usage: python matrix.py int:FRONT_WHEELS_COUNT int:BACK_WHEELS_COUNT")
    exit()
    
FNAME = "com_" + str(FR) + "x" + str(BK) + "_bMatrix.txt"
N = FR+BK
T = 2**N
A = []

print("CURRENT SETTINGS:\n")
print("T="+str(T)+" | FRONT="+str(FR)+" | BACK="+str(BK)+" | N="+str(N)+"\n")
raw_input("Press Enter to continue...")

with open(FNAME,'w') as F:
    if USE_TH:
        F.write("[FRONT]\t[BACK]\n")
    for i in range(0,T):
        strVal = '{0:0{C}b}'.format(i,C=N)
        line = "[" + strVal[:FR] + "]\t[" + strVal[BK:] + "]"
        F.write(line + "\n")
        print("Row dumped: " +line+ " | Data="+strVal+"\n")
    F.write("THIS IS KUNNOW's CODE!\n")
    F.close()

now = int(round(time.time() * 1000))
print("\nOutput name:" + FNAME)
print("\nMatrices count: " +str(T))
print("\nTotal computations: " +str(T*N))
print("\nDone!\t\tExecution time: " + str(now-millis) + " ms")
print("\nKUNNOW!")

