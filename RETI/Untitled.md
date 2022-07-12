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

Per le linee di uscita del secondo stadio il discorso è analogo: *la probabilità di avere una linea di uscita del secondo stadio da occupata da un certo ingresso è $p=a$*:
$$
p=\frac{n \cdot a}{k} \stackrel{n=k}{=} \frac{k \cdot a}{k}=a
$$
![[Pasted image 20220712213920.png|250]]
- stessa probabilità in formule anche per il passaggio dal secondo al terzo stadio

Allora, la probabilità di avere un **percorso libero** da un blocco del primo stadio verso un determinato blocco del terzo stadio sarà data dalla probabilità che *entrambi* le componenti del cammino (collegamenti 1° $\to$ 2° stadio e 2° $\to$ 3° stadio) siano liberi
Pertanto, dato che:
$$
\begin{gather}
p &=& \text{prob. collegamento occupato} \\
1-p&=& \text{prob collegamento libero}
\end{gather}
$$
Allora: 
$$
\begin{gather}
\text{prob}\{\text{cammino libero}\} &=& (1-p)^{2} \\
\text{prob}\{\text{cammino occupato}\} &=& 1-(1-p)^{2}
\end{gather}
$$
Dato che i cammini da un certo ingresso verso una determinata uscita sono in tutto $k$, si può estendere la formula trovando la probabilità di blocco della rete, ovvero la probabilità in cui risulta non possibile il collegamento tra un elemento del primo blocco con un elemento del terzo blocco:
$$
\large \boxed{\text{prob}\{ \text{blocco} \} = P_{B}= [1-(1-p)^{2}]^{k}}
$$
- in questo caso nessuno dei $k$ percorsi completi ingresso uscita è disponibile, quindi la struttura è bloccante

Abbiamo ottenuto la **formula di Lee**

😃: $P_{B}$ e $k$ sono indipendenti l'uno dall'altro quindi a seconda dei casi ci possiamo adeguare:
- se ci viene dato $P_{B}$ e tutte le ipotesi aggiuntive si può definire/ricavare $k$ (numero linee uscita blocchi primo stadio) in modo tale che il vincolo su $P_{B}$ sia rispettato
- se ci viene dato $k$ in relazione a un fattore di costo che vogliamo avere, si può verificare $P_{B}$ per capire come si comporta la relazione con tale costo (cioè se ha o meno una alta probabilità di blocco)

Facciamo un esempio:
- $n=120$
- $k=128$
- $a=128$

Allora:
$$
\text{CLOS: }k= 2n-1=2 \cdot 120 -1 =239
$$
Con probabilità di blocco:
$$
P_{B}=[1-(1-p)^{2}]^{k}=\left[1-\left(1- \frac{a \cdot n}{k}\right)\right]^{k}=10^{-7}
$$
(controlla i conti, anche il due all'esponente che a lezione non l'ha messo)
- Probabilità molto bassa
- Anche il costo è molto ridotto rispetto a quello di Clos, e ci siamo arrivati semplicemente "sacrificando" una piccola probabilità di bloccaggio (verifica quanto valgono i costi effettivamente)

> [!note] L'analisi di Lee non è una analisi esatta
> è cioè una analisi approssimata
> Verifichiamo: abbiamo ottenuto un valore certo di $P_{B}$, ovvero $10^{-7}$.
> Da Clos sappiamo che la probabilità di blocco nel caso in cui $k=2^{n}-1$ è $0$ per definizione. Se sostituiamo il valore di $k$ di Clos nella formula di Lee non troviamo tuttavia questo valore.
> Si verifica appunto sostituendo in quest'ultimo esempio $239$ nella formula finale

>La tecnologia attuale che porta ad avere reti sempre più veloci e impegnativi, di conseguenza anche i commutatori si sono evoluti. Le tecniche nuove si sono evolute nelle fast-packet-switching, con probabilità sempre più basse di bloccaggio


