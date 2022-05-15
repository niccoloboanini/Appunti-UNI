#### 2) progetto: calcolo bit necessari (segnale sinusoidale (con rumore))
Sia $x(t) + r(t)$ il segnale sinusoidale di partenza di riferimento (affetto da rumore).
- Supponiamo quindi $SNR_{i} = 10^3=30dB$

> [!faq] Determina $B \quad \text{t.c. } \Delta_{dB} = 0.1 dB$
> > Dove $\Delta_{dB}$ è la *degradazione* in $dB$ del segnale all'uscita, ovvero $$SNR_{in}-SNR{out} \leq 0.1dB$$
> > Pertanto deve valere: $$SNR_{out} \geq 29.9 dB$$

Ricordando che la dinamica per i segnali *sinusoidali* è pari a $(-A,A)$ e supponendo ancora una volta la dinamica del quantizzatore pari a $(-1,1)$, si ottiene il seguente schema riassuntivo:
![[Pasted image 20220515184634.png|500]]

Il **guadagno** (supponendo al solito di evitare i casi di overflow), sarà (per adattare l'ampiezza (dinamica) del segnale alla dinamica del quantizzatore):
$$
G = \frac{1}{A}
$$
Quindi:
$$
SNR_{out}=\frac{P_{x'}}{P_{r'}+P_e} 
$$
Come abbiamo fatto nell'esercizio precedente:
$$
\frac{1}{SNR_{out}} = \frac{P_{r'}+P_{e}}{P_{x'}} = \underbrace{\frac{P_{r'}}{P_{x'}}}_{1/SNR_i} + \frac{P_{e}}{P_{x'}}
$$
- Da cui, ricordando che $\displaystyle P_{e}= \frac{2^{-2B}}{3}$
- 