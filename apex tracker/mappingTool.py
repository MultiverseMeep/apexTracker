import matplotlib.pyplot as plt
import numpy

# Using readline()
filename = "2021-06-25_21-58-419.csv"
file1 = open('coordinateData/' + filename, 'r')
count = 0
xList = []
yList = []

map = input("which map? 1.Olympus 2.Worlds Edge")
 
 
while True:
    try:
        count += 1
     
        # Get next line from file
        line = file1.readline()
     
        # if line is empty
        # end of file is reached
        if not line:
            break
        #print(line.strip())
        lst = line.split()
        line1 = lst[0]
        line2 = lst[1]
        
        if (int(map) == 2):
            line1 = (int(float(line1)) + 32189)/65981
            line2 = (int(float(line2)) + 45298)/82140
        if (int(map) == 1):
            line1 = (int(float(line1)) + 44992)/74629
            line2 = (int(float(line2)) + 35707)/75079
        
        #line1 = int(float(line1))
        #line2 = int(float(line2))
        
        if ((line1 >= 0) and (line1 <= 1) and (line2 >= 0) and (line2 <= 1)):
            #print(str(line1) + " " + str(line2))
            #line1 = line1 * 100
            #line2 = line2 * 100
            xList.append(line1)
            yList.append(line2)
    except:
        pass
if (int(map) == 2):
    img = plt.imread("mapData/worldsEdge.png")
if (int(map) == 1):
    img = plt.imread("mapData/olympus.png")

fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 1, 0, 1])
#ax.scatter(TMIN, PRCP, color="#ebb734")
#plt.show()
plt.axis([0, 1, 0, 1])
plt.plot(xList, yList)
plt.show()
   
    

file1.close()