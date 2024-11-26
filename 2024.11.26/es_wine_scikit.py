'''
2024.11.26 11.23

scikit learn
esercizio base con dataset Wine

1. carica il dataset wine

2 standardizza le caratteristiche

3 suddividi i dati in trainig e test (70/30)

4 applica un algoritmo di classificazione (decisiontreeclassifier)

5 valuta la performance del modello

6 visualizza la matrice di confusione


'''


# Importare i moduli necessari
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Caricare il dataset wine
wine = load_wine()

# Stampare le prime 5 righe del dataset

print("Prime 5 righe del dataset wine:")
print(wine.data[:5])
print()

# Definire x e y
X = wine.data
y = wine.target

# Standardizzare le caratteristiche 
scaler = StandardScaler()
# Applicare lo scaler alle caratteristiche
X_scaled = scaler.fit_transform(X)

# Suddivisione dei dati in train e test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=420)

# Definire il modello 
model = DecisionTreeClassifier()

# Addestrare il modello
model.fit(X_train, y_train)

# Predire i valori per il test
y_predicted = model.predict(X_test)

# Calcolare l'accuratezza
accuracy = accuracy_score(y_test, y_predicted)
print("Accuracy del modello:", accuracy)

# Visualizzare il report di accuratezza:
print("Classification Report:")
print(classification_report(y_test, y_predicted))

# Visualizzare la matrice di confusione
cm = confusion_matrix(y_test, y_predicted)
fig, ax = plt.subplots(figsize=(5, 5))
sns.heatmap(cm, annot=True, ax=ax)

ax.set_title("Wine Dataset: Decision Tree Classifier\nConfusion Matrix")
ax.set_xlabel("Predicted Label")
ax.set_ylabel("True Label")

# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)

textstr = classification_report(y_test, y_predicted)
# place a text box in upper left in axes coords
ax.text(0.25, 0.95, textstr, transform=ax.transAxes, fontsize=6,
        verticalalignment='top', bbox=props)
fig.savefig("wine_DecisionTreeClass_confusion_matrix.png")

