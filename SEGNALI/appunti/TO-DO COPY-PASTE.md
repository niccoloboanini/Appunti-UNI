### ESEMPI/ESERCIZI SNR
#### SEGNALE SINUSOIDALE
Sia $x(t)$ un segnale della forma:
$$
x(t) = A \ \cos (2\pi f_{0} \ t + \varphi)
$$
Essendo $A$ l'ampiezza del segnale, ne consegue che la relativa *dinamica* sia compresa nell'intervallo $[-A,A]$. Supponiamo la stessa anche per la dinamica del quantizzatore. Riassumendo:
$$
D_{s}= [-A,A] \quad \quad D = 2A
$$
Utilizzando la formula del $SNR$ (precedente) si ottiene:
$$
SNR = 6.02B + 10 \log_{10} \frac{12S}{D^{2}} = 6.02B + 10 \log_{10} \frac{12 \cdot \frac{\cancel{A^2}}{2}}{4\cancel{A^{2}}} = 6.02B + \underbrace{10 \log_{10}\frac{3}{2}}_{1.76}
$$
>> Quindi **nelle ipotesi sulla dinamica appena fatte**, se abbiamo un segnale **sinusoidale** vale la seguente formula: $$ \boxed{SNR = 6.02B + 1.76}$$



