# # import pandas as pd
# # from sklearn.model_selection import train_test_split
# # from sklearn.preprocessing import LabelEncoder
# # from sklearn.linear_model import LinearRegression
# # from sklearn.metrics import mean_squared_error, r2_score

# # # Load dataset
# # df = pd.read_csv("HospitalsInIndia.csv")

# # # Initialize LabelEncoder
# # le = LabelEncoder()

# # # Encode categorical columns
# # df['hospital'] = le.fit_transform(df['Hospital'])
# # df['state'] = le.fit_transform(df['State'])
# # df['city'] = le.fit_transform(df['City'])
# # df['pincode'] = le.fit_transform(df['Pincode'])

# # # Define input and output features
# # X = df[['state', 'city', 'pincode']]
# # y = df['hospital']

# # # we should alwasy do train test split 
# # # what that fucntion do it will suffle the whole cleaned dat set and give 80 % to model and give 20% for 
# # # testing so we can test the model

# # # Train-test split
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # # Initialize and train model
# # model = LinearRegression()
# # model.fit(X_train, y_train)

# # # Predict on test set
# # y_pred = model.predict(X_test)

# # # Evaluate model
# # mse = mean_squared_error(y_test, y_pred)
# # r2 = r2_score(y_test, y_pred)

# # print("Mean Squared Error:", mse)
# # print("R² Score:", r2)

# #___________________________________________________________________________________________________________



# # linear regresion with scrath with only maths no sklearn


# # Your pipeline with slight refinement:

# # 1. Create dataset (X, y)
# # 2. Initialize: m = random, c = random, learning_rate = 0.01
# # 3. For each iteration (epoch):
# #    a. Calculate predictions: y_hat = m*X + c
# #    b. Calculate MSE loss: (1/n) * sum((y - y_hat)^2)
# #    c. Calculate gradients: 
# #       - dm = -(2/n) * sum(X * (y - y_hat))
# #       - dc = -(2/n) * sum(y - y_hat)
# #    d. Update weights:
# #       - m = m - learning_rate * dm
# #       - c = c - learning_rate * dc
# # 4. Repeat step 3 until loss stops decreasing




# # step - 2

# # create dataset 
# import numpy as np

# x = np.array([1,2,3,4,5])  
# # --> input data , output data = np.array([3,5,7,9,11])


# # now lets assign the value for m and c for slope first it will be random value

# m = 0.6
# c = 0.4

# # now we are gettting the slope

# y = m*x + c

# # now the answer slope we got [1. 1.6 2.2 2.8 3.4]
# n =5
# # now we got the slope so we will use the mse mean squared error

# y_true = np.array([3,5,7,9,11])
# y_pred = np.array([1,1.6, 2.2 ,2.8 ,3.4])

# mse = np.mean(np.square(y_true - y_pred))


# # the mse is 26.959999999999997



# dm = -(2/n) * sum(x * (y_true - y_pred))
# # the ouput is  -34.4

# dc = -(2/n) * sum(y_true - y_pred)
# # the ouput is -9.6000000001



# # calculate the gradeint 
# learning_rate = 0.01 

# m_new = m - (learning_rate * dm)
# c_new = c - (learning_rate * dc)

# # print(f"here is the m_new mse : {m_new} and c_new mse : {c_new}")


# y_pred_new = m_new*x+c_new


# # output - [1.44  2.384 3.328 4.272 5.216]


# error = y_true - y_pred_new

# # output - [1.56  2.616 3.672 4.728 5.784]


# mse_new = np.mean(np.square(error))
# n = len(x)

# for loss in range(1001):
#     # Step 1: predictions
#     y_pred = m*x + c  # Use m and c, not m_new/c_new
    
#     # Step 2: MSE
#     mse = np.mean(np.square(y_true - y_pred))  # Fix this!
    
#     # Step 3: gradients
#     dm = -(2/n) * sum(x * (y_true - y_pred))
#     dc = -(2/n) * sum(y_true - y_pred)
    
#     # Step 4: UPDATE (fill this!)
#     m = m - learning_rate * dm
#     c = c - learning_rate * dc
    
#     # Step 5: print
#     if loss % 100 == 0:
#         print(f"Iteration: {loss}, MSE: {mse}, m: {m}, c: {c}")

# # now the code has been completed 



# # Thanks Linear Regression

# # lets write the code again be cause we are x 

# a = np.array([6,4,2,1,3])
# print(a)
import numpy as np
X = np.array([2,7,9,1,8])
m = 0.83
c = 0.41
y_true = m*X+c
        
print(y_true)