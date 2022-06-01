### PRINCIPIO SOVRAPPOSIZIONE DEGLI EFFETTI (per sistemi lineari)
Supponendo di avere come condizione iniziale la combinazione di due condizioni iniziali, ovvero:
$$
x(0) = \alpha_{1}x_{1} + \alpha_{2}x_{2}
$$
#### EVOLUZIONE LIBERA: CONSIDERIAMO LE CONDIZIONI INIZIALI
Si trova facilmente l'evoluzione libera in questo modo:
$$
\begin{align*}
x_{\ell}(t) &= A^{t}x(0)\\
&= A^{t}(\alpha_{1}x_{1}+\alpha_{2}x_{2})\\
&= \alpha_{1}A^{t}x_{1}+\alpha_{2}A^{t}x_{2}\\
\end{align*}
$$
Quindi abbiamo una **combinazione lineare delle due**

Per quanto riguarda la *risposta*, abbiamo:
$$
y_{\ell}(t) = \alpha_{1}C\ A^{t}x_{1}+\alpha_{2}C \ A^{t}x_{2}
$$
- cioè ancora una combinazione lineare (rispetto a $C$)

Siamo in grado quindi di prevedere la combinazione lineare in risposta di due condizioni iniziali, semplicemente conoscendo l'evoluzione delle due condizioni prese singolarmente
- Basta appunto combinare linearmente le due
- sovrapposizione $\longleftrightarrow$  combinazione lineare

Riassumendo:
![[Pasted image 20220601184813.png]]
- nota: vale sia per il tempo continuo che per il caso discreto

#### EVOLUZIONE FORZATA: CONSIDERIAMO GLI INGRESSI
A partire dal generico:
$$
u(t) = \alpha_{1}u_{1}(t) + \alpha_{2}u_{2}(t)
$$
Si trova l'evoluzione forzata, sostituendo:


Ovvero l'evoluzione forzata in risposta a una combinazione lineare degli ingressi è ancora una combinazione lineare delle risposte dei singoli ingressi, ovvero:
- Data una combinazione lineare d'ingressi: la risposta del sistema è data dalla combinazione lineare delle singole risposte
![[Pasted image 20220601164155.png]]

#### EVOLUZIONE COMPLESSIVA: METTIAMO TUTTO INSIEME
Combiniamo quindi *condizioni iniziali* e *ingressi*
![[Pasted image 20220601164535.png]]
Quindi: 
*l'evoluzione complessiva in risposta alle singole cause è la somma (combo lineare) delle evoluzioni in risposta alle singole cause*
- principio divide et impera: posso combinare il sistema conoscendo semplicemente come risponde il sistema com singoli ingressi per singoli stati, ovvero $x_{i} \longrightarrow u_{i}(t)$
	- vale lo stesso anche per l'uscita (non solo per lo stato)

- sarà utili negli esercizi ricondurci a trattare singoli termini elementari


## RISPOSTA NEI SISTEMI LTI TC
- Più complicato in generale perché dobbiamo *risolvere una equazione differenziale*
	- Dobbiamo in particolare risolvere un **problema di Cauchy** (perchè conosciamo la condizione iniziale $x(0)=0$ e il segnale d'ingresso $u(t)$) 
	- supponendo senza dimostrare che la soluzione esiste ed + è unica

$$
\begin{cases}
\dot x(t) = Ax(t) +Bu(t) \\
y(t) = Cx(t) + Du(t)
\end{cases}
$$
Ricordando che $x$ in generale è un vettore (quindi dovremo risolvere un *sistema di equazioni differenziali :(*   )


#### CASO SCALARE: $\dim(x) = 1$
$$
\dot x(t) = a \ x(t)  \quad , \quad \begin{cases} \frac{d}{dt} x(t) = a \ x(t) \\ x(0) = x_{0} \end{cases}
$$
- al posto della matrice $A$ abbiamo uno scalare $a$

Dobbiamo trovare $x(t)$ che derivata è uguale a sé stessa moltiplicata per uno scalare $a$, ovvero l'**esponenziale**:
$$
x(t) = e^{at}x_{0}
$$
Infatti
$$
x(0) = e^{0}x_{0} = x_{0}
$$
Da cui:
$$
\frac{d}{dt}x(t) = a \ e^{at}x_{0} = a \ x(t)
$$

#### CASO GENERALE $\dim(x) = n$ (caos autonomo)
Problema di Cauchy:
$$
\dot x(t) = A x(t)  \quad , \quad
\begin{cases}
\frac{d}{dt} x(t) = A x(t)  \\
x(0) = x_{0}
\end{cases}
$$
La soluzione è: 
$$
\Large \boxed {e^{At}x_{0}}
$$
Stessa soluzione, solo che qui abbiamo un **esponenziale di matrice**, che è una funzione del tempo matriciale: per ogni istante di tempo associa una matrice, ovvero $e^{At}: \ \mathbb{R} \to \mathbb{R}^{n\times n}$

### RISPOSTA NEL CASO AUTONOMO
Abbiamo un integrale definito nel tempo d'interesse invece di una sommatoria
![[Pasted image 20220601181825.png|500]]
Dove:
- L'evoluzione libera dipende dall'esponenziale di matrice
- L'evoluzione forza dipende dall'integrale (detto di *convoluzione*)

#### DIMOSTRAZIONE
![[Pasted image 20220601182502.png|500]]
![[Pasted image 20220601183017.png|500]]


## ESPONENZIALE DI MATRICE
- Si definisce attraverso la *serie di Taylor*, infatti (vediamo i due casi a confronto):
![[Pasted image 20220601174300.png]]

- che è la soluzione del problema di Cauchy lineare tempo invariante nel caso autonomo
	- Infatti abbiamo ancora l'esponenziale di matrice pre moltiplicata per la matrice $A$ stessa

### PROPRIETA' (molte simili all'esponenziale "classico")
#### DERIVATA: SE' STESSA PER UNA COSTANTE
Andiamo a derivare l'esponenziale di matrice
($A$ è gestita come costante, la variabile di riferimento per la derivazione è $t$)
![[Pasted image 20220601174711.png|600]]
- l'esponenziale di matrice quindi *soddisfa l'equazione differenziale in questione*
	- Soddisfa anche la condizione iniziale

#### ELEVAZIONE ALLA ZERO
Vale:
$$
e^{A0} = I = \text{matrice identita'}
$$
### COME SI CALCOLA
- Per definizione, se la matrice è diagonalizzabile
- Trasformata di Laplace, se la matrice non è diagonalizzabile

### PERCHE' SI CALCOLA
Per capire l'evoluzione del tempo dell'evoluzione libera e di quella forzata