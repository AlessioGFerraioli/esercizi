'''
2024.11.26 10.36

esercizio scikit-learn per classificazione con LinearRegressoin usando il dataset Iris

carica dataset iris
standardizza usando standardscaler
suddividi i dati in training e test (70/30)
applica l'algoritmo decisointreeclassifier
valuta la performance del modello usando classification_report
visualizza la matrice di confusione
'''

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

iris = load_iris()

print("Prime 5 righe del dataset iris:")
print(iris.data[:5])
print()

# definisci x e y
X = iris.data
y = iris.target

# standardizza i dat icon standard scaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


print("Dataset standardizzato:")
print(X_scaled[:5])



# separa in train e test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# definisci il modello linear regressoin
model = DecisionTreeClassifier()

# training
model.fit(X, y)

# make a prediction
predictions_test = model.predict(X_test)

# evaluate the accuracy
accuracy = accuracy_score(y_test, predictions_test)

print("DecisionTreeClassifier")
print("Accuracy on test data:", accuracy)
# mostro classification report
print(classification_report(y_test, predictions_test))
# mostro matrice di confusione
print("Matrice di confusione:")
cm = confusion_matrix(y_test, predictions_test)
print(cm)

# esempio di predizoine
print("Esempio di predictoin")
print("REAL   |   PREDICTED")
for i in range(len(y_test)):
    print(f"{y_test[i]}      |       {predictions_test[i]}")




