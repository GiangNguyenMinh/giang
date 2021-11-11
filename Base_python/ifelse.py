a = 1
if a == 10 :
	print("a=10")
elif a!=10:
	print("a!=10")


s = 0 
while (a < 11) :
	print('riven sprit blossom')
	s += 1
	a += 1
else:
	print(s)
print("end")


s = (x for x in range(3))
for value in s:
	print(value)

d = [1,2,3,4]
for t in d :
	print(t)


for i in "riven":
	print(i)


dict1 = {"name":"vox","name1":"taka"}
for key , value in dict1.items() : 
	print(key , ":" , value)