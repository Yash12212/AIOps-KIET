#reading the file
with open("application.log","r") as file:
    logs=file.readlines()

'''print("These are all the logs in the form of list:",logs)

for log in logs:
    print(log.split())'''


#now we are going to parse
"""logger="2026-08-18 10:01:01 INFO UserService Request successful"
parse=logger.split()

print(parse)"""

'''#calculating the number of errors in the log file
no_of_errors=0
for log in logs:
    if "ERROR" in log:
        no_of_errors+=1

print("the total number of errors are:",no_of_errors)'''

#using the counter function to calculate the number of errors in a particular time frame
from collections import Counter #importing the counter function

error_by_minute=Counter()       #making the object

for log in logs:
    parts=log.split()

    if "ERROR" in log:
        minute=parts[1][:5]
        error_by_minute[minute]+=1

print(error_by_minute)

#performing the single rule based detection

threshold=3 #defining a threshold

for minute,count in error_by_minute.items():
    if count>threshold:
        print("ANOMALY:",minute,"had",count,"errors")

#using isolationforest forest for anomaly detection
from sklearn.ensemble import IsolationForest  #importing isolationforest
errors=[[2],[5],[100],[4],[10],[200]]       #making some errors
model=IsolationForest(contamination=0.1, random_state=42)

model.fit(errors) #model starts analyzing the errors variable

predict=model.predict(errors)

print(predict)



