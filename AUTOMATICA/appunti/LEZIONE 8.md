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
