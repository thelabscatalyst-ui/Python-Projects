import numpy as np 

np.random.seed(42)
# we are performing a forward pass of a neural netork

# network dimentions
input_size = 4 #there are 4 unique features in an ultrasound per patient
hidden_1 = 8
hidden_2 = 4
output_size = 1 # we are doing binary classification, so output size is 1

# so we have a batch of 5 patients and features are 4
x = np.random.rand(5, input_size)
y = np.random.randint(0,2, (5, output_size)) # binary labels for 5 patients

# now we need to initialize the weights and biases for the network
weights_1 = np.random.rand(input_size, hidden_1) # weights for input to hidden layer 1
biases_1 = np.random.rand(1, hidden_1) # biases for hidden layer 1'

weights_2 = np.random.rand(hidden_1, hidden_2) 
biases_2 = np.random.rand(1, hidden_2)

weight_3 = np.random.rand(hidden_2, output_size)
biases_3 = np.random.rand(1, output_size)

# these are the activation functions for activation of the hidden layers and output layer
def relu(x):
    return np.maximum(0, x)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

z1 = x @ weights_1 + biases_1 #linear transformation
a1 = relu(z1) # removes the negetives
print(np.shape(a1)) # shape of the first hidden layer   

z2 = a1 @ weights_2 + biases_2
a2 = relu(z2)
print(np.shape(a2)) # shape of the second hidden layer

z3 = a2 @ weight_3 + biases_3
a3 = sigmoid(z3) # output layer activation 
# we used sigmoid beaucse this is last layer - classfication
print(np.shape(a3)) # shape of the output layer

# now we will prediction bias
predictions = (a3 > 0.5).astype(int).flatten()
print("Predictions: ", predictions)
print("True labels: ", y.flatten())

# now we will binary cross entropy loss
epsilon = 1e-8 # to avoid log(0)
y_hat = a3.flatten()

# this is the fromula for entropy loss for binary classification
bce_loss = -np.mean(y * np.log(y_hat + epsilon) + (1 - y) * np.log(1 - y_hat +epsilon))
print("Binary Cross-Entropy Loss: ", bce_loss)

#calculating accuracy
accuracy = np.mean(predictions == y.flatten())
print("Accuracy: ", accuracy)

