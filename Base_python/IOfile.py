newfile = open("abcd.text","w")
newfile.write("riven")
newfile.close()




new1 = open("abcd.text","r")
s = new1.read()
print(s)
new1.close()

new2 = open("abcd.text")
s1 = new2.read(3)
print(s1)
new2.close()



p = open("abcd.text","wb")
print(p.closed)
print(p.name)
#print(p.softspace)
print(p.mode)