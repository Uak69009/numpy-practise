import numpy as np 


size = np.array([650, 785, 1200, 1450, 1600, 1850, 2100, 2400])
price = np.array([45, 52, 78, 95, 105, 120, 135, 155])
print(size) # prints the size array
print(price) # prints the price array
X = np.column_stack((np.ones(len(size)), size)) # adds a column of ones to the size array to account for the intercept term in linear regression
print(X) # prints the new array with the added column of ones
# Step 2: Normal equation apply karo
theta = np.linalg.inv(X.T @ X) @ X.T @ price
c, m = theta
print(f"Slope (m): {m:.4f}")
print(f"Intercept (c): {c:.4f}")
def predict(sq_ft):
    return m * sq_ft + c

# Step 4: Test - 2000 sq ft ghar ka price?
print(f"Predicted price for 2000 sq ft: {predict(2000):.2f} lakhs")

predictions = predict(size)
mse = np.mean((price - predictions)**2)
print(f"Mean Squared Error: {mse:.4f}")
