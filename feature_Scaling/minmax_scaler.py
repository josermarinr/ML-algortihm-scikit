from sklearn.preprocessing import MinMaxScaler
import  numpy
## we use a number with '.' in the end becauses we need a float result and in other case without the dot
## generate an error
weights = numpy.array([[115.], [140.], [175.]])
scaler = MinMaxScaler()
rescalerd_weight = scaler.fit_transform(weights)

print  rescalerd_weight