# %% [markdown]
# # Esercizio finale 2
# 
# ### Esercizio riepilogativo di numpy, pandas, matplotlib e seaborn
# 
# L'obiettivo di questo esercizio è generare un set di dati, analizzarli con pandas e visualizzarli con matplotlib e seaborn.
# 
# Devono essere implementati i seguenti punti:
# 
# 1. __Gerazione dei dati__: con numpy, generare una serie temporale di 305 giorni di dati, simulando il numero di visitatori giornalieri in un ospedale. Assumere che il numero medio di visitatori sia 1200 con una deviazione standard di 900. Mano mano che il tempo passa, la media aumenta progressivamente mentre la deviazione standard diminuisce progressivamente.
# 
# 2. __Creazione del DataFrame__: creare un dataframe pandas con le date come indice e il numero di visitatori come colonna. Ogni visitatore ha una "motivazione" per il ricovero (problema alle ossa, al cuore, alla testa), generata casualmente. 
# 
# 3. __Analisi dei dati__: calcolare il numero medio di visitatori per mese e la deviazione standard e quale patologia è più o meno trovata.
# 
# 4. __Visualizzazione dei dati__: 
#     - creare un grafico a linee del numero di visitatori gionralieri
#     - aggiungere al grafico la media mobile a 7 giorni per mostrare la tendenza settimanale
#     - creare un secondo grafico che mostri la media mensile dei visitatori.
#     - creare un grafioc che mostri la distribuzione dei motivi per il ricovero.

# %% [markdown]
# # Import Librerie

# %%
import numpy as np
import random 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# # 1. Generazione dei dati
# 
# 
#  con numpy, generare una serie temporale di 305 giorni di dati, simulando il numero di visitatori giornalieri in un ospedale. Assumere che il numero medio di visitatori sia 1200 con una deviazione standard di 900. Mano mano che il tempo passa, la media aumenta progressivamente mentre la deviazione standard diminuisce progressivamente.

# %% [markdown]
# Per semplicità, genero un attimo una versione con la media e la deviazione fisse.

# %%
# genera time series con pandas
list_date = pd.date_range(start='2024-01-01', periods=305, freq='D')

# n_visitatori è una lista dei numeri di visitatori 
# nb : il numero di visitatori deve essere intero positivo
n_visitatori = []
# parametri per la distr normale
avg=1200
std=900
for giorno in list_date:
    random_number = -1
    # se il numero di visitatori è negativo, lo scarto e ne genero un altro 
    while random_number < 0:
        random_number = np.random.normal(loc=avg, scale=std)
        if random_number >= 0:
            n_visitatori.append(int(random_number))
    # ogni giorno, la media aumenta e la deviazione standard diminuisce        
    avg = avg*1.001
    std = std*0.99

# %% [markdown]
# 
# # 2. Creazione del DataFrame
# 
# Creare un dataframe pandas con le date come indice e il numero di visitatori come colonna. Ogni visitatore ha una "motivazione" per il ricovero (problema alle ossa, al cuore, alla testa), generata casualmente. 
# 
# Dunque genererò due dataframe. Il primo è:
# 
# DataFrame __date__
# 
# Indice: data 
# 
# Colonne: numero_visitatori, n_visitatori_testa, n_visitatori_cuore, n_visitatori_testa
# 
# 
# DataFrame __visitatori__
# 
# Indice: id 
# 
# Colonne: data, motivazione=("ossa" oppure "cuore" oppure "testa")

# %% [markdown]
# ### Generazione Dataframe date

# %%
# create a dictionary with date and number of visitors
date = pd.DataFrame({'giorno': list_date, 'n_visitatori': n_visitatori})

# %%
date.head(-10)

# %% [markdown]
# ### Generazione Dataframe visitatori

# %%
# genero due liste con le quali creare il dataframe visitatori
# una che contiene il giorno ripetuto tante volte quante sono i visitatori del giorno 
# l'altra che in corrispondenza genera una motivazione casuale
# queste due liste avranno la stessa lunghezza e messe insieme identificano un singolo visitatore

indici_giorni = []
motivazioni = []
for giorno in date.giorno:
    n_visitatori_odierno = date.loc[date['giorno'] == giorno, 'n_visitatori'].values[0]
    #print(f"Giorno {giorno}")
    #print(f"Visitatori tot: {n_visitatori_odierno}")
    for i in range(n_visitatori_odierno):
        motivazioni.append(random.choice(["ossa", "cuore", "testa"]))
        #print(f"Motivazione: {motivazione}")
        indici_giorni.append(giorno)

# %%
#creo il dataframe visitatori, che ha come colonne data e motivazione
visitatori = pd.DataFrame({'data': indici_giorni,'motivazione': motivazioni})

# %%
visitatori.tail()

# %% [markdown]
# # 3. Analisi dei dati
# 
#  calcolare il numero medio di visitatori per mese e la deviazione standard e quale patologia è più o meno trovata.
# 

# %%
# calcolo media e deviazione standard di visitatori per mese
n_visitatori_giornalieri_mese = []
media_mese = []
std_mese = []
# for per scorrere sui mesi
for i in date["mese"].unique():
    n_visitatori_giornalieri_mese.append(date[date['mese'] == i]["n_visitatori"])
    media_mese.append(n_visitatori_giornalieri_mese[i-1].mean())
    std_mese.append(n_visitatori_giornalieri_mese[i-1].std())


