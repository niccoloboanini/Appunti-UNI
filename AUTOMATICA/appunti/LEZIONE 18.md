## RISPOSTA IMPULSIVA
L'antitrasformata della funzione di trasferimento. Ovvero quest'ultima osservata nel dominio del tempo:
$$
\large \boxed{g(t) = \mathcal{L}^{-1}\{G(s)\}}
$$
Sfruttando la linearità dell'antitrasformata si arriva a dire che:
$$
{\large g(t)} = \mathcal{L}^{-1}\{C(SI-A)^{-1}B +D]\} = \large Ce^{At}B+D\delta(t)
$$

Chiamata risposta impulsiva perché equivale alla risposta forzata del sistema se prendiamo come ingresso un segnale impulsivo di Dirac, infatti:
$$
u(t) = \delta(t) \Rightarrow U(s) = \mathcal{L}^{-1}\{u(t)\} = 1 \implies Y_{f}(s) = G(s)U(s) = G(s) \longleftrightarrow  \large y_{f}(t) = g(t)
$$
![[Pasted image 20220607105414.png|300]]


