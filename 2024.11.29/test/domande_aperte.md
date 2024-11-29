#### 3.Quale il meccanismo delle classi e degli oggetti del OOP? come funziona? che pezzi DEVE avere la classe? 
(1 punto)

Una classe è uno strumento presente in molti linguaggi di programmazione, tra cui Python, che permette di definire un tipo secondario di dati con delle specifiche personalizzabili. Una volta definita la classe, possono essere istanziate delle sue realizzazioni, chiamate "Oggetti", ovvero delle variabili che hanno delle caratteristiche comuni definite dalla classe. Ad esempio, una classe può definire al suo interno specifiche strutture di dati (attributi) o specifiche funzioni (metodi) che possono svolgere scopi comuni e utili a tutti gli oggetti della classe.

Gli oggetti appartenenti a una classe possono essere considerati come variabili di un tipo secondario definito dalla classe. Per funzionare, una classe deve avere alcune caratteristiche. La classe deve avere un nome identificativo unico, tramite il quale può essere richiamata per creare un numero a piacere di oggetti. La classe deve contenere (implicitamente o non) una funzione speciale chiamata "costruttore della classe" e identificata dal nome __init__. Il costruttore si esegue ogni volta che viene istanziato un oggetto della classe, e specifica una serie di operazioni da compiere. Il costruttore è sempre presente: se non è specificato esplicitamente, è comunque presente implicitamente come funzione che non compie nessuna operazione. 

La classe può poi contenere un numero potenzialmente infinito di attributi, ovvero variabili specifiche della classe, e metodi, ovvero funzioni specifiche della classe, che possono entrambi essere richiamati e utilizzati da tutti gli oggetti della classe. 


#### 6.Cos'è e quali sono le le fasi del ML (6)

Il Machine Learning è una branca dell'intelligenza artificiale che consiste nell'utilizzo di modelli matematici che sono in grado di adattare i propri parametri sulla base di un set di dati di "addestramento" al fine di predire un output sulla base di un input. L'addestramento funziona valutando l'ouput prodotto dal modello sull'input di addestramento secondo delle metriche di accuratezza per poi modificare iterativamente i parametri del modello al fine di ottenere una migliore accuratezza. 

Le fasi principali del machine learning sono:

Analisi e preparazione dei dati: i dati vengono esplorati e analizzati, in modo da capire le loro caratteristiche. Vengono effettuate eventuali processi di pulizia di dati mancanti o errati; vengono valutate le feature, i loro ruoli e le loro relazioni in modo da capire quali possono essere più o meno utili al modello; possono essere implementate moltissime analisi per combinare più feature insieme al fine di ottenere minor numero di feature ma più informative (riduzione della dimensionalità), o al contrario si possono creare nuove feature che sono risultati di operazioni anche complesse sulle altre feature al fine di evidenziare qualche comportamento che si ritiene utile per il modello (aumento della dimensionalità)
Split: il modello di machine learning deve poter effettuare l'apprendimento su un gruppo di dati detto training set, ed effettuare la valutazione dell'apprendimento su un altro gruppo di dati, detto test set, diverso dal primo. Il motivo della diversità viene dal fatto che il modello deve essere pronto idealmente a lavorare correttamente con dati che non conosce, diversi da quelli su cui è stato addestrato. Per questo motivo, bisogna dividere il dataset a disposizione in un set di training e uno di test, solitamente con proprizioni 80/20
Addestramento: i dati di training vengono fatti passare attraverso il modello, il quale ripete iterativamente un processo di predizione, valutazione della qualità della predizione, aggiornamento dei parametri dei modello al fine di migliorare le predizione. Questo viene ripetuto per un numero di iterazioni specificato dall'utente o finché non si raggiunge una accuratezza voluta.
Predizione: Una volta che il modello è stato addestrato, significa che i suoi parametri sono stati affinati per poter effettuare delle predizioni con una certa precisione. A questo punto dunque possiamo usare il modello per predire un output, in base a un input fornito.
Validazione: Per valutare l'accuratezza del modello, va effettuato un test dell'accurettezza dei valori predetti sul dataset di test. Esistono moltissime metriche che valutano l'accuratezza o in generale la "qualità" del modello; diversi contesti richiedono metriche di valutazione diverse.
Ottimizzazione: una volta valutato il modello, si può ripetere l'intero processo al fine di ottimizzare il risultato, ad esempio modificando il pre-processing, lo split, e le caratteristiche del modello matematico utilizzato.


#### 9.Cos'è una JOIN? di che tipo ne esistono?

La keyword JOIN in SQL indica un'operazione che combina due tabelle in una. Più JOIN possono essere combinati sequenzialmente in modo da combinare più di due tabelle. Le colonne selezionate delle tabelle vengono affiancate, unendo le righe sulla base di indici comuni. Nel momento in cui si effettua un JOIN, infatti, viene specificata una colonna per ogni tabella che funge da indice per collegare le tabelle. Esistono diversi tipi di JOIN a seconda di quali risultati prendere:
INNER JOIN: prende solo le righe che hanno corrispondenza in entrambe le tabelle (intersezione tra le tabelle)
OUTER JOIN: prende tutte le righe di tutte e due le tabelle (unione tra le tabelle)
LEFT JOIN: prende tutte le righe della prima tabella e dalla seconda solo le righe che hanno corrispondenza nella prima tabella 
RIGHT JOIN: prende tutte le righe della seconda tabella e dalla prima solo le righe che hanno corrispondenza nella seconda tabella 