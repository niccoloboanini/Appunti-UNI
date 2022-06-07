## RISPOSTA IMPULSIVA
L'antitrasformata della funzione di trasferimento. Ovvero quest'ultima osservata nel dominio del tempo:
$$
\large \boxed{g(t) = \mathcal{L}^{-1}\{G(s)\}}
$$
Sfruttando la linearità dell'antitrasformata si arriva a dire che:
$$
{\large g(t)} = \mathcal{L}^{-1}\{C(SI-A)^{-1}B +D]\} = \large Ce^{At}B+D\delta(t)
$$

Chiamata risposta impulsiva perché equivale alla risposta forzata del sistema se prendiamo come ingresso un segnale impulsivo di Dirac, infatti:
$$
u(t) = \delta(t) \Rightarrow U(s) = \mathcal{L}^{-1}\{u(t)\} = 1 \implies Y_{f}(s) = G(s)U(s) = G(s) \longleftrightarrow  \large y_{f}(t) = g(t)
$$
![[Pasted image 20220607105414.png|300]]

Essendo una "rielaborazione" di $G(s)$, anche la risposta impulsiva *non comprende quei poli nascosti all'interno del sistema* 
- In altre parole, solo i poli (autovalori) visibili a $G(s)$ danno un contributo alla risposta impulsiva
	- Quindi i **modi di evolvere** descritti dalla risposta impulsiva sono relativi solo a un **sottoinsieme di quelli totali del sistema**
		- I modi che non si osservano sono detti *modi nascosti* del sistema

#### ESEMPIO DEL CARRELLO
- caso a) non ci sono poli nascosti quindi non ci sono modi nascosti
- caso b) ci sono poli nascosti quindi ci sono anche modi nascosti (si vede solo il modo esponenziale)
![[Pasted image 20220607114436.png|600]]

## CALCOLO DELLA RISPOSTA FORZATA
Sappiamo che:
$$
Y_{f}(s) = G(s) \ U(s)
$$
Se in ingresso abbiamo $u(t)$ con trasformata $U(s)$ razionale, allora
- poli di $Y_{f}(s) = \text{poli funzione trasferimento + poli ingresso}$
- modi di $y_{f}(t) = \text{modi risposta impulsiva } g(t) + \text{modi ingresso } u(t)$

