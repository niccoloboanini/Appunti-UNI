## ESERCIZI CALCOLO ANTITRASFORMATA
### 0) LINEE GUIDA + Applicazione teorema dei residui
Passi per l'antitrasformata:
- Rendo il denominatore monico (coefficiente grado più alto uguale a $1$)
- Fattorizzo il denominatore ed eventualmente anche il numeratore
- Controllo eventuali semplicifazioni
- Individuo esplicitamente i poli (radici di $a(s)$)
- Posiziono i poli sul piano complesso, così da capire e classificare i modi di evoluzione associati
- Fratti semplici (tanti quanti sono i poli)
- Esplicito la combinazione lineare tra i $K_{i}$ e i modi di evoluzione associati ai poli $p_{i}$
- In certi casi semplici (vedi esercizio 3), si può concludere subito il calcolo dell'antitrasformata da tabellina, scomponendo $F(s)$ (capita quando ho poli puramente immaginari), altrimenti:
- Calcolo i residui applicando il teorema: $K_{i} = \lim_{s \to p_{i}} (s-p_{i})F(s)$
	- compare una semplificazione: se non compare, fattorizzo il polinomio per farla comparire
	- scrivo parte reale e parte immaginaria $\alpha_{i}$ e $\beta_{i}$, stando attento nel caso della parte immaginaria a non scrivere anche $j$, ovvero scrivo solo: $\beta_{i} = numero$ e *non* $b_{i} = j \ numero$ 
- eventualmente faccio il grafico
	- Nota: avrò una somma di termini da plottare, se uno di questi diverge allora anche il grafico diverge
![[Pasted image 20220605171548.png|600]]


### 1)
- Qui ci sono semplificazioni al denominatore quando lo fattorizzo
	- Un solo modo di evoluzione dovuto proprio alla semplificazione (apparentemente sembra ce ne siano $2$)
![[Pasted image 20220605172011.png|600]]

### 2)
- Non ci sono semplificazioni
- Coppia di poli complessi coniugati
	- Convergente oscillante in questo caso perché parte reale minore di zero e parte immaginaria diversa da zero
![[Pasted image 20220605172455.png|600]]
- Calcoliamo l'antitrasformata utilizzando la formula vista per i poli complessi coniugati
- Nota: scrivo $\beta_1$ (parte immaginaria) senza il $j$, perché deve rimanere un segnale reale alla fine
![[Pasted image 20220605173308.png|600]]
- Avevamo previsto due modi di evoluzione ma alla fine ne è presente uno solo. Questo può succedere quando abbiamo poli complessi coniugati (l'importante è che almeno uno ci sia)

### 3)
- Polo reale + poli complessi coniugati
	- polo reale? Modo esponenziale
	- coppia poli complessi coniugati (immaginari)? Formula
![[Pasted image 20220605174000.png|600]]
- calcolo i residui (teorema - formula)
	- fattorizzo il denominatore nel calcolo del secondo residuo per eseguire la semplificazione
![[Pasted image 20220605174305.png|600]]

### 3)
- poli puramente immaginari $\Rightarrow$ modi evoluzione "puramente" oscillatori
- non applico il teorema dei residui, perché scomponendo $F(s)$ si trova da tabellina le antitrasformate relative
 ![[Pasted image 20220605174822.png|600]]
 - entrambi i modi presenti (seno e coseno)
 - sennò coi residui tornava uguale

## POLI CON MOLTEPLICITA' MAGGIORE DI UNO
Partendo da:
$$
F(s) = \frac{b(s)}{a(s)}
$$
Se un polo $p_{i}$ ha molteplicità $m_{i}$, possiamo riscrivere, fattorizzando quando necessario:
$$
F(s) = \frac{b(s)}{\prod_{i=1}^{k} (s-p_{i})^{m_{i}}}
$$
Ricordando anche che la somma delle molteplicità deve essere uguale al grado "totale" $n$: $\sum_{i=1}^{k} m_{i} = n$

#### ESEMPIO
- Polo $p_{1}$ con molteplicità $2$ $\Rightarrow$ $2$ radici coincidenti (in questo caso) in $0$
- abbiamo due termini associato al polo in $0$
	- Questo perché abbiamo molteplicità $2$, ovvero **abbiamo tanti modi di evoluzione quanto è la molteplicità**
		- in generale aumentando la molteplicità si va incontro a una divergenza del grafico relativo al modo di evoluzione
![[Pasted image 20220605175816.png|600]]

## TEOREMA DEI RESIDUI - CASO GENERALE
- **Associati a ogni polo abbiamo tanti termini e residui quanto è molteplicità del polo stesso**
	- Esempio: molteplicità 5 allora ho 5 termini con associati altrettanti residui
![[Pasted image 20220605180108.png|600]]
- non faremo esercizi di calcolo di residui con molteplicità maggiore di 1
- però è necessario sapere i modi di evoluzione e l'antitrasformata dei singoli termini (da tabellina)
![[Pasted image 20220605180339.png|600]]

Ciascun termine $\displaystyle \frac{k_{i\ell}}{(s-p_{i})^{\ell}}$ ha associato un modo di evoluzione $t^{\ell-1}e^{p_{i}t}1(t)$ 
- conoscendo un polo con la sua molteplicità, posso scrivere i relativi modi, che sono tanti esponenziali quanto è la molteplicità e ciascuno di essi è pre-moltiplicato per $1,t,t^{2},\dots,t^m_{i}-1$ 
	- se il polo è complesso prenderemo ciascun modo "a coppie", come visto finora

