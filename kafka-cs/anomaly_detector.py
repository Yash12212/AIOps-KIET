#reading a log file
with open("application.log","r") as file:  
    logs=file.readlines()

'''for log in logs:
    print(log.split())'''

'''#parsing
anomaly="2026-08-18 10:01:01 INFO UserService Request successful"
parse=anomaly.split()

print(parse[0])'''

errors_in_log=0
for log in logs:
    if "ERROR" in log:
        errors_in_log=errors_in_log+1
    
print("The number of errors are:",errors_in_log)

#counting the number of errors by minute
from collections import Counter

errors_by_minute=Counter()

for log in logs:
    parse=log.split()

    if "ERROR" in log:
        minute=parse[1][:5]
        errors_by_minute[minute]=errors_by_minute[minute]+1
    
    print(errors_by_minute)


#doing single rule based detection

threshold=6

for minute,count in errors_by_minute.items():
    if count>threshold:
        print("Anomaly:",minute,"had",count,"erros")


#using isolationforest to determine the anomaly

from sklearn.ensemble import IsolationForest
model=IsolationForest(contamination=0.1, random_state=46)

error=[34,64,200,45,24,76,30]
errors=[[2],[5],[100],[4],[10],[200]] 
model.fit(errors)

#making zip function
for value, prediction in zip(error,predictions):
    if prediction == -1:
        print("error found")