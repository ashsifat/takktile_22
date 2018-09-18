#!/usr/bin/env python
from sklearn.neural_network import MLPRegressor
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

x= np.array( [0, 309, 600,  756, 1057, 1287, 1503, 1779, 2011, 2319, 2448, 2743,2927, 3031,3212, 3253, 3298, 3348,3417, 3457, 3580, 3600, 3649]).reshape(-1, 1)
y=np.array([1200, 12200, 14800, 17100, 21000, 28800, 29000, 31100, 34900, 39000,  42800, 43100, 47600, 49600, 50400, 51300, 52200, 52900, 53300, 55100, 54800,  55800,  56000])    
print "after reshape:", x
#scaler.fit(x)
nn = MLPRegressor(
    hidden_layer_sizes=(500,),  activation='relu', solver='lbfgs', alpha=0.0001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=5000, shuffle=True,
    random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

n = nn.fit(x,y)
test_x = np.arange(100, 3005, 5).reshape(-1, 1)
#test_x = np.arange(100, 50000, 50).reshape(-1, 1)
#test_x = np.array([0, 223, 500, 707, 1008, 1230, 1522,  1718, 1847, 2098, 2275, 2495, 2814, 3043, 3242, 3475, 3575,3629,  3517, 3519, 3486, 3476, 3329]).reshape(-1,1)
scaler.fit(test_x)
test_y = nn.predict(test_x)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(x,y, s=1, c='b', marker="D", label='real')
ax1.scatter(test_x,test_y, s=10, c='r', marker="o", label='NN Prediction')
plt.show()
print test_y
