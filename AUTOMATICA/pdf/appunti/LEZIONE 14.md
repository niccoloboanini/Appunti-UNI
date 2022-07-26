### POLO REALE MINORE DI ZERO
- Nel prodotto tra $t$ e $e^{p_{i}t}$ *predomina l'esponenziale*, quindi **indipendentemente dalla potenza $t^{\ell}$ abbiamo modo convergenti a $0$**
 ![[Pasted image 20220605182150.png|500]]

### POLO REALE UGUALE A ZERO
- Rimane solo $t^{\ell}$ nel prodotto
	- Quindi l'evoluzione dipende da quanto vale $\ell$
- Pertanto, **la molteplicità influenza l'evoluzione** se il polo reale è uguale a zero
![[Pasted image 20220605182504.png|500]]

### POLO REALE MAGGIORE DI ZERO
Nel prodotto tra $t$ e $e^{p_{i}t}$ *predomina l'esponenziale*, quindi **indipendentemente dalla potenza $t^{\ell}$ abbiamo modo convergenti a $\infty$**
![[Pasted image 20220605182608.png|500]]

#### RIASSUMENDO
Relativamente ai modi di $t^{\ell} \ e^{p_{i}t}1(t)$
![[Pasted image 20220605182735.png|600]]
- se abbiamo $m_{i} = 1$ abbiamo solo il modo $e^{p_{i}t}$
- se abbiamo $m_{i} > 1$ abbiamo due modi $t^{\ell} \ e^{p_{i}t}$, con $\ell > 0$


## POLI COMPLESSI (CONIUGATI)
- Lì prendiamo a coppie (il coniugato ha la stessa molteplicità di quello non coniugato)
Stessi modi di evoluzione di quelli già visti, soltanto che ogni termine è moltiplicato per $1,t,t^{2},\dots,t^{m_{i}-1}$, ovvero:
![[Pasted image 20220605183215.png|600]]
- stessi modi ma moltiplicati per potenze successive di $t$

### CON PARTE REALE MINORE DI ZERO
- Domina l'esponenziale
Costruiamo il grafico con l'inviluppo:
![[Pasted image 20220605183451.png|150]]
Poi moltiplico per il seno
![[Pasted image 20220605183525.png|150]]

Abbiamo tutti **modi convergenti a zero**, indipendentemente dalla molteplicità
![[Pasted image 20220605183611.png|500]]

### CON PARTE REALE MAGGIORE DI ZERO
- Domina l'esponenziale, che quindi fa divergere il tutto (caso duale del precedente)
![[Pasted image 20220605183723.png|500]]
- segnali **tutti divergenti, indipendentemente dalla molteplicità**
	- perché posizionati sulla destra nel piano complesso

### CON PARTE REALE UGUALE A ZERO
- Non c'è l'esponenziale, quindi dipende solo da $\ell$
>> La molteplicità influenza sulla divergenza

Se $\ell  = 0$ allora abbiamo un andamento limitato, altrimenti se $l>0$ abbiamo divergenza (lineare)

![[Pasted image 20220605184007.png|500]]

#### riassumendo
![[Pasted image 20220605184042.png|600]]
![[Pasted image 20220605184109.png|600]]

Quindi in generale:
- [ ] se il polo è posizionato a sinistra, abbiamo convergenza
- [ ] se il polo è posizionato a destra, abbiamo divergenza
- [ ] se il polo è centrato in zero, devo stare attento alla molteplicità
	- [ ] Se essa è maggiore di zero, abbiamo divergenza
	- [ ] Se essa è zero, abbiamo un andamento limitato
![[Pasted image 20220605184343.png|500]]


## TEOREMA: RELAZIONE POLI ED EVOLUZIONE NEL TEMPO
- Formalizziamo le condizioni sopra riportate nella tabella presentando questo teorema
![[Pasted image 20220605184841.png|700]]


## TEOREMA DEL VALORE FINALE
Utile per calcolare il limite di un segnale nel tempo quando abbiamo la sua trasformata $F(s)$, senza calcolare esplicitamente l'antitrasformata
*- Nota: valido solo quando questo limite esiste, ovvero quando non ci sono oscillazioni persistenti (caso $\boxed{b}$ del teorema precedente)* --> poli complessi con parte immaginaria diversa da zero

I casi validi quindi sono i seguenti:
![[Pasted image 20220606095402.png]]
- dove in $0$ si prendono solo i poli con $m = 1$ per escludere i casi sopra descritti

