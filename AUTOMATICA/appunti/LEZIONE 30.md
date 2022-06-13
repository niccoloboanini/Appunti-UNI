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
