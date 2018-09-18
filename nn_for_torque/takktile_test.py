#!/usr/bin/env python
from sklearn.neural_network import MLPRegressor
import numpy as np
import serial, time
import itertools
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

##################################### foot1 ###############################################################

#x1= np.array( [0, 309, 600,  756, 1057, 1287, 1503, 1779, 2011, 2319, 2448, 2743,2927, 3031,3212, 3253, 3298, 3348,3417, 3457, 3580, 3600, 3649]).reshape(-1, 1)
#y=np.array([1200, 12200, 14800, 17100, 21000, 28800, 29000, 31100, 34900, 39000,  42800, 43100, 47600, 49600, 50400, 51300, 52200, 52900, 53300, 55100, 54800,  55800,  56000])    

#force1=np.array([0,        350,    508,   1039,    1564,  2324,     3104,  3325,   2518,   2274,  2188,   1772,   1509,   1332,     829,   539,    432,   270,     224,  2034,  2212,    2425,  2312,  2994,    3024,  3152,  3030,    2864,   2724,  2750,   1749,   2364,   1673,  2144,   2475,  2524,    2635,   2841,  2949,   3036,   3100,   2161,  1925,   1590,   1390,  1210,   1058,    922,     656,    348,   1522,    2005,  2424,   2617,   2733,  2872,   3089,   3125,   1389,   891,    432,    198,   1106,   2144,  2828,    3062,   3188,  2482,  2832,   2274,   1715,   1329,   1224,   738,     306,   1334,   1506,  2103,   2712,   2929,   3014,  3100,    2720,   2124,  1688,   1528,   935,     839,     623,    519,    145,   1256,  1576,   2294,   2499,  2995,   3032,   3132,  3152,   1328,    689,    452,     343])

#force1=force1*9.8/1000


#v1=np.array([ 3000, 13300, 17100, 27200, 33900, 46600,  56300, 56200, 49100, 46500, 43000, 38300, 30600, 28800, 20900, 14700, 12800, 8100, 7400, 44400, 45300, 48900, 49100, 56200, 56300, 56300, 56300, 54500, 54100, 54700, 40000, 49900, 38000, 44600, 51100, 51900, 54800, 56100, 56200, 56300, 56300, 47000, 43300, 35600, 33900, 31200, 28200, 26500, 21000, 10600, 32900, 40700, 47500, 51700, 53200, 35300, 56200, 56300, 25900, 21000, 13200, 6500, 29900, 44600, 56000, 56200, 56300, 48900, 56200, 45500, 38200, 30800, 26900, 19400,  7900, 32200, 32700, 44500, 53100, 56200, 56200,  56300, 54500, 45000, 34600, 33500, 21800, 21000, 17800, 16200, 3800, 32600, 33500, 46500, 48500, 56200, 56300, 56300, 56400, 21200, 17900, 13700, 11900])
#v1=v1/100-30

force1=np.array([ 0,       480,  882,   1086,   1473,  1802,   2095,    2556,  2786,  3002])

force1=force1*9.8/1000


