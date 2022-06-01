### ESERCIZI: PASSAGGIO ALLE EQ. DI STATO (SLIDE 94)
#### 3) 
 ![[Pasted image 20220531122458.png|500]]

#### 4)
- Riscrivo innanzitutto in forma normale
- singolo ingresso $\to \text{B}$ matrice colonna 
![[Pasted image 20220531122819.png|500]]

#### TEMPO CONTINUO (autonomo oppure ingresso non derivato)
#### 7)
- $y(t)$ come prima variabile di stato
![[Pasted image 20220531123111.png|500]]

#### 8)
- caso TV
- ingresso compare ma non derivato $m=0$
![[Pasted image 20220531124004.png|500]]


# SIMULAZIONE DEI SISTEMI DINAMICI
Conoscendo:
- il modello matematico
- la condizione iniziale $x(t_{0}) = x_{0}$
- come l'ambiente esterno influisce sul sistema (ingresso nell'intervallo d'interesse, ovvero: $u(t)$ in $[t_{0},t_{f}]$)

Ci si chiede come calcolare (numericamente) l'**andamento dello stato $x(t)$ e dell'uscita $y(t)$** nell'intervallo di tempo d'interesse
- Esempio: meteo ---> conosco com'è il tempo oggi e il modello matematico (eq. diff). Studio come si evolverà lo stato del sistema (temperatura, umidità, etc...)

In caso TD:
![[Pasted image 20220531124620.png|300]]

Caso TC:
- equazioni differenziali: più complesso (problema di Cauchy) :/
- Si cerca una *soluzione approssimata*
	- Affetto da errore di quantizzazione
- Si utilizzano metodi numerici, come il **metodo di Eulero**
	- si esegue in generale una discretizzazione (il tempo continuo diventa discreto t.c. Sia una approssimazione valida --> è un campionamento)
		- Da qui si scrivono le equazioni alle differenze

## METODO di EULERO
**Permette di approssimare la soluzione di una equazione differenziale (sistema TC) con un corrispondente sistema TD**. 
- Attraverso una discretizzazione (campionamento) dell'intervallo temporale e poi approssimando la derivata (limite che tende a $0$ del rapporto incrementale) con un incremento di tempo finito pari al passo di discretizzazione $\Delta$.
$$
\dot x(t) = \frac{dx(t)}{dt} \approx \boxed{\frac{x(t_{k}+\Delta)-x(t_{k})}{\Delta} = f(t_{k},x(t_{k}),u(t_{k}))}  \quad , \quad t_{k} = t_{0}+k \Delta
$$
- $t_{k}$ è il $k-esimo$ istante di tempo (discreto)
- Scegliendo $\Delta$ sempre più piccolo, si ottiene una approssimazione più precisa
![[Pasted image 20220601150437.png|300]]
- $k$ indica proprio l'istante di campionamento ($0,1,2$ sono proprio i valori di $k$)

![[Pasted image 20220601150617.png]]

Quindi: *sostituendo la derivata con il rapporto incrementale, si passa da una equazione differenziale (TC) a una equazione alle differenze (TD)*

Dalla formula precedentemente scritta, si giunge alla equazione generale per calcolare il campione successivo:
$$
\boxed{x(t_{k}+1) = x(t_{k}) + \Delta f (t_{k}, x(t_{k}), u(t_{k}))}  \quad , \quad y(t_{k}) = h(t_{k},  x(t_{k}), u(t_{k}))
$$
- Dato $f$ (che descrive il sistema tempo continuo), si associa un sistema TD "gestito" da $k$


## Problemi della Simulazione
La simulazione, presume che noi conosciamo con precisione le condizioni iniziali del sistema. Questo nella realtà *non è quasi mai garantito*
- Esempio: previsioni del tempo per le prossime $2$ settimane - *errore*: abbiamo un sistema approssimato in partenza (evoluzione caotica)
- Inoltre la simulazione in stile "Montecarlo" è dispendiosa: per capire l'evoluzione di un sistema dovremmo fare centinaia o migliaia di simulazioni (e poi magari in realtà si evolve in un altro modo)

Per capire il comportamento del sistema se la simulazione non è sufficiente si utilizza **l'analisi**
- cioè capire il comportamento a livello teorico

---

# **2) ANALISI DEI SISTEMI DINAMICI**

# RISPOSTA LIBERA E FORZATA NEI SISTEMI LTI
- Studiare il comportamento del sistema dal punto di vista teorico, senza simulare cioè.


## RISPOSTA NEI SISTEMI LTI TD
Sappiamo già che per descrivere un sistema $LTI$ abbiamo bisogno delle $4$ matrici $A,B,C,D$, ovvero:
$$
\begin{rcases} x(t+1)=Ax(t)+Bu(t) \\ y(t) \quad \ \ \ =Cx(t)+Du(t)  \end{rcases} = LTI \longleftrightarrow (A,B,C,D)
$$
- basta conoscere le $4$ matrici per descrivere un sistema LTI TD
	- Da cui poi studiare le proprietà e **capire la risposta**

Il nostro obiettivo è cioè **calcolare l'evoluzione nel tempo di $x(t)$ e $y(t)$ a partire dalla condizione iniziale $x(0)=x_{0}$ e dalla sequenza di ingresso $u(i)$**
- se il sistema è TI (come vediamo noi prevalentemente), è sufficiente conoscere la condizione iniziale (non importa l'istante di partenza, per questo si sceglie sempre tempo iniziale $0$)

In generale, in maniera ricorsiva partendo da $x(0) = x_{0}$ e andando avanti ($x(1),x(2) \dots$ in funzione degli istanti precedenti che ho calcolato e i relativi ingressi)
- Si arriva a trovare un pattern abbastanza evidente che mi permette di calcolare un generico $x(t)$

![[Pasted image 20220601154437.png|500]]

Scritto meglio:
![[Pasted image 20220601154827.png|500]]

- dove il primo addendo *dipende soltanto dalla condizione iniziale*: viene detta **evoluzione libera $x_{\ell}(t)$**
- dove il secondo addendo *dipende soltanto dall'ingresso*: viene detta **evoluzione forzata $x_{f}(t)$**

L'evoluzione **complessiva** quindi (essendo un sistema lineare) si ottiene dalla combinazione di evoluzione libera e forzata

L'**uscita**, essendo in generale
$$
y(t) = \text{C} x(t)  + \text{D} u(t) = \text{C} \big[ x_{\ell}(t) + x_{f}(t) \big] + \text{D} u(t) = \underbrace{\text{C} x_{\ell}(t)}_{\Large y_{\ell}(t)}+ \underbrace{\text{C}x_{f}(t)+Du(t)}_{\Large y_{f}(t)}
$$
Riassumendo
![[Pasted image 20220601155414.png|500]]


