from sklearn import tree
#buoc1 thu thap du lieu
#buoc 2 xu ly du lieu
#buoc 3 tranning model
#buoc 4 du doan ket qua
#buoc 5 danh gia xem model co hieu qua khong
myTree = tree.DecisionTreeClassifier()
# dctrung = [['nhe','tb','tb','nhieu'],
#            ['nang','thap','cao','it'],
#            ['nhe','thap','cao','it'],
#            ['nang','cao','cao','tb'],
#            ['nhe','cao','cao','nhieu'],
#            ['tb','thap','tb','nhieu'],
#            ['tb','tb','tb','it'],
#            ['nang','thap','thap','nhieu']]
# quyuoc
# nhe =1
# thap =2
# tb = 3
# cao =4
# nang = 5
# it =6
# nhieu =7
dactrung = [[1,3,3,7],
            [5,2,4,6],
            [1,2,4,6],
            [5,4,4,3],
            [1,4,4,7],
            [3,2,3,7],
            [3,3,3,6],
            [5,2,2,7]]
# khanangbibenhdauchan
# co = 1
# khong = 0
nhan = [0,1,1,0,0,0,0,1]
rest = myTree.fit(dactrung,nhan)
kq = rest.predict([[1,4,3,6],[1,4,3,7]])
print(kq)