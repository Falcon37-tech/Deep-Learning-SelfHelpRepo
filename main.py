from sklearn.linear_model import Perceptron
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X,y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

#random state 42 is a convention in the machine learning community, it is used to ensure that the results are reproducible. By setting the random state to a specific value, you can ensure that the same random numbers are generated each time you run the code, which can be useful for debugging and comparing results.
#classes will be 2 means no. of lables will be 2

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42)

#Hyper para meters are the parameters that are set before the training of the model, they are not learned from the data. They are used to control the learning process and can have a significant impact on the performance of the model. Some common hyperparameters for a perceptron include:
#max_iter: The maximum number of iterations for the training process. This is used to prevent the training process from running indefinitely if the model does not converge.
#eta0: The learning rate for the model. This controls how much the weights are updated during each iteration of the training process. A higher learning rate can lead to faster convergence, but it can also cause the model to overshoot the optimal weights.
#random_state: The random state for the model. This is used to ensure that the results are reproducible. By setting the random state to a specific value, you can ensure that the same random numbers are generated each time you run the code, which can be useful for debugging and comparing results.
#tol: The tolerance for the stopping criterion. This is used to determine when the training process should stop. If the change in the weights is less than the specified tolerance, the training process will stop. A smaller tolerance can lead to a more accurate model, but it can also increase the training time. 
clf = Perceptron(
    max_iter = 1000,
    eta0=0.1,
    random_state = 42,
    tol = 1e-3,
    shuffle=True
    )

#fit method is used to train the model on the training data. It takes the training data (X_train) and the corresponding labels (y_train) as input and updates the weights of the model based on the training data. The fit method will iterate through the training data and update the weights until it reaches the maximum number of iterations or until the change in weights is less than the specified tolerance. After fitting the model, you can use it to make predictions on new data or evaluate its performance on a test set.

clf.fit(X_train, y_train)


accuracy = clf.score(X_test, y_test)
print(f"Accuracy is {accuracy}")
