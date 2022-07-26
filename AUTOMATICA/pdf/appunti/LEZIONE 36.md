# **ESERCITAZIONI DI FINE CORSO**
## ESERCIZIO: PROGETTAZIONE DEL REGOLATORE
Dati del problema: $A,B,C$

- Verifica che il problema sia ben posto (autovalori nascosti con $\text{Re}<0$)
		- Autovalori non controllabili con $\text{Re}<0$ per capire $F$
		- Autovalori non osservabili con $\text{Re}<0$ per capire $L$
	- Attraverso il polinomio di controllo e il polinomio osservabile
		- $(sI-A)^{-1}B$ da cui si deriva $\varphi_{\text{c}}(s)$ e $\varphi_{\text{nc}}(s)$
		- $C(sI-A)^{-1}$ da cui si deriva $\varphi_{\text{o}}(s)$ e $\varphi_{\text{no}}(s)$
	- Quindi in ogni caso devo trovare $(sI-A)^{-1}$, poi vedo se moltiplicando per $B$ o $C$ si cancella qualche autovalore
![[Pasted image 20220616120823.png]]
> Nella moltiplicazione per $B$ non ci sono semplicifazioni (completamente controllabile quindi posso trovare $F$: andiamo a progettarla calcolando $A-BF$ e poi $\det(sI-A+BF)$ )
![[Pasted image 20220616121350.png]]
- abbiamo scelto due valori di $F$ casuali, purché rispettino le condizioni

> Nella moltiplicazione per $C$ c'è una semplificazione (scompare l'autovalore in $-1$): controllo quindi che gli autovalori non osservabili hanno $\text{Re}<0$ per avere completa osservabilità e trovare quindi un possibile guadagno $L$: andiamo a progettarlo calcolando $A-LC$ e poi $\det(sI-A+LC)$, e verifico fattorizzando che la parte stabile di $\varphi(s)$ (che è non osservabile) rimane fissa. Si può modificare invece la parte instabile, e quindi regolando gli $\ell_{i}$ si può rendere stabile 

![[Pasted image 20220616122119.png]]
- si rende quindi anche il secondo fattore con radice con $\text{Re}<0$, scegliendo ad esempio $\begin{cases} \ell_{1}= 100  \\ l_{2}=1 \end{cases}$
	- In questo modo si rende l'errore di stima tendente a $0$ e quindi $\hat x \approx x$
![[Pasted image 20220616122356.png]]

*Mettendo tutto insieme* (esplicitando $\varphi^{*}(s)$ [polinomio caratteristico in ciclo chiuso]):
![[Pasted image 20220616122501.png]]

Calcolo infine **la funzione di trasferimento in ciclo chiuso** (che non dipende dal regolatore):
- E quindi poi si trova anche $H$ per soddisfare la specifica $2$
![[Pasted image 20220616122643.png]]

*Studia anche sul perché si fanno le procedure* (per parte orale)
- Anche come son fatte le strutture di controllo (schemi, proprietà etc..)

---

## ESERCIZIO: RETROAZIONE SULLO STATO
![[Pasted image 20220616122956.png|600]]

### 0)
- Scrivo le matrici di stato $A,B,C$ (la riga i-esima di ciascuna è legata alla riga i-esima equazione di stato)

### A)
> $\varphi_{\text{c}}(s)$ a variare di $\alpha$

- Cerco subito di vedere se esistono $\alpha$ guardando la matrice $\mathcal{R}$ di raggiungibilità (perché completa controllabilità $\iff$ completa raggiungibilità)
	- Accade quando $\det\{\mathcal{R}\}\neq 0$ (rango massimo)
	- In questo modo abbiamo in generale la coincidenza tra $\varphi_{\text{c}}(s)$ e $\varphi(s)$, così che devo studiare solo alcuni caso particolari in cui perdo di controllabilità
