## DOMANDE TIPICHE

### RETROAZIONE SULLO STATO
-  $\varphi_{c}(s)$ al variare di $\alpha$
	- m.c.m. denominatori di $(sI-A)^{-1}B$ e valori di $\alpha$ che causano semplificazioni
- $X_{r}$ per certi valori di $\alpha$
	- $\mathbb{R}^n$ se completamente controllabile, altrimenti $\mathcal{R}$ e quindi $\text{Im}\{R\}$
- $\alpha$ per cui esiste legge di controllo tale da rendere il sistema asintoticamente stabile
	- autovalori non controllabili asintoticamente stabili
- $\alpha$ per cui esiste legge di controllo tale da posizionare gli autovalori in $\lambda_{i}^{*}$
	- se tutti i $\lambda_{i}^{*} \neq \text{autovalori sistema}$ si può fare se completamente controllabile
- Dato $\alpha$ fare legge di controllo per garantire stabilità asintotica in ciclo chiuso e inseguimento perfetto di $y^\text{o}$ costante
	- $A^{*}$, $\varphi^{*}(s) \text{ avente poli con Re}<0 \to$ $f_{i}$ adatti e relativi autovalori $\lambda_{i}^{*}$ 
	- Inseguimento perfetto: $G^{*}_{y^\text{o}y}(0)=\frac{r(0)}{\varphi^{*}(0)}H=1$ da cui si individua $H$
- Risposta forzata (transitorio e permanente) per riferimento a gradino dato
	- $Y_{f}(s)=G^{*}_{y^\text{o}y}(s)\underbrace{Y^\text{o}(s)}_{\text{ingresso}}$ $\to$ se poli distinti $\Rightarrow$ $Y_{f}(s)=\underbrace{\frac{K_{i}}{s-p_{i}}}_{\text{transitorio}}+\underbrace{\frac{\tilde K_{i}}{s-p_{i}}}_{\text{permanente}}$ 
		- Permanente: teorema risposta in frequenza
		- Transitorio: teorema residui su $Y_{f}(s)$ e antitrasformata per avere nel tempo
---
