## ESERCIZIO: RETROAZIONE SULL'USCITA
![[Pasted image 20220616150623.png]]

### 0)
- Mi scrivo le matrici $A,B,C$
![[Pasted image 20220616150712.png]]
### A)
> $\varphi(s)$ e $G(s)$

- Calcolo il determinante secondo la prima riga (per esempio)
- Fattorizzo il polinomio
	- Essendo di grado $3$, faccio una prima fattorizzazione e poi eguaglio i coefficienti $a$,$b$ scelti
- Sempre utile fattorizzarlo infine secondo le proprie radici
	- Dagli autovalori capisco se è stabile oppure no (mi avvantaggio per dopo)

- Calcolo poi $G(s)$ (l'aggiogata ce l'ho di già)
	- Conviene fare il prodotto partendo dalle matrici con più zeri presenti
	- *Verifico anche se ci sono semplificazioni*

![[Pasted image 20220616151253.png]]
![[Pasted image 20220616151410.png|500]]

### B)
- Facile se abbiamo risposto in maniera completa ad A)  (con le semplificazioni)
	-  Infatti per $\alpha=-1$ avevamo semplificazioni, quindi vuol dire che è presente un autovalore nascosto (instabile in questo caso)
![[Pasted image 20220616151930.png]]
##### FINE STUDIO PARAMETRICO
### C)
- Cerchiamo $K$ stabilizzanti (asintotici a ciclo chiuso)
- Abbiamo retroazione sull'uscita quindi utilizzeremo la formula adeguata
	- $\varphi_{h}(s)=1$ perché come visto in B) non ci sono autovalori nascosti per $\alpha \neq -1$ 
![[Pasted image 20220616152212.png]]
Vediamo per quali $K$ abbiamo stabilità asintotica in ciclo chiuso
- Costruisco la tabella di Routh perché ho un polinomio di $3°$ grado
	- $\varphi^{*}(s)$ asintoticamente stabile $\iff$ tutti gli elementi della prima colonna ha lo stesso segno 
		- Risolviamo il sistema di disequazioni
			- Osservando che il denominatore della seconda disequazione deve essere positivo quindi si riduce allo studio del solo numeratore (che è semplice perché di secondo grado)
			- considero solo $K \in \mathbb{R}$
![[Pasted image 20220616152733.png]]

### D)
- Progetto per rispettare le specifiche: 
	- stabilità asintotica in ciclo chiuso (già fatto $\checkmark$)
	- inseguimento perfetto in riferimento costante
		- Scrivo la funzione di trasferimento in caso di retroazione algebrica sull'uscita (vedi formula)
		- Calcolo in zero
		- Trovo $H$ (in funzione di $K$)
![[Pasted image 20220616153112.png|600]]
- Scelgo un $K$ arbitrario per trovare un valore (numero) anche per $H$

### E) 
- Riferimento sinusoidale (applico teorema risposta in frequenza per segnali tipici)
	- Applico la formula del teorema della risposta in frequenza (ricordando che ho un sistema in ciclo chiuso: quindi l'ingresso è il riferimento e l'uscita è $y$ e ha funzione di trasferimento $G^{*}_{y^{\text{o}}y}$)
![[Pasted image 20220616153243.png]]
Prendendo gli stessi $H$ e $K$ dell'esercizio D), si ottiene:
- Calcolo alla fine la risposta in frequenza con $\omega_{0}=1$
	- Cerco $\text{Re}$ e $\text{Im}$
	- Li metto nella formula di $y_{f}^{Y^{o}}(t)$
![[Pasted image 20220616153710.png]]

---

## ESERCIZI: RETROAZIONE DINAMICA SULL'USCITA
- Non c'è prefiltro $H_{f}$
![[Pasted image 20220616163336.png]]

### A)
> $K(s)$ per rendere il sistema in ciclo chiuso asintoticamente stabile
- $K(s)$ è un rapporto di polinomi di grado $n_{K}$ opportuno
	- $n_{K}\geq \text{grado }a(s)-1\geq2-1\geq1$
		- In questo caso quindi abbiamo $3$ parametro
