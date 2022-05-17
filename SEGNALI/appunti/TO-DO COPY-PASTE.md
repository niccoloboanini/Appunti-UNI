### ESEMPIO
#inseriscifoto

## TEOREMI

### 1) LINEARITA'
(Dalla definizione)
### 2) RITARDO
Sia $x[n] \longleftrightarrow X(Z)$ 
Allora,
$$
\boxed{x[n-n_{0}] \longleftrightarrow z^{-n_0} \ X(Z)}
$$
**Dimostrazione:**
$$
Z\{ x[n-n_{0}] \} = \sum_{n=-\infty}^{\infty} x[n-n_{0}] \ z^{-n}\underbrace{=}_{m=n-n_{0}} \sum_{m=-\infty}^{\infty} x[m] \ z^{-m-n_0} = \sum_{m=-\infty}^{\infty} x[m] \ z^{-m} \cdot z^{-n_{0}}= z^{-{n_0}} \underbrace{\sum_{m=-\infty}^{\infty} x[m] \cdot z^{-m}}_{X(Z)} 
$$

Si può mostrare inoltre che la $ROC$ non varia:
$$
ROC_{x[n-n_0]} = ROC_{x[n]}
$$

### 3) PRODOTTO PER ESPONENZIALE
Sia $x[n] \longleftrightarrow X(Z)$, con $ROC = \{ z: r_1<|z|<r_{2} \}$ (forma generale, $r_1$ e $r_2$ arbitrari)

Allora ci chiediamo quanto vale la trasformata della stessa sequenza moltiplicata per un esponenziale:
$$
y[n] = a^{n}x[n]
$$
Si dimostra che:
$$
\boxed{a^nx[n] =y[n] \longleftrightarrow Y(Z) = X(a^{-1}z)}
$$
**Dimostrazione**
$$
Y(Z) = \sum_{n=-\infty}^{\infty} a^{n} x[n] z^{-n} = \underbrace{\sum_{n=-\infty}^{\infty} x[n](a^{-1}z)^{-n}}_{X(a^{-1}z)}
$$

Inoltre abbiamo convergenza se:
$$
r_{1}<|a^{-1}|<r_{2}
$$
Da cui quindi si giunge alla formula relativa a *come varia la regione di convergenza a seguito di una moltiplicazione per un esponenziale*:
$$
ROC_y = \{ |a|r_1<|z|<|a|r_2 \}
$$

### 4)
Sia $y[n] = x^*[n]$
Allora,
$$
\boxed{x^*[n]= y[n] \longleftrightarrow Y(Z) = \bigg(X(z^*)\bigg)^*}
$$
**Dimostrazione:**
$$
Y(Z) = \sum_{n=-\infty}^{\infty} x^{*[n]}z^{-n}=\left( \sum_{n=-\infty}^{\infty} x[n] (z^*)^{-n} \right)^* = \bigg(X(z^*)\bigg)^*
$$

Si può dimostrare anche che la $ROC$ rimane la stessa, ovvero:
$$
ROC_Y = ROC_X
$$