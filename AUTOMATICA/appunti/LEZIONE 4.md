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
			- Se avessimo un ingresso che governa la transizione, si parlerebbe di *processo decisionale di Markov*

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

