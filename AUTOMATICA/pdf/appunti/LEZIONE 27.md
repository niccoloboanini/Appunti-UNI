#### SITEMA A CICLO CHIUSO $\mathcal{P}^{*}$
- Supponiamo $\mathcal{C}$ e $\mathcal{P}$ come detto LTI
Possiamo quindi **combinarli** e ottenere un unico sistema LTI generalizzato, che chiamiamo $\mathcal{P}^{*}$ ("pi star"). È il nostro sistema a ciclo chiuso (in *retroazione*)
![[Pasted image 20220610162100.png|400]]
- Dato un riferimento, $\mathcal{P}^{*}$ ci dice come si comporta il sistema di controllo una volta preso un riferimento $y^{o}$

## FUNZIONE DI TRASFERIMENTO
Essendo $\mathcal{P}^{*}$ un sistema LTI, possiamo definire una funzione di trasferimento: $$ G^{*}_{y^{o}\ y}(s) $$
- indica la funzione di trasferimento in ciclo chiuso tra riferimento $y^{o}$ e l'uscita $y$

Quindi in pratica avremo:
$$
^{y^{0}}\rightarrow\boxed{ G^{*}_{y^{o}\ y}(s)}\rightarrow ^{y}
$$
Essa indica *come il sistema si comporta in riferimento a un certo valore desiderato*
Dato che $\mathcal{P}$ ha una sua $G(s)$ di riferimento, l'obiettivo del controllo è quello di scegliere $\mathcal{C}$ adeguatamente per avere una funzione di trasferimento totale $G^{*}_{y^{o}\ y}(s)$ come vogliamo e quindi che l'uscita $y$ tenda a $y^{o}$ di riferimento

### RISPOSTA FORZATA
Posso scrivere la risposta forzata in due parti:
- **Transitorio** - parte di risposta forzata che dipende dai poli della funzione di trasferimento $G^{*}_{y^{o}\ y}(s)$
- **Regime Permanente** - parte di risposta forzata che dipende dai poli dai poli dell'ingresso ovvero il riferimento $y^{o}$ 

