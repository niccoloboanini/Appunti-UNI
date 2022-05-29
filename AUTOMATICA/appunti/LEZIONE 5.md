# ALGORITMI ITERATIVI
I sistemi dinamici possono anche *descrivere il comportamento degli algoritmi*
- In particolare vediamo adesso gli algoritmi iterativi (es. Metodo di Newton), che possono essere riscritti appunti come sistemi dinamici TD
	- Il *tempo* $t$ del sistema non è più in generale il tempo ma bensì *l'iterazione dell'algoritmo*
	- Lo *stato* $x(t)$ del sistema è rappresentato dalle *variabili in memoria*
	- Gli *ingressi* $u(t)$ sono gli *input dell'algoritmo stesso*
	- L'*uscita* $y(t)$ è l'eventuale *output dell'algoritmo*

## ALGORITMO DEL GRADIENTE
Algoritmo per trovare il minimo di una funzione $J$. Ovvero ad esempio *ottimizzare* i costi. In generale: $$ \min_{x}\ J(x) $$
- è una funzione di più variabili

*L'approccio del calcolo della derivata diventa poco utile quando le funzioni di più variabili sono complesse o a maggior ragione se non conosco la sua espressione analitica*

Si parte perciò a tentativo da un punto $x(0)$ e ci si muove:
- Verso la direzione in cui abbiamo una decrescita maggiore
![[Pasted image 20220529142703.png]]
- idea intuitiva: metto una pallina su $x(0)$ e poi per gravità questa si muoverà verso il valore minimo

#### MODELLO MATEMATICO
- Si calcola il *gradiente*, ovvero il vettore delle derivate parziali $$ \nabla J(x) = \begin{bmatrix} \frac{\partial \ J(x)}{\partial \ x_{1}} \\ \vdots \\ \frac{\partial \ J(x)}{\partial \ x_{n}} \end{bmatrix} $$
- il gradiente è perpendicolare (verso l'esterno) alla curva di livello calcolata nel punto di riferimento (in partenza $x(0)$). *Ci si muove pertanto nella direzione dell'antigradiente* (freccia in rosso - direzione di massima discesa)
![[Pasted image 20220529143841.png|300]]

In generale, l'equazione è la seguente:
$$
\boxed{x(t+1) = x(t) + \gamma \nabla J\big(x(t)\big)}
$$
- $\gamma$ è detto *passo di discesa*
- **È un sistema TD autonomo e tempo-invariante** (perché non dipende dalla iterazione $t$)
	- Diventa tempo variante se il passo di discesa non è costante (in generale negli algoritmi usati in realtà $\gamma$ diventa sempre più piccolo con l'aumentare dell iterazioni)
- Sono sistemi dinamici

- Nota: con questo algoritmo si trova un minimo locale (e solo sotto opportune ipotesi)

# MODELLI DI SISTEMI FISICI
- Partendo dalle equazioni della fisica si ricavano le informazioni necessarie per creare un sistema dinamico (comodo da gestire/studiare)
	- I sistemi fisici sono dinamici perché *evolvono nel tempo*

- Lo stato nei sistemi fisici è rappresentato dagli *elementi che immagazzinano energia* (ovvero coloro che hanno "memoria")
	- Ad esempio: correnti sugli induttori, tensioni sui condensatori, temperature, posizioni, velocità (cinetica/potenziale)...


### ESEMPIO: SISTEMA MECCANICO
- Con un solo grado di libertà "orizzontale"
![[Pasted image 20220529144841.png|300]]

Trovo le equazioni fisiche descrittive - ovvero il secondo principio di Newton (massa x accelerazione = somma delle forze)
$$
M \ \ddot y(t) = u(t) - b \ \dot y(t)
$$
- supponendo come forza d'attrito quello viscoso $-b \ \dot y(t)$
- $y(t)$ è la posizione al tempo $t$

Scegliamo come stato la *posizione e la velocità*
- A partire da queste variabili, si possono scrivere le **equazioni di stato** che cerchiamo:
$$
x(t) = \begin{bmatrix} x_{1}(t) \\ x_2(t) \end{bmatrix} = \begin{bmatrix} y(t) \\ \dot y(t) \end{bmatrix} = \begin{bmatrix} \text{posizione} \\ \text{velocita'} \end{bmatrix}
$$