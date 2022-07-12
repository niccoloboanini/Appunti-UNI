### STRUTTURE T-S-T
Struttura non omogenea: si vuole unire le funzioni di cambio di linea e cambio di canale, auspicando sempre ad avere una struttura non bloccante e costo più basso possibile
- Con le strutture bistadio $\text{T-S}$ si ottenevano le funzionalità richieste ma non si garantiva la non bloccanza

Si compone in questo modo:
![[Pasted image 20220712181938.png|400]]

Ingressi:
- $N$ gruppi (blocchi)
- $n$ linee in ingresso a ogni blocco $\text{T}$
- $k$ linee di uscita a ogni blocco $\text{T}$, $k>>n$

Uscite (simmetrico):
- $N$ gruppi (blocchi)
- $k$ linee in ingresso a ogni blocco $\text{T}$
- $n$ linee di uscita a ogni blocco $\text{T}$


>L'idea sarà quella di trovare $k$ il più piccolo possibile che ci consente di ottenere costo minimo e avere una struttura non bloccante. Si ricorda $k>>n$


> [!example] Arriviamoci con un esempio:

$$
\begin{gather}
\text{Canale } 7 \text{ linea } 1 \longrightarrow \text{ Canale } 10 \text{ linea } 3 \\
\text{Canale } 12 \text{ linea } 1 \longrightarrow \text{Canale } 10 \text{ linea } 7
\end{gather}
$$
*Nota:* Con una $\text{T-S}$ non si riusciva a fare (potevo esaudire solo una richiesta, perché si poteva veicolare una sola richiesta verso lo stesso canale (il $10$ in questo caso) di arrivo)
$$
\text{Canale } 7 \text{ linea } 1 \stackrel{\text{T}}{\longrightarrow } \text{ Canale } 10 \text{ linea } 1 \stackrel{\text{S}}{\longrightarrow } \text{ Canale } 10 \text{ linea } 3 \stackrel{\text{T}}{\longrightarrow } \text{ Canale } 10 \text{ linea } 3 
$$
  abbiamo soddisfatto la prima richiesta (l'ultima struttura $\text{T}$ ha lasciato tutto inalterato perché avevo già raggiunto il risultato)

Per la seconda, si nota che il canale $10$ è già occupato dalla precedente, quindi l'unica è "parcheggiare" temporaneamente la richiesta su un canale libero (ad esempio il $20$ in questo caso, con il primo $\text{T}$), successivamente cambiare linea con l'$\text{S}$ e infine finalmente cambiare il canale con il desiderato grazie all'ultimo $\text{T}$:
$$
\text{Canale } 12 \text{ linea } 1 \stackrel{\text{T}}{\longrightarrow } \text{ Canale } 20 \text{ linea } 1 \stackrel{\text{S}}{\longrightarrow } \text{ Canale } 20 \text{ linea } 7 \stackrel{\text{T}}{\longrightarrow } \text{ Canale } 10 \text{ linea } 7 
$$
---
#### FORMULA DI CLOS STRUTTURE T-S-T
Cerchiamo un $k$ che mantenga la struttura non bloccante e che permetta altresì di limitare i costi.
È espresso ancora dalla medesima analisi di Clos, che infatti porta al risultato: $$\boxed{k=2n-1}$$
Dobbiamo però *adattare le ipotesi di lavoro* al nuovo contesto:
- Nella $\text{S-S-S}$ avevamo solo lo spazio
- Nella $\text{T-S-T}$ abbiamo un contesto misto tempo & spazio

##### worst case analysis
Per capire le ipotesi, consideriamo la trama (insieme di linee) di uscita dei primi blocchi $\text{T}$ che costituisce l'ingresso dei blocchi $\text{T}$ del terzo stadio
- Essa ha $k$ posizioni
![[Pasted image 20220712190257.png|300]]
Le ipotesi sono (prime due analoghe al caso $\text{S-S-S}$):
- Si vuole connettere l'unico canale libero di un ingresso all'unico canale libero su un'uscita (le altre $n-1$ linee si suppongono occupate $\text{X}$):
![[Pasted image 20220712190824.png|300]]
- Le uscite e gli ingressi non hanno elementi in comune (ovvero sono insiemi disgiunti: nessun ingresso di un blocco $i$ in ingresso lo ritroviamo tra le uscite del blocco $i$ di destinazione)
![[Pasted image 20220712190922.png|300]]
- Le linee di uscita occupate del primo blocco sono diverse dalle linee occupate in ingressi dai canali presenti nell'uscita considerata
![[Pasted image 20220712191125.png|350]]

Facendo i conti: $\overbrace{n-1}+\overbrace{n-1}+\overbrace{1}=2n-1$, che corrisponde al valore minimo di $k$ e alla Formula di Clos

😃: Abbiamo aumentato le funzionalità rendendo i costi minimi (Clos)

---

## ANALISI DI LEE
>La consideriamo solo per casi $\text{S-S-S}$ ma si può generalizzare anche per le altre

Assume l'eventualità di blocco come *evento aleatorio*
- Si cerca cioè ci capire con che **probabilità** una richiesta genera un blocco della struttura (analisi statistica, non più deterministica)

**Idea**: si accetta un minimo di tolleranza per il bloccaggio rispetto all'analisi di Clos ma si vuole comunque rendere tale evento raro
- L'analisi è conveniente se effettivamente abbiamo una riduzione del costo

### IPOTESI
Abbiamo le seguenti ipotesi:
- Struttura $\text{S-S-S}$
- Probabilità di avere una richiesta di connessione in ingresso fissata a priori
- Probabilità di selezione delle uscite fissata a priori

Consideriamo la seguente struttura (semplificata per questioni di ordine), in cui si considerano solo i collegamenti tra primo e secondo stadio e il collegamento verso il blocco voluto tra secondo e terzo stadio
![[Pasted image 20220712193909.png|300]]

### ANALISI
- Parametri $N$, $n$ e $k$ sono fissati
- Indichiamo con $a$ la probabilità di avere una richiesta in ingresso
	- Dato che le linee d'ingresso sono $n$, allora la probabilità di avere un ingresso occupato è $\displaystyle n \cdot a$
	- La probabilità che la richiesta in ingresso sia mandata su una certa linea di uscita tra le $k$ possibili la consideriamo uniforme, quindi $1/k$

Quindi, la *probabilità di avere una linea di uscita del primo stadio già occupata da un certo ingresso* è $$ \large p =\frac{n\cdot a}{k} $$
Dato che le uscite del primo stadio sono gli ingressi per il secondo stadio, le uscite occupate del primo stadio rendono anche i relativi ingressi del secondo stadio occupati
Esempio:
![[Pasted image 20220712201147.png|400]]
- La prima uscita del primo blocco del primo stadio è occupata, quindi il collegamento con il primo blocco del secondo stadio è indisponibile

