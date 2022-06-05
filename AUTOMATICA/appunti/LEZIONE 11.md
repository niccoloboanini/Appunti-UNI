#### proprietà (riassunto)
![[Pasted image 20220603151820.png|500]]
- $s \longleftrightarrow \text{derivazione}$
- $\displaystyle \frac{1}{s} \longleftrightarrow \text{integrazione}$

### ESERCIZI: CALCOLO DI TRASFORMATE
#### 1) $f(t) = \cos(\omega_{o} t) \ 1(t)$
- metodo 1: vedere il coseno come la derivata del seno e applicare la P4
- metodo 2: sfruttare le formule di Eulero
![[Pasted image 20220603152254.png|500]]
- nota: era già presente nella tabella delle trasformate

#### 2) $f(t) = 2(1-e^{-3t}) \ 1(t)$ 
- Si sfrutta la prop. distributiva e la linearità
![[Pasted image 20220603152511.png|500]]
- Nota: abbiamo ancora una funzione razionale nel dominio $s$ perché abbiamo fatto una combinazione lineare di funzioni elementari
	- Questo sarà comodo poi per l'antitrasformata

#### 3) $f(t) = [2 \sin(3t) + 4 \cos(3t)] \ 1(t)$
- linearità per isolare seno e coseno e applicare le formule in tabella delle trasformate fondamentali
![[Pasted image 20220603152828.png|500]]

#### 4) $e^{-2t} \sin(t) \ 1(t)$
- metodo 1: Eulero per riscrivere seno e coseno
- metodo 2: traslazione in frequenza - perché abbiamo un esponenziale a moltiplicare (vediamo questo)
![[Pasted image 20220603153309.png|500]]


# RISPOSTA LIBERA E FORZATA NEL DOMINIO DI LAPLACE

Abbiamo un sistema LTI TC del tipo:
$$
\begin{cases}
\dot x(t) = Ax(t) +Bu(t) \\
y(t) = Cx(t) + Du(t)
\end{cases}
$$
### STATO
Possiamo calcolare la trasformata dello stato $\dot x(t)$, sfruttando le proprietà $1$ (linearità, utile per il membro di destra) e $4$ (operatore $s$ derivata, utile per $\dot x(t)$):
![[Pasted image 20220603153937.png|600]]
- con la trasformata abbiamo ottenuto una *equazione algebrica*
	- $X(s)$ è il vettore delle trasformate

Da cui:
$$
s X(s) - A X(s) = x(0)+BU(s)
$$
Riscrivendo $X(s)$ (sfruttando le proprietà della matrice identica):
$$
s \ I \ X(s) - AX(S) = x(0) + BU(s)
$$
Raccogliendo:
$$
(sI-A) X(s) = x(0)+BU(s)
$$
Ecco che abbiamo la soluzione:
$$
\large \boxed{X(s) = (sI-A)^{-1}\big[x(0)+BU(s)\big]}
$$
Distribuendo il prodotto, si evince al meglio il parallelo con l'evoluzione libera nel dominio del tempo:
$$
X(s) = \underbrace{(sI-A)^{-1}\ x(0)}_{\Large X_{\ell}(s)} + \underbrace{(sI-A)^{-1} BU(s)}_{\Large  X_{f}(s)} 
$$
- $X_{\ell}(s)$ viene detta **risposta libera**
- $X_{f}(s)$ viene detta **risposta forzata**

### USCITA
In maniera del tutto equivalente:
$$
y(t) = Cx(t) + Du(t) \longleftrightarrow Y(s) = C X(s) + DU(s)
$$
Riscrivendo, sfruttando il fatto che $X(s)$ lo abbiamo già calcolato precedentemente:
$$
Y(s) = \underbrace{C(sI-A)^{-1}\ x(0)}_{\Large X_{\ell}(s)} + \underbrace{C(sI-A)^{-1} BU(s) + DU(s)}_{\Large  X_{f}(s)} 
$$
Dove dal secondo addendo si ricava la **funzione di trasferimento** :
$$
\underbrace{C(sI-A)^{-1} BU(s) + DU(s)}_{\Large  X_{f}(s)} = \underbrace{\bigg[C(sI-A)^{-1} B+ D\bigg]}_{\Large G_{s} = \large \text{funzione di trasferimento}} \cdot U(s)
$$
- essa contiene tutte le informazioni *ingresso-uscita* del sistema
 ![[Pasted image 20220603160304.png|200]]

