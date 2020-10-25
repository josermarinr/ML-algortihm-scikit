from sklearn.linear_model import Lasso

features, label = getMyData()

regression = Lasso()

regression.fi(features, label)

regression.predict([2, 4])

print regression.coef_

