'''Problem Statement

You are working as an AIOps Engineer for an online university portal. The monitoring system has recorded the following server response times in milliseconds over 20 time intervals:

response_time = [
    120, 125, 118, 130, 122,
    127, 124, 121, 129, 126,
    123, 128, 125, 122, 131,
    700, 127, 119, 650, 124
]

Most of the requests have a response time between approximately 118–131 ms, but some values appear significantly different.

Your task is to build a Python-based anomaly detection system using Isolation Forest.'''

# code

response_time = [
    120, 125, 118, 130, 122,
    127, 124, 121, 129, 126,
    123, 128, 125, 122, 131,
    700, 127, 119, 650, 124
]

input = [[n] for n in response_time]

# importing isolation forest from sklearn 
from sklearn.ensemble import IsolationForest

# creating model object
forest = IsolationForest(contamination=0.1, random_state=46)

# fitting input data into model
forest.fit(input)

# prediction
pred = forest.predict(input)

print(pred)

import matplotlib.pyplot as plt

plt.plot(input)
plt.plot(pred)