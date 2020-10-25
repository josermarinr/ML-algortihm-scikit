def studentRegression(ages_train, net_worths_train):
    ### import the sklearn regression module,
    ### create and train a regression

    ### name your regression reg

    from sklearn.linear_model import LinearRegression

    reg = LinearRegression()

    reg.fit(ages_train, net_worths_train)
    """
    for make a prediction just need put the number inside
    reg.predict([27])
    
    print "katie's net worth prediction", reg.predict([27])
    print "slope", reg.coef_
    print "intercept:", reg.intercept_
    ### 
    print "\n ###### stat on test dataset ######## \n"
    print "r-squared score:", reg.score(ages-test, net-worths_test)
    
    print "\n ###### stat on training dataset ######## \n"
    print "r-squared score:", reg.score(ages_train, net_worths_train) 
    """
    ### slope
    reg.coef_
    ### intercept
    reg.intercept_
    return reg
