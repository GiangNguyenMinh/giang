itera = (x for x in range(3))
intea1 = [x for x in range(3)]



print(intea1)
print(iter(itera)) # iter kiem tra kieu iterator
print(iter(intea1))
print(max(itera))
print(max([], default = "riven"))
#print(min(itera)) khi con tro duoc dua den cuoi cua iterable thi khong dung duoc ca ham nua


# print(sum(itera,2)) in ra tong cac cac phan tu trong iterable , chi so 2 co the co hoac khong khi co co nghia la cong tong them 2 . Dung sum thi khong dung duoc next() nua 

print(itera)
#print(next(itera)) in lan luot cac phan tu theo vi tri con tro
#print(next(itera))
#print(next(itera))

#.sorted(iterator,reverse = True or Flase) de sap xep cac phan tu
