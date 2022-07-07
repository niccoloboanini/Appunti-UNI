### TIPI DI COMUNICAZIONE
Può essere:
- Duplex ($\Rightarrow$)
- Half-Duplex ($\Rightarrow$ or $\Leftarrow$)
- Full-Duplex ($\iff$)

### CARATTERISTICHE DI UNA RETE
- Prestazioni:  $\underbrace{\text{Throughput}}_{\text{trasmissione max (bit/s)}} + \quad \underbrace{\text{Delay}}_{\text{ritardo}}$
- Affidabilità
- Sicurezza

### MODALITA' DI COMUNICAZIONE
- Punto-Punto:  $\text{A} \to \text{B}$
- Multi-Punti (multicast): $\text{A} \to \underbrace{\text{B,C,D,...}}_{u+v}$
	- Broadcast: $u$ numero di destinatari $=$ $u+v$

## TOPOLOGIA

### FISICA
#### MESH: a maglia completa
- Punto-Punto per ogni dispositivo $i, \quad i=1,\dots,n \quad \quad n=\text{nodi}$ 
	- Duplex: $n(n-1)$ collegamenti
	- Full-Duplex: $\displaystyle \frac{n(n-1)}{2}\approx n^{2}$
![[Pasted image 20220707155305.png|150]]
😃: collegamenti esclusivi; resiliente a guasti
😡: collegamenti/porte I/O crescono come $n^{2}$; no multicast

#### STELLA
- Collegamento verso un *centro stella* (commutatore - dispositivo intelligente)
![[Pasted image 20220707161406.png|150]]
😃: meno collegamenti ($n$); sì multicast; buona resilienza a guasti
😡: nodi non direttamente collegati; se si guasta il centro stella, si blocca tutta la rete

#### BUS
- Come quello nelle architetture dei PC
 ![[Pasted image 20220707161735.png|180]]
😃: sia punto-punto che broadcast; facile da implementare
😡: se il bus si rompe, si blocca tutta la rete

#### ANELLO (RING)
