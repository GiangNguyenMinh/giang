import numpy as np
print("  *************khoi tao ham thuong**************")
a0 = np.array([1,2,3])
a1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("mang 1 chieu : \n" , a0)
print("mang 2 chiue : \n" , a1)
print(" kich thuoc cua mang a0 la : ", a0.shape)
print("kich thuoc cua mang a1 la : ", a1.shape)
print(" kich thuoc cua hang la %d , kich thuoc cua cot la %d " %(a1.shape[0],a1.shape[1]))










print("********khoi tao mang bang ham co san*************")
a = np.zeros((2,2,2),dtype= int) # tao ma tran 0 kieu int
print(a)

b = np.ones((2,2)) # tao ma tran 1 kieu mac dinh
print(b)

c = np.full((2,2),6,dtype= int) # tao ma tran toan phan tu 6 kieu int
print(c)

d = np.eye(5,dtype= int) # tao ra ma tran don vi 5x5
print(d)

e = np.random.random((2,2)) # random ra 1 mang trong khong 0-1
print(e)

f = np.arange(0,10) # tao ra 1 mang 1 chieu trong khong da cho
print(f)



# slicing
a11 = a1[1:3,1:3]
a12 = a1[1,:]
print(a11,a11.shape)
print(a12,a12.shape)

a11[0,0] = 1
print(a1)

# tao ra mang gom cac phan tu trong 1 ma tran
a13 = a1[[0,1,2],[0,2,1]]
a1[np.arange(3),[1,2,0]] += 10 #thay doi gia tri mang tao ra cung lam thay doi gs ma tran ban dau
print(a13)
print(a1)

print(np.random.rand(100,1))

# print(np.random.seed(1))