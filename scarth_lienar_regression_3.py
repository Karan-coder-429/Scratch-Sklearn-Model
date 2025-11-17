# Ok here we are going to write the linear regression from scratch


import numpy as np

X = np.array([2,5,6,7,1])

# m = 9.5
# c = 2.3

m = 0.78
c = 0.23

y_pred= np.array( [21.3, 49.8 ,59.3, 68.8, 11.8])

y_true = np.array([21.3, 49.8 ,59.3, 68.8, 11.8])



mse = np.mean(np.square(y_true-y_pred))


epoch = 100000
n = len(X)
learning_rate = 0.0001

for loss in range(epoch) :
    y_pred = m*X+c
    mse = np.mean(np.square(y_true-y_pred))
    # now lets calcualte the graindet as pipeline say
    
    dm = -(2/n) * np.sum(X*(y_true-y_pred))
    dc = -(2/n) * np.sum(y_true-y_pred)
    
    
    # now lets take the optimzer
    
    m = m - (dm*learning_rate)
    c = c - (dc*learning_rate)
    
    if loss % 100 == 0 :
        print(f"The Iteration : {loss},MSE : {mse},M : {m},C : {c}")


