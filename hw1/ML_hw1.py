#ML HW1


import csv
import numpy as np


data = []
# 每一個維度儲存一種污染物的資訊
for i in range(18):
	data.append([])



n_row = 0
train_f = open('train.csv', 'r', encoding='big5')
row = csv.reader(train_f, delimiter =  ',')

for  r in row:
    if n_row != 0:
            for i in range(3, 27):
                if r[i] != 'NR':
                    data[(n_row - 1)%18].append(float(r[i]))
                else:
                    data[(n_row-1)%18].append(float(0))
    n_row += 1

train_f.close()

print(data)



#parse data to (x,y)
x = []
y = []

for i in range(12):
    for j in range(471):
        x.append([])

        for t in range(18):
            for s in range(9):
                x[471*i + j].append(data[t][480 * i + j +s])

        y.append(data[9][480 * i + j + 9])

x = np.array(x)
y = np.array(y)

#add bias (前九小時所有data加一個constant,12個月共可以組成有12*47個連續的九小時)
x = np.concatenate((np.ones((x.shape[0], 1)), x), axis=1)

#init weight and some hyperparameters

#前９九小時包含bias共有18*9 + 1個參數
w = np.zeros(len(x[0]))  #column vector (default)


w = np.array(w)
print(w)
l_rate = 0.01
repeat  = 100
hypo = np.dot(x,w)


#start training

#by least square error
#可以用least square error的結果當作初始去train
inverse = np.linalg.inv(np.dot(x.transpose(), x))    #(x'x)**(-1)
w = np.dot(x.transpose() , y)
w = np.dot(inverse, w)


#start training


l_rate = 0.00001
repeat  = 100

x_t = x.transpose()
sum_grad = np.zeros(len(x[0]))

for i in range(repeat):
	hypothesis = np.dot(x, w)
	loss = hypothesis -  y

	cost = np.sum(loss **2)  #cost function
	a_cost = np.sqrt(cost / len(loss) )
	grad = np.dot(x_t, loss)

	sum_grad += grad ** 2
	ada = np.sqrt(sum_grad)

	w = w - l_rate * grad / ada

	print('iteration: %d | Cost: %f' %(i, a_cost))


	#save/read model
np.save('model.npy',w)
w = np.load('model.npy')

#read testing data

test_x = []

n_row = 0
t_data = open('test.csv', 'r')
row = csv.reader(t_data, delimiter = ',')

for r in row:
    #把每九小時內所有data存成test_x裡的一個row

    if n_row %18 == 0:
        test_x.append([1])  #[1]: 先加bias
        for i in range(2, 11):
            test_x[n_row // 18].append(float(r[i]))

    else:
        for i in range(2,11):
            if r[i] != 'NR':
                test_x[n_row // 18].append(float(r[i]))
            else:
                test_x[n_row // 18].append(0)
    n_row += 1
t_data.close()
test_x = np.array(test_x)



#get ans.csv(prediction result) with your model
ans = []

for i in range(len(test_x)):
    ans.append(['id_' + str(i)])
    a = np.dot(test_x[i], w)
    print(i, a)
    ans[i].append(a)

filename = 'predict.csv'
result = open(filename, 'w+')  #w+: 開新檔並可讀寫
s = csv.writer(result, delimiter = ',', lineterminator = '\n')
s.writerow(['id', 'value'])  #表格的title
for i in range(len(ans)):
    print(ans[i])
    s.writerow(ans[i])   #writerow: 可以直接把一行row array寫成一行

result.close()





'''

#by least square error
inverse = np.linalg.inv(np.dot(x.transpose(), x))    #(x'x)**(-1)
w = np.dot(x.transpose() , y)
w = np.dot(inverse, w)


hypothesis = np.dot(x, w)
loss = hypothesis -  y
cost = np.sum(loss **2)
a_cost = np.sqrt(cost / len(loss) )
print(a_cost)

#可以用least square error的結果當作初始去train
#start training


l_rate = 0.00001
repeat  = 1000000

x_t = x.transpose()
sum_grad = np.zeros(len(x[0]))

for i in range(repeat):
	hypothesis = np.dot(x, w)
	loss = hypothesis -  y

	cost = np.sum(loss **2)  #cost function
	a_cost = np.sqrt(cost / len(loss) )
	grad = np.dot(x_t, loss)

	sum_grad += grad ** 2
	ada = np.sqrt(sum_grad)

	w = w - l_rate * grad / ada

	print('iteration: %d | Cost: %f' %(i, a_cost))


	#save/read model
np.save('model.npy',w)
w = np.load('model.npy')
'''