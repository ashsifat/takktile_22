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


bias1=1900
bias2=1500
bias3=100
bias4=1300
bias5=4200

try:
    i=0
    p2x=0
    p2y=0
    p3x=80
    p3y=0
    p4x=80
    p4y=140
    p1x=0
    p1y=140
    p5x=40
    p5y=70
    copx=[]
    copy=[]
    arduino = serial.Serial('/dev/ttyACM0', 1000000)
    print "Connection successful"
    last_time =time.time()
    while True:
        data = arduino.readline()
        if data:
            try:
		print "data", data
                values = [float(j) for j in data.split(",") if len(j) > 2]
                print "values", values
		if values[4]:
#			data1= 53500-values[0]-bias1
#			data2= 49000-values[1]-bias2
#			data3= 50500-values[2]-bias3
#			data4= 53200-values[3]-bias4
#			data5= 48000-values[4]-bias5
#			print "data1", data1
#			print "data2", data2
#			print "data3", data3
#			print "data4", data4
#			print "data5", data5
#			data1=data1/100
##			data1=data1.reshape(-1,1)
#			force1= n1.predict(data1)
#			print "force1:", force1*1000/9.8
#			data2=data2/100
##			data2=data2.reshape(-1,1)
#			force2= n2.predict(data2)
#			print "force2:", force2*1000/9.8
#			data3=data3/100
##			data3=data3.reshape(-1,1)
#			force3= n3.predict(data3)
#			print "force3:", force3*1000/9.8
#			data4=data4/100
##			data4=data4.reshape(-1,1)
#			force4= n4.predict(data4)
#			print "force4:", force4*1000/9.8
#			data5=data5/100
##			data5=data5.reshape(-1,1)
#			force5= n5.predict(data5)
#			print "force5:", force5*1000/9.8
#			force= force1+force2+force3+force4+force5
#			print "force:", force*1000/9.8
			data1= 53500-values[0]-bias1
			data2= 49000-values[1]-bias2
			data3= 50500-values[2]-bias3
			data4= 53200-values[3]-bias4
			data5= 48000-values[4]-bias5
			print "data1", data1
			print "data2", data2
			print "data3", data3
			print "data4", data4
			print "data5", data5
#			data1=data1/100
##			data1=data1.reshape(-1,1)
#			force1= n1.predict(data1)
			force1= data1/18
			print "force1:", force1#*1000/9.8
			force2= data2/21
			print "force2:", force2#*1000/9.8
			force3= data3/18
			print "force3:", force3#*1000/9.8
			force4= data4/19
			print "force4:", force4#*1000/9.8
			force5= data5/18
			print "force5:", force5#*1000/9.8
			force= force1+force2+force3+force4+force5
			print "force:", force
            		i+=1
#			cx=(force1*p1x+force2*p2x+force3*p3x+force4*p4x+force5*p5x)/force
#			cy=(force1*p1y+force2*p2y+force3*p3y+force4*p4y+force5*p5y)/force
#			copx.append(cx)
#			copy.append(cy)
		        current_time =time.time()
#		print "x:", copx
#		print "y:", copy
		if i>1000:
			print i
			print "time:", current_time-last_time
			break
#50100.0, 53000.0, 28100.0, 57500.0, 58300.0
		
#		if values[0]>20000:
#			print "done"
#		else :
#			print "none"
            except ValueError:
                print "invalid string:"
               
		

except:
    "Connection failed"
