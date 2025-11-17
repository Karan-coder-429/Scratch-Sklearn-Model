#now we will write the code of lr with full power and under the time limit lets boomm
# import numpy as np
# import numpy as np

# x = np.array([2, 5, 8, 11, 14, 17, 20, 23, 26, 29])


# y_true = np.array([7, 13, 19, 25, 31, 37, 43, 49, 55, 61]) 

# n = 10

# m = 0.6
# c = 0.4

# y_pred = m*x+c  # [ 1.6  3.4  5.2  7.   8.8 10.6 12.4 14.2 16.  17.8]


# mse = np.mean(np.square(y_true - y_pred))   # 736.0200000000001

 
# for loss in range(10000):
#     lr = 0.001
#     y_pred = m*x + c
#     mse = np.mean(np.square(y_true - y_pred))
#     dm = (-2/n) * sum(x * (y_true - y_pred))
#     dc = (-2/n) * sum(y_true - y_pred)

#     m = m - lr * dm
#     c = c - lr * dc

#     # Optional: recalculate y_pred after update
#     y_pred = m*x + c
#     mse = np.mean(np.square(y_true - y_pred))

#     if loss % 100 == 0:
#         print(f"Iteration: {loss}, MSE: {mse:.4f}, m: {m:.4f}, c: {c:.4f}")




# lets write the linear regression scartch


import numpy as np

x = np.array([5,1,7,0])
m = 0.7
c = 0.3
y_true = np.array([45,13,61,5])

n = len(x)
epochs = 1000001
learning_rate = 0.000001
for i in range(epochs) :
    y_pred = m*x+c
    mse = np.mean(np.square(y_true-y_pred))

    # now lets calculate the gradient 

    dm = -(2/n)*np.sum(x*(y_true-y_pred))
    dc = -(2/n)*np.sum(y_true-y_pred)

    # now lets go for optimzer

    m = m - (learning_rate*dm)
    c = c - (learning_rate*dc)

    if i % 100 == 0:
       print(f"Iteration: {i}, MSE: {mse:.4f}, m: {m:.4f}, c: {c:.4f}")


