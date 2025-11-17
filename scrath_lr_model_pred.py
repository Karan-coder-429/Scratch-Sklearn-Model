# # Real house data example

# # later we will add the city ,state mdta and take predction 

# import numpy as np
# square_feet = np.array([1000, 1500, 2000, 2500, 3000])  # Input
# prices = np.array([200000, 300000, 400000, 500000, 600000])  # Output (training data)

# # Your scratch model trains on this
# m = 0.5
# c = 10000
# learning_rate = 0.01
# n = len(square_feet)

# # Train for 10000 iterations (same code you wrote)
# for i in range(10000):
#     y_pred = m * square_feet + c
#     mse = np.mean(np.square(prices - y_pred))
#     dm = (-2/n) * sum(square_feet * (prices - y_pred))
#     dc = (-2/n) * sum(prices - y_pred)
#     m = m - learning_rate * dm
#     c = c - learning_rate * dc

# # After training, your model learned the relationship!
# # Now you can predict NEW house prices:

# new_house_sqft = int(input("Enter House Sqft : "))

# predicted_price = m * new_house_sqft + c
# print(f"Predicted price: ${predicted_price}") #here ourput is givng non so we will sovle it 



# import numpy as np 

# x = np.array([3, 7, 11, 15, 19, 23])   # ouput ---> [14 30 46 62 78 94],the m = 4,c =2
# n = 6
# learning_rate = 0.01

# m = 0.63
# c = 0.45

# y_true = np.array([14, 30, 46 ,62 ,78 ,94])

# y_pred = np.array([ 2.34,  4.86  ,7.38  ,9.9  ,12.42, 14.94])

# mse = np.mean(np.square(y_true - y_pred))  # output loss --> 2587.5182666666665



# for loss in range(1000) :
#     lr = 0.001
#     n =6

#     #calcualte the slope
#     y_pred = m*x+c
#     # calcuate the mse mean sqared error 
#     mse = np.mean(np.square(y_true - y_pred))
#     # now the step for calculateting the gradinet
#     dm = (-2/n)*sum(x*(y_true-y_pred))
#     dc = (-2/n)*sum(y_true-y_pred)
#     # now lets put the optimzer
#     m= m-(lr*dm)
#     c = c-(lr*dc)

#     if loss%100 == 0:
#         print(f"The Loss is : {loss},MSE :{mse}, M : {m}, C : {c}")


 

# import numpy as np 



# x = np.array([12, 47, 33, 89, 25, 61])
# m = 0.8
# c = 0.3

# y_true = np.array([ 73 ,283 ,199 ,535, 151 ,367])

# y_pred = np.array([ 9.9 ,37.9, 26.7 ,71.5, 20.3 ,49.1])

# mse = np.mean(np.square(y_true-y_pred))


# for loss in range(1000) :
#     lr = 0.00001
#     n = 6
#     y_pred = m*x+c
#     mse = np.mean(np.square(y_true - y_pred))
#     dm = (-2/n)*sum(x*(y_true - y_pred))
#     dc = (-2/n)*sum(y_true-y_pred)
#     m = m - (lr*dm)
#     c = c - (lr*dc)

#     if loss % 100 == 0 :
#         print(f"The Loss is : {loss} , MSE : {mse}, M : {m} , C : {c}")


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # ---------- Data ----------
# np.random.seed(42)
# x = np.linspace(0, 10, 50)
# y = 3 * x + 7 + np.random.randn(50) * 2   # line with noise

# # ---------- Hyperparams ----------
# lr = 0.01
# epochs = 100
# m, c = 0, 0  # initial values

# history = []  # store (m,c) at each step

# # ---------- Gradient Descent ----------
# for i in range(epochs):
#     y_pred = m * x + c
#     dm = (-2/len(x)) * np.sum(x * (y - y_pred))
#     dc = (-2/len(x)) * np.sum(y - y_pred)
#     m = m - lr * dm
#     c = c - lr * dc
#     history.append((m, c, y_pred))

# # ---------- Animation ----------
# fig, ax = plt.subplots()
# ax.scatter(x, y, color="blue", label="Data")
# line, = ax.plot([], [], color="red", lw=2, label="Prediction")
# ax.legend()

# def init():
#     line.set_data([], [])
#     return line,

# def update(frame):
#     m, c, y_pred = history[frame]
#     line.set_data(x, m*x + c)
#     ax.set_title(f"Epoch {frame}, m={m:.2f}, c={c:.2f}")
#     return line,

# ani = FuncAnimation(fig, update, frames=len(history), init_func=init,
#                     interval=200, blit=True, repeat=False)

# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Data
# x = np.array([12, 47, 33, 89, 25, 61])
# y_true = np.array([73, 283, 199, 535, 151, 367])

# # Initial parameters
# m = 0.8
# c = 0.3
# lr = 0.001
# n = len(x)
# epochs = 500

# history = []  # store states

# # Gradient Descent training loop
# for epoch in range(epochs):
#     y_pred = m * x + c
#     mse = np.mean((y_true - y_pred) ** 2)
#     dm = (-2/n) * np.sum(x * (y_true - y_pred))
#     dc = (-2/n) * np.sum(y_true - y_pred)
#     m = m - lr * dm
#     c = c - lr * dc
#     history.append((m, c, mse))

# # ---------- Animation ----------
# fig, ax = plt.subplots()
# ax.scatter(x, y_true, color="blue", label="Data")  # real points
# line, = ax.plot([], [], color="red", lw=2, label="Prediction")
# ax.legend()

# def init():
#     line.set_data([], [])
#     return line,

