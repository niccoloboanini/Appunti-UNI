### MATRICE DI RAGGIUNGIBILITA' (finita)
Mettiamo insieme tutti i vettori si costruisce come detto la *matrice di raggiungibilità*, così definita:
$$
\mathcal{R} = [B | AB|\cdots|A^{n-1}B]
$$
Immagine di una matrice: lo span delle sue colonne, ovvero i vettori generati combinando linearmente le colonne della matrice
- Essa coincide proprio con $\mathcal{R}$ insieme degli spazi raggiungibili
	- Per capire gli stati raggiungibili quindi basta costruire $\mathcal{R}$ e trovare l'immagine
In altre parole: $$ X_{r} = \text{immagine di } \mathcal{R} $$
![[Pasted image 20220612175710.png|500]]

**Nota:** il tempo $t^{\text{o}}$ non compare, il che significa che dal momento che uno stato è raggiungibile, si può giungere a esso in un qualsiasi tempo (corto, lungo) a seconda dell'ingresso per il controllo


### ESEMPIO: sistema non completamente raggiungibile/controllabile
- Abbiamo un sistema di ordine $n=2$ quindi mi fermo dopo due termini
- Comodo perché scrivo la matrice senza passare dalle equazioni di stato (come avevamo già fatto con questo sistema)
![[Pasted image 20220612180812.png]]
Abbiamo semplicemente:
- Costruito la matrice di raggiungibilità
- Calcolato e osservato la relativa immagine
- Concluso sugli stati raggiungibili

### COMPLETA RAGGIUNGIBILITA'
Per sistemi SISO abbiamo $n$ vettore di dimensione $n$, quindi viene una matrice di raggiungibilità quadrata e di dimensione $n \times n$

- Tutti gli stati devono essere raggiungibili per avere un sistema completamente raggiungibile, quindi quando il rango della matrice di raggiungibilità vale $n$
![[Pasted image 20220612181109.png]]
- Cioè quando ha rango massimo
	- Combinando opportunamente le colonne posso raggiungere tutti gli stati
	- Il rango lo vedo guardando le colonne linearmente indipendenti di $\mathcal{R}$
		**- L'insieme degli stati raggiungibili è un sottospazio lineare dello spazio di stato che ha una dimensione pari al rango della matrice di raggiungibilità $\mathcal{R}$**
			- Se il rango ha dimensione $n$ allora è completamente raggiungibile perché i due spazi di riferimento sono equi dimensionali
				- Altrimenti non è completamente raggiungibile
- Nell'esempio precedente avevamo:
$$
\mathcal{R} = \begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}
$$, che ha rango $1$, quindi non è completamente raggiungibile
- Il sottospazio in particolare avendo dimensione $\text{rank}(\mathcal{R})=1$ è una retta (se avesse avuto dimensione $2$ sarebbe stato un piano e così via)
![[Pasted image 20220612181628.png|200]]

