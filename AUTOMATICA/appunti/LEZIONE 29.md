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

## STATI RAGGIUNGIBILI
- Indicati con $X_{r}$: sono tutti quegli stati che possono essere raggiunti mediante il controllo (è un sottoinsieme degli stati se il sistema non è completamente raggiungibile, altrimenti è coincidente con l'insieme generico degli stati $\mathbb{R}^{n}$)
	- Nota: se il sistema è completamente raggiungibile, allora applicando l'opportuno controllo si può raggiungere qualsiasi stato
![[Pasted image 20220612164251.png|600]]


## ESEMPIO
![[Pasted image 20220612164951.png|300]]
Partiamo da un sistema già visto non completamente controllabile
	- Si vede che non è nemmeno completamente raggiungibile, infatti *esiste una equazione di stato che non dipende dal controllo*, quindi per capire come si evolve si risolve l'equazione differenziale associata e si nota che non dipende dal controllo
		- Nel dettaglio: $$ \dot x_{2} = -x_{2} \quad \text{ha soluzione } x_{2}(t) = e^{-t}x_{2}(0) $$ si vede che il controllo non influisce. Se partiamo con condizioni iniziali nulle, ovvero $x_{0}=\begin{bmatrix} x_{1}(0) \\ x_{2}(0)  \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \Rightarrow$  $x_{2}(0)=0$ allora $x_{2}(t) =0 \ \ \forall t$
		- Quindi la seconda componente dello stato non si muove da $0$. Partendo dallo stato $x(0)=0$ non posso raggiungere stati $x_{2}(t)\neq 0$
- Con il controllo posso modificare $x_{1}$ ma non $x_{2}$ (quindi mi muovo solo sulla retta orizzontale in figura)
![[Pasted image 20220612164927.png]]

- Ne deriva che l'insieme degli stati raggiungibili è $$ X_{r} = \bigg\{ \begin{bmatrix}\beta  \\ 0 \end{bmatrix}  \text{ con } \beta \in \mathbb{R} \bigg\}$$
- Quindi $X_{r}$ coincide con un *sottospazio lineare* dello spazio $\mathbb{R}^{x_{1}\times x_{2}}$ coincidente con la sola retta $x_{1}$


### CAPIRE SE UN SISTEMA È O MENO COMPLETAMENTE RAGGIUNGIBILE
- Caso semplice: c'è una equazione di stato che non dipende dal controllo
- Caso più complesso: devo analizzare matematicamente com'è fatta la risposta forzata nel tempo $x_{f}(t)$

Infatti:
Partendo da: $x_{f}(t^{o}) = \int_{0}^{t^{o}} e^{A(t-\tau)}B \ u(\tau) \,d \tau$
Ci chiediamo quali stati possiamo raggiungere a partire da questo stato in un certo tempo $t^{o}$. Possiamo riscrivere l'esponenziale di matrice come serie di Taylor:
$$
e^{At} = \sum_{k=0}^{\infty} \frac{(At)^k}{k!}
$$
Quindi:
$$
x_{f}(t^{o}) = \int_{0}^{t^{o}} \sum_{k=0}^{\infty} \frac{(A)^k(t^{o}-\tau)^{k}}{k!} B \ u(\tau) \,d \tau
$$
Portando fuori quello che non dipende dall'integrale:
$$
x_{f}(t) = \sum_{k=0}^{\infty} A^{k}B \ \underbrace{\int_{0}^{t^{o}} \frac{(t^{o}-\tau)^{k}}{k!} u(\tau) \,d\tau}_{\Large u_{k}(t^{o})}
$$
- dove con $u_{k}(t^{o})$ abbiamo individuato il *momento k-esimo* di $u(t)$ al tempo $t^{o}$
	- È la parte della risposta forzata che  *dipende dal controllo*. Ovvero al variare di $u$ abbiamo coefficienti arbitrari (che possiamo scegliere con il controllo)
Ci rimane, sviluppando la sommatoria (ricordando che per $k=0$ l'esponenziale di matrice diventa l'identità):
$$
x_{f}(t) = B \ u_{0}(t^{o}) + AB \ u_{1}(t^{o})+ A^{2}B \ u_{2}(t^{o})+ \dots
$$
	- Una combinazione lineare di termini *arbitrari* $u_{0}(t^{o}), u_{1}(t^{o}),u_{2}(t^{o}),\dots$ 
Questi rappresentano tutti gli stati raggiungibili attraverso la combinazione lineare tra i vettori (termini arbitrari) di controllo appena citati ($u_{0}(t^{o}), u_{1}(t^{o}),u_{2}(t^{o}),\dots$) e le quantità $A,AB,A^{2}B,\dots$

Dal teorema di Cayley-Hamilton, tutte le potenze della matrice $A$ da un certo ordine $n$ in poi ($A^{n},A^{n+1},\dots$) sono riscrivibili come *combinazione lineare delle precedenti*, ovvero $I,A,A^{2},\dots,A^{n-1}$
Quindi: 
$$
A^{k}  \quad , \quad k \geq n \quad \text{è scrivibile come combo lineare di } A^{0}=I,A,A^{2},\dots,A^{n-1}
$$
Allora anche:
$$
A^{k}B  \quad , \quad k \geq n \quad \text{è scrivibile come combo lineare di } B,AB,A^{2}B,\dots,A^{n-1}B
$$

> Quindi si conclude che uno stato è raggiungibile solo se è scrivibile come combinazione lineare dei primi $n$ vettori del tipo $B,AB,A^{2}B,\dots,A^{n-1}B$, grazie al Teorema di Cayley-Hamilton. Se non esiste una combinazione lineare opportuna per riscrivere lo stato, allora tale stato non è raggiungibile e quindi il sistema non è completamente raggiungibile (almeno)

Mettendo insieme tali vettori nelle cosiddetta *matrice di raggiungibilità*, si capisce molto rapidamente quali stati del sistema sono raggiungibili e quali no

