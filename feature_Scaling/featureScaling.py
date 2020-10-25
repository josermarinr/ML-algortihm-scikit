""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    newArr=[]
    max_arr = max(arr)
    min_arr = min(arr)
    down_formula = float(max_arr-min_arr)
    print min_arr, max_arr, down_formula

    x = 25
    y = 60
    z = x / y
    print "este es el valor de  25 entre 60", z
    for i in arr:
        if (max_arr & min_arr != 0):
            newi = round(float((i-min_arr)/(down_formula)),2)
            print newi
            newArr.append(newi)
        else:
            print "it same max and min"

    return newArr

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)