**Nota:** *per sistemi SISO*, 
$$
\text{rank}(\mathcal{R})=n \iff \det(\mathcal{R})\neq 0
$$
- Quindi una volta che si costruisce $\mathcal{R}$ **basta guardare il determinante** per capire la raggiungibilità (invece di studiare l'immagine tramite tutte le definizioni date)

## RAGGIUNGIBILITA' E CONTROLLABILITA'
Sappiamo che un sistema generico può essere diviso in $\mathcal{S}_{c}$ e $\mathcal{S}_{\text{nc}}$
- dove possiamo assegnare lo stato come vogliamo solo per $\mathcal{S}_{c}$ perché è l'unica parte che è influenzata dal controllo
	- $\mathcal{S}_{\text{nc}}$ invece evolve liberamente

Quindi dal punto di vista della raggiungibilità possiamo dire che una parte dello stato può essere gestita dalla raggiungibilità stesse a un'altra no
- Quindi raggiungibilità e controllabilità sono concetti legati tra loro

In particolare vale la relazione
$$
\large \boxed{\text{sistema completamente raggiungibile} \iff \text{sistema completamente controllabile}}
$$
- Controllabilità: ci chiediamo come possiamo modificare gli autovalori --> dominio $s$
- Raggiungibilità: ci chiediamo come possiamo modificare lo stato --> dominio dello spazio di stato (esempio: tempo)

Quindi tipo negli esercizi a volte conviene passare da una piuttosto che l'altra

---
Inoltre, sappiamo che:
$$
\varphi(s) = \varphi_{\text{c}}(s) \  \varphi_{\text{nc}}(s)
$$
Possiamo dire che:
- $\varphi_{\text{c}}(s)$ è un polinomio che contiene gli autovalori controllabili del sistema. Indichiamo con $n_{c}$ il numero di questi autovalori
	- Quindi $\varphi_{\text{c}}(s)$ è un polinomio di grado $n_{c}$

Allora, *il numero di autovalori controllabili $n_{c}$ coincide con la dimensione dello spazio degli stati raggiungibili $X_{r}$*, ovvero: $$ \text{rank}\{\mathcal{R}\}=\dim\{ X_{r} \} = n_{c} $$
- quindi guardando il rango della matrice di raggiungibilità si capisce il numero di autovalori controllabili del sistema

Possiamo estendere la precedente relazione:
$$
\boxed{\text{completamente raggiungibile} \iff \text{ completamente controllabile}\iff \text{rank}\{\mathcal{R}\}=n}
$$
- utile negli esercizi parametrici

### ESEMPIO: studio di controllabilità e stabilizzabilità al variare del parametro
- Dovrei calcolare il polinomio caratteristico e vedere quando ci sono semplificazioni
	- Dato che non è sempre facile vedere le semplificazioni, sfruttiamo le relazioni viste per semplificare: $$\text{completamente raggiungibile} \iff \text{ completamente controllabile}\iff \text{rank}\{\mathcal{R}\}=n $$
- Calcolo allora $\mathcal{R}$
- Guardo il rango [massimo] (ovvero il determinante [diverso da zero] se la matrice è quadrata)
- Trovo i valori per cui $\det \neq 0$, così da trovare i valori di $\alpha$ per la completa raggiungibilità e quindi completa controllabilità
	- Esplicito dimensione di $X_{r}$ e il fatto che $\varphi(s)=\varphi_{\text{c}}(s)$
- Guardo i comportamenti per valori particolari di $\alpha$ (ovvero quando non è garantita completa raggiungibilità)
	- Esplicito dimensione di $X_{r}$ (combinando linearmente le colonne)
	- Cerco di capire com'è grado di $\varphi_{\text{c}}(s)$, ovvero $n_{c}=\text{rank}\{\mathcal{R}\}$
		- E quindi quanti autovalori controllabili abbiamo
			- Per capire qual è questo autovalore devo calcolare $(sI-A)^{-1}B$
![[Pasted image 20220613160103.png|600]]
![[Pasted image 20220613160256.png|500]]

---
# RISPOSTA AL GRADINO

## INTRO
Sappiamo che per garantire la *specifica $3$* bisogna mantenere una transitorio rapido e con escursioni/oscillazioni limitate il più possibile
- Queste sono espresse in termini di risposta al gradino in ciclo chiuso, infatti abbiamo questa situazione:
![[Pasted image 20220613163601.png|200]]

Per ottimizzare al meglio il fenomeno, si deve studiare (dal punto di vista soprattutto algebrico) com'è fatta la risposta al gradino in ciclo chiuso, ovvero:
![[Pasted image 20220613163717.png|600]]

Dove:
$$
G_{y^{o}\ y}^{*}(s) = \frac{r(s)}{\varphi^{*}(s)}
$$
- $r(s)$ è un polinomio dato dipendente da $A,B,C$ e che quindi non si può modificare
- $H$ è un guadagno garantire la specifica$2$, quindi anch'esso non va toccato
- *Posso agire solo su $\varphi^{*}(s)$ per garantire alla risposta al gradino un comportamento desiderato nel transitorio*
		- in particolare i relativi zeri che poi diventano i poli di $G_{y^{o}\ y}^{*}(s)$

Ricordiamo
$$
\varphi^{*}(s) = \det(sI-A+BF)
$$
- Come si nota **dipende da $F$**, quindi dobbiamo scegliere un adeguato valore del guadagno in feedback per garantisce un transitorio come desideriamo (asintoticamente stabile e rapido)

### ESEMPIO: soddisfare la specifica nel transitorio
- Progettiamo l'intero progetto per soddisfare le $3$ specifiche ($u=-Fx+Hy^{o}$)

- Verifichiamo se posso farlo calcolando $\mathcal{R}$ e il relativo determinante per capire se è completamente raggiungibile e controllabile. Se questo è possibile mediante $F$ possiamo assegnare tutti gli autovalori come vogliamo
- Calcolo $\varphi^{*}(s)$
	- Quindi devo trovare $A^{*}$
	- Si nota se abbiamo fatto i conti giusti che il polinomio finale dipende dai parametri $f_{i}$, quindi possiamo agire sui relativi autovalori
- Calcolo $G_{y^{o}\ y}^{*}(s)$ per poi garantirli una forma desiderata
	- In particolare devo calcolare $r(s)$
![[Pasted image 20220613165637.png|600]]
- Fattorizzo se possibile
- Il numeratore a differenza del denominatore non si può scegliere come si vuole, però se riesco a fattorizzare il denominatore in modo adeguato, magari riesco a fare una semplificazione tra numeratore e denominatore per rendere poi lo studio più leggero
	- Per fare ciò, fattorizzo il denominatore per garantire semplificazioni (tanto gli $f_{i}$ li posso scegliere)
		- In particolare, dato che il polinomio è personalizzabile, scelgo autonomamente le radici (una di queste mi permette la semplificazione), assegnando un valore che voglio a $a_{0}^{*}$ (in questo esempio $10$) --> si fa tanti fattori quanto è il grado del denominatore (in questo caso due)
			- Se facciamo il prodotto, si evince quanto valgono $f_{i}$
- Riscrivo $G_{y^{o}\ y}^{*}(s)$ ora semplificata
- Rimane solo il termine $H$ che lo scelgo appositamente per avere un guadagno in continua unitario (specifica $2$: $G_{y^{o}\ y}^{*}(0)=1$)
![[Pasted image 20220613170726.png|650]]

Abbiamo inoltre anche la risposta forzata in ciclo chiuso
- Facendo la scomposizione in fratti semplici e la antitrasformata per tornare nel dominio del tempo (e capire l'evoluzione nel tempo)
	- Posso poi individuare il regime permanente e il transitorio (osservando a cosa sono associati i poli)
- Grafico (osservando che il regime permanente coincide col gradino e il transitorio ha un andamento come desiderato)
![[Pasted image 20220613171212.png|600]]


### CASO POSITIVO (come nell'esercizio)
Transitorio esponenziale che evolve secondo una costante di tempo $a^{*}_{0}$ relativa al polo di $G_{y^{o}\ y}^{*}(s)$ che abbiamo scelto/ottenuto
- In particolare la durata di tempo del transitorio è $\tau=1/(a^{*}_{0})$
![[Pasted image 20220613171723.png|600]]
![[Pasted image 20220613171743.png|500]]

Quindi il polo di $G_{y^{o}\ y}^{*}(s)$ denominato $a^{*}_{0}$ determina la velocità di convergenza del transitorio a $0$ 
- Quindi tale velocità posso sceglierla a seconda delle esigenze del *tempo di assestamento* (ovvero un intorno del valore di regime - perché l'assestamento è asintotico)
	- L'intorno può essere espresso ad esempio in percentuale 
![[Pasted image 20220613172215.png]]
Formalmente:
![[Pasted image 20220613172236.png]]

La formula per capire il tempo è il seguente:
![[Pasted image 20220613172359.png]]
![[Pasted image 20220613172527.png]]
- tanto più portiamo a sinistra il polo $a^{*}_{0}$ tanto più l'esponenziale è rapida e quindi tanto meno è il tempo per arrivare a regime
	- $\large \upvarepsilon$ è una specifica in percentuale data dal problema
	- viene dato anche il tempo di assestamento
	- Risolvendo l'equazione $T_{a,\large \upvarepsilon}$ quindi si ricava facilmente anche $a_{0}^{*}$
