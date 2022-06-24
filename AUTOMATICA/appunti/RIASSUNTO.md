# MODELLISTICA

## MODELLO
1) TC/TC
2) AUTONOMI/NON
3) TV/TI

Hanno:
$$
f(t,x(t),u(t)) \longleftrightarrow y=h(t,x(t),u(t))
$$
, ovvero:
- Equazione transizione stato (passare da $x(t)$ a $x(t+1)$ o da $x(t)$ a $\dot x(t)$)
- Equazione uscita sistema (da un certo $x(t)$ e con certi ingressi $u(t)$)

### ESEMPI e TIPOLOGIE
- Robot Mobile
- Sistema Scolastico (trasferimento risorse)
- Laurea Magistrale (compartimentale)
- Catena Produzione (compartimentale)
- Previsioni Meteo (transizione di stato)
- Page Rank (transizione di stato) [ricorda: Damping factor, convergenza]
- Preda Predatore (influenza) [ricorda: influenza predatori su ecosistema]
- Dinamica di Opinione (influenza)
- Sistema Meccanico (sistema fisico) [carrello con un grado di libertà]
	- Si esegue passaggio: eq. fisica $\to$ equazioni di stato (posizione, velocità) $\to$ forma matriciale e poi si analizza 
- Circuito RLC (sistema fisico) [L,C sono le variabili di stato perché elementi con memoria - derivate corrente]

## STATO SISTEMA
- Fotografia della configurazione del sistema
- Insieme di variabili (vettore) necessarie per descrivere un sistema in un certo istante
	- Indicato con $x(t) = \begin{bmatrix} x_{1}(t)  \\ x_{2}(t) \\ \vdots  \\ x_{n}(t) \end{bmatrix}$, con $n= \text{dimensione sistema}$
### VARIABILI DI STATO
$x_1,x_2,\dots,x_n$ che sono elementi con memoria (ad esempio se sono le derivate di un altro elemento)

## ALGORITMI ITERATIVI
Usare i sistemi dinamici per descrivere comportamento algoritmi
- Il tempo $t$ diventa l'iterazione
- Lo stato $x(t)$ diventa le variabili in memoria (utilizzabili)

