#!/usr/bin/python

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

#Counting number of keys in the dictionary
points = len(enron_data)
print("Number of people in the dataset are : " + str(points))

#Counting total number of valueS
count = 0
for key, value in enron_data.items():
    count += len(value)

#Counting values in each key
values_key = count/points
print("The number of values in each key are : " + str(values_key))

#Persons of interest with value of 1
counts = 0
for user in enron_data:
    if enron_data[user]['poi'] == True:
        counts+=1
print("The number of persons of interest with value of 1 is : " + str(counts))

#Number of POI's
names = open('C:/Users/hellen/Desktop/ud120-projects/final_project/poi_names.txt', 'r')
poi_names = names.readlines()
lenght = len(poi_names[2:])
print("The total number of POI's are : " + str(lenght))
names.close()

#James's stock
james_stock = enron_data["PRENTICE JAMES"]["total_stock_value"]
print("Total stock value for James : " + str(james_stock))

#Emails from Welsey to persons of interest
welsey_email = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print("Number of emails sent to POI's by Wesley : " + str(welsey_email))

#Value of stock options exercised by Jeffrey
jeffrey_exercised_stock = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print("Jeffrey's exercised stock options : " + str(jeffrey_exercised_stock))

#Largest value
kenneth = enron_data["LAY KENNETH L"]["total_payments"]
skilling = enron_data["SKILLING JEFFREY K"]["total_payments"]
fastow = enron_data["FASTOW ANDREW S"]["total_payments"]

values = enron_data["LAY KENNETH L"]["total_payments"], enron_data["SKILLING JEFFREY K"]["total_payments"], enron_data["FASTOW ANDREW S"]["total_payments"]
maximum = max(values)

if kenneth == maximum:
    print("Kenneth Lay had the largest total payment of " + str(maximum))

if skilling == maximum:
    print("Jeffrey Skiling had the largest total payment of " + str(maximum))

if fastow == maximum:
    print("Andrew Fastow had the largest total payment of " + str(maximum))

#Unfilled data
print(enron_data["LEMAISTRE CHARLES"]["salary"])

#Quoted salary and known email
quantified_salaries = 0
known_emails = 0
for key in enron_data.keys():
    if enron_data[key]["salary"] != "NaN":
        quantified_salaries += 1   
    if enron_data[key]["email_address"] != "NaN":
        known_emails += 1

print("Number of quantified salaries : " + str(quantified_salaries))
print("Number of known emails : " + str(known_emails))

#Percentage of people with NaN for their total payments
quantified_payments = 0

for key in enron_data.keys():
    if enron_data[key]["total_payments"] == "NaN":
        quantified_payments += 1


percentage = (quantified_payments/len(enron_data.keys()))*100
print(percentage)
print(quantified_payments)

#Percentage of POI's with NaN for their total payment
POI_count = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True :
         POI_count += 1

percentage_POI = (POI_count/len(enron_data.keys()))
print("Number of POI's with NaN values : " + str(POI_count))
print("Percentage of POI's with NaN values : " + str(percentage_POI))