Quindi:
$$
\large y_{f}(t) = t_{f}^{G^{*}}(t) + y_{f}^{Y^{o}}(t)
$$

 
Sappiamo dalla teoria che *se un sistema è asintoticamente stabile, allora la risposta complessiva $y(t)$ converge al regime permanente $y_{f}^{Y^{o}}(t)$*
- Siccome abbiamo supposto che il riferimento sia costante (ovvero un gradino), sappiamo anche calcolare il regime permanente (e quindi l'uscita)
![[Pasted image 20220610164226.png|500]]
- quindi in uscita avremo ancora un gradino in ingresso $G^{*}_{y^{o}\ y}(s)$ moltiplicato per un certo $Y_{0}$
![[Pasted image 20220610164425.png]]

**L'obiettivo quindi è portare l'uscita** (che è ancora come detto una costante e coincide col regime permanente per sistemi asintoticamente stabili) **al valore di riferimento**
- Quindi cercheremo di fare attenuazioni o guadagni a seconda del caso o dell'istante
Deve quindi valere la relazione:
$$
y_{f}^{Y^{o}}(t) =  G^{*}_{y^{o}\ y}(0) \cdot Y_{0} \cdot 1(t) = \underbrace{Y_{0} \cdot 1(t)}_{\text{riferimento}}
$$
Pertanto, dovremo trovare il modo in cui il guadagno $G^{*}_{y^{o}\ y}(s)$ sia $1$, cosicché
$$
y_{f}^{Y^{o}}(t) =  \underbrace{1}_{G^{*}_{y^{o}\ y}(0)} \cdot Y_{0} \cdot 1(t) = \underbrace{Y_{0} \cdot 1(t)}_{\text{riferimento}}  \quad  \quad \checkmark
$$
valga la relazione (il regime permanente coincide col riferimento)
Abbiamo ottenuto quindi che: $$ \lim_{t \to \infty} y(t) = Y_{0}  \quad , \quad \forall Y_{0}, \forall x(0)$$
viene detto *inseguimento perfetto* del riferimento

> [!abstract] Cosa ci serve: SPECIFICHE DEL PROGETTO
> Progettare un sistema di controllo $\mathcal{P}^{*}$ che sia *asintoticamente stabile* (che mi garantisce convergenza al regime permanente) e tale per cui il *guadagno in continua sia unitario*, significa **avere un sistema la cui uscita converge al valore di riferimento** [che è l'obiettivo del controllo]

![[Pasted image 20220610165557.png|600]]

Sono dette le *specifiche a regime* (o specifiche statiche)
Quindi il nostro obiettivo ora è costruire un **controllore** che rispetti le specifiche necessarie


## RIFERIMENTI LENTAMENTE VARIABILI
Fin ora abbiamo visto i casi in cui il riferimento è costante. Si dimostra che anche con riferimenti lentamente variabili (ad esempio la traiettoria che la macchina deve assumere in un percorso relativamente semplice - ad esempio "quasi" rettilineo) vanno bene le specifiche $1$ e $2$ sopra descritte per il progetto di un controllore $\mathcal{C}$

Prendiamo il caso di *riferimento sinusoidale* di bassa frequenza ($\omega_{0} \approx 0$)

Abbiamo un ingresso sinusoidale --> La risposta in frequenza (regime permanente) è ancora una sinusoide (scrivibile in termini parte reale e parte immaginaria oppure in termini di modulo e fase)
- Se applichiamo la specifica $2$ (guadagno in continua unitario), si vede che per $\omega_{0}\approx 0$, la risposta in frequenza coincide *approssimativamente* con l'andamento desiderato
- Si esegue un piccolo errore ma se $\omega_{0}$ è piccola allora l'errore è trascurabile per certi esperimenti/aspetti
![[Pasted image 20220610170857.png|600]]
Quindi le specifiche $1$ e $2$ sono valide anche per riferimenti che variano di poco

## SPECIFICHE DEL TRANSITORIO
Le specifiche $1$ e $2$ garantiscono un certo comportamento per il *regime permanente*, ma non ci dicono tanto riguardo la risposta transitoria
Si parla allora di **specifica $3$**, che mi assicura di arrivare rapidamente al regime permanente (che se è progettato con $1$ e $2$ coincide o quasi con il riferimento)
	- Esempio della doccia: arrivare più velocemente possibile alla temperatura desiderata, evitando inaspettate escursioni di temperatura repentine

$$
\text{Specifica 3: transitorio rapido + escursioni limitate}
$$
Possibili casi da evitare (qualitativi)
![[Pasted image 20220610171359.png]]

Si premura che la parte transitoria della risposta forzata sia corretta per l'esigenze che abbiamo
$$
\large y_{f}(t) = \underbrace{t_{f}^{G^{*}}(t)}_{\text{spec. 3}} + \underbrace{y_{f}^{Y^{o}}(t)}_{\text{spec. 1,2}} = \mathcal{L}^{-1}\{ \underbrace{G^{*}_{y^{o}\ y}(s)}_{\text{spec. 3}} Y^{o}(s)\} 
$$
- l'obiettivo del controllo quindi sarà quello di assegnale alla funzione di trasferimento a ciclo chiuso una forma desiderata

## ATTENUARE o REIETTARE I DISTURBI
Se un sistema presenta dei disturbi $d$ come in figura, allora occorrono *nuove specifiche* per attenuare o reiettare completamente questi ultimi 
![[Pasted image 20220610173601.png|400]]
- nei sistemi reali $d$ è sempre presente 
	- Esempio: aeroplano --> turbolenza: il controllore $\mathcal{C}$ cercherà di attenuare questi disturbi

Agiscono quindi nel sistema due ingressi: $y^{o}$ e $d$ sul sistema a ciclo chiuso quindi l'andamento dell'uscita dipende da entrambi
- A causa di questo infatti esistono due funzioni di trasferimento: $G^{*}_{y^{o}\ y}(s)$ e $G^{*}_{d\ y}(s)$
	- Cioè una tra il riferimento e l'uscita e una tra il disturbo e l'uscita
		- Essendo il sistema lineare ci si può concentrare su una delle due singolarmente


# TECNICHE DI CONTROLLO: fase progettuale
## 1° Tecnica: RETROAZIONE ALGEBRICA SULLO STATO
Supponiamo di avere informazione completa sullo stato (sistema di controllo in *informazione completa*), ovvero $w = x$
![[Pasted image 20220610174816.png|200]]
Quindi per ogni istante di tempo $t$ dobbiamo scegliere un $u$ opportuno, sulla base di $2$ ingressi: lo stato $x$ e il riferimento $y^{o}$. Quindi $u$ è una funzione di $2$ variabili: $$ u = \mathcal{C}(x,y^{o}) $$
Supponiamo che venga generata una azione di controllo $u(t)$ *lineare*. Sarà allora della forma matrice per vettore:
$$
\large \text{Legge di controllo (}\mathcal{C}): \quad \boxed{u(t) = \underbrace{-Fx(t)}_{\text{feedback}} + \underbrace{Hy^{o}(t)}_{\text{feedforward}}}
$$
- Dove $F$ e $H$ sono matrici di dimensioni opportune 
	- Il meno davanti a $F$ si inserisce per default (ma sarebbe indifferente come idea)
Il controllo in $\text{feedback è pari a } -Fx(t)$ e dipende dallo stato $x$
	- $F$ è il guadagno in feedback ed è una matrice $\dim(u) \times \dim(x)$
Il controllo in $\text{feedforward è pari a } Hy^{o}(t)$ e dipende dal riferimento $y^{o}$
	- $H$ è il guadagno in feedforward ed è una matrice $\dim(u) \times \dim(y)$
![[Pasted image 20220610175519.png|500]]

#### SISTEMI SISO ($\dim(u)=\dim(y)=1$)
Per sistemi SISO:
- $F$ è un vettore riga $F = [f_{1},f_{2}, \cdots,f_{n}]  \quad , \quad n = \dim(x)$
	- (dato che lo stato è un vettore colonna $\begin{bmatrix} x_{1}  \\  \vdots  \\ x_{n} \end{bmatrix}$)
- $H$ è uno scalare
	- (dato che il riferimento è un valore)

Risolvere un problema di controllo significa quindi determinare correttamente:
$$ \underbrace{n}_{F}+\underbrace{1}_{H}  \quad \text{parametri di progetto} $$
### EQUAZIONI DI STATO
Si possono riscrivere le equazioni di stato del sistema a ciclo chiuso sulla base di quanto abbiamo detto (applicando cioè un determinato controllo $\mathcal{C}$), per rappresentarlo algebricamente

- Sappiamo infatti che il controllo dovrà essere del tipo: $\mathcal{C} \to \  \{ u=-Fx+Hy^{o}$
- Sostituiamo $u$ del controllo in $\begin{cases} \dot x = Ax +Bu  \\ y = Cx + \cancelto{0}{Du} \end{cases}$
Ottenendo:
- $\dot x = Ax+B(-Fx+Hy^{o}) = Ax-BFx+BHy^{o}=(A-BF)x+BHy^{o}$
Quindi il problema a ciclo chiuso:
$$
\large \mathcal{P^{*}} = \begin{cases} \dot x = \overbrace{(A-BF)}^{\Large A^*}x +\overbrace{BH}^{\Large B^{*}}y^{o}  \\ y = Cx \end{cases}
$$
- Dove abbiamo rinominato le matrici che compaiono in $\dot x$ con $A^{*}$ e $B^{*}$

> Quindi agendo sui parametri di progetto $F$ e $B$ si può modificare l'uscita del sistema $y^{o}$ a nostro piacimento rendendo addirittura in certi casi stabile un $\mathcal{P}$ che in origine non lo era. Questo lo possiamo fare in maniera più generale specificando la retroazione $u=-Fx+Hy^{o}$ che appunto modifica la dinamica del sistema

![[Pasted image 20220610181833.png|550]]

![[Pasted image 20220610181914.png|400]]
- dove appunto abbiamo modificato le matrici $B$ e $A$. Quest'ultima in particolare è importante perché è quella che determina i modi di evoluzione del sistema (per fare un esempio)

#### POLINOMIO CARATTERISTICO IN CICLO CHIUSO
Se vogliamo agire sulla stabilità, dobbiamo gestire gli zeri del polinomio caratteristico $\varphi(s)$. Pertanto, si definisce *polinomio caratteristico in ciclo chiuso*, il seguente: $$ \varphi^{*}(s) =\det(sI-A^{*})=\det(sI-A+BF) $$
perché appunto è cambiata la matrice $A$
- notiamo che qui entra in gioco solo la matrice $F$. Ci possiamo aspettare che inserendo determinati valori in essa, vadano a variare sul piano $s$ i poli di $\varphi(s)^{*}$, e dunque le condizioni di stabilità
	- Quindi: agire su $F \approx$ spostare gli autovalori 

#### FUNZIONE TRASFERIMENTO IN CICLO CHIUSO
Analogamente, definiamo la *funzione di trasferimento in ciclo chiuso* come:
$$
G_{y^{o}\ y}^{*}(s) = C(sI-A^{*})^{-1}B^{*}=C(sI-A+BF)^{-1}BH
$$
- agendo (anche) su $H$, possiamo ottenenere uno specifico guadagno del sistema a ciclo chiuso

> [!important] Formule per sistemi SISO (da usare negli esercizi)
> Si dimostra che la funzione di trasferimento a ciclo chiuso si calcola come:  $$ \boxed{G_{y^{o}\ y}^{*}(s) = \frac{r(s)}{\varphi^{*}(s)}\cdot H} $$
> Dove $r(s)$ è lo stesso di un sistema generico LTI TC lineare, ovvero $$ r(s)=C Adj(SI-A)\cdot B $$
> 	In pratica $r(s)$ *non dipende da $F$* (cioè se calcolassi $r(s)$ in un sistema a ciclo chiuso otterrei comunque gli stessi valori)
> 	Nel caso generale di sistema LTI TC lineare (ad anello aperto), abbiamo: $G(s)=\frac{r(s)}{\varphi(s)}$
> 	Quindi varia soltanto il polinomio caratteristico ($\varphi(s)\to \varphi(s)^{*}$) e poi la successiva moltiplicazione per $H$
> 		Infatti dipende come detto da $F$ che è all'interno di $\varphi(s)^{*}$ che mi determinano i poli del polinomio caratteristico e $H$ (costante moltiplicativa) che determina il guadagno per un sistema a ciclo chiuso
![[Pasted image 20220610183725.png|600]]

- **Nota:** la retroazione algebrica (feedback) modifica sullo stato i poli (perché influenza $(\varphi(s)^{*})$) ma non modifica gli zeri della funzione di trasferimento $G_{y^{o}\ y}^{*}(s)$
- Quando si vede l'asterisco è da leggere come "a ciclo chiuso". Ad esempio: polinomio caratteristico a ciclo chiuso $\to \varphi(s)^{*}$

## PROGETTO
Dobbiamo soddisfare le $3$ specifiche

#### SPECIFICA 1 e 3
(spec.1)Basta che il "nuovo" polinomio caratteristico abbia tutte radici con $\text{Re}<0$ in modo tale che sia *asintoticamente stabile*
(spec.3)Dato che vogliamo anche garantire  un transitorio rapido con escursioni limitate dovremo *posizionare i poli di $\varphi(s)^{*}$ in modo opportuno* (vedi lezioni successive)
$$
\varphi^{*}(s) = \det(sI-A+BF)  \quad , \quad \text{con Re}<0 \text{ e posizionate adeguatamente}
$$
(sono specigiche: pole placement, perché legate direttamente alla posizione dei poli sul piano complesso - in particolare nel semipiano sinistro perché li vogliamo asintoticamente stabili)
#### SPECIFICA 2
Dobbiamo avere un *guadagno in continua in ciclo chiuso tale che sia unitario*, ovvero deve valere:
$$
G_{y^{o}\ y}^{*}(s)|_{s=0} = G_{y^{o}\ y}^{*}(0)= 1
$$
Essendo come detto:
$$
G_{y^{o}\ y}^{*}(s) = \frac{r(s)}{\varphi^{*}(s)}\cdot H
$$
Allora deve valere:
$$
G_{y^{o}\ y}^{*}(s)|_{s=0} = G_{y^{o}\ y}^{*}(0) = \frac{r(0)}{\varphi^{*}(0)}\cdot H = 1
$$
Quindi basta porre:
$$
H = \frac{\varphi^{*}(0)}{r(0)}
$$
Cosicché:
$$
G_{y^{o}\ y}^{*}(0) = \frac{r(0)}{\varphi^{*}(0)}\cdot \frac{\varphi^{*}(0)}{r(0)} = 1 $$
##### RIASSUMENDO
![[Pasted image 20220610185836.png|500]]
Prima progetto $F$ poi $H$
- Poi ho fatto perché posso determinare il giusto $u=-Fx+Hy^{o}$
