# %s
str1 = 'my name is %s' %('giang')
print(str1)
str2 = 'i am %s%s year old '%('1','2')
print(str2)
# %d là số nguyên 
# %<sô chữ số thập phân>f là số thập phân 
# %r %s là giá trị của phương thức _repr_ và _str_





# fstring lấy giá trị của chuỗi trong {} thay thế vào nó
t = 'i'
b =  f'{t} student in hanoi university'
print(b) 
# format
# không đưa số vào
a = 'a={},b ={},c ={}'.format(1,2,3)
print(a)
# có đưa số vào
c = 'a={2},b={1},c= {0}'.format(2,3,4)
print(c)
# ghi chi tiết 
d = 'a={ichi},b= {tam}, c = {two}'.format(ichi=1, tam=3, two = 2)
print(d)
# căn lên trong format 
# căn trái        : kí tự thay cho khoảng trắng < khoảng cách cần căn  
# căn phải        : kí tự thay cho khoảng trắng > khoảng cách cần căn 
# căn giữa        : kí tự thay cho khoảng trắng ^ khoảng cách cần căn 
e = 'a = {:@<10}b = {:@<10}c = {:@<10}'.format(1,2,3)
print(e)