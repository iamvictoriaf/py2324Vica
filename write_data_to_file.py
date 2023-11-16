vegetables = ("kapusta", "morkov", "kartofel","pomidory")
f = open ("vegetables.txt","w")
#print(type(vegetables))

for vegetable in vegetables:
    #print(vegetable)
    f.write(vegetables+"\n")

f.close()