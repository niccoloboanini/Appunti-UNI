### ESEMPIO: CONTROLLO DI POSIZIONE
- L'uscita è rappresentata dalla posizione del carrello $y(t)$
- L'ingresso (da controllare) è la spinta da dietro $u$
- Esiste l'attrito (viscoso) $b$
- Il carrello ha massa $M$

Si vuole portare il carrello in una posizione desiderata $Y_{0}$ con il controllo $u$ a partire da una certa posizione di partenza $y(0)$
![[Pasted image 20220611125657.png|300]]
Dobbiamo quindi far accadere che: $$ \lim_{t \to \infty} y(t) \approx Y_{0} $$
Supponiamo di aver accesso allo stato per agire sulla legge del controllo
- Lo stato è come al solito: composto da due componenti $x(t)=\begin{bmatrix} x_{1}(t) \\ x_{2}(t) \end{bmatrix}=\begin{bmatrix} y(t)  \\ \dot y(t) \end{bmatrix}=\begin{bmatrix} \text{posizione}  \\ \text{velocita'} \end{bmatrix}$
	- Conoscere lo stato significa sapere a ogni istante $t$ la posizione e la velocità del carrello

Sappiamo già per questo sistema che:
(funzione di trasferimento in cui si vuole ricavare l'uscita, infatti $C=[1 \ \ 0]$)
![[Pasted image 20220611130253.png|500]]

Sappiamo per le specifiche di progetto che:
$$
u(t) = -F x(t) + Hy^{o}(t)
$$
- Il guadagno in feedback $F$ avrà la stessa dimensione del vettore di stato, quindi: $F=\begin{bmatrix} f_{1} & f_{2} \end{bmatrix}$
- $H$ invece è uno scalare (sistema SISO)
Totale: $3$ parametri da controllare $\to f_{1},f_{2},H$ 

#### PRIMO PASSO: polinomio caratteristico a ciclo chiuso (specifica 1)
![[Pasted image 20220611131014.png|600]]
Come si nota, abbiamo un polinomio a ciclo chiuso in cui possiamo agire direttamente sui parametri moltiplicativi alla variabile di riferimento $s$. In questo modo posso arbitrariamente gestire la stabilità perché posso modificare gli zeri (ovvero i poli della funzione di trasferimento a ciclo chiuso in questo caso)
- Se avessimo usato il polinomio ad anello aperto, avremmo ottenuto $$ \varphi(s) = s^{2}+s $$ su cui non avrei potuto far niente se non concludere che veniva un sistema marginalmente stabile (osservando gli zeri)
- Adesso invece con quelli che ho rinominato $a_{1}^{*}$ e $a_{2}^{*}$ posso regolarmi, perché dipendono da $f_{i}$ ovvero gli elementi della matrice $F$ di controllo/guadagno in feedback. Posso rendere il sistema *asintoticamente* stabile

Basta applicare il criterio algebrico di Cartesio a nostro favore, infatti basta che i coefficienti $a_{1}^{*}$ e $a_{2}^{*}$ siano entrambi positivi:
$$
\begin{cases}a_{1}^{*} > 0  \\a_{2}^{*} > 0\end{cases}\Rightarrow
\begin{cases}1+f_{2} > 0  \\f_{1} > 0 \end{cases}\Rightarrow
\boxed{\begin{cases}f_{2} > -1  \\f_{1} > 0 \end{cases}}
$$
Questi sono quindi i guadagni tali da ottenere *poli con parte reale minore di zero* e rispettare la specifica $1$
- Poi per la specifica $3$ questi poli dovranno essere posizionati in un certo modo sul semipiano sinistro così da ottenere un transitorio che scompare rapidamente

#### specifica 2
Applico la formula per trovare $H$:
![[Pasted image 20220611145629.png|400]]
Dove si nota che $H$ dipende da $f_{1}$ che avevamo trovato precedentemente
- $H=f_{1}=1$

#### SPECIFICA 3
Vogliamo che il transitorio "scompaia" velocemente, ovvero vogliamo che l'uscita converga il prima possibile (e senza troppe oscillazioni possibilmente) al regime permanente, che corrisponde al nostro $Y_{0}$ di riferimento.
- Ancora non abbiamo visto un modo quantitativo per soddisfare questa richiesta, ma sappiamo in generale che dipende dalla posizione dei poli del polinomio caratteristico a ciclo chiuso. Ci saranno alcuni casi in cui abbiamo un andamento soddisfacente, e altri in cui non si rispetta questa specifica.
##### ESEMPIO 1
Sappiamo che $\varphi(s)^{*} = s^{2}+(f_{2}+1)s+f_{1}$ 
- Poniamo $f_{1}=1$ e $f_{2}=-0.9$ e vediamo che succede
- $\varphi(s)^{*}$ diventa $$ \varphi(s)^{*}=s^{2}+0.1\ s+1 $$
- Se li calcoliamo, si ottengono poli *complessi coniugati*, posizionati naturalmente nel semipiano sinistro perché abbiamo scelto $f_{1}$ e $f_{2}$ conformi alla specifica $1$.
	- Questo causa una *risposta in ciclo chiuso oscillante*
![[Pasted image 20220611150642.png|600]]
- Fisicamente l'uscita (che rappresenta la posizione del carrello) non è ottimale al nostro caso: il carrello infatti prima di arrivare alla posizione desiderata $Y_{0}=1$, va avanti e indietro a questa (arrivando anche a valori vicino a $2$). Inoltre ci mette anche diverso tempo
	- Questo accade perché abbiamo autovalori sì stabili (parte reale minore di $0$), ma sono oscillanti (complessi coniugati) e *vicino all'asse verticale immaginario*, ovvero alla zona di "confine" per l'instabilità

##### ESEMPIO 2
Cambiamo solo $f_{2}$, facendolo diventare $0$
- Cambia quindi il polinomio caratteristico a ciclo chiuso e cambiano quindi i relativi autovalori
	- In questo caso sono posizionati più lontani dalla instabilità e hanno oscillazioni minori (e ci arrivo anche più velocemente)
![[Pasted image 20220611151301.png|500]]

##### ESEMPIO 3
Cambiamo $f_{1}$ e $f_{2}$ così *autovalori in ciclo chiuso reali*
- L'andamento è non oscillante, ma *ci mette tanto tempo ad assestarmi*
	- Transitorio non oscillante :) però lento :(


#### CONCLUDIAMO LA LEGGE DEL CONTROLLO con le specifiche
Con $f_{1}>0$ e $f_{2}>-1$ e $H=f_{1}$

![[Pasted image 20220611151918.png|600]]
Abbiamo un termine che *dipende dalla posizione* (in particolare dalla differenza tra la posizione desiderata e quella in cui siamo $y^{o}-y$) e dalla *velocità* ($\dot y$) - detto proporzionale derivativo (PD)
- Sulla base di queste due informazioni progettiamo il nostro controllo (forza che agisce sul carrello) 

**Nota:** esistono anche sistemi non controllabili (in cui non c'è la possibilità ad esempio di controllare gli autovalori di $\varphi(s)^{*}$ perché gli elementi di $F$ non compaiono nel polinomio stesso o sono configurati in maniera non concorde con le condizioni da imporre per altre specifiche (ad esempio per calcolare un $H$ adatto)
![[Pasted image 20220611152532.png|600]]
- Se $r(0)=0$ abbiamo $\displaystyle H=\frac{\varphi(0)^*}{\underbrace{r(0)}_{0}}$ (impossibile)
	- Quindi quando progetto il controllo devo prestare subito attenzione a questi vincoli, altrimenti le specifiche potrebbero non essere soddisfatte
		- Per la specifica $2$ come visto è facile, basta che $r(0)\neq 0$
		- Per la specifica $1$ è più complicato, e bisogna parlare di *controllabilità* (vedi dopo)

# CONTROLLABILITA' E STABILIZZABILITA'
