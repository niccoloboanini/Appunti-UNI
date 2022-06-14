### TRATTAZIONE FORMALE: IPOTESI SEMPLIFICATIVE
Supponiamo che:
- Il sistema sia completamente controllabile (così che si può assegnare liberamente tutti gli autovalori in ciclo chiuso)
	- Posso scegliere come voglio i coefficienti di $\varphi^{*}(s)$ (polinomio caratteristico a ciclo chiuso) - con il vincolo che il primo sia $s^{n} \cdot \varphi^{*}_{n}$, con $\varphi^{*}_{n}=1$ (monico)
- $r(s)$ ha tutte radici con parti reali minori di zero ($r(s) = CAdj(sI-A)B$, va al numeratore di $G^{*}_{y^{o}\ y}(s)$)
- - In questo modo, essendo stabile ci sono possibili semplificazioni tra numeratore e denominatore di $G^{*}_{y^{o}\ y}(s)$

Abbiamo:
$$
\large \varphi^{*}(s) = s^{n} + \varphi^{*}_{n-1}s^{n-1} + \dots + \varphi^{*}_{1}s + \varphi^{*}_{0}
$$

Ora:
- $r(s)$ è un generico polinomio di grado $m$, con $m<n$ tale che: $$ r(s)=r_{m}s^{m}+r_{m-1}s^{m-1}+\dots+r_{1}s+r_0 $$
- $\varphi^{*}(s)$ è un polinomio di grado $n$, che scegliamo di questo tipo: $$ \varphi^{*}(s)=\frac{\overbrace{r(s)}^{\text{grado } m}}{r_{m}}\ \overbrace{a^{*}(s)}^{\text{grado }n-m} = \dots = \left(s^{m}+\frac{r_{m-1}}{r_{m}}+\dots+\frac{r_{0}}{r_{m}}\right)a^{*}(s) $$
	- Dove $a^{*}(s)$ è un polinomio scelto da me (monico)
	- Dividendo per $r_{m}$ diventa monico anche $r(s)$ 

Tutto questo è comodo perché:
$$
G_{y^{o}\ y}^{*}(s) = \frac{r(s)}{\varphi^{*}(s)}H= \frac{\cancel{r(s)}}{\frac{\cancel{r(s)}}{r_{m}}a^{*}(s)}H=\frac{r_{m}}{a^{*}(s)}H
$$
- Abbiamo i poli esclusivamente in $a^{*}(s)$, che è come detto un polinomio scelto appositamente e infine due termini costanti $r_{m}$ e $H$

Per garantire la specifica $2$, si sceglie $\displaystyle H=\frac{a^{*}_{0}}{r_{m}}$ (così che $G_{y^{o}\ y}^{*}(0)=1$)
E allora si giunge alla forma:
$$
\large \boxed{G_{y^{o}\ y}^{*}(s)=\frac{a^{*}_{0}}{a^{*}(s)}}
$$
- Con $a^{*}(s) =s^{n-m}+a^{*}_{n-m-1}s^{n-m-1}+\dots+a^{*}_{0}$ scelto da me (monico) - utile per dare l'andamento che vogliamo alla risposta a gradino a ciclo chiuso


Pertanto la risposta forzata al gradino in ciclo chiuso che abbiamo già visto in precedenza diventa:
![[Pasted image 20220614113418.png]]


> [!hint] Importante: stabilità di $r(s)$
>**Nota bene**: il polinomio **$r(s)$** si semplifica (cancella) $\iff$ $r(s)$ è stabile (altrimenti poi diventerebbe instabile anche $\varphi^{*}(s)$)
![[Pasted image 20220614113705.png]] 

Nell'esempio di progetto precedente avevamo $n-m=1$ 
- In questi casi la funzione di trasferimento si dice del **I ordine** ed è della forma:
- $$
G^{*}_{y^{o}\ y}(s)=\frac{a^{*}_{0}}{s+a^{*}_{0}}  \quad , \quad\text{ con } a^{*}_{0}>0 \text{ numero scelto da me}
$$
- Tale funzione di trasferimento dà luogo a una risposta al gradino $y^{o}(t)$ del tipo:
![[Pasted image 20220614114456.png|400]]
	- Dove l'esponenziale $e^{-a^{*}_{0}t}$ dipende dalla posizione del polo che abbiamo assegnato dove vogliamo per garantire una convergenza a $0$ di tale esponenziale sufficientemente alta
![[Pasted image 20220614114516.png]]

