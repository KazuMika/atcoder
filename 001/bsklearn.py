from sklearn.datasets import make_classification
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from pprint import pprint

x, y = make_classification(random_state=0)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
clf = GradientBoostingClassifier(random_state=0)
clf.fit(x_train, y_train)
p = clf.predict(x_test[:2])
s = clf.score(x_test, y_test)

for (i, j) in zip(x, y):
    pprint(i.tolist())
    pprint(j)