- Scrivo $\varphi^{*}(s)$ (spesso in questo esercizi $\varphi_{h}(s)=1$, in particolare quando viene data $G(s)$)
	- Rendo il polinomio stabile (asintotica in ciclo chiuso)
		- Se non viene richiesto una posizione particolare dei poli, basta eguagliare il polinomio coi suoi coefficienti a un altro polinomio stabile che scelgo (con radici aventi $\text{Re}<0$, in questo caso $(s+1)^{3}$ che ha $3$ radici in $-1$)
![[Pasted image 20220616164209.png|500]]

### B)
>Ancora progetto di un controllore con azione dinamica sull'uscita però stavolta con azione integrale (denominatore con polo in $0$, ovvero $p_{0}=0$)
- Sempre per avere stabilità asintotica in ciclo chiuso

**Nota:** Il grado deve essere almeno $2$, perché vogliamo azione integrale quindi $n_{K}\geq \text{grado } a(s)=2$

![[Pasted image 20220616164436.png|500]]
- ci saranno un po' più di conti da fare perché abbiamo grado più alto di $p(s)$ e $q(s)$
- anche in questo caso si pone $\varphi^{*}(s)$ uguale a un polinomio stabile che conosciamo, ad esempio $(s+1)^{4}$

- si esplicita infine la funzione di trasferimento del controllore
![[Pasted image 20220616164828.png]]

### C)
> Valutare il comportamento a regime con riferimento e disturbo costante (di ampiezza data) + errore d'inseguimento a regime

- Sistema $\mathcal{P}$ a ciclo chiuso (dinamico) con due ingressi: uno di riferimento e un disturbo
	- Abbiamo due regimi permanenti da sommare (principio sovrapposizione delle cause)
		- Avendo segnali costanti, posso applicare il teorema della risposta in frequenza per segnali costanti, quindi viene una somma di due guadagni in continua (funzioni trasferimento in ciclo chiuso - quindi calcolati in zero - uno tra riferimento e uscita e uno tra disturbo e uscita) moltiplicati ciascuno per l'ampiezza data
- al denominatore al posto di $a(s)p(s)+(s)q(s)$ viene $(s+1)^{3}$ perché l'ho progettato/calcolato prima - in questo modo evito di ricalcolarlo (cfr. con l'altro controllore per capire per capire meglio)
#### CALCOLI CON IL PRIMO CONTROLLORE
![[Pasted image 20220616170039.png]]
Cerco i guadagni in continua a ciclo chiuso e poi scrivo il regime permanente sostituendo i valori trovati. Infine calcolo l'errore al regime (sottraendo al riferimento il valore del regime permanente):
![[Pasted image 20220616170225.png]]
- **Nota:** abbiamo un errore grande a causa del disturbo ma anche per il fatto che il controllore non garantisce un inseguimento perfetto (guadagno in continua non unitario, fa $-2$. Per risolvere questo problema, dovremmo inserire un apposito prefiltro - ma per ipotesi non c'è, $H_{f}=1$)

#### CONTROLLORE INTEGRALE
Facciamo la stessa procedura anche per l'altro controllore, cioè quello integrale (cambia $K(s)$)
- Anche in questo caso al denominatore sappiamo già che viene il polinomio dei poli in ciclo chiuso che abbiamo costruito/assegnato - ed eguagliato a $(s-1)^{4}$
- infine (dopo) si trova il regime permanente
![[Pasted image 20220616171238.png]]
- Abbiamo ottenuto un guadagno in continua tra riferimento e uscita unitario e la reiezione del disturbo in zero (me lo potevo aspettare perché ho progettato un controllore con azione integrale)
	- notiamo anche che l'errore in uscita è nullo 
		- cioè si converge al regime permanente anche se abbiamo un disturbo (questo perché esso è costante e il guadagno in continua è zero)
			- Se il disturbo fosse stato sinusoidale, non potevo calcolare l'effetto con il guadagno in continua tra disturbo e uscita costante (minore frequenza, minore effetto). Dovevo vederlo con la risposta in frequenza (che in generale sarà zero)


# ESAME (STRUTTURA)
- Prima parte di esercizi (domande sulla parte di analisi e progettazione sistemi di controllo -  retroazione su stato e uscita, algebrica e dinamica, osservatore, etc.. )
- Parte orale (approfondimento) - tutto il corso (modellistica in poi)

- I sistemi possono essere dati in varie forse (equazioni di stato, ingresso/uscita, funzione di trasferimento, linearizzazione sistemi non lineari)
