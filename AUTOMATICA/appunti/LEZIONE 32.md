## ESERCIZIO: STUDIO CONTROLLABILITA'/STABILITA'
- Trovo il polinomio caratteristico $\varphi(s)$
- Calcolo matrice inversa $(sI-A)^{-1}$
- Calcolo i polinomi: 
	- Di controllo: $(sI-A)^{-1} B$
		- Trovo $\varphi_{\text{c}}(s)$ facendo il m.c.m degli elementi al denominatore nella matrice ottenuta
			- concludo sulla completa controllabilità o meno esplicitando eventualmente $\varphi_{\text{nc}}(s)$
	- Di osservabilità: $C(sI-A)^{-1}$
		- Trovo $\varphi_{\text{o}}(s)$ facendo il m.c.m degli elementi al denominatore nella matrice ottenuta
			- concludo sulla completa controllabilità o meno esplicitando eventualmente $\varphi_{\text{no}}(s)$
- Osservo le posizioni sul piano complesso di tutti gli autovalori ottenuti (di controllo e di osservabilità)
![[Pasted image 20220614163529.png]]
- Controllo che effettivamente gli autovalori non osservabili sono tali, calcolando $Y_{\ell}(s)=C(sI-A)^{-1} \ x(0)$ e poi antitrasformando per vedere i modi naturali osservabili
	- In questo caso si vede solo il modo $e^{t}$ associato a un autovalore osservabile $\lambda_{1}=1$
- Se calcoliamo la funzione di trasferimento $G(s) = C(sI-A)^{-1}B$, rimangono solo gli autovalori sia osservabili che controllabili (in questo caso $\lambda_{1}=1$)
![[Pasted image 20220614164034.png|600]]

---

# RETROAZIONE ALGEBRICA SULL'USCITA
- Finora abbiamo visto solo il controllo relativo alla retroazione sullo stato, che ci fornisce una informazione completa del sistema
Adesso invece cerchiamo una informazione *parziale*, perché supponiamo di osservare solo i dati d'ingresso e uscita (e che quindi sia visibile in generale solo $y$)
![[Pasted image 20220614164347.png]]
- si può già intuire che la parte non osservabile non può essere modificata con il controllo in retroazione, perché non è presente in uscita
	- con il controllo in uscita quindi potremmo agire solo su ciò che è sia controllabile che osservabile (*ciò che è nascosto è incontrollabile*)
		- questo perché abbiamo accesso solo ad alcune variabili del sistema (di uscita)

## LEGGE DI CONTROLLO
Utilizziamo in maniera duale rispetto a quanto visto sullo stato, una *funzione lienare sull'uscita*: $$ \mathcal{C}: \quad u(t) = -K\ y(t) + H \ y^{\text{o}}(t) $$
Molto simile a quella dello stato: $u(t) = -F\ x(t) + H \ y^{\text{o}}(t)$, dove come si vede avevamo informazioni dell'intero stato $x(t)$; adesso invece conosciamo solo l'uscita $y(t)$
![[Pasted image 20220614164936.png]]
- a livello di notazione cambia lettera da stato a uscita: $F \to K$; perché adesso la retroazione è sull'uscita (quindi moltiplicata per $y$)

![[Pasted image 20220614165120.png]]

- esistono anche altri tipi di retroazione (questo è il caso più semplice di funzione lineare)

### GUADAGNO IN FEEDBACK E IN FEEDFORWARD
Per soddisfare le specifiche di controllo dovremo specificare $K$ e $H$
In generale: $\text{dim}(K)=\text{dim}(H)=\text{dim}(u) \times \text{dim}(y)$ 

Per sistemi **SISO**, $u$ e $y$ non sono vettori ma sono scalari:
$$ K \ \text{e} \  H \text{ sono scalari} $$

