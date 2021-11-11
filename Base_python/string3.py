a = "he's a Man In The Bus"

# capitalize() hàm viết hoa chữ cái đầu của chuỗi các kí tứ còn lại viết thường
b = a.capitalize()
print(b)


# upper() tất cả viết hoa 
c= a.upper()
print(c)

# lower() viết thường tất cả các chữ
d = a.lower()
print(d)


#swapcase() chuyển chữ viết hoa thành viết thường và viết thường thành viết hoa
e = a.swapcase()
print(e)




#title() đưa các chữ bắt đầu của từ thành chữ hoa còn lại là chữ thường 
f = a.title()
print(f)  


# center(width,[fillchar]) trả về 1 chuỗi được căn giũa với chiểu rộng width ,[] kí tự thay thế cho khoảng trắng vả chỉ thuộc kiểu char
g = a.center(30,'^')
print(g)



# encode() mã hóa dữ liệu theo 1 chuẩn


#join() cộng danh sách vào 1 chuỗi
h = a.join([' 1 ',' 2 ',' 3 ',' 4 '])
print(h)


# replace( , ) thay thế 1 chuỗi bằng 1 chuỗi , có thể điển vào số lần thay thế tính tứ trái qua phải
i = a.replace('a','o',1)
print(i)




# strip() trong ngoặc là kí tự đầu tiên hoặc cuối cùng của dãy tính cả khoảng trắng ,có tác dụng xóa đi kí tự đầu và cuỗi trong ngoặc
# rstrip() cắt phần bên phải
# lstrip() cắt phần bên tráiB
k =a.strip('he')
print(k)