v1=np.array([  3100,11800,18400,20600,28000, 33000, 37200, 41400, 44600, 55000])
v1=v1/100-31
v1=v1.reshape(-1,1)
print "after reshape v1:", v1
#scaler.fit(x)
nn1 = MLPRegressor(
    hidden_layer_sizes=(500,),  activation='relu', solver='lbfgs', alpha=0.0001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=5000, shuffle=True,
    random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

n1 = nn1.fit(v1, force1)

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

#######################################################################################################
force21=np.array([  0,        471,     682,    890,     985,     993,   1083,   1200,   1367,   1642,  1806,  2018,   2125,   2392,   2397,   2245,   2199,  2079,   1888,   1733,  1623,   1597,   1352,  1251,   1173,   1031,    956,   836,     679,     545,    420,   243,    517,   1236,  2163])  
v_count21=np.array([2300, 19900, 23300, 26300, 27400, 27600, 29600, 32400, 33900, 38100, 41000, 44900, 46900, 49200, 49200, 49000, 47900, 45800, 43400, 40400, 37700, 37100, 34100, 32200, 29800, 26800, 24600, 22000, 19800, 16700,14200, 8200, 16100,33600, 47300])
v_count21=v_count21/100 -23
print "v21:", v_count21

force22=np.array([  2332,     1839,   1582,  1250,   1052,    823,     318,   1769,   2320,  2388,    2145 ,  1214,     861,    545,   2022,   2400,    1716,  1536,    2318,    924,    2224,   1432, 1123,   305,   2302,   1764,    1138,   377,    2356,    1536,   311] )

v_count22=np.array([50800,  43500, 37700, 31700, 28500, 23400, 11800, 43600, 50800, 50900,  50100,  29100, 24600, 14300, 49000, 50800, 43100, 42300,  50800, 26500, 50800,  34700, 28900, 9600, 50800, 41700, 28200, 15700, 50900,  37500, 13100])

v_count22=v_count22/100 -40

force2=np.concatenate((force21,force22), axis=None)
force2=force2*9.8/1000
print "force:", force2

v2=np.concatenate((v_count21,v_count22), axis=None)
#v2 = v_count21+v_count22
print v2
#v2=np.array(v2).reshape(-1,1)
#v2=np.array(v2, dtype=int)
v2=v2.reshape(-1,1)
#scaler.fit(v2)
print "after reshape:", v2

nn2 = MLPRegressor(
    hidden_layer_sizes=(500, ),  activation='relu', solver='lbfgs', alpha=0.0001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=5000, shuffle=True,
    random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

n2 = nn2.fit(v2, force2)
#test_x = np.arange(0, 470, 1).reshape(-1, 1)
#scaler.fit(test_x)
#test_y = nn2.predict(test_x)


#fig = plt.figure()
#ax1 = fig.add_subplot(111)
#ax1.scatter(v2, force2, s=1, c='b', marker="D", label='real')
#ax1.scatter(test_x,test_y, s=10, c='r', marker="o", label='NN Prediction')
#plt.legend(loc='best')
#plt.show()
#print test_y


#########################################################################################################################
force3=np.array([0,    863,    1235,  1550,   2388,   3131,   1479,   1735,  1833,   2156,   2335,   3144,  3155,    2333,   1652,  1233,    533,    3055,   3013,   1772,  1014,   655,   143,     31,   1374,   1735,   2014,  2024,   2790,   3118,   1937,   1062,  2823,  2573,    1300,  196,   1587,   2072,  2145,  2315,  3199,    3283,  2952,  1022,   136,  2929,  3280,   1871,   1449,   1289,  2183,  2351,    2858,   3168,  199,   3200])

force3=force3*9.8/1000


v3=np.array([ 2100,25800, 33900, 36000, 48500, 54100, 36600, 39900, 41200, 47200, 49500, 54200, 54200,  48700, 37400, 29600, 15900, 54100, 54100, 33100, 23600, 17800, 3700, 2300, 36900, 41800, 47300, 48400, 54100, 54100, 40100, 21500, 54100, 52400, 28900, 5600, 36700, 45500,45900,47200, 54100, 54200, 54000, 20700, 3300,54000, 54200, 40700, 34100, 31300,44400, 48000,  54100, 54200,3100, 54200])
v3=v3/100-21
v3=v3.reshape(-1,1)
print "after reshape v3:", v3
#scaler.fit(x)
nn3 = MLPRegressor(
    hidden_layer_sizes=(500,),  activation='relu', solver='lbfgs', alpha=0.0001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=5000, shuffle=True,
    random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

n3 = nn3.fit(v3, force3)

#test_x = np.arange(10, 530, 2).reshape(-1, 1)
#scaler.fit(test_x)
#test_y = n3.predict(test_x)

#fig = plt.figure()
#ax1 = fig.add_subplot(111)
#ax1.scatter(v3, force3, s=1, c='b', marker="D", label='real')
#ax1.scatter(test_x,test_y, s=10, c='r', marker="o", label='NN Prediction')
#plt.legend(loc='best')
#plt.show()
#print test_y


#############################################################################################################################
force4=np.array([    0,    1482,  1768,   1800,  2104,  2335,    2525,  2663,     2288,   2035,   1250,    730,  1513,  1653,  1963,   2051,   2525,   2635,    2522,  1352,    1996,  2225,  2596,   2625,   2384,   2335,  1562,   1247,    766,    495,   252,     1685,  2115,   2537,   2599,    2256,  1887,   1475,  1286,  1152,   952,      857,    622,    585,   413,   205,   1399,  1660,  1818,   2004,   2280,   858,    1612,   1785,  2252,   2599,   1053,    2036,   2335,  2533,   1388,    821,    333,    1899,  2201,  2483,   2393,   1186,   1592,   1878,  2373,     2414,  2143,   1689,   1088,   1861,  3230,  1285,   522,     284,  2222,  2478,   1424,    929,  267,     819,   1377,    2219,   2337,  2515,    1838,  1239,   700,     569,    357,  2183,  2340,    2596,  1932,  1514,    836 , 302])

force4=force4*9.8/1000

v4=np.array([ 2500, 37000, 41400, 42400, 49800, 53500, 56500, 56600,  51000, 46600, 32100, 21100,36600, 42200, 46000,  47800,54900, 56600,  55400, 35500, 45400, 51000, 56400, 56600, 52200, 53400, 38600, 33000, 22600,17000, 11200, 41800, 50200, 56500, 56600, 53800, 46800, 37800,32200, 30200, 25900, 24300, 19400, 17700,12600,9700, 38000,42400, 45400, 49000, 53300, 27500, 39600, 42500, 50900, 56600,  30600, 48900, 53400,  56600, 24900, 22700, 11800,42800, 50400, 56500, 56100, 31300, 41000, 44500, 55600, 52400, 49400, 38200, 27100, 46300, 55600,33800, 18000,11300,54200, 56500, 37800, 25200,13000, 23900, 33600, 53800, 56500, 56600,  41100, 30100,19900,16800, 12000,52900, 55700, 56600, 42600, 31700,24000, 6800])
v4=v4/100-25
v4=v4.reshape(-1,1)
print "after reshape v4:", v4
#scaler.fit(x)
nn4 = MLPRegressor(
    hidden_layer_sizes=(500,),  activation='relu', solver='lbfgs', alpha=0.0001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=5000, shuffle=True,
    random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

n4 = nn4.fit(v4, force4)

#test_x = np.arange(10, 530, 2).reshape(-1, 1)
#scaler.fit(test_x)
#test_y = n4.predict(test_x)

#fig = plt.figure()
#ax1 = fig.add_subplot(111)
#ax1.scatter(v4, force4, s=1, c='b', marker="D", label='real')
#ax1.scatter(test_x,test_y, s=10, c='r', marker="o", label='NN Prediction')
#plt.legend(loc='best')
#plt.show()
#print test_y

###############################################################################################################################

force5=np.array([0,     221,    288,    756,    1099,    1229,   2098,    2385,    2004,  1692,  1299,    1085,   896,     686,   496,    298,   1606,  2307,  2482,    2404,  2274,  1600,   1112,     879,   487,      654,   1433,   2378,   2473,   2584, 2098,   1972,   1236,   265,   196,   488,    1652,  1856,  2018,   2231,   2555,   1534,    856,   148,    715,    2554, 2424,   1885,  1525,    1386,   1162,    871,   521,   1303,   1558,   1795,  2032, 2137,   2245,   2374,  2478,   2076,   1162,  952,    572,     346,   288,  1250,    1503,  1900,   2256,  2554,   2271,  1364,  909,      747,     523,   345,   231,    654,   1522,    2256,  2375,   2451,    2232,   2028,   1565,   1026,  275, 1224,    1611,   1855, 1953, 2178,  2354,  2706,   1962,   1688,  1165,    837,  654,    555,  156,   559,    1580,  2183,   2306, 2453,   2569,   2324,   1677, 1289,  1055,      872,  209,    1586,  2469, 2108,     1088,    756,   290,  585,    2056,    2231,  2424,  2142,   1656,   1165,   882,      447,   357,  56])

force5=force5*9.8/1000


v5=np.array([ 6100, 9500, 11800,  24800, 26000,  29800,  43500, 47700,  40200, 32400, 25700, 21000, 19000, 17000,11900, 8700, 38200,46900, 47800,  45600, 40400, 30500, 25300, 19000, 13500, 16300, 35100, 47600, 47700,  47800,41400, 40600, 27100, 8800, 6800, 14200, 36100,39900, 44800,47600, 47700,  38000, 20800, 6500, 18600, 47800,47700, 38600,  35200, 27600, 26100, 20500,11400, 29900, 36200, 38400,42400,46200, 47500, 47600, 47800, 40000, 26000,21600,13100, 10900,8600, 30200, 34000, 40200, 46400,47700,  44300, 28300,18800, 17900, 14200,10700, 8000, 16000, 36000, 47300, 47700, 47800,  43600, 41400, 33700, 20900, 8700,25200, 37800, 4100, 42200,47600, 47600,47700, 40200, 33400, 23500,18800,15500,15500,7900,17800, 35300, 44300,47600,47700, 47800, 45900, 35300, 26000,22100, 20000, 8100, 38200, 47800,42800, 21900, 17800, 8400, 15900, 44200, 45400, 47700, 43300, 34300, 27300, 19500,13600, 10700,6900])
v5=v5/100-61
v5=v5.reshape(-1,1)
print "after reshape v5:", v5
#scaler.fit(x)
nn5 = MLPRegressor(
    hidden_layer_sizes=(500,),  activation='relu', solver='lbfgs', alpha=0.0001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=5000, shuffle=True,
    random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

n5 = nn5.fit(v5, force5)

#test_x = np.arange(10, 530, 2).reshape(-1, 1)
#scaler.fit(test_x)
#test_y = n5.predict(test_x)

#fig = plt.figure()
#ax1 = fig.add_subplot(111)
#ax1.scatter(v5, force5, s=1, c='b', marker="D", label='real')
#ax1.scatter(test_x,test_y, s=10, c='r', marker="o", label='NN Prediction')
#plt.legend(loc='best')
#plt.show()
#print test_y

###############################################################################################################################3


bias1=3200
bias2=3800
bias3=1500
bias4=1700
bias5=3400

try:
    i=0
    p1x=0
    p1y=0
    p2x=80
    p2y=0
    p3x=80
    p3y=140
    p4x=0
    p4y=140
    p5x=40
    p5y=50
    copx=[]
    copy=[]
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
			data1=data1/100
#			data1=data1.reshape(-1,1)
			force1= n1.predict(data1)
			print "force1:", force1*1000/9.8
			data2=data2/100
#			data2=data2.reshape(-1,1)
			force2= n2.predict(data2)
			print "force2:", force2*1000/9.8
			data3=data3/100
#			data3=data3.reshape(-1,1)
			force3= n3.predict(data3)
			print "force3:", force3*1000/9.8
			data4=data4/100
#			data4=data4.reshape(-1,1)
			force4= n4.predict(data4)
			print "force4:", force4*1000/9.8
			data5=data5/100
#			data5=data5.reshape(-1,1)
			force5= n5.predict(data5)
			print "force5:", force5*1000/9.8
			force= force1+force2+force3+force4+force5
			print "force:", force*1000/9.8
#			cx=(force1*p1x+force2*p2x+force3*p3x+force4*p4x+force5*p5x)/force
#			cy=(force1*p1y+force2*p2y+force3*p3y+force4*p4y+force5*p5y)/force
#			copx.append(cx)
#			copy.append(cy)
#		print "x:", copx
#		print "y:", copy
		
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





