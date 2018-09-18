#!/usr/bin/env python
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
#X = [[0., 0.], [1., 1.]]
X = [[26.9,1.145], [ 53.8,1.145], [80.7,1.145], [107.6,1.145], [121.05,1.145], [134.5,1.145], [147.95,1.145], [161.4,1.145], [188.3,1.145], [215.2,1.145], [26.9,2.29], [ 53.8,2.29], [80.7,2.29], [107.6,2.29], [121.05,2.29], [134.5,2.29], [147.95,2.29], [161.4,2.29], [188.3,2.29], [215.2,2.29], [26.9,3.435], [ 53.8,3.435], [80.7,3.435], [107.6,3.435], [121.05,3.435], [134.5,3.435], [147.95,3.435], [161.4,3.435], [188.3,3.435], [215.2,3.435], [ 53.8, 4.58], [80.7,4.58], [107.6,4.58], [121.05,4.58], [134.5,4.58], [147.95,4.58], [161.4,4.58], [188.3,4.58], [215.2,4.58], [ 53.8, 5.725], [80.7,5.725], [107.6,5.725], [121.05,5.725], [134.5,5.725], [147.95,5.725], [161.4,5.725], [188.3,5.725], [215.2,5.725], [80.7,6.87], [107.6,6.87], [121.05,6.87], [134.5,6.87], [147.95,6.87], [161.4,6.87], [188.3,6.87], [215.2,6.87] ]
#y = [0, 1]
X=np.asarray(X)
scaler.fit(X)
#print X
y = [0.012, 0.036, 0.073, 0.09, 0.1, 0.12, 0.12, 0.125, 0.155, 0.17, 0.008, 0.035, 0.062, 0.08, 0.09, 0.11, 0.11, 0.12, 0.14, 0.15, 0.004, 0.034, 0.051, 0.07, 0.085, 0.1, 0.105, 0.115, 0.12, 0.12 ,  0.031, 0.042, 0.06, 0.08, 0.09, 0.1, 0.113, 0.1, 0.098, 0.027, 0.03, 0.05, 0.075, 0.085, 0.09, 0.112, 0.08 , 0.08, 0.02, 0.04, 0.07, 0.08, 0.085, 0.111, 0.07, 0.075]

#clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
#...                     hidden_layer_sizes=(5, 2), random_state=1)

nn = MLPRegressor(
    hidden_layer_sizes=(100,100),  activation='relu', solver='lbfgs', alpha=0.001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=5000, shuffle=True,
    random_state=0, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

nn = nn.fit(X, y)
xx = np.arange(30, 100, 0.5)
yy = np.arange(3, 5, 0.5)
XX,YY = np.meshgrid(xx,yy)
#test_x = np.arange(0.0, 1, 0.05).reshape(-1, 1)
XY=np.array([XX.flatten(),YY.flatten()]).T

test_x=XY
scaler.fit(test_x)
test_y = nn.predict(test_x)
print test_x, test_y
#mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.plot(X[:,0], X[:,1], y, label='parametric curve')
#ax = fig.add_subplot(111, projection='3d')
ax1 = fig.add_subplot(111, projection='3d')
ax1.scatter(X[:,0], X[:,1], y, s=1, c='b', marker="s", label='real test data')
ax1.scatter(test_x[:,0],test_x[:,1], test_y, s=10, c='r', marker="o", label='NN Prediction')
ax1.set_xlabel('velocity (rad/sec)')
ax1.set_ylabel('current (ampere)')
ax1.set_zlabel('torque (N)')
plt.legend(loc='best')
plt.show()

#clf.fit(X, y)                         
#MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
#       beta_1=0.9, beta_2=0.999, early_stopping=False,
#       epsilon=1e-08, hidden_layer_sizes=(5, 2), learning_rate='constant',
#       learning_rate_init=0.001, max_iter=200, momentum=0.9,
#       nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
#       solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False,
#       warm_start=False)
