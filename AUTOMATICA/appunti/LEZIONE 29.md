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

# RAGGIUNGIABILITA'
- Metodo utile poi per capire quando si perde di controllabilità

Per ora, definiamo la raggiungibilità come l'insieme di **proprietà** tali per cui, se applicate opportunamente sul sistema, permettono attraverso un certo **controllo $u$** di **portare lo stato iniziale** del sistema nullo $x(0)=0$ **a un certo stato specifico** che si desidera $x(t) = x^{\text{o}}$
 > Si cerca in altre parole di capire se esiste un certo segnale di controllo $u$ che porta lo stato del sistema a un certo valore desiderato di "obiettivo" $x^{\text{o}}$
 ![[Pasted image 20220612162502.png|200]]
- esempio: braccio robotico --> portare l'oggetto in una certa posizione desiderata in un certo lasso di tempo

Dato che le condizioni iniziali le supponiamo nulle, allora l'evoluzione dello stato $x(t)$ dipende solo  dalla risposta forzata $x_{f}(t)$, perché ($x_{\ell}(t)$ dipende dalle sole condizioni iniziali). Ovvero:
$$
x(t) = \cancelto{0}{x_\ell(t)}+x_{f}(t)
$$
Quindi:
$$
x(t) = x_{f}(t) = \int_{0}^{t} e^{A(t-\tau)} B \ u(\tau) \,d\tau
$$
> Conviene per la raggiungibilità di ragionare nel tempo. Altrimenti in Laplace avremmo $X_{f}(t) = (sI-A)^{-1}B \ U(s)$, come abbiamo visto per la stabilità. Tuttavia come vedremo conviene rimanere nel tempo



### ESEMPIO DI APPLICAZIONE
- Applicare le proprietà di raggiungibilità per capire se possiamo portare il sistema complessivo (lo stato di tutti gli agenti) a un valore desiderato
	- Ad esempio nella dinamica delle opinioni potremmo pensare a una campagna di marketing (che può influenzare anche un sottoinsieme di agenti - ovvero i nodi del grado) tale per cui lo stato complessivo raggiunga un valore di riferimento (ad esempio uno stato di fiducia verso un brand che faccia fare più acquisti)
![[Pasted image 20220612163538.png|500]]
	- Nel caso ci si regola a mano a mano, aumentando ad esempio il numero di ingressi $u_{i}$ per influenzare più persone

- L'esempio inverso può essere quello di agire in maniera malevola sullo stato degli agenti per capire la robustezza del sistema (usato in cyber-security)
	- Utile per progettare poi un sistema più sicuro

### STATI RAGGIUNGIBILI
- Indicati con $X_{r}$: sono tutti quegli stati che possono essere raggiunti mediante il controllo (è un sottoinsieme degli stati)