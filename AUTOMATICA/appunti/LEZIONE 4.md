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



