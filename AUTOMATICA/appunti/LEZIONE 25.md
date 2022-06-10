### SINUSOIDE
- Leggermente più complesso perché abbiamo poli puramente immaginari nella trasformata
	- Facendo il prodotto per calcolare $Y_{f}(s)$ otteniamo una funzione che va poi separata coi fratti semplici. In particolare ancora una volta, mi interessa solo l'addendo relativo all'ingresso ovvero $Y_{f}^{U}(s)$
		- Siccome l'ingresso ha due poli, abbiamo due addendi e quindi due residui $\tilde K_{1}$ e $\tilde K_{2}$
- Per trovare il regime permanente faccio l'antitrasformata dei due fratti semplici che mi interessano, così da ottenere appunto $y_{f}^{U}(s)$
- Basta trovare uno dei due residui perché sono l'uno il complesso coniugato dell'altro
*Tutto questo vale se $G(s)$ non ha poli in $\pm j \omega_0$* (sennò entra in risonanza)
	- Ad esempio il primo residuo si calcola come: $\tilde K_{1} = \lim_{s \to j \omega_{0} } (s-j \omega_{0})Y_{f}(s)$ e invece l'altro è il realtivo coniugato appunto
![[Pasted image 20220609120634.png|600]]
>> Otteniamo come regime permanente ancora una sinusoide di frequenza $\omega_{0}$

##### CALCOLIAMO IL RESIDUO
- Fattorizziamo il denominatore $U(s) = s^{2}+\omega_{0}^{2}$ in relazione ai poli di ciò che moltiplica $Y_{f}(s)$, ovvero $s- j \omega_{0}$, così da ottenere le (necessarie) semplificazioni
 - Riscrivo poi in termini di parte reale e parte immaginaria di $G(s)$, con $s = j \omega_{0}$ così da capire come sono fatte parte reale e immaginaria del residuo
	 - Viene $-$ all'ultimo passaggio perché $\frac{1}{j}=-j$
	 - Notiamo che il residuo dipende dalla funzione di trasferimento
![[Pasted image 20220610100010.png|500]]
- $\tilde K_{2}$ come detto di ottiene facendo il coniugato di quanto appena ottenuto
Infine si va a sostituire tutto in $Y_{f}(s)$ e poi si *antitrasforma* per tornare nel dominio del tempo

Dalle formule in tabellina per le antitrasformate
![[Pasted image 20220610100513.png]]

Quindi, sollecitando in ingresso il sistema con un ingresso sinusoidale si ottiene come regime permanente in uscita un segnale che ha lo stesso tipo di andamento, per essere precisi è una combinazione (lineare) di seno e coseno della stessa frequenza $\omega_{0}$ dove il $\sin$ è moltiplicato per la parte reale di $j\omega_{0}$ mentre il $\cos$ è moltiplicato per la parte immaginaria di $j\omega_{0}$
- Quindi stessa frequenza (e diversa ampiezza)
![[Pasted image 20220610101020.png]]
![[Pasted image 20220610101129.png|400]]
- Essendo $G$ un segnale reale, poi la $j$ va tolta dall'argomento!
Comoda la formula finale perché per calcolare il regime permanente con ingresso sinusoidale mi basta applicare quella, senza calcolare esplicitamente l'antitrasformata
- In particolare quella vista riguarda la risposta di $G(s)$ con ingresso un $\sin$ 
	- Se avessimo il $\cos$ sarebbe: 
	![[Pasted image 20220610102628.png|500]]

**Nota:** $G(j\omega_{0})$ viene detta *risposta in frequenza* o risposta armonica

> [!abstract] Approfondimento: Formula equivalente per sistemi SISO
> La stessa formula per sistemi SISO si piò riscrivere come modulo e fase
> ![[Pasted image 20220610112525.png|400]]

