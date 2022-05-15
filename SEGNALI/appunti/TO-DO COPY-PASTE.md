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

