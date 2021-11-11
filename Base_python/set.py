set1 = {1,"riven",2,"yasuo",3,"yone"}
set3 = {1,2,3,4,5}


set1.add("darius")
print(set1)



set1.update(["garen","aatrox"]) # ham update phai co []
print(set1)




set1.remove("garen")
print(set1) #neu khong co trong set phat sinh loi , neu dung discard neu khong co se khong phat sinh loi 





#.pop() xoa di phan tu cuoi cua set , nhung khong biet phan tu cuoi la phan tu nao
#.clear() xoa toan bo phan tu trong set
#del set : xoa set trong python 


print(10 in set1)
print(10 not in set1 ) 



set2 = {"riven","nevermore","berseker",2,1}
print(set1 | set2) # phep hop = print(set1.union(set2)) 


print(set1 & set2)  # phep giao = print(set1.intersection(set2)) 


print(set1 - set2) # phan tu khac cua set1 so voi set2 = print(set1.difference(set2))


print(set1 ^ set2) # bo di cac phan tu giong nhau va gop 2 tap hop lai = print(set1.symmetric_difference(set2))



# max() , min() , sorted(reverse = True (or False)) , sum() , any()
print(sorted(set3,reverse = False))