### TEOREMA DELLA RISPOSTA IN FREQUENZA (RIASSUNTIVO)
- $G(s)$ priva di poli sull'asse immaginario perché così abbiamo poli distinti di sicuro (ipotesi fondamentale)
- Stabilità esterna: poli con $\text{Re}<0$
>> Se il sistema lineare è asintoticamente stabile e riceve un ingresso sinusoidale, allora la risposta permanente è ancora sinusoidale e la risposta complessiva converge al regime permanente (ci sarà all'inizio un transitorio che poi converge al permanente)
![[Pasted image 20220610101658.png]]

Quindi la funzione di trasferimento calcolata in $0$ (ovvero $G(0)$) ci dà in qualche modo informazioni sul gradino, invece la stessa calcolata in $j\omega_{0}$ (ovvero $G(j\omega_{0}$) ci dà informazioni sul regime permanente in risposta a un ingresso sinusoidale
- In particolare, $G(j\omega_{0})$ viene detto **risposta in frequenza**
	- Quindi è la restrizione di $s$ in $G(s)$ esclusiva all'asse immaginario $j\omega$
	![[Pasted image 20220610102443.png|150]]

Le formule scritte valgono anche per segnali multi ingresso e multi uscite

>Se abbiamo un segnale che è la somma di tanti contributi a frequenza diverse, per il *principio di sovrapposizione degli effetti* si può calcolare il regime permanente in risposta a ciascuna frequenza e poi il regime permanente complessivo come somma dei vari contributi
>	L'esempio al limite è il caso delle *serie di Fourier* in cui abbiamo infinite sinusoidi

#### Esempio: calcolo regime permanente in risposta a una combinazione lineare
Calcoliamo il regime permanente in risposta all'ingresso $$ u(t) = [3+\sin(2t)]\ 1(t) $$
Con funzione $\displaystyle G(s) = \frac{1}{s^{2}+s+2}$
##### PASSI
- Controllo che il denominatore non abbia poli sull'asse immaginaria $j \omega$
	- Addirittura qui si conclude che è esternamente stabile perché ha tutti poli con $\text{Re}<0$ (da Cartesio)
	- In questo modo posso applicare il teorema della risposta in frequenza
- Scompongo l'ingresso come somma di contributi e nomino ciascuno con un nome $u_{i}  \quad , \quad i=1,2,\dots,n \text{ contributi}$
	- Così che il regime permanente è la somma dei singoli contributi: $y_{f}^{U}(t) = \sum_{i=1}^{n \text{ contributi}} y_{f}^{U_{i}}(t)$
- Calcolo quindi i singoli regimi permanenti (a seconda se abbiamo in ingresso gradino o sinusoidi)
	- Ricordandosi di non includere $j$ per la risposta a un segnale sinusoidale perché $G(\dots)$ è un segnale reale!
- Metto insieme tutti i contributi come detto


![[Pasted image 20220610103821.png|500]]
![[Pasted image 20220610112222.png|600]]
Mettendo insieme:
![[Pasted image 20220610112255.png|600]]

---
# ANALISI TD (TEMPO DISCRETO)
## INTRO
- Abbiamo equazioni alle differenze
- Sappiamo già le soluzioni, ovvero l'evoluzioni nel tempo dello stato e dell'uscita
	- *Stato*: Al posto dell'esponenziale di matrice abbiamo una potenza di matrice $A^{t}$ (che sarà da trovare ovviamente) per l'evoluzione libera e invece abbiamo una serie al posto dell'integrale nell'evoluzione forzata
	- *Uscita*: Matrice $C$ che moltiplica lo stato nell'evoluzione libera e una sommatoria al posto dell'integrale per l'evoluzione forzata
![[Pasted image 20220610113124.png|500]]

## TRASFORMATA Z
- Nei sistemi TC per capire l'evoluzione del sistema era necessario studiare l'esponenziale di matrice. Questo lo facevamo grazie alla trasformata di Laplace
- Analogamente, in tempo discreto TD, procediamo analogamente utilizzando la **trasformata Zeta** (generalizza la trasformata di Fourier discreta)

Definizione (dato segnale $f(t)$ causale):
$$
\boxed{f(t) \longleftrightarrow \sum_{t=0}^{\infty} f(t) z^{-t}=F(z)}
$$
con $z$ variabile complessa

### PROPRIETA'
- nota: in Laplace l'operatore di riferimento ($s$), equivaleva a un operatore di derivazione/integrazione. In Zeta invece l'operatore ($z$) è associato al ritardo/anticipo
![[Pasted image 20220610113800.png|600]]
- torna perché in tempo continuo abbiamo $\dot x(t)$, adesso invece $x(t+1)$
*Quindi la trasformata Z serve per passare dalle equazioni alle differenze a equazioni algebriche*

## RISPOSTA LIBERA E FORZATA IN Z
Applicando le proprietà appena viste, si giunge facilmente alle soluzioni generali del sistema
![[Pasted image 20220610114206.png|500]]
Basta risolvere l'equazione algebrica ottenuta, isolando $X(z)$
![[Pasted image 20220610114402.png|500]]
Vale, ancora una volta la seguente:
![[Pasted image 20220610114446.png|500]]
- ovvero si può distinguere evoluzione libera e forza di ingresso e uscita, e la loro somma porta proprio a l'evoluzione complessiva

## PARALLELO TEMPO-Z
![[Pasted image 20220610114558.png|500]]
- l'evoluzione forzata è come quella del tempo continuo solo che al posto di $s$ abbiamo $z$
- l'evoluzione libera invece è la stessa solo che devo moltiplicare per $z$, questo per come è stata definita tale trasformata
