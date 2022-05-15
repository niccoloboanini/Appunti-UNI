### ESERCIZI (cfr. slides)
#### 1) segnale gaussiano (già AFFETTO DA RUMORE)
Si vuole quantizzare il segnale
$$
x(t) + r(t), \quad \quad r(t) = \text{rumore additivo}
$$
Ipotesi $SNR$:
$$
SNR_{\text{ingresso}}=SNR_i = 30dB
$$
Dove:
$$
SNR_i = 30dB = \frac{E[x^2(t)]}{[r^2(t)]}\overbrace{=}^{WSS}P_{x}/R_{r}=\frac{E[x^2[t]]}{E[r^2[t]]}
$$
>>Stesso rapporto tra dominio tempo continuo e dominio tempo discreto

I grafici generali relativi alla densità spettrale sono così rappresentabili:
![[Pasted image 20220515153804.png|350]]

Si utilizza poi un filtro (in blu) per limitare effettivamente la banda (perché idealmente i segnali hanno tutti banda infinita). Esso viene detto *filtro di anti-aliasing* (ideale):
![[Pasted image 20220515153926.png|400]]
>> cfr: "rapporto segnale rumore in ingresso nella banda di interesse" (vuol dire quanto detto sopra)


> [!faq] Ci si chiede quando vale $SNR_{out}$, supponendo $B = 9$ (bit quantizzatore) 
> Ovvero: 
> ![[Pasted image 20220515154443.png|300]]

Può capitare che (è per questi casi che facciamo l'esercizio) $SNR_{out} \neq SNR_{out}$, perché abbiamo due componenti che introducono rumore:
- Uno dovuto a $r[t]$
- Uno dovuto *all'errore di quantizzazione* $e[n]$ dovuto al quantizzatore stesso

Pertanto in uscita avremo i campioni di segnale "utile", cioè $x[n]$ e ognuno di esso è affetto dal campionamento del segnale $r[t]$ e l'errore di quantizzazione $e[n]$
Quindi, ricordando che sarà il quantizzatore ad aggiungere (ulteriore) rumore:
$$
x(t)+r(t)\overbrace{\longrightarrow}^{\text{campionamento}} x[n]+r[n] \overbrace{\longrightarrow}^{\text{quantizzatore}} \underbrace{x[n]+\overbrace{r[n]+e[n]}}^{\quad \quad\text{da rimuovere}}_{\text{uscita}}
$$
Pertanto:
$$
\boxed{SNR_{out}=\frac{P_{x}}{P_{r}+P_e}}
$$
- Nota: le potenze si sommano perché la somma delle potenze è uguale alla potenza della somma, perché l'errore di quantizzazione è *incorrelato* col segnale d'ingresso per ipotesi. DIM (05/04 - h1, m.59):
-  ![[Pasted image 20220515160522.png|300]]

Supponendo (come faremo sempre) $D_{s}=(-1,1)$, dobbiamo all'occorrenza inserire un *guadagno* in ingresso al quantizzatore stesso per adattare la dinamica, che nelle nostre ipotesi sarà pari a $G=1/4\sigma x$:
![[Pasted image 20220515163157.png|400]]
Dove:
- $x'(t)$ e $r'(t)$ sono i segnali dopo il guadagno
- $x'[n]$, $r'[n]$,$e[n]$ sono i segnali sopo la quantizzazione 
![[Pasted image 20220515163456.png|500]]

Ci chiediamo ora se $SNR$ è variato dopo il guadagno, ovvero: $SNR' \neq SNR \ ?$
$$
SNR'=\frac{E[(x'(t))^2]}{E[r'(t)^2]}=\frac{E[(G\cdot x(t))^{2}]}{E[(G\cdot r(t))^{2}]} \underbrace{=}_{G\text{ costante}} = \frac{\cancel G^2 \ E[x^2(t)]}{\cancel G^2 \ E[r^2(t)]}
$$
- E come si nota quindi, il guadagno $G$ (utilizzando un amplificatore ideale) non altera $SNR$ , pertanto:
$$
SNR = SNR' \quad \quad \text{utilizzando un filtro ideale}
$$

Calcoliamo ora per comodità anche la potenza del segnale $x'$, quindi dopo il guadagno (nelle stesse ipotesi):
$$
P_{x'} = E[x'(t)^{2}] = E[ G^2 \ x^2(t) ] = E\left[\left(\frac{1}{4\sigma x}\right)^2 \cdot x^2(t)\right] = \frac{1}{16\sigma x^2} \cdot E[\underbrace{x^2(t)}_{\sigma x^2}] = \frac{1}{16} 
$$

*Andiamo adesso a calcolare $SNR_{out}$* (nota: il segnale è già stato quantizzato quindi si utilizza $x'$):
$$
SNR_{out} = \frac{Px'}{Pr' + P_{e}}, \quad \quad P_{e}=\frac{\Delta^2}{12} = \frac{(\frac{2}{2B})^2}{12} = \frac{4 \cdot 2^{-2B}}{12} = \frac{2^{-2B}}{3}
$$

Pertanto (per comodità si calcola l'inverso):
$$
\frac{1}{SNR_{out}}= \frac{P_{r'}+P_e}{P_{x'}} = \frac{P_{r'}}{P_{x'}} + \frac{P_e}{P_{x'}} = \frac{1}{\underbrace{SNR_{i}}_{30dB \rightarrow 10^3}} + \frac{\overbrace{P_e}^{2^{-2B}/{3}}}{\underbrace{P_{x'}}}_{1/16} $$
Quindi (ricordando che $B = 9$):
$$
SNR_{out} = 29.91 dB \quad \quad \text{(in lineare: } 980.03 \text{)} 
$$