## RIASSUNTO E PARAGONE TEMPO-LAPLACE
![[Pasted image 20220603155445.png|500]]
- nel tempo abbiamo l'esponenziale di matrice $e^{At}$ oppure un integrale (di convoluzione) che in generale sono complicati da calcolare.
	- In Laplace invece abbiamo soltanto da calcolare l'**inversa di una matrice**: $(sI-A)^{-1}$ oppure un **prodotto** $(sI-A)^{-1} BU(s)$


## CALCOLO DELL'ESPONENZIALE DI MATRICE CON LAPLACE
Sappiamo che:
$$
\mathcal{L}\{e^{at}\} = \frac{1}{s-a}
$$
Generalizzando all'esponenziale di matrice:
$$
\mathcal{L}\{e^{At}\} = (sI-A)^{-1}
$$
Quindi **per calcolare l'esponenziale di matrice**:
- 1) Calcolo della matrice inversa $(sI-A)^{-1}$
- 2) **antitrasformata** di quanto trovato per tornare nel dominio del tempo $$ \large\boxed{e^{At} = \mathcal{L}^{-1}\{(sI-A)^{-1}\}}$$
### ESEMPIO: CARRELLO
Calcoliamo l'esponenziale di matrice senza sapere che la matrice è diagonalizzabile, e quindi attraverso la trasformata (nelle precedenti lezioni lo abbiamo fatto con l'altro metodo perché sapevamo che era diagonalizzabile)

> [!tip] Inversa matrice $2 \times 2$
> (inverso del determinante per matrice aggiogata)
> ![[Pasted image 20220603161645.png|450]]
> [vedi poi caso generale]

![[Pasted image 20220603161947.png|600]]

Da cui:
![[Pasted image 20220603162235.png|600]]

Ci rimane un solo termine da antitrasformare, che è $1/s(s+1)$. Per farlo sfruttiamo la scomposizione in fratti semplici (somma di due frazioni):
![[Pasted image 20220603162512.png|600]]
![[Pasted image 20220603162650.png|600]]

E quindi **finalmente** abbiamo:

$$
(sI-A)^{-1} = \frac{1}{s(s+1)}\begin{bmatrix} 1(t)  & 1(t)-e^{-t} 1(t)  \\  0  &  e^{-t}1(t) \end{bmatrix}
$$


### INVERSA MATRICE
$$
\Large \boxed{(sI-A)^{-1} = \frac{1}{\varphi(s)} \ Adj(sI-A)}
$$
- gli elementi della matrice inversa sono **funzioni razionali tali che il grado del numeratore è minore del grado del denominatore**



# ANTITRASFORMATA DI LAPLACE
- Per il tempo discreto avremo invece la trasformata 

### DEFINIZIONE (APPROFONDIMENTO)
![[Pasted image 20220603163349.png|400]]

- POCO PRATICA
- Per questo andremo a scomporre la $F(s)$ (razionale) in una combinazione lineare di **funzioni elementari** e poi andremo ad antitrasformare ciascun termine elementare (con la tabellina)

### ESEMPIO
- Nota: $F(s)$ viene scomposta in $2$ fratti semplici perché ci sono altrettanti poli al denominatore
	- In particolare associato a ogni polo in questo caso abbiamo dei termini esponenziali (uno convergente e uno divergente)
![[Pasted image 20220603163832.png|700]]

Solo *dopo* (per comodità) calcoliamo $K_{1}$ e $K_{2}$:
![[Pasted image 20220603163938.png|450]]