# def update(frame):
#     m, c, mse = history[frame]
#     y_line = m * x + c
#     # plot best fit line for given frame
#     line.set_data(x, y_line)
#     ax.set_title(f"Epoch {frame}, MSE={mse:.2f}, m={m:.2f}, c={c:.2f}")
#     return line,

# ani = FuncAnimation(fig, update, frames=len(history), init_func=init,
#                     interval=200, blit=True, repeat=False)

# plt.show()
 

# 
# ________________________________________________________________________________________________________

# Best Animation To Learn About Overshoting and other thing 


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # ---- Define Loss Function ----
# # f(x,y) = x^2 + y^2 (simple convex bowl)
# def loss(x, y):
#     return x**2 + y**2

# def grad(x, y):
#     return np.array([2*x, 2*y])  # gradient wrt x and y

# # ---- Gradient Descent ----
# lr = 0.8   # learning rate (try 0.05 vs 0.8 to see stable vs overshoot)
# epochs = 30
# point = np.array([6.0, 6.0])   # start point

# history = [point.copy()]
# for i in range(epochs):
#     g = grad(point[0], point[1])
#     point = point - lr * g
#     history.append(point.copy())

# history = np.array(history)

# # ---- Plot Contours ----
# x_vals = np.linspace(-7, 7, 400)
# y_vals = np.linspace(-7, 7, 400)
# X, Y = np.meshgrid(x_vals, y_vals)
# Z = loss(X, Y)

# fig, ax = plt.subplots(figsize=(6,6))
# contours = ax.contour(X, Y, Z, levels=30, cmap="jet")
# ax.clabel(contours, inline=True, fontsize=8)
# point_plot, = ax.plot([], [], 'ro-', markersize=8)

# def init():
#     point_plot.set_data([], [])
#     return point_plot,

# def update(frame):
#     point_plot.set_data(history[:frame+1,0], history[:frame+1,1])
#     ax.set_title(f"Step {frame}, x={history[frame,0]:.2f}, y={history[frame,1]:.2f}")
#     return point_plot,

# ani = FuncAnimation(fig, update, frames=len(history), init_func=init,
#                     interval=500, blit=True, repeat=False)

# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Non-convex function (2D Gaussian mixture style)
# def f(x, y):
#     return (3*(1-x)**2*np.exp(-(x**2) - (y+1)**2)
#             -10*(x/5 - x**3 - y**5)*np.exp(-x**2 - y**2)
#             -1/3*np.exp(-(x+1)**2 - y**2))

# # Gradient (numerical approximation)
# def grad(x, y):
#     eps = 1e-5
#     dfdx = (f(x+eps,y)-f(x-eps,y))/(2*eps)
#     dfdy = (f(x,y+eps)-f(x,y-eps))/(2*eps)
#     return np.array([dfdx, dfdy])

# # Gradient Descent
# lr = 0.10
# epochs = 60
# point = np.array([2.0, 2.0])   # start near top-right hill
# history = [point.copy()]

# for i in range(epochs):
#     g = grad(point[0], point[1])
#     point = point - lr * g
#     history.append(point.copy())

# history = np.array(history)

# # -------- Visualization 2D Contour --------
# x_vals = np.linspace(-3, 3, 200)
# y_vals = np.linspace(-3, 3, 200)
# X, Y = np.meshgrid(x_vals, y_vals)
# Z = f(X, Y)

# fig, ax = plt.subplots(figsize=(7,6))
# contour = ax.contourf(X, Y, Z, levels=50, cmap="viridis")
# ax.contour(X, Y, Z, levels=20, colors="black", alpha=0.3)
# point_plot, = ax.plot([], [], "ro-", markersize=5)

# def init():
#     point_plot.set_data([], [])
#     return point_plot,

# def update(frame):
#     point_plot.set_data(history[:frame+1,0], history[:frame+1,1])
#     ax.set_title(f"Step {frame}, x={history[frame,0]:.2f}, y={history[frame,1]:.2f}")
#     return point_plot,

# ani = FuncAnimation(fig, update, frames=len(history),
#                     init_func=init, interval=500, blit=True, repeat=False)

# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation

def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

def grad_himmelblau(x, y):
    dx = 4*x*(x**2 + y - 11) + 2*(x + y**2 - 7)
    dy = 2*(x**2 + y - 11) + 4*y*(x + y**2 - 7)
    return np.array([dx, dy])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x_vals = np.linspace(-6, 6, 400)
y_vals = np.linspace(-6, 6, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = himmelblau(X, Y)

ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap=cm.terrain, alpha=0.8, edgecolor='none')
ax.set_title("🌄 Gradient Descent on Himmelblau Function", fontsize=14)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Loss")

start_point = np.array([5.0, 5.0])
lr = 0.01
iterations = 500

point = start_point.copy()
path = [point.copy()]

for _ in range(iterations):
    grad = grad_himmelblau(point[0], point[1])
    point -= lr * grad
    path.append(point.copy())

path = np.array(path)

ball, = ax.plot([], [], [], 'ro', markersize=8)
line, = ax.plot([], [], [], 'r-', lw=2)

def init():
    ball.set_data([], [])
    ball.set_3d_properties([])
    line.set_data([], [])
    line.set_3d_properties([])
    return ball, line

def update(frame):
    x, y = path[frame]
    z = himmelblau(x, y)
    ball.set_data([x], [y])
    ball.set_3d_properties([z])
    line.set_data(path[:frame, 0], path[:frame, 1])
    line.set_3d_properties([himmelblau(px, py) for px, py in path[:frame]])
    return ball, line

ani = FuncAnimation(fig, update, frames=len(path), init_func=init, interval=150, blit=True, repeat=False)

plt.tight_layout()
plt.show()

