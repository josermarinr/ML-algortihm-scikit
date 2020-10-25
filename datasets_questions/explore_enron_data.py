#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import panda as pd
import numpy as np
"""
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# print len(enron_data["SKILLING JEFFREY K"])

poi = 0

for x in enron_data:

#    print enron_data[x]["poi"]
    if enron_data[x]["poi"]:
        poi += 1

#    print poi

# how many poi

poi = open("../final_project/poi_names.txt").read().split("\n")

poi_total = [record for record in poi if "(y)" in record or "(n)" in record]

print "total number of POI:", len(poi_total)

"""
"""
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# print enron_data["PRENTICE JAMES"]

# print enron_data['COLWELL WESLEY']
# print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
import re
name = 'SKILLING K JEFFREY'

#skilling =>  8682716
#lay =>     103559793
#FASTOW =>    2424083
print enron_data['FASTOW ANDREW S']
for x in enron_data.keys():
    finded = re.search(name, x)
    if finded:
        print  enron_data[x]
    if x.startswith("FASTOW"):
        print x
"""
"""
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print enron_data["PRENTICE JAMES"]
salary = 0
salariados = 0
for x in enron_data:
    salario = enron_data[x]['salary']
    email = enron_data[x]['email_address']
    if email != 'NaN':
        salariados += 1

    if salario != 'NaN':

        salary += 1
    print salary, salariados

"""
"""
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print enron_data["PRENTICE JAMES"]
is_nan = 0

data_total = len(enron_data)
for x in enron_data:
    payment = enron_data[x]['total_payments']

    if payment == 'NaN':
        is_nan += 1

# print is_nan
# print data_total
total = is_nan * 100 / data_total

print total
"""
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print enron_data["PRENTICE JAMES"]
is_nan = 0
poi_total =0
data_total = len(enron_data)
for x in enron_data:
    poi = enron_data[x]['poi']

    payment = enron_data[x]['total_payments']
    if poi:
        poi_total += 1
    if poi and payment =='NaN':

        is_nan += 1

print is_nan, poi_total
# print is_nan
# print data_total
total = is_nan * 100 / data_total+10

print total