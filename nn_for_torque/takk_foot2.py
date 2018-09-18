#!/usr/bin/env python
from sklearn.neural_network import MLPRegressor
import numpy as np
import serial, time
import itertools
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


#force1=np.array([ 0,       480,  882,   1086,   1473,  1802,   2095,    2556,  2786,  3002])

#force1=force1*9.8/1000
#print "force1: ", force1

#v1=np.array([  3100,11800,18400,20600,28000, 33000, 37200, 41400, 44600, 55000])
#v1=v1/100-31
#v1=v1.reshape(-1,1)
#print "after reshape v1:", v1

##scaler.fit(x)
## lin fit slope:  16.05 +- 0.7042 


#nn1 = MLPRegressor(
#    hidden_layer_sizes=(500,),  activation='relu', solver='lbfgs', alpha=0.0001, batch_size='auto',
#    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=5000, shuffle=True,
#    random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
#    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

#n1 = nn1.fit(v1, force1)

#test_x = np.arange(10, 530, 2).reshape(-1, 1)
#scaler.fit(test_x)
#test_y = n1.predict(test_x)

#fig = plt.figure()
#ax1 = fig.add_subplot(111)
#ax1.scatter(v1, force1, s=1, c='b', marker="D", label='real')
#ax1.scatter(test_x,test_y, s=10, c='r', marker="o", label='NN Prediction')
#plt.legend(loc='best')
#plt.show()
#print test_y


bias1=-200
bias2=-200
bias3=-400
bias4=600
bias5=-400

i=0
p2x=0
p2y=0
p5x=80
p5y=0
p3x=80
p3y=140
p1x=0
p1y=140
p4x=40
p4y=70
copx=[]
copy=[]
cx=0
cy=0

try:

    arduino = serial.Serial('/dev/ttyACM0', 115200)
    print "Connection successful"
    while True:
        data = arduino.readline()
        if data:
            try:
		print "data", data
                values = [float(j) for j in data.split(",") if len(j) > 2]
                print "values", values
		if values[4]:
			data1= 50500-values[0]-bias1
			data2= 47500-values[1]-bias2
			data3= 49000-values[2]-bias3
			data4= 50300-values[3]-bias4
			data5= 50000-values[4]-bias5
			print "data1", data1
			print "data2", data2
			print "data3", data3
			print "data4", data4
			print "data5", data5
#			data1=data1/100
##			data1=data1.reshape(-1,1)
#			force1= n1.predict(data1)
			force1= data1/21
			print "force1:", force1#*1000/9.8
			force2= data2/28
			print "force2:", force2
			force3= data3/20
			print "force3:", force3
			force4= data4/19
			print "force4:", force4
			force5= data5/18
			print "force5:", force5
			force= force1+force2+force3+force5#+force5
			print "force:", force#*1.248
#			print "force:", force*1000/9.8
#			cx=(force1*p1x+force2*p2x+force3*p3x+force4*p4x+force5*p5x)/force
#			cy=(force1*p1y+force2*p2y+force3*p3y+force4*p4y+force5*p5y)/force
			cx=(force1*p1x+force2*p2x+force3*p3x+force5*p5x)/force
			cy=(force1*p1y+force2*p2y+force3*p3y+force5*p5y)/force
#			print "copx:", cx
			copx.append(cx)
			copy.append(cy)
		print "x:", copx
		print "y:", copy
#		xmin=0
#		xmax=80
#		ymin=0
#		ymax=140
#		l=len(copx)
#		print "length:", l
#		#xlim((xmin, xmax))   # set the xlim to xmin, xmax
#		#ylim((ymin, ymax))   # set the xlim to xmin, xmax
#		#plot(x,y)
#		theta = np.radians(-2)
#		c, s = np.cos(theta), np.sin(theta)
#		R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))
#		print(R)
#		#XX,YY = np.meshgrid(x,y)
#		#XY=np.array([XX.flatten(),YY.flatten()]).T
#		XY=np.array([copx,copy]).T
#		print "XY", XY
#		xy=np.dot(R, XY.T).T
#		print "xy", xy

#		X=xy[:,0]-8
#		Y=xy[:,1]
#		#X=xy[0,:]
#		#Y=xy[1,:]
#		print "X", X, "Y:", Y
#		fig = plt.figure()
#		ax1 = fig.add_subplot(111)
#		ax1.axis([xmin, xmax, ymin, ymax])
#		#ax1.plot(x, y, c='b', marker="D", label='zmp trahectory')
#		#ax1.plot(x[300:900], y[300:900], c='b', marker="o", label='zmp trahectory')
#		ax1.plot(X[300:900] , Y[300:900] , c='b', marker="o", label='zmp trahectory')
#		#ax1.scatter(X , Y , s=1, c='b', marker="o", label='zmp trahectory')
#		plt.legend(loc='best')
#		plt.xlabel('x')
#		plt.ylabel('y')
#		plt.show()
#		
#50100.0, 53000.0, 28100.0, 57500.0, 58300.0
		
#		if values[0]>20000:
#			print "done"
#		else :
#			print "none"
            except ValueError:
                print "invalid string:"
               
		
            i+=1
except:
    "Connection failed"