### ESEMPI
#### Algoritmo Gradiente
- Trovare minimo locale funzione (anche più variabili)
	- Si parte da un $x(0)$ e si va verso la parte in cui abbiamo maggiore discesa scegliendo $\gamma$ passo di discesa (costante)
	- Come? Calcolando il gradiente (vettore derivate parziali che è perpendicolare - verso l'esterno) e poi ci si muove verso l'antigradiente

## RAPPRESENTAZIONE INGRESSO USCITA
- Non si conosce cosa succede all'interno del sistema
- Si osserva cosa esce ($y$) sulla base di certi ingressi $(u)$
### TD
- È rappresentabile come una funzione autoregressiva (TD)
	- ovvero che dipende da sé stessa agli istanti precedenti $$ y=\ g\ \big(t,y(t-1),\dots,y(t-n), \ \ u(t), \dots, u(t-m)\big) $$
	- Grado massimo di: uscita ($n$) e ingresso ($m$)

##### PASSAGGIO ALLE EQ. DI STATO
 Si può sempre passare elle equazioni di stato: basta tenere in memoria le informazioni necessarie per descrivere l'istante successivo
 - Esempio: Fibonacci $\to$ per descrivere $t+1$ mi basta conoscere $y(t-1)$ e $y(t-2)$, quindi $n=2$, $m=0$, quindi: $$ x(t) = \begin{bmatrix} y(t-1) \\ y(t-2) \end{bmatrix} =\begin{bmatrix} x_{1}(t) \\ x_2(t) \end{bmatrix} \Rightarrow y(t)=x_{1}(t)+x_{2}(t)$$
$$
\begin{cases}
x_{1}(t+1) &=& y(t) &=& x_{1}(t)+x_{2}(t) \\
x_{2}(t+1) &=& y(t-1) &=& x_{1}(t)
\end{cases} \quad , \quad y(t) = x_{1}(t) +x_{2}(t)
$$

##### PASSI:
- Scrivo $x(t)$ come vettore di uscite fino a $y(t-m)$ e d'ingressi fino a $u(t-n)$
- Esplicito l'equazioni di stato $x_{i}(t+1)$, con $i=1,2,\dots,n+m$
 
 ### TC
 - Rappresentabile con una equazione differenziale
$$
y^{(n)}(t)=g\big(t,y^{(n-1)}(t),\dots, \dot y(t) , y(t), \ \ , u^{(m)}(t),\dots,\dot u(t),u(t)\big)
$$
Funzione "autoregressiva delle derivate": infatti la derivata $n$-esima è in funzione di tutte le altre $n-1$ derivate dell'uscita e delle $m$ derivate dell'ingresso, con vincolo $m \leq n$

##### PASSAGGIO ALL EQ. DI STATO (caso autonomo)
###### ESEMPIO
![[Pasted image 20220618155411.png|400]]


## SISTEMI LINEARI
Un sistema è lineare se $f$ e $h$ sono lineari (funzioni relative rispettivamente a stato e uscita)
### FUNZIONI LINEARI
Possono essere riscritte come matrici $m \times n$
- Valgono: Additività e Omogeneità

### MATRICI A,B,C,D
Per sistemi SISO ($\dim(u)=1, \dim(y)=1$)
- $A,B$ $\longleftrightarrow$ equazioni di stato. In particolare
	- $A \to n \times n$ [descrive lo stato]
	- $B \to 1 \times n$ [passaggio ingresso a stato]
- $C,D$ $\longleftrightarrow$ uscita. In particolare
	- $C \to n \times 1$ [passaggio stato a uscita]
	- $D \to 1 \times 1$ [passaggio ingresso a uscita]

### RAPPRESENTAZIONE INGRESSO USCITA
#### CASO TD
Si può riscrivere l'uscita autoregressiva come combinazione lineare degli argomenti scegliendo opportuni coefficienti $\alpha_{i}$ per le uscite e $b_{i}$ per gli ingressi
$$
y(t) = a_{1}y(t-1)+ \dots + a_{n}y(t-n)+ b_{0}u(t)+\dots+ b_{m}u(t-m)
$$
#### CASO TC
Analogamente solo con le derivate
$$
y^{(n)} = a_{n-1}y^{(n-1)}+ \dots + a_{0}y(t)+ b_{m}u^{(m)}(t)+\dots+ b_{0}u(t)
$$
![[Pasted image 20220618162433.png]]


## SIMULAZIONE SISTEMI DINAMICI
Calcolare l'evoluzione dello stato $x(t)$ e dell'uscita $y(t)$ in un certo intervallo d'interesse
- A partire da $x_{0}=x(0)$ con un relativo modello matematico e gli ingressi esterni $u(t)$
	- vedi (idea): meteo - conosco il meteo di oggi mi chiedo come sarà domani (considerando gli ingressi: vento, umidità, etc..)
	- Caso TC: soluzione approssimata alla eq. differenziale (Metodo di Eulero, in cui si discretizza la funzione continua con un campionamento di passo $t_{k}$ per arrivare a una equazione seppur approssimata ma alle differenze invece che differenziale)

---

# ***ANALISI***
Studiare *teoricamente* il comportamento del sistema (perché non sempre simulare vale la pena, è possibile oppure si fa senza errori - vedi previsioni meteo per le prossime $2$ settimane)

# RISPOSTA (LTI)
## TD
Risposta $\longleftrightarrow$ come reagisce/evolve $x(t)$ e $y(t)$ a partire da $x(0)$ e $u(i)$ $\approx$ analizzare le $4$ matrici $A,B,C,D$
$$
\begin{cases}
x(t+1) &= Ax(t)+Bu(t) \\
y(t) &= Cx(t) + Du(t) 
\end{cases}
 \quad , \quad \text{su cui si applica:} \quad \underbrace{x(t+1)=Ax(t)+Bu(t)}_{\text{eq. transizione stato}} 
$$
si ottiene:
![[Pasted image 20220618165210.png|500]]

Quindi l'*evoluzione complessiva* di un sistema all'istante $t$ generico è data dalla combinazione lineare di $x_{\ell}(t)$ e $x_{f}(t)$
	- $x_{\ell}(t)$ dipende solo dalla condizione iniziale $x(0)$: come evolve il sistema senza sollecitazioni esterne - EVOLUZIONE LIBERA
	- $x_{f}(t)$ dipende solo dalle sollecitazioni esterne $u(t)$: come evolve il sistema quando è sottoposto a ingressi esterni senza tenere conto della condizione iniziale - EVOLUZIONE FORZATA

##### USCITA
![[Pasted image 20220618170809.png]]

### SOVRAPPOSIZIONE DEGLI EFFETTI
Si prende come condizione iniziale la combinazione lineare di due condizioni inziali, cioè:
$$
x(0) = \alpha_{1}x_{1}+\alpha_{2}x_{2}
$$
#### EVOLUZIONE LIBERA
![[Pasted image 20220618171154.png]], ![[Pasted image 20220618171204.png|250]]
Combinazione lineare delle due
#### EVOLUZIONE FORZATA
![[Pasted image 20220618172447.png]]

##### EVOLUZIONE COMPLESSIVA
![[Pasted image 20220618172538.png]]


## TC
Abbiamo una eq. Differenziale :(
- Dobbiamo perciò risolvere un **problema di Cauchy**

> Se $\dim(x)=1$, si scopre che la soluzione è l'**esponenziale** $e^{at}x_{0}$ (al posto di $A$ matrice abbiamo $a$ scalare)

Nel caso generale, procedendo con lo stesso ragionamento, si scopre che la soluzione è:
$$
x(t) = e^{At}x_0
$$
- Dove $e^{At}$ è detto **esponenziale di matrice** (funzione che associa una matrice $n \times n$ a ogni istante di tempo)

 ### ESPONENZIALE DI MATRICE
 Si definisce estendendo il concetto di serie di Taylor per l'esponenziale:
 ![[Pasted image 20220619182705.png|400]]
#### PROPRIETA'
- Derivata: l'esponenziale stesso per $A$, ovvero: $\displaystyle \frac{de^{At}}{dt}=A\cdot e^{At}$
- Elevazione alla zero: matrice identità: $e^{A0}=I$
#### COME SI CALCOLA
- Per definizione se $A$ è diagonalizzabile
	- In particolare se $A$ è diagonale basta fare l'esponenziale dei termini sulla diagonale
	- Diagonalizzabile: posso riscrivere $A = T \begin{bmatrix} \lambda_{1} & 0 & \dots \\ 0 & \ddots & 0 \\ \vdots & \dots & \lambda_{n} \end{bmatrix}T^{-1}$, ovvero $A=T\Lambda T^{-1}$
		- Da cui, $A^{k} = T \Lambda^{k}T^{-1}$
		- Quindi: $\displaystyle e^{At}=\sum_{k=0}^{\infty} T \Lambda^{k}T^{-1}\ \frac{t^{k}}{k!}=Te^{\Lambda t} T^{-1}$, dalla definizione con Taylor e portando poi fuori dalla sommatoria $T$
- **Trasformata di Laplace**
	- Utile sia per $x_\ell$ che per $x_{f}$ (quindi per tutta la risposta complessiva)
#### PERCHE' SI CALCOLA
- Capire evoluzione del sistema (*traiettorie*) che può assumere (*modi naturali*)

### RISPOSTA
In maniera duale rispetto al caso precedente, abbiamo un integrale al posto della sommatoria, in particolare:
![[Pasted image 20220619182337.png|500]]

- che soddisfa condizione iniziale ($e^{At}|_{t=0}=I$) e soddisfa l'equazione differenziale (formula di Leibniz)

## TRASFORMATA LAPLACE
Passaggio da dominio del tempo a dominio trasformato $s$, $s=\sigma + j\omega$: $\displaystyle F(s) = \mathcal{L}\{f(t)\} = \int_{0}^{\infty} f(t)e^{-st} \,dt$
#### PROPRIETA'
![[Pasted image 20220619185222.png|400]]
![[Pasted image 20220619185204.png|200]]
#### TRASFORMATE FONDAMENTALI
![[Pasted image 20220619185242.png|400]]

## RISPOSTA LIBERA E FORZATA IN LAPLACE
Si ha: $\begin{cases} \dot x = Ax +Bu  \\ y = Cx + Du \end{cases}$ , che abbiamo detto risolvibile trovando la soluzione della eq. differenziale. Sfruttando Laplace, si passa a una eq. algebrica.
#### STATO
$$
\dot x = Ax + Bu \longleftrightarrow sX(s)-x(0) = AX(s)+BU(s)
$$
Da cui, raccogliendo e quindi isolando $X(s)$:
$$
(sI-A)X(s) = x(0)+BU(s) \Rightarrow X(s) = (sI-A)^{-1}[x(0)+BU(s)]  
$$
Quindi:
$$
\boxed{X(s) = \underbrace{(sI-A)^{-1}x(0)}_{\stackrel{\Large X_\ell(s)}{\large \text{Risposta Libera}}} + \underbrace{(sI-A)^{-1}BU(s)}_{\stackrel{\Large X_{f}(s)}{\large \text{Risposta forzata}}}}
$$
##### USCITA
Analogamente:
![[Pasted image 20220620093753.png]]
![[Pasted image 20220620093859.png|400]]

## RIASSUNTO TEMPO - LAPLACE
![[Pasted image 20220620093944.png]]

## ESPONENZIALE MATRICE CON LAPLACE
![[Pasted image 20220620094100.png|500]]