**Tuttavia**, nel prodotto $G(s) \ U(s)$ **potrebbero esserci semplificazioni**, che portano una riduzione dei poli; oppure **potrebbe esserci un aumento di molteplicità** che fanno comparire nuovi modi di evoluzione (quando il polo dell'ingresso coincide con il polo della funzione di trasferimento)
- Il caso tipico (no semplificazioni o aumento di molteplicità) lo abbiamo solo quando i poli sono *disgiunti*

#### ESEMPIO 1: CASO TIPICO
- Compaiono tutti i modi associati all'ingresso e alla funzione di trasferimento (abbiamo la somma dei due in uscita)
![[Pasted image 20220607115558.png|600]]

#### ESEMPIO 2: SEMPLIFICAZIONI
- Calcolo della risposta forzata (tipica domanda da esame)
- Calcolo $G(s)$ se non ce l'ho già
- Trasformo l'ingresso $u(t) \to U(S)$
- Individuo i poli di $U(s)$ e $G(s)$ (magari anche sul piano complesso)
	- La risposta impulsiva (facoltativo) basta trovare $g(t)$ come antitrasformata di $G(s)$
- Applico la formula per $Y_{f}(s)$
	- Osservo se ci sono semplificazioni (in questo caso compaiono)
- Faccio $\mathcal{L}^{-1}\{Y_{f}(s)\}$ per trovare la risposta forzata $y_{f}(s)$
	- Osservo se ci sono state semplificazioni (in questo caso sì, scompare il modo associato alla funzione di trasferimento $G(s)$ perché si semplifica con uno zero di $U(s)$)
![[Pasted image 20220607120618.png|600]]

#### ESEMPIO 3: AUMENTO MOLTEPLICITà --> RISONANZA
- Calcolo $Y_{f}(s)$, facendo le relative antitrasformate quando necessario
	*- Osservo che l'ingresso e la funzione di trasferimento hanno entrambi un polo in $0$*
		- Questo implica un aumento della molteplicità
- Calcolo $y_{f}(s)$, osservando che compare un *nuovo* modo di evoluzione (RAMPA) dovuto a un aumento della molteplicità: infatti avevamo due modi di evoluzione gradino (uno relativo alla $g(t)$ e uno relativo a $u(t)$)
*- Abbiamo sollecitato il sistema con lo stesso modo di evoluzione* del sistema stesso. Questo fenomeno viene detto **risonanza**
![[Pasted image 20220607121147.png|600]]
- ingresso limitato --> uscita divergente (instabilità esterna come vedremo)


# STABILITA' ESTERNA
*- Effetto delle perturbazioni dell'ingresso sull'uscita*
	- Lasciamo invariate le condizioni iniziali
	- Perturbiamo "semplicemente" l'ingresso
	- Poi osserviamo come si è influenzata l'uscita

## MAPPA TRANSIZIONE GLOBALE USCITA
$$
y(t) = \Psi(t,x_{0}, u) = Ce^{At} x_{0}+ \int_{0}^{t} Ce^{A(t-\tau)}Bu(\tau) \,d\tau = C x(t) + D u(t)
$$
Con $\Psi(t,x_{0},u)$ **mappa transizione dell'uscita**
- essa è una funzione che dice a partire da una condizione iniziale $x_{0}$ e supponendo di applicare un certo ingresso $u$ il valore dell'uscita a un certo tempo $t$.
- la mappa di transizione di stato invece mi dava informazioni sullo stato (invece dell'uscita)

## EFFETTO PERTURBAZIONE
Confronto tra:
$$
y(t) = \Psi(t,x_{0},u) \longleftrightarrow y(t) = \Psi(t,x_{0},u+\tilde u)
$$
- Dove abbiamo perturbato l'ingresso di un valore $\tilde u$
- Vediamo come reagisce il sistema con questi due ingressi distinti e poi osserviamo la *differenza*, così da capire l'effetto della perturbazione dell'ingresso
![[Pasted image 20220607124511.png|550]]
- dove l'evoluzione libere si sono semplificate, rimane solo la risposta forzata
- La risposta all'ingresso nominale della risposta forzata si cancella. **Rimane solo la risposta forzata alla perturbazione $\tilde u$**
	- Nel dominio di Laplace essa si calcola come $\large \boxed{G(s) \ \tilde U(s)}$
	- Non dipende né dal tipo di ingresso $u$ né dalle condizioni iniziali $x_{0}$
		- Ovvero se cambiamo $u$ e $x_{0}$ ma il sistema e la perturbazioni sono le stesse, allora l'uscita è la stessa --> tutte le traiettorie hanno le stesse proprietà di stabilità rispetto alle perturbazioni dell'ingresso
		**- Quindi la stabilità esterna è una proprietà intrinseca del sistema**, questo perché appunto la scelta di $x_{0}$ e $u$ è irrilevante per calcolare l'effetto della perturbazione
	- Cercheremo di capire se questo effetto si mantiene limitato così da garantire stabilità

Riassumendo:
![[Pasted image 20220607125234.png|600]]

## STABILITA' ESTERNA
Un sistema è **esternamente stabile** se una perturbazione limitata $\tilde u$ porta una variazione limitata dell'uscita $y$
![[Pasted image 20220607125636.png]]
**Un sistema di questo tipo è $BIBO$ (bounded input bounded output)**
- la risposta forzata a un ingresso limitato è sempre limitata

### CONDIZIONI PER LA STABILITA' ESTERNA
Abbiamo in considerazione: $\tilde Y(s) = G(s) \tilde U(s)$
Quindi possiamo riscrivere al solito:
$$
G(s) = \frac{b(s)}{a(s)}
$$
Un sistema è esternamente stabile **se tutti i poli di $G(s)$ hanno parte reale $<0$**
- Ovvero si trovano nella regione di stabilità nel piano $s$, corrispondente al semipiano sinistro
![[Pasted image 20220607130206.png|200]]
- Non si ammettono come nella stabilità interna i poli in $0$ (condizione più restrittiva per la stabilità esterna)

Quindi l'effetto degli ingressi o si mantiene limitato oppure è illimitato (non c'è vie di mezzo)
- In caso di multipli ingressi, $G(s)$ è una matrice quindi in quel caso vado a vedere tutti i poli di ogni elemento di tale matrice


## STABILITA' - RIASSUNTOZZO
![[Pasted image 20220607130427.png|600]]

> Per la stabilità interna devo guardare $\varphi(s)$ ed eventualmente $m(s)$ (non basta $G(s)$, perché potrebbero esserci poli nascosti)

> Per la stabilità esterna mi basta vedere $G(s)$ (funzione di trasferimento), senza interessi circa la molteplicità, a differenza della stabilità interna

