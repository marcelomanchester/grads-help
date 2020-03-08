late = open("late.txt", "r")
lateLines = late.readlines()
lon = open("lon.txt", "r")
lonLines = lon.readlines()
prec = open("prec.txt", "r")
precLines = prec.readlines()
newFile = open("final.txt", "w+")
index = 0
print("Creating file ...")
while(index < len(lonLines)-1):
    if index != 0:
        newFile.write(str(lateLines[index]).replace("\n", "") + " " + str(lonLines[index]).replace("\n", "") + " " + str(precLines[index]).replace("\n", "") +"\n")
    index += 1
print("Finished")
