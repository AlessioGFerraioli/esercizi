# es 2 ML

# imports
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import adjusted_rand_score, homogeneity_score
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

import numpy as np


# load the dataset
iris = load_iris()
print("\nDataset caricato.")
# crea un dataframe con pandas per analisi e visualizzaione
iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])


print("\n\nStampo le prime righe del dataset")
iris_df.head()

# pairplot con seaborn
sns.set_style("whitegrid")
sns.pairplot(iris_df,hue="target",height=3);
plt.savefig("pairplot.png")



# splitto train e test data
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=666)

# definisco la pipeline composta da normalizzazione, riduzione dimensionalita, clustering
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA()),
    ('kmeans', KMeans(n_clusters=3))
    ])    

# definisco una distribuzione dei parametri della pca per fare un gird dei migliori parametri
param_grid = {
    'pca__n_components': np.arange(2,5),   
}

# Configurazione della validazione incrociata stratificata
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Configurazione di RandomizedSearchCV
grid_search = GridSearchCV(
    pipeline, 
    param_grid=param_grid,
    cv=cv,
    scoring='accuracy')

print("Inizio il training..")

# fitto il grid search
grid_search.fit(X_train, y_train)

print("Training completato.")
# salvo la miglior versione della pipeline trovata con grid search
model_opt = grid_search.best_estimator_

#predico dei valori sui dati di test per validation
y_pred = model_opt.predict(X_test)



#adjusted_rand_score, homogeneity_score
print("\nValutazioni dell'accuracy:")
print(f"Adjusted Rand Score: {adjusted_rand_score(y_test, y_pred):.3f}")
print(f"Homogeneity Score: {homogeneity_score(y_test, y_pred):.3f}")


# ## Confronto cluster reali e predetti su INTERO dataset

# aggiungo al dataframe una colonna di predizioni per ogni dato 
y_pred_df = model_opt.predict(iris_df.drop('target', axis=1))
iris_df['predicted_class'] = y_pred_df

# faccio un remapping per avere i colori corrispondenti nel grafico 
#1 reale -> 0 pred
#0 reale -> 1 pred
#2 reale -> 2 pred 
iris_df['predicted_class'] = iris_df['predicted_class'].replace({0: 1, 1: 0, 2: 2})


# questi grafici a SEGUIRE li potrei fare tutti con una singola funzione invece di riscrivere lo stesso codice
# ma l'ho fatto così per ora e se ho tempo lo cambio

# ### plot sepal length vs sepal width
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.scatterplot(data=iris_df, x='sepal length (cm)', y='sepal width (cm)', hue='target', ax=axes[0])
sns.scatterplot(data=iris_df, x='sepal length (cm)', y='sepal width (cm)', hue='predicted_class', ax=axes[1])
fig.suptitle("Clusters in Real Data and Predicted Data\nsepal length vs sepal width")
axes[0].set_title("Real Classes")
axes[1].set_title("Predicted Classes")
fig.savefig("sep-len_sep-wid.png")

# ### sepal length vs petal width
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.scatterplot(data=iris_df, x='sepal length (cm)', y='petal width (cm)', hue='target', ax=axes[0])
sns.scatterplot(data=iris_df, x='sepal length (cm)', y='petal width (cm)', hue='predicted_class', ax=axes[1])
fig.suptitle("Clusters in Real Data and Predicted Data\nsepal length vs petal width")
axes[0].set_title("Real Classes")
axes[1].set_title("Predicted Classes")
fig.savefig("sep-len_pet-wid.png")

# ### petal length vs petal width
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.scatterplot(data=iris_df, x='petal length (cm)', y='petal width (cm)', hue='target', ax=axes[0])
sns.scatterplot(data=iris_df, x='petal length (cm)', y='petal width (cm)', hue='predicted_class', ax=axes[1])
fig.suptitle("Clusters in Real Data and Predicted Data\npetal length vs petal width")
axes[0].set_title("Real Classes")
axes[1].set_title("Predicted Classes")
fig.savefig("pet-len_pet-wid.png")

# ### petal length vs sepal width
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.scatterplot(data=iris_df, x='petal length (cm)', y='sepal width (cm)', hue='target', ax=axes[0])
sns.scatterplot(data=iris_df, x='petal length (cm)', y='sepal width (cm)', hue='predicted_class', ax=axes[1])
fig.suptitle("Clusters in Real Data and Predicted Data\npetal length vs sepal width")
axes[0].set_title("Real Classes")
axes[1].set_title("Predicted Classes")
fig.savefig("pet-len_sep-wid.png")


# ## Confronto clusters solo su TEST data
#per semplicita creo un dataframe solo con i dati di test
iris_test_df = pd.DataFrame(data=np.c_[X_test, y_test], columns=iris['feature_names'] + ['target'])
iris_test_df['predicted_class'] = y_pred
iris_test_df['predicted_class'] = iris_test_df['predicted_class'].replace({1: 0, 0: 1, 2: 2})


# ### sepal length vs sepal width
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.scatterplot(data=iris_test_df, x='sepal length (cm)', y='sepal width (cm)', hue='target', ax=axes[0])
sns.scatterplot(data=iris_test_df, x='sepal length (cm)', y='sepal width (cm)', hue='predicted_class', ax=axes[1])
fig.suptitle("Clusters in Real Data and Predicted Data\nsepal length vs sepal width")
axes[0].set_title("Real Classes")
axes[1].set_title("Predicted Classes")
fig.savefig("sep-len_sep-wid_TEST.png")


# ### sepal lengt vs petal width
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.scatterplot(data=iris_test_df, x='sepal length (cm)', y='petal width (cm)', hue='target', ax=axes[0])
sns.scatterplot(data=iris_test_df, x='sepal length (cm)', y='petal width (cm)', hue='predicted_class', ax=axes[1])
fig.suptitle("Clusters in Real Data and Predicted Data\nsepal length vs petal width")
axes[0].set_title("Real Classes")
axes[1].set_title("Predicted Classes")
fig.savefig("sep-len_pet-wid_TEST.png")

# ### petal length vs petal width
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.scatterplot(data=iris_test_df, x='petal length (cm)', y='petal width (cm)', hue='target', ax=axes[0])
sns.scatterplot(data=iris_test_df, x='petal length (cm)', y='petal width (cm)', hue='predicted_class', ax=axes[1])
fig.suptitle("Clusters in Real Data and Predicted Data\npetal length vs petal width")
axes[0].set_title("Real Classes")
axes[1].set_title("Predicted Classes")
fig.savefig("pet-len_pet-wid_TEST.png")


# ### petal length vs sepal width
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.scatterplot(data=iris_test_df, x='petal length (cm)', y='sepal width (cm)', hue='target', ax=axes[0])
sns.scatterplot(data=iris_test_df, x='petal length (cm)', y='sepal width (cm)', hue='predicted_class', ax=axes[1])
fig.suptitle("Clusters in Real Data and Predicted Data\npetal length vs sepal width")
centers = pipeline["kmeans"].cluster_centers_
axes[1].scatter(centers[:, 0], centers[:, 1], c='black', s=200);
axes[0].set_title("Real Classes")
axes[1].set_title("Predicted Classes")
fig.savefig("pet-len_sep-wid_TEST.png")
