'''
có thế dùng các dấu '' hoặc "" hoặc  """ """ hoặc để khai báo kiểu chuỗi
/n xuỗng dòng 
/a tiếng bell 
/b xóa kí tự trước nó 
/t cách ra một khoảng 
/' in ra kí tư'
/"in ra kí tự "
// in ra kí tự /

'''

# chuỗi trần không xử dụng đước các lênh / 
# khai báo chuối trần 
print(r"ronaldo's the best football player i/n the word ")
# cộng chuỗi 
str1="ronaldo "
str2="is the best"
str3 = str1 + str2 
print(str3)
# nhân chuỗi 
str4= str1 * 3
print(str4)
# chuỗi trong chuỗi 
str5 = 'n'
bol = str5 in str1
print(bol)
print(type(bol))
# lấy kí tự trong chuỗi 
print(str1[2])
#len(<chuỗi >) là độ dài của chuỗi
print(str1[len(str1)-2])
# cắt chuỗi 
str6 = str1[1:5]
str7 = str1[1:None] #None có thể là đầu hoắc cuối
print(str6)
print(str7)
print(str1[None:5:1]) #  cắt phần tử từ đầu đến vị trí thứ 5 theo bước nhảy là 1
print(str1[None:5:-1]) # cắt phần tử tứ cuối dãy cho đến phần tử thứ 5 
#ép kiểu giá trị
p = str(69)
t = int("59")

print(p)
print(t)
# thay đổi giá trị trong chuỗi 
string1 ='roben'
string1 = string1[None:1]+ '0' + string1[2:None]
print(string1) 