- la costante di tempo è utile per capire in quanto tempo si arriva alla risposta a regime
	- il tempo di assestamento in particolare mi dice esattamente in quanto tempo di arriva in un intorno sufficientemente piccolo della risposta a regime

**Se il grado relativo fosse $2$**, ovvero $n-m=2$ si ottiene:
![[Pasted image 20220614115714.png|600]]
dove infatti:
![[Pasted image 20220614115641.png|500]]
- lo smorzamento e la pulsazione naturale sono stati introdotti per caratterizzare il sistema perché ci daranno maggiori informazioni su esso

In particolare:
- al variare dello smorzamento abbiamo poli reali oppure immaginari
> Se i poli sono reali abbiamo modi di evoluzione non oscillanti. Quindi la funzione al gradino al ciclo chiuso ha un andamento monotono quindi senza oscillazioni (che è buono per la specifica $3$)

> Nel caso sottosmorzato abbiamo comunque stabilità asintotica ($\text{Re}<0$), però è presente la parte immaginaria quindi ci saranno modi di evoluzione oscillanti

![[Pasted image 20220614120332.png]]

Da cui (evitando tutti i conti) si ottiene per il caso *sottosmorzato*:
- dove in rosso abbiamo il transitorio, infatti:
	- compare l'esponenziale reale (velocità di convergenza relativa ai poli)
	- compare anche la parte immaginaria (velocità delle oscillazioni)
- in blu invece il regime permanente (a gradino)
![[Pasted image 20220614120703.png|600]]

**Nota:** Smorzamento piccolo $\to$ tante oscillazioni
- il transitorio non converge se abbiamo poli puramente immaginari
![[Pasted image 20220614121913.png|600]]
- compaiono *sovra elongazioni* (supera il valore del permanente) 
![[Pasted image 20220614121121.png|600]]
- di quanto supero in percentuale il valore asintotico della risposta a regime
	- dipende dallo smorzamento: tanto più è piccolo, tanto più è grande la sovraelungazione (vedi grafico)
		- se lo smorzamento vale più di $1$ come già detto non c'è sovraelungazione
Valgono le formule:
![[Pasted image 20220614121341.png]]
- dove il tempo di assestamento dipende come già detto dalla parte reale dei poli: tanto più essi sono lontani dall'asse immaginario, tanto più è veloce (piccolo) il tempo di assestamento del transitorio


Nei progetti si assegnano $T_{a,\large \upvarepsilon}$ e $S$  e si determinano la posizione dei poli (smorzamento e pulsazione naturale) per soddisfare le specifiche
![[Pasted image 20220614122015.png|600]]

#### CASO GENERALE $n-m>2$
Ci si cerca di ricondurre ai casi precedenti fattorizzando $a^{*}(s)$, dopo aver posizionato i *poli dominanti* e gli altri poli con alta frequenza (lontani dall'asse immaginari), così che la funzione dipende solo dai ($2$) poli dominanti (asintoticamente - perché hanno transitorio molto rapido)
![[Pasted image 20220614122413.png|500]]


##### LIMITI FISICI
Se vogliamo avere un transitorio molto rapido (ad esempio nell'ordine dei millisecondi), è necessario scegliere un guadagno $F$ molto grande $\to$ guardando la legge di controllo però ci si accorge che non possiamo scegliere $F$ arbitrariamente grande perché l'azione di controllo diventerebbe molto elevata (al punto da essere ingestibile)
- Nella pratica si sceglie un compromesso
	- Esempio: tranvia $\to$ si sceglie una via di mezzo per portare il mezzo in una certa posizione in un tempo relativamente buono per i miei scopo senza "sovraccaricare" il controllo
![[Pasted image 20220614122943.png|500]]

Un modo alternativo per scegliere $F$ (invece di posizionare i poli in modo da avere transitorio soddisfacente) è il *controllo ottimo*
- Tiene conto del compromesso sopra descritto (transitorio rapido pur rientrando nei limiti fisici)
	- Idea: tenere basso l'errore d'inseguimento e l'azione di controllo - sulla base di un parametro $\rho$ a seconda delle mie esigenze (se preferisco avere un po' di più di errore o di controllo)
![[Pasted image 20220614123319.png|500]]

### ZERI INSTABILI (cioè se r(s) non è stabile)
- ci sono zeri non cancellabili - rimangono nella funzione di trasferimento a ciclo chiuso
- abbiamo una sottoelongazione (perché avremo un polo con $\text{Re}>0$)
![[Pasted image 20220614123615.png|400]]
- come si vede c'è uno zero al numeratore in $1$

# CONTROLLO IN RETROAZIONE SULL'USCITA
- 