Si possono esprimere poi tutte le equazioni di stato sotto forma *matriciale*:
$$
x(t+1)=\underbrace{\begin{bmatrix} 1/2 & 1/2 & 0 \\ 1/2 & 1/2 & 1/4 \\ 0 & 1/4 & 1/2\end{bmatrix}}_{\text{A}} x(t)
$$
- *La matrice $\text{A}$ quindi governa la transizione di stato*
- Il sistema è **TD** **TI** (no dipendenza dal tempo) e **autonomo** non essendo presenti ingressi esterni
- **ogni colonna ha somma $1$**, perché in un certo istante discreto $t$ dobbiamo trovarci in un certo stato --> matrice **stocastica**

Un esempio di simulazione del sistema è il seguente:
- Si parte da un evento certo, ad esempio *soleggiato*: $$\underbrace{\begin{bmatrix}1 \\ 0 \\ 0\end{bmatrix}}_{x_{0}}$$
	- A partire da qui, sfruttando la matrice $\text{A}$ si può calcolare una distribuzione di probabilità e capire in generale come si evolverà il sistema
		- Questo perché vale l'**ipotesi di Markov** (processo senza memoria, mi basta sapere com'è il modello al tempo $t$ per capire in generale come potrebbe evolversi)
			- Nel nostro caso abbiamo un *processo di Markov omogeneo*, in quanto le probabilità $a_{ij}$ di transizione sono indipendenti dal tempo
			- Se avessimo un ingresso che governa la transizione, si parlerebbe di *processo decisionale di Markov*, del tipo: $\text{A}(u(t))$

## MODELLO GENERALE
Troviamo una forma generale per il modello transizione di stato:
$$
\large \boxed{\begin{align*}
x(t+1) &= \alpha_{1i}x_{1}(t) + \alpha_{2i}+x_{2}(t) + \dots + \alpha_{ni}x_{n}(t)\\
&=\sum_{j=1}^{n} \alpha_{ji}x_{j}(t)
\end{align*}}
$$
Dove:
- $x_{i}(t)$ è la prob. di trovarsi al tempo $t$ nello stato $i$
- $\alpha_{ij}$ è la prob. di transizione dallo stato $i$ allo stato $j$

Come già detto deve valere: $\sum_{i=1}^{n} \alpha_{ji}=1$ (matrice stocastica)

### ESEMPIO: PAGE RANK
- Algoritmo che consente di associare un peso (che quantifica l'importanza) a ciascuna pagina web
- Applicabile su ogni grafo relazionale composto ovviamente da nodi

![[Pasted image 20220528154251.png|200]]

Si basa su un modello probabilistico caratterizzato da una *random walk* sul grafo (camminatore casuale)
- Si cerca la probabilità di trovarsi in un certo nodo dopo un certo periodo di tempo (idealmente all'infinito), eseguendo appunto una camminata aleatoria
	- In figura è più probabile che asintoticamente ci si trovi nel nodo $\text{B}$

#### FORMULAZIONE MATEMATICA
Ipotizzando che l'utente scelga i link a cui accedere in maniera casuale:
$$
\large \alpha_{ji} = \begin{cases} 1/L_{j}& \text{se } j \in N_{i} \\ 0 & \text{altrimenti} \end{cases}
$$
Dove:
- $L_{j}$ sono i possibili link a cui accedere a partire da $j$
- $N_{i}$ totale delle pagine che puntano a $i$
- $\alpha_{ji}$ è al solito la prob. di passare dalla pagina $j$ alla pagina $i$

Si giunge in maniera semplice alla equazione di stato *calcolando la probabilità che l'utente si trovi a una pagina $i$ al tempo $t+1$*:
$$
x_{i}(t+1) = \sum_{j\in N_i}^{} x_{j}(t) \cdot \frac{1}{L_{j}}  \quad , \quad i=1,\dots,N
$$
- ovvero la somma di tutte le pagine che linkano a $i$  moltiplicata per la probabilità di passare da $j$ a $i$, che è appunto $1/L_{j}$. Rieseguo tutto per tutte le $N$ pagine web
- stesso modello delle previsioni del tempo, solo che in quel caso avevo solo $3$ stati

	Per simulare il modello, si parte da una condizione iniziale casuale, del tipo $x_{i}(0)=1/n$
	- ovvero parto da una pagina a caso e faccio partire l'algoritmo

#### ESEMPIO
![[Pasted image 20220528155905.png|500]]

L'elemento $A_{ij}$ mi dice la probabilità di passare da $j$ a $i$ (si legge al "contrario")
- Ad esempio $A_{23}$ mi dice la probabilità di passare dallo stato $3$ allo stato $2$.

#### CONVERGENZA E DAMPING FACTOR
Nel modello che abbiamo presentato *non* è garantita la convergenza. Infatti c'è la possibilità che si finisca in una pagina e che da lì non ci si muova più per com'è fatto il grafico (*nodo assorbente*).
- Per tale motivo si introduce il **Damping factor ($d$)** che garantisce che anche se giungiamo su un nodo assorbente, si passa comunque a un altro nodo (pagina), scegliendo se necessario quest'ultimo in modo casuale.
- Questo garantisce la convergenza, ovvero esiste sempre una possibilità di essere in una determinata pagina $i$ dopo un certo periodo di tempo sufficiente, in generale: $$ \lim_{t \to \infty} x_{i}(t) = \overline x_{i}  $$

In particolare, con probabilità $d$ si sceglie uno dei link possibili (come sempre - camminata casuale) e con probabilità $1-d$ si sceglie una pagina a caso invece di seguire i link, pertanto:
$$
x_{i}(t+1) = \underbrace{d \sum_{n \in N_i}^{} \frac{x_j(t)}{L_{j}}}_{\text{pagina linkata}}+\underbrace{(1-d)\sum_{j=1}^{n} \frac{x_j(t)}{n}}_{\text{una pagina a caso}}
$$
- scelta tipica del fattore: $d>0  \quad , \quad d = 0.5$

L'esempio precedente diventa:
![[Pasted image 20220528173425.png|500]]

- (rientra negli esempi di catena di Markov)

# MODELLI DI INFLUENZA
In questi modelli vengono descritti i modi con cui una certa grandezza può *influenzare* un'altra grandezza.
- Più in generale studiano le *interazioni* tra varie grandezza

### ESEMPIO: MODELLO PREDA-PREDATORE
Si studia come l'interazione tra *due animali* influenza l'*ecosistema*
- La prima popolazione è relativa alla preda ed è indicata con $x_{1}(t)$
- La seconda popolazione è relativa al predatore ed è indicata con $x_{2}(t)$
$$
\begin{cases}
\dot x_{1}(t) &= &\overbrace{\alpha x_{1}(t)}^{\text{solo prede}} - \overbrace{\beta x_{1}(t)x_{2}(t)}^{\text{predatori}} \\
\dot x_{2}(t) &= &-\delta x_{2}(t) + \gamma x_{1}(t)x_{2}(t) \\
\end{cases}
$$
- Prima equazione: di per sè le prede tendono ad aumentare, ma la presenza di predatori fa ridurre questa crescita
- Seconda equazione: di per sè i predatori tendono a diminuire, ma la presenza di prede fa invertire questo trend


Ad esempio, si possono influenza in questo modo:
	Un numero alto di predatori causa una riduzione della popolazione delle prede
	Un numero basso di prede causa una riduzione della popolazione di predatori

![[Pasted image 20220528184658.png|600]]

Con $\alpha, \delta > 0$

## MODELLO GENERALE
![[Pasted image 20220528185106.png]]
- il secondo termine (addendo) è ciò che influenza la crescita/decrescita del modello

Qualora ci fossero degli ingressi il modello diventa il seguente:
![[Pasted image 20220528185335.png]]
- nel caso di preda/predatori potrebbe essere la caccia oppure un ripopolamento "artificiale" eseguito dall'esterno (dall'uomo)

### ESEMPIO: DINAMICA DI OPINIONE
Si associa un opinione $x_{i}(t)$ a ogni utente $i$
- Se $x_{i}(t) =0$ allora la valutazione è neutra (indifferente)
- Se $x_{i}(t) >0$ allora la valutazione è positiva
- Se $x_{i}(t) <0$ allora la valutazione è negativa

Ogni utente è influenzato da una cerchia di persone (amici, conoscenti etc...), che indichiamo con $N_{i}$

Si arriva a definire l'equazione del modello:
$$
\large \dot x_{i}(t) = \sum_{j\in N_i} w_{ij}(x_{j}(t)-x_{i}(t))  \quad , \quad i=1,\dots,n
$$
- dove $w_{ij}$ è il peso del nodo $i$ sull'opinione di $j$ (maggiore se è un conoscente stretto, parente etc..)
- Si esegue in pratica la differenza tra la mia opinione e quella di un mio amico 
	- Se questo valore è positivo, allora il mio amico ha una opinione migliore della mia
		- Tende a influenzare positivamente la mia opinione (derivata positiva)
	- - Se questo valore è negativo, allora il mio amico ha una opinione peggiore della mia
		- - Tende a influenzare negativamente la mia opinione (derivata negativa)
	- Reitero poi questo per ogni mio amico (sommatoria $\Sigma$)

