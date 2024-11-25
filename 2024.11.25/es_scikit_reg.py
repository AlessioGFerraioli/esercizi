'''
2024.11.25
esercizio scikit-learn per classificazione con LinearRegressoin usando il dataset Iris

'''

from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()

print("Prime 5 righe del dataset iris:")
print(iris.data[:5])
print()

# definisci x e y
X = iris.data
y = iris.target

# separa in train e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# definisci il modello linear regressoin
model = LinearRegression()

# training
model.fit(X, y)

# make a prediction
predictions_test = model.predict(X_test)
predictions_test = [round(pred) for pred in predictions_test]  # round predictions to the nearest integer for classification problems

# evaluate the accuracy
accuracy = accuracy_score(y_test, predictions_test)

print("Linear Regression Model")
print("Accuracy on test data:", accuracy)

print("REAL   |   PREDICTED")
for i in range(len(y_test)):
    print(f"{y_test[i]}      |       {predictions_test[i]}")




