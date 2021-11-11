a = "Riven sprit blossom"
b = "Riven"
c = "yasuo"
print(b in a)
print(c in a)
print(b*5) # nhan chuoi
 

d = b + " " + c   #  cong chuoi 
print(d)
print(b + " " +c )
print(len(a) - 1 ) # do dai chuoi
print(a[1:7]) # lay tu vi tri thu 1 den vi tri thu 4
print(a[0])
print(a[-7])
print(a[1:None])# in tu dau den vi cuoi cua chuoi 
print(a[None:None]) # in ca chuoi 
print(a[None:5:1])# in voi buoc nhay la 1 
print("riven sprit \nblossom")
print(r"riven sprit \nblossom")# chuoi tran bo qua cac ki tu \ 

print(str(69) + "5") # ep kien chuoi
# thay doi ki tu trong chuoi 
print(a[0:14] + "0" + a[15:None])





print("riven %s blossom is the %s "%("sprit","best")) # %d, %f giong nhu c la kieu so nguyen va kieu so thuc

s = "hello %s sprit %s is the %s"   # thay the %s bang %()
result = s %("riven","blossom","best")
print(result)



aa  = "riven"
bb = "sprit"
cc = "blossom"
dd = f"{aa} {bb} {cc}"
print(dd)