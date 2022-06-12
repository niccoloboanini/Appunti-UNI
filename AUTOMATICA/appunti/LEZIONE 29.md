## ESERCIZI
![[Pasted image 20220612113407.png|500]]

### ESERCIZIO 1: sistema parametrico
- Calcolo $\varphi(s)$, per capire gli autovalori del sistema
	- Se il sistema fosse già asintoticamente stabile, allora non devo procedere oltre (non c'è bisogno del controllo)
- Osservo gli autovalori instabili per capire se questi sono controllabili o meno
	- Se sono controllabili, allora il sistema è stabilizzabile
- Calcolo quindi $\varphi_{c}(s)$, ovvero $(sI-A)^{-1}B$, dove $(sI-A)^{-1}=\frac{1}{\varphi(s)}Adj(sI-A)$, ovvero la funzione di trasferimento tra ingresso e stato (per capire l'evoluzione forzata dello stato)
	- In questo caso $B$ dipende dal parametro
	- Se abbiamo un singolo ingresso allora viene un vettore colonna 
![[Pasted image 20220612114028.png|500]]
- Studio $\varphi_{c}(s)$ al variare di $\alpha$
	- Cioè per quali valori di $\alpha$ ho *semplificazioni* (per capire se qualche autovalore si cancella e quindi è definibile non controllabile) --> guardo per quali valori abbiamo stesse radici sia al numeratore che al denominatore (quindi in questo caso guardo le radici del denominatore e poi mi arrangio un po' a occhio)
- Per $\alpha=0$ abbiamo semplificazioni, in particolare l'autovalore in $1$ si cancella
	- Come parte controllabile abbiamo il minimo comune multiplo degli elementi, ma in questo caso abbiamo solo $\frac{1}{s+1}$, quindi la parte controllabile è $\varphi_{c}(s)=s+1$
		- Quindi $\lambda_{1}=-1$ è un autovalore controllabile
	- Trovo facendo il complementare anche $\varphi_{\text{nc}}(s)=\frac{\varphi(s)}{\varphi_{\text{c}}(s)}=s-1$
		- Quindi $\lambda_2=1$ è un autovalore non controllabile 
			- Avendo $\text{Re}>0$, il sistema è non stabilizzabile
- Per $\alpha=2$, stesso procedimento, risultati duali
	- Rimane un autovalore non controllabile con $\text{Re}>0$, quindi il sistema è stabilizzabile
![[Pasted image 20220612114822.png|600]]
- Nei casi rimanenti, non ci sono semplificazioni (quindi il sistema è completamente controllabile quindi stabilizzabile)
![[Pasted image 20220612115130.png|500]]

- Al variare di $B$ possono variare le proprietà di stabilità, infatti essa è la matrice che dice come il controllo agisce sulla dinamica del sistema
	- Se abbiamo un sistema stabilizzabile, allora è sufficiente cambiare $B$ in modo da rendere il sistema controllabile (comodo perché non devo cambiare tutto il sistema)

### ESERCIZIO 2: sistema di dimensione tre
- Calcolo $\varphi(s)$ come al solito per vedere se è già stabile
	- Lo calcolo secondo la prima riga in questo caso
	- Otteniamo un polinomio già fattorizzato quindi si vedono bene gli autovalori
		- Abbiamo $\lambda_{1}$ con $\text{Re}>0$, quindi dobbiamo studiare la sua controllabilità
- Calcolo $(sI-A)^{-1}B$
	- Prima calcolo $(sI-A)^{-1}$, osservando che è una matrice a blocchi (quindi basta che faccio l'inversa dei due blocchi al massimo di dimensione $2 \times 2$)
![[Pasted image 20220612115748.png|600]]
	- Da cui, si moltiplica per $B$
		- Singolo ingresso --> vettore colonna
- Trovo $\varphi_{c}(s)$ e $\varphi_{\text{nc}}(s)$
	- Controllando che quelli non controllabili siano già stabili e tra quelli non controllabili ci siano quelli (in questo caso solo $1$) instabili
![[Pasted image 20220612120044.png|550]]

### ESERCIZIO 3: esercizio parametrico (cfr. ESERCIZIO 1)
- Entrambi gli autovalori con $\text{Re}\geq 0$
	- Quindi il sistema è stabilizzabile se tutti gli autovalori sono controllabili (quindi se il sistema è *completamente controllabile*)
		- Ricordiamo che vogliamo avere un sistema asintoticamente stabile, quindi vogliamo avere autovalori tutti con $\text{Re}<0$, quindi devo escludere anche quelli sul "confine" in $0$, indipendentemente dalla loro molteplicità
- Calcolo al solito $(sI-A)^{-1} B$
![[Pasted image 20220612120423.png|600]]

- Controllo per quali $\alpha$ abbiamo semplificazioni (per studiare la controllabilità)
	- Guardo radici in comune tra numeratore e denominatore
- Abbiamo semplificazioni per $\alpha=1$ (relativa a $s=0$) e per $\alpha=\frac{1}{2}$ (relativa a $s=1$)
	- Avendo ottenuto due autovalori con $\text{Re}>0$, il sistema è non controllabile
![[Pasted image 20220612121121.png|600]]
Infine, dimostriamo che non abbiamo semplificazioni per gli altri valori non considerati di $\alpha$, quindi i casi in cui abbiamo completa controllabilità e quindi stabilizzabilità
![[Pasted image 20220612121255.png|500]]

#minuto_11_lezione_29_parte_2
