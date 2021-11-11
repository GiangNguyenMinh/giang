from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
iris_data = load_iris()# lay du lieu cua data
# print(iris_data.target)# in ra cac nhan cua data co san
X_train, X_test, Y_train, Y_test = train_test_split(iris_data.data,iris_data.target,random_state=0)
# print(X_train)
# print(X_test)
# print(Y_train)
# print(Y_test)
model = DecisionTreeClassifier()
myModle = model.fit(X_train,Y_train)
print(myModle.predict(X_test))
print(myModle.score(X_test,Y_test))
