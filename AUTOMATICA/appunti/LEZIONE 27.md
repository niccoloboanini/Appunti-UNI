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
