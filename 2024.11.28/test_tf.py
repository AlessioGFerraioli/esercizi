#Importazione delle Librerie:
import numpy as np # per operazioni numeriche.
from keras.datasets import mnist # per caricare il dataset.
from keras.models import Sequential # per costruire il modello sequenziale.
from keras.layers import Dense # per aggiungere strati al modello.
from keras.utils import to_categorical # per convertire le etichette in formato one-hot
import matplotlib.pyplot as plt  # per visualizzare i dati


# Caricamento del dataset MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Visualizzazione di un esempio
plt.imshow(X_train[0], cmap='gray')
plt.title(f'Etichetta: {y_train[0]}')
plt.show()

print("Normalizzo i dati...")
# Normalizzazione dei dati
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255
print("Dati normalizzati")
print("Reshape dei dati..")
# Reshape dei dati
X_train = X_train.reshape(-1, 28*28)
X_test = X_test.reshape(-1, 28*28)
print("Dati reshaped")
# Conversione delle etichette in formato one-hot encoding
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)



# Creazione del modello
model = Sequential()

# Aggiunta degli strati
model.add(Dense(units=128, activation='relu', input_shape=(784,)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=10, activation='softmax'))


# compilazione del modello
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print("\nModello compilato con successo.")

print("\nInizia l'addestramento del modello...")
# Addestramento del modello
history = model.fit(X_train, y_train,
                    epochs=10,
                    batch_size=32,
                    validation_split=0.1)

print("\nAddestramento del modello completato. \nVisualizzo metriche di accuracy sul test set:\n")
# Visualizzazione delle metriche
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Perdita sul test set: {test_loss:.4f}')
print(f'Accuratezza sul test set: {test_accuracy:.4f}')


# Grafico accuratezza
plt.plot(history.history['accuracy'],
label='Accuratezza Training')
plt.plot(history.history['val_accuracy'],
label='Accuratezza Validazione')
plt.xlabel('Epoca')
plt.ylabel('Accuratezza')
plt.legend()
plt.title('Andamento dell\'Accuratezza')
plt.show()

# grafioc della loss
plt.plot(history.history['loss'],
label='Perdita Training')
plt.plot(history.history['val_loss']
, label='Perdita Validazione')
plt.xlabel('Epoca')
plt.ylabel('Perdita')
plt.legend()
plt.title('Andamento della Perdita')
plt.show()


# fare predizioni
# Predizioni sul test set
predictions = model.predict(X_test)

# Conversione delle predizioni in etichette
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test, axis=1)



#Valutare le Predizioni
# con confusion matricx
from sklearn.metrics import confusion_matrix
import seaborn as sns

conf_matrix = confusion_matrix(true_classes, predicted_classes)

plt.figure(figsize=(10,8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Matrice di Confusione')
plt.xlabel('Classe Predetta')
plt.ylabel('Classe Vera')
plt.show()


# classification report
from sklearn.metrics import classification_report

report = classification_report(true_classes, predicted_classes)
print('Report di Classificazione:')
print(report)



# Visualizzazione di alcune predizioni
num_images = 5
random_indices = np.random.choice(len(X_test), num_images)
plt.figure(figsize=(15,3))
for i, idx in enumerate(random_indices):
    image = X_test[idx].reshape(28, 28)
    true_label = true_classes[idx]
    predicted_label = predicted_classes[idx]
    
    plt.subplot(1, num_images, i+1)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.title(f'T:{true_label}, P:{predicted_label}')
plt.show()