![[Pasted image 20220616123911.png]]
- per quei valori di $\alpha$ particolari, il sistema è non completamente controllabile
	- Quindi devo calcolare $\varphi_\text{c}(s)$ attraverso il passaggio lungo, ovvero tramite $(sI-A)^{-1}B$
		- Calcolo intanto $\varphi(s)$ e poi derivo $\varphi_{c}(s)$ per i casi particolari
			- (ci saranno semplificazioni perché si perde di controllabilità)
![[Pasted image 20220616124355.png|600]]
Faccio lo stesso per l'altro valore particolare di $\alpha$, ovvero $\alpha=-2$
![[Pasted image 20220616124524.png|600]]

### B)
> $\alpha$ tali che lo stato $\begin{bmatrix} 4 \\ 2\end{bmatrix}$ è raggiungibile

- Si calcola la matrice di raggiungibilità $\mathcal{R}$ (già fatto $\checkmark$) 
	- Verifico che lo stato è ottenibile come combinazione lineare delle colonne di $\mathcal{R}$
	- Sappiamo dall'esercizio A) che in molti casi abbiamo completa raggiungibilità, quindi possiamo portare lo stato dove vogliamo. Dobbiamo studiare solo i casi particolari di $\alpha$ (in questo caso $\alpha \neq 1,-2$)
![[Pasted image 20220616124846.png]]
Studio quei due casi particolari:
![[Pasted image 20220616125109.png]]
- non abbiamo completa raggiungibilità ma quello specifico stato è raggiungibile
Altro caso:
![[Pasted image 20220616125518.png]]
- $X_{\text{r}}$ composto da vettori in cui la seconda componente è uguale alla prima cambiata di segno
	- Si nota che lo stato richiesto non è raggiungibile

### C)
> $\alpha$ per avere $F$ tale che l'azione di controllo in retroazione sullo stato è stabilizzante

- Sappiamo che esiste $F$ stabilizzante se abbiamo autovalori non controllabili con $\text{Re}<0$
	- Facile nei casi generici
	- Nei casi particolari devo vedere $\varphi_\text{c}(s)$ attraverso il passaggio lungo, ovvero tramite $(sI-A)^{-1}B$ ma è già stato calcolato nell'esercizio A) $\checkmark$
![[Pasted image 20220616125939.png|600]]

### D)
> $\alpha$ per avere $F$ per posizionare gli autovalori in ciclo chiuso in $-10$ (attraverso il controllo in retroazione sullo stato)
> 
![[Pasted image 20220616130437.png]]
- Quindi non voglio solo stabilizzare, ma voglio anche mettere (entrambe per l'ordine del sistema è $2$) le radici in $-10$

- Facile se abbiamo completa controllabilità (lo possiamo fare sicuro)
	- Devo verificare invece nei casi particolari $\alpha=1,-2$

- Per $\alpha=1$ abbiamo un autovalore non controllabile in $-2$, quindi non si possono mettere *entrambe* le radici in $-10$
- Stesso ragionamento per $\alpha=-2$

![[Pasted image 20220616130543.png]]


### E) [TODO]
> $\alpha=0$ progettare $F$ e $H$ 
![[Pasted image 20220616130807.png|500]]

(vedi prima parte di lezione)
Soluzione della funzione di trasferimento: $$ G^{*}_{y^{\text{o}}y}(s) = \frac{1}{s^{2}+s+1} $$

### F)
> Andamento nel tempo della risposta forzata con riferimento $y^{\text{o}}(t)$ a gradino (si deve tracciare $y_{f}(t)$)

- Modo 1: antitrasformata [metodo lungo :( ]
![[Pasted image 20220616131100.png|400]]

- Modo 2: sappiamo l'andamento della risposta forzata per segnali tipici per sistemi di I e II ordine
![[Pasted image 20220616131457.png]]
	- caso sottosmorzato (oscilla)
	- posso calcolare i parametri tipici utilizzando le formule

Grafico (indicativo):
![[Pasted image 20220616131546.png]]

---