# %%
# count occorrenza di ogni motivazione
motivazioni_count = visitatori['motivazione'].value_counts()
print("Occorrenza totale delle motivazioni:")
print(motivazioni_count)

# %% [markdown]
# # 4. Visualizzazione dei dati 
# - creare un grafico a linee del numero di visitatori gionralieri
# - aggiungere al grafico la media mobile a 7 giorni per mostrare la tendenza settimanale
# - creare un secondo grafico che mostri la media mensile dei visitatori.
# - creare un grafioc che mostri la distribuzione dei motivi per il ricovero.

# %% [markdown]
# ### Numero di visitatori giornalieri

# %%
# creo un grafico a linee del numero di visitatori giornalieri

fig, ax = plt.subplots(figsize=(15,5))

ax.plot(date.giorno, date.n_visitatori, linewidth=0.3)
ax.set_title("Numero di visitatori giornalieri")
ax.set_ylabel("Numero di visitatori")
ax.set_xlabel("Data")
plt.xticks(rotation=45)


# %% [markdown]
# #### Aggiungere al grafico la media mobile a 7 giorni per mostrare la tendenza settimanale

# %%
#calcolo la media mobile a 7 giorni per mostrare la tendenza sett
date['media_mobile_7giorni'] = date.n_visitatori.rolling(window=7).mean()


# %%

fig, ax = plt.subplots(figsize=(15,5))
# parte per creare il grafico uguale a prima
ax.plot(date.giorno, date.n_visitatori, linewidth=0.3, label="Numero visitatore giornaliero")
# plot della media mobile
ax.plot(date.giorno, date.media_mobile_7giorni, color='red', linestyle='dashed', label='Media mobile 7 giorni')

ax.set_title("Numero di visitatori giornalieri")
ax.set_ylabel("Numero di visitatori")
ax.set_xlabel("Data")
ax.legend()
plt.xticks(rotation=45)


# %% [markdown]
# ### creare un secondo grafico che mostri la media mensile dei visitatori.

# %%
# mostra media di ogni mese con boxplot

fig, ax = plt.subplots(figsize=(15,5))

ax.boxplot(n_visitatori_giornalieri_mese, labels=date["mese"].unique())
ax.set_title("Medie numero visitatori al mese")
ax.set_xlabel("Mese")
ax.set_ylabel("Numero di visitatori")


# %% [markdown]
# ### creare un grafico che mostri la distribuzione dei motivi per il ricovero.

# %%
# calcolo percentuali tre motivazioni per mese
n_visitatori_giornalieri_mese = []
cuore_mese = [0]*len(date["mese"].unique())
ossa_mese = [0]*len(date["mese"].unique())
testa_mese = [0]*len(date["mese"].unique())

# for per scorrere sui mesi
for i in date["mese"].unique():
    for giorno in date[date['mese'] == i]["giorno"]:
        for motivazione in visitatori[visitatori['data'] == giorno]["motivazione"]:
            if motivazione == "cuore":
                cuore_mese[i-1] += 1
            elif motivazione == "ossa":
                ossa_mese[i-1] += 1
            elif motivazione == "testa":
                testa_mese[i-1] += 1


# %%
mesi = pd.DataFrame({'mese': date["mese"].unique(), 'cuore': cuore_mese, 'ossa': ossa_mese, 'testa': testa_mese})

# %%
mesi

# %%
# plot motivazioni per mese
fig, ax = plt.subplots(figsize=(15,5))
barwidth = 0.1
ax.bar(mesi["mese"], mesi["cuore"], width=barwidth, color="pink", label="Cuore")
ax.bar(mesi["mese"]+1.1*barwidth, mesi["ossa"], width=barwidth, color="lightgrey", label="Ossa")
ax.bar(mesi["mese"]+2.2*barwidth, mesi["testa"], width=barwidth, color="lightblue", label="Testa")

ax.legend()
ax.set_title("Motivazioni di visite per mese")
ax.set_xlabel("Mese")
ax.set_ylabel("Numero di visitatori")

# %%
mesi["tot"] = mesi["cuore"] + mesi["ossa"] + mesi["testa"]
mesi["cuore_percentuale"] = mesi["cuore"] / mesi.tot * 100
mesi["ossa_percentuale"] = mesi["ossa"] / mesi.tot * 100
mesi["testa_percentuale"] = mesi["testa"] / mesi.tot * 100

# %%
# plot motivazioni percentuali per mese


fig, ax = plt.subplots(figsize=(15,5))
barwidth = 0.1
ax.bar(mesi["mese"], mesi["cuore_percentuale"], width=barwidth, color="pink", label="Cuore (%)")
ax.bar(mesi["mese"]+1.1*barwidth, mesi["ossa_percentuale"], width=barwidth, color="lightgrey", label="Ossa (%)")
ax.bar(mesi["mese"]+2.2*barwidth, mesi["testa_percentuale"], width=barwidth, color="lightblue", label="Testa (%)")
#ax.barplot(x="mese", y="ossa", ax=ax, width=barwidth, color="grey", label="Ossa")
ax.legend()
ax.set_title("Motivazioni di visite per mese in percentuale")
ax.set_xlabel("Mese")
ax.set_ylabel("Percentuale di visitatori")

# %%



