dict1 = {1:"riven" , (1,2,"name"):"yasuo" , 3:1} # bao gom cac item (key:value) key chi co the la kieu du lieu khong the thay doi nhu string , so , tuple ; kieu du lieu cua value la bat ki 
print(dict1)
print(type(dict1))






dict2 = {1:"riven", 2:"yasuo",3:"yone",4:"aatrox",1:"blossom riven"}
print(dict2) # co 2 key giong nhau trong 1 dict thi no se dc gan values cuoi cung 




#truy cap gia tri cua dict thong qua key 
print(dict1[(1,2,"name")])
print(type(dict1[3]))

# them item , chinh sua item 
dict1[1] = "riven blossom"
dict1[4] = "garen"
print(dict1[3])



# del dict[key]  : xoa key khoi dict
# del dict : xoa dict






#....... cac ham cua dict 
# cmp(dict1,dict2) so sanh phan tu trong cac dict
# len(dict) so item trong dict
# str(dict) tao ra 1 chuoi tu dict co the in duoc 




#....... cac phuong thuc cua dict
#.clear() xoa tat ca cac phan tu trong dict
#.copy(dict) tra ve ban sao cua dict
#.keys() tra ve tat cac key cua dict
#.values() tra ve tat cac cac value cua dict
#.items() tra ve cac cap items cua dict
#.has_key() tra ve true neu co chua key do
#.update(dict1) them dict1 vao dict
#.get(key,defaut = None ) tra ve gia tri cua key , neu khong co thi tra ve gia tri None
#.setdefault(key,default = None) tra ve gia tri cua key , neu khi khong ton tai thi tra ve gia tri mac dinh  


dict3 = dict.fromkeys(("1","2","3"),2) #tao ra 1 dict moi tu key va day 
print(dict3)


