# kiểm decimal 
from decimal import*
# lấy tối đa 30 chữ số phần nguyên và phân thập phân của Decimal
# * có nghĩa là mọi thứ từ hàm đó

getcontext().prec = 30 
# chỉ cần 1 thằng la decimal thì hiểu là tất cả là decimal 
d = Decimal(10)/Decimal(3) 
print(d)
print(type(d))
