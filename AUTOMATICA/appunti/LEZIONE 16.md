## RIASSUNTOZZO
Consideriamo il sistema: $\dot x = Ax + Bu$
- Dove andiamo a considerare solo la matrice $A$ perché è quella che mi interessa per l'analisi modale che mi dà luogo ai modi naturali del sistema
Sappiamo che esso evolve in assenza di sollecitazioni esterne come: $x_{\ell}(t) = e^{At}x(0)$
- Capire l'evoluzione quindi vuol dire calcolare l'esponenziale di matrice. Essendo un oggetto piuttosto complesso, "ci siamo accorti" che passando dal dominio di Laplace le cose si semplificano di molto. Infatti: $$ e^{At} = \mathcal{L}^{-1}\{(sI-A)^{-1}\}  $$
- Pertanto riduciamo il lavoro al calcolo di una inversa di una matrice. Sappiamo che tale inversa equivale a: $$ (sI-A)^{-1} = \frac{1}{\varphi(s)}Adj(sI-A) $$
- Abbiamo evidentemente che i poli della inversa sono gli zeri di $\varphi(s)$, da cui possiamo dedurre numerose informazioni sui segnali del tempo (l'andamento, convergenti, divergenti etc...)
- In particolare, $\varphi(s)$ si può fattorizzare in un primo tempo in questo modo: $$ \varphi(s) = (s-\lambda_{1})^{\mu_{1}}(s-\lambda_{2})^{\mu_{2}} \dots (s-\lambda_{k})^{\mu_{k}} $$
- Una volta fattorizzato ci siamo accorti che possono capitare delle semplificazioni, pertanto abbiamo definito un nuovo polinomio, il *polinomio minimo* $m(s)$, che di fatto è un sottomultiplo di $\varphi(s)$: $$m(s) = (s-\lambda_{1})^{m_{1}}(s-\lambda_{2})^{m_{2}} \dots (s-\lambda_{k})^{m_{k}} $$
	- Esso ci dice con quale molteplicità appare ogni polo nella matrice inversa $(sI-A)^{-1}$. È una espressione più generale, perché $\varphi(s)$ mi aiutava a capire la molteplicità del singolo polinomio caratteristico, e non della inversa stessa. $m(s)$ quindi si applica meglio per comprendere i modi di evoluzione del sistema. Vale inoltre la relazione: $1 \leq m_{i} \leq \mu_{i}$ (cioè la molteplicità di $m(s)$ si può abbassare da $\mu_{i}$ fino a $1$ ma non può scomparire)
	- Dalla teoria sappiamo che un polo in $\lambda_{i}$ con molteplicità $m_{i}$ dà luogo ai cosiddetti *modi naturali* del sistema, ovvero i modi di evoluzione presenti nell'esponenziale di matrice (ottenuti in combinazione antitrasformando ciascun termine della matrice inversa): $$ e^{\lambda_{i}t}, t e^{\lambda_{i}t}, t^{2}e^{\lambda_{i}t}, \dots, t^{m_{i}-1} e^{\lambda_{i}t}  \quad , \quad i = 1,2,\dots,k \quad \text{(numero autovalori)}$$
	- In caso di *autovalori complessi coniugati* conviene **prenderli combinati insieme**, ovvero: ![[Pasted image 20220606154131.png|400]]

#### esempio: sistema meccanico
Lo abbiamo già visto e abbiamo già calcolato i modi di evolvere: diagonalizzando e poi più avanti con il calcolo esplicito dell'antitrasformata
- Vediamo ora di farlo col polinomio minimo
![[Pasted image 20220606154547.png|500]]

### ESERCIZI: DETERMINA MODI NATURALE DEL SISTEMA
#### ESEMPIO 1): COMPLETO
- Trovo $\varphi(s)$
- Calcolo autovalori e guardo la loro relativa molteplicità
- Fattorizzo $\varphi(s)$
- Se le molteplicità sono unitarie, scrivo già $m(s)$. Altrimenti devo stare attento a eventuali semplificazioni
- Cerco d'intuire i modi naturali. In questo primo esempio è semplice perché abbiamo poli con $m=1$ e che sono complessi coniugati tra loro. Quindi li prendo insieme e scopro quanto valgono $\sigma$ e $\omega$ per scriverli meglio
![[Pasted image 20220606155030.png|600]]
- Calcoliamo ora anche l'inversa per completezza, anche se come visto non è necessaria per capire i modi naturali del sistema (in questo caso con molteplicità $1$)
- Antitrasformo ogni singolo elemento della matrice e controllo se torna (sì perché abbiamo ancora combinazione lineari di seno e coseno)
![[Pasted image 20220606155259.png|600]]
- Troviamo infine l'evoluzione libera applicando la formula:
![[Pasted image 20220606155325.png|600]]
	- dove la prima riga della matrice ci dice come evolve la prima componente di stato del sistema e la seconda riga ci dice come evolve la seconda componente di stato
	- quindi *l'evoluzione libera è una combinazione lineare dei modi naturali dipendente dalla condizione iniziale $x(0)$*

#### ESERCIZIO 2): MATRICE 3x3 DIAGONALE A BLOCCHI
![[Pasted image 20220606155627.png|600]]

![[Pasted image 20220606160117.png|600]]
- Non si possono scrivere da subito i modi naturali a causa della molteplicità, ma intanto posso dire che sono tutti convergenti avendo tutti parte reale minore di zero
	- Però per capire esplicitamente quali sono devo calcolare $m(s)$
- Calcolo quindi l'inversa $(sI-A)^{-1}$
	- Sfrutto che è diagonale a blocchi così evito di fare tutti i conti con l'aggiogata di una matrice $3 \times 3$
- Dopodiché per il polinomio minimo faccio l'm.c.m degli elementi dell'inversa, e osservo la molteplicità.
	- In particolare compaiono due poli entrambi con molteplicità $1$ nel polinomio minimo
![[Pasted image 20220606160618.png|600]]
- Quindi si è abbassato il grado di molteplicità nel passaggio $\varphi(s) \to m(s)$, infatti $\varphi(s) = (s+4)(s+1)^{2}$ e $m(s) = (s+4)(s+1)$
	- Da cui si trovano facilmente i modi naturali, osservando gli zeri di $m(s)$

- Abbiamo solo $2$ modi di evolvere anche se la dimensione del sistema era $3 \times 3$. Questo accade quando abbiamo un abbassamento di molteplicità
	- Se calcolassimo esplicitamente l'antitrasformata ($e^{At} = \mathcal{L}^{-1}\{(sI-A)^{-1}\}$) della matrice inversa otterremmo lo stesso risultato, mettendo in combinazione lineare gli elementi della matrice.
![[Pasted image 20220606161209.png|600]]
---