A differenza delle equazioni dello stato in cui $F=[f_{1},\dots,f_{n}]$ aveva dimensione vettoriale riga $1 \times n$, dove $n$ sono le variabili di stato
- Adesso invece **abbiamo meno gradi di libertà**, perché $K$ non è più un vettore (con cui potevo un po' gestirmi i valori), ma è **uno scalare** (cioè un singolo numero / parametro)
- Scelte vincolate
	- Nello retroazione dello stato invece i poli controllabili potevo posizionarli come volevo e se il sistema era completamente controllabile potevo scegliere e personalizzare il polinomio in ciclo chiuso
	- Quindi la *retroazione sull'uscita è una particolare retroazione sullo stato in cui abbiamo fissata una direzione del guadagno* (quindi abbiamo un $F$ prefissato)
![[Pasted image 20220614170337.png|500]]

#### SISTEMA IN CICLO CHIUSO $\mathcal{P}^{*}$
![[Pasted image 20220614170614.png|500]]

Dove $KC$ è l'equivalente di $F$ per lo stato
![[Pasted image 20220614170740.png|600]]
![[Pasted image 20220614170846.png|600]]
**Nota:** Queste sono formule generali, poi noi ci concentreremo sui sistemi SISO che hanno formule più semplici
## FUNZIONE DI TRASFERIMENTO IN CICLO CHIUSO
![[Pasted image 20220614175037.png]]
Quindi:
![[Pasted image 20220614175158.png|500]]
Che si può riscrivere in termini di polinomi, ricordando che $G(s) = \frac{b(s)}{a(s)}$:
![[Pasted image 20220614175337.png]]

Quindi:
![[Pasted image 20220614175601.png]]
- dove i poli $a(s)$ sono quelli relativi prima di applicare il controllo sull'uscita
- dopo il controllo invece abbiamo al denominatore un nuovo polinomio che definisce i poli dopo il controllo, che denominiamo $a^{*}(s)$ [polinomio dei poli in ciclo chiuso]
	- Gli zeri rimangono gli stessi perché c'è sempre $b(s)$

Pertanto, **la retroazione algebrica di uscita modifica gli zeri ma non i poli**

## MODO ALTERNATIVO PER POLINOMIO CARATTERISTICO A CICLO CHIUSO
Sappiamo che possiamo fattorizzare $\varphi(s)$ in anello aperto come: $\varphi(s)=a(s) \varphi_{h}(s)$
Applicando la retroazione algebrica si ottiene:
$$
	\varphi^{*}(s) = a^{*}(s)\ \varphi_{h}(s)=[a(s)+k\ b(s)] \ \varphi_{h}(s)
$$
- questo perché con la retroazione algebrica sull'uscita si può modificare solo quello che è sia controllabile che osservabile
	- Quindi dopo il controllo i poli cambiano perché si esegue il passaggio $a(s) \to a^{*}(s)$ applicando il controllo, invece la parte nascosta non varia, quindi $\varphi_{h}(s) \to \varphi_{h}(s)$ applicando il controllo
![[Pasted image 20220614180143.png]]

- quindi per sistemi **SISO** abbiamo formule più semplici


#### RIASSUMENDO
![[Pasted image 20220614180311.png|600]]
- dove abbiamo visto per bene solo la dimostrazione della funzione di trasferimento (il polinomio caratteristico invece abbiamo solo l'idea di dimostrazione)
Inoltre:
![[Pasted image 20220614180437.png|500]]


### ESEMPIO: CARRELLO
Portare il carrello in posizione $Y_{0}$ (setpoint) misurando solo la posizione $y$ (tramite il contorollo $u$)
![[Pasted image 20220614180535.png|500]]
- calcolo il polinomio caratteristico $\varphi(s)$
- calcolo la funzione di trasferimento $G(s) = \frac{b(s)}{a(s)}$ 
- fattorizzo il polinomio caratteristico (con la parte nascosta) $\varphi(s) = a(s)\varphi_{h}(s)$
- posso scrivermi sia $\varphi^{*}(s)$ che $G^{*}_{y^{\text{o}}\ y}(s)$
- faccio il progetto (specifiche $1,2,3$)

>- calcolo il polinomio caratteristico $\varphi(s)$
>- calcolo la funzione di trasferimento $G(s) = \frac{b(s)}{a(s)}$ 
>- fattorizzo il polinomio caratteristico (con la parte nascosta) $\varphi(s) = a(s)\varphi_{h}(s)$
![[Pasted image 20220614180914.png|500]]

>posso scrivermi sia $\varphi^{*}(s)$ che $G^{*}_{y^{\text{o}}\ y}(s)$

Da cui, applicando le formule:
(notiamo come su $a^{*}(s)$ posso modificare un solo parametro $K$)
![[Pasted image 20220614181128.png]]


> faccio il progetto (specifiche $1,2,3$)

Proseguo con le specifiche:
![[Pasted image 20220614181402.png]]
Per la specifica $3$ notiamo come la funzione di trasferimento sia del II ordine!
- Solo che $a^{*}(s)$ non possiamo crearlo personalizzato (quindi non potrò scegliere la posizione di tutti i poli). Si nota bene osservando $a^{*}(s)$ in cui compare $K$ una sola volta in questo esercizio
	- Devo trovare il cosiddetto *luogo delle radici*
![[Pasted image 20220614181706.png]]
- dove è stata applicata la formula: $x_{1,2}=\frac{-b \pm \sqrt{\Delta}}{2a}$
- si nota che i poli in ciclo chiuso variano al variare di $K$