Il teorema garantisce che vale:
$$
\lim_{t \to \infty} f(t) = K  \quad \text{con} \quad K = \lim_{s \to 0} s F(s)
$$
Ovvero, uguagliando i termini:
$$
\Large \boxed{\lim_{t \to \infty} f(t) = \lim_{s \to 0} s F(s)} 
$$
 #### DIMOSTRAZIONE (TEOREMA RESIDUI)
  - Dalla scomposizione in fratti semplici di $F(s)$ generica, portiamo fuori dalle sommatorie il residuo relativo al polo in $0$ (e quindi facciamo partire le $\Sigma$ dall'indice successivo)
  - Notiamo facendo l'antitrasformata, che:
	  - Il polo in $0$ è un gradino (perché a meno del residuo rimane da antitrasformare $1/s$)
	  - Gli altri poli (nelle sommatorie) sono convergenti a $0$ perché per ipotesi sono relativi a poli con parte reale minore di $0$.
	- Di tutto quindi rimane soltanto il residuo del polo in $0$, pertanto il comportamento asintotico è dato da: $\lim_{t \to \infty} f(t) = K_{1}$
 ![[Pasted image 20220606100613.png|600]]
- se non c'è il polo in $0$ il teorema vale lo stesso e $\lim_{t \to \infty} f(t) = 0$, ovvero il segnale è convergente se ci sono tutti i poli con parte reale minore di $0$.

## ESERCIZI: COMPORTAMENTO ASINTOTICO
### 0)
- Guardo le radici di $a(s)$, notando che c'è un polo in $0$ con molteplicità $1$ e un polo in $-2$ con molteplicità $1$
- Possiamo applicare il teorema del valore finale
	- In maniera alternativa si può calcolare l'antitrasformata facendo la scomposizione in fratti semplici 
		- Però se avessi avuto un polo con molteplicità elevata sarebbe venuta una scomposizione esageratamente pesante
		![[Pasted image 20220606101159.png|350]]

![[Pasted image 20220606101242.png|600]]

### 1)
- Poli puramente immaginanari: non si può applicare il teorema del valore finale
- Siamo nel punto $\boxed{b}$ del teorema, che mi garantisce che $f(t)$ è limitata: tutti i poli con parte reale $\leq 0$ e quelli con parte reale $=0$ hanno $m=1$
	- Infatti i modi di evoluzione sono: gradino (polo in $0$), seno e coseno (poli complessi coniugati)
![[Pasted image 20220606101721.png|600]]

### 2)
- Guardo i poli di $a(s)$, notando che hanno $m=2$ e sono complessi coniugati
- Il limite asintotico è $0$ perché abbiamo tutti poli con parte reale $\leq 0$, quindi modi di evoluzione convergenti (caso $\boxed{a}$ del teorema)
	- calcoliamo anche esplicitamente i modi, guardando quando vale $\sigma_{1}$ e $\omega_{1}$ per i poli complessi, e ricordandosi di aggiungere i modi moltiplicati per $t$ dato che abbiamo $m = 2$
![[Pasted image 20220606102115.png|600]]
- abbiamo $4$ modi come ci aspettavamo (dato che $\Sigma \text{ molteplicita'}=4$)

#### ULTIMI 4 ESERCIZI: LEZIONE 14
### 3)
- Si osserva che ci sono semplificazioni (stesso polo al numeratore e al denominatore)
	- Un polo "va via"
	- Ci rimangono solo poli complessi coniugati
- Si può applicare anche il teorema del valore finale
![[Pasted image 20220606104405.png|500]]
- modi esplicitamente calcolati nell'esercizio 2)

### 4)
- coppia di poli complessi coniugati
- non si può applicare il TVF (parte reale maggiore di zero)
	- parte reale maggiore di zero: divergenti
	- parte immaginaria presente: oscillanti
- quindi modi divergenti e oscillanti
	- caso $\boxed{c}$
![[Pasted image 20220606104723.png|500]]
- il limite non esiste perché abbiamo oscillazioni 
![[Pasted image 20220606104802.png]]

### 5) 
- non si può applicare il TVF perché la parte reale è uguale a zero
	- inoltre abbiamo molteplicità $2$, quindi diverge a $\infty$
		- $4$ modi di evoluzione in generale (abbiamo un termine alla seconda al quadrato al denominatore)
- caso $\boxed{c}$ del teorema (divergenza)
![[Pasted image 20220606105402.png|600]]

### 6)
- Semplificazioni! (fattorizzando il denominatore)
	- Polo in $0$ con $m = 1$
	- Polo in $-2$ con $m=1$
- Posso applicare il TVF

Due modi di evoluzione:
- gradino, associato al polo in $0$
- esponenziale decrescente, associato al polo in $-2$
![[Pasted image 20220606105621.png|600]]

## TEOREMA DEI RESIDUI ESTESO: GRADO N = GRADO D
Sia $F(s)$ una funzione semplicemente propria, dotata quindi dello stesso grado al numeratore e al denominatore
	- Nota: finora abbiamo visto il caso di funzione strettamente propria
Allora si può espandere in fratti semplici come:
$$
F(s) = K_{0}+ \sum_{i=1}^{k} \sum_{\ell = 1}^{m_{i}} \frac{K_{i\ell}}{(s-p_{i})^{\ell}}
$$
- ovvero si aggiunge un termine aggiuntivo $K_0$ dovuto al termine di grado massimo al denominatore
- Si dimostra che $\boxed{K_{0}= b_{n} }$ , quindi non va nemmeno calcolata faticosamente
	- Per dimostrarlo basta fare $\lim_{s \to \infty} F(s)$

### ANTITRASFORMATA
Per linearità basta antitrasformare ciascun termine
- La parte delle sommatorie è analoga
- La parte del termine costante $K_{0}$ porta con l'antitrasformata alla $\delta(t)$ di ampiezza $K_{0}$, ovvero $\boxed{K_{0} \ \delta(t)}$

#### ESEMPIO
![[Pasted image 20220606103521.png|600]]

