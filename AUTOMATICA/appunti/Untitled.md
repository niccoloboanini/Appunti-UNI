# SITEMI LINEARI
## FUNZIONI LINEARI
![[Pasted image 20220530124407.png|500]]
- si può cioè "portare fuori" dall'operatore i termini $+$ e $\alpha$

In generale quindi vale:
$$
J(\alpha_{1} \ x_{1}  + \alpha_{2} \ x_{2}) = \alpha_{1}J(x_{1}) + \alpha_{2} J (x_{2})
$$

- Vantaggio principale: *ogni funzione lineare può essere riscritta come matrice $m \times n$*, ovvero: $$ J(x) = M \ x $$

> [!example] Esempi di grafici lineari
> ![[Pasted image 20220531102600.png|400]]

$$
\begin{rcases}
(TC) \quad \dot x(t) \\ \\
(TD) \quad x(t+1) \quad
\end{rcases}
\ = f(x(t),u(t))  \quad , \quad y(t) = h(x(t),u(t))
$$
Un sistema TI di questo tipo è **lineare** se **$f$ e $h$ sono lineari** rispetto ai loro argomenti ($x$ e $u$), ovvero:
$$
\boxed{\begin{align*}
&f(x,u) = A\ x + B\ u  \quad \longleftrightarrow \text{associata alla eq. di stato}\\
&h(x,u) = C\ x + D\ u \quad \longleftrightarrow \text{associata all'uscita}
\end{align*}}
$$
Con $A,B,C,D$ di dimensioni opportune
- $A$ matrice quadrata, di dimensioni pari a quella dello stato. Ovvero $\dim(x) \times \dim(x)$
- $B$ esegue il passaggio da ingresso a stato, quindi $\dim(x) \times \dim(u)$
- $C$ esegue il passaggio da stato a uscita, quindi $\dim(y) \times \dim(x)$
- $D$ esegue il passaggio da ingresso a uscita, quindi $\dim(y) \times \dim(u)$

 >> Se consideriamo sistemi $SISO$, allora $\dim(u) = \dim(y) = 1$, quindi molte dimensioni delle matrici diventano vettori, verticali o orizzontali a seconda del caso.

- È utile studiare i sistemi lineari anche per capire il comportamento dei sistemi non lineari, perlomeno in una zona "locale"
-  Se le variazioni temporali sono lente, studieremo tali sistemi come TI (tempo invarianti).
	- In questi casi si parla di **sistemi $LTI$**.
	- Nei sistemi TV, le matrici dipendono e quindi variano nel  tempo, avremo in questi casi:
		- $f(t,x(t),u(t)) = A(t)x(t) + B(t) u(t)  \quad , \quad y(t) = h(t,x(t),u(t)) = C(t)x(t)+D(t)u(t)$
			- In cui appunto compare la $t$ del tempo

![[Pasted image 20220531104817.png|500]]


