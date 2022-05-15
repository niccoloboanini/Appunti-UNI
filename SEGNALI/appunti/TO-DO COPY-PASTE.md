#### segnale gaussiano
Un segnale è gaussiano se è un *processo aleatorio* (quindi $x(nT) \text{ sono v.a.}$ distribuite come una gaussiana). Supponiamo anche che abbia media nulla e varianza pari a $\sigma^{2}x$, quindi:
$$
x(t) \rightarrow x(nT) \text{ sono v.a. e } \sim N(0, \sigma^2_{x}) 
$$
In generale quindi un campione ha una distribuzione di probabilità così rappresentata:
![[Pasted image 20220515150833.png|400]]
- Ha una dinamica in teoria compresa nell'intervallo $(-\infty, \infty)$, ovvero illimitata: tuttavia nella pratica *si assume di poter limitare tale intervallo a $[-A,A]$*, infatti oltre tali valori la $pdf$ assume valori trascurabili per l'analisi.
	- Ci si chiede quindi: **come scegliere A**

Per scegliere il valore giusto da scegliere per $A$, bisogna utilizzare delle formule per calcolare la probabilità che un campione con distribuzione gaussiana sia in valore assoluto maggiore di un certo numero di volte ($k$) la deviazione standard, ovvero:
$$
Prob\{|x| > k \cdot \sigma x\}
$$
- La probabilità al crescere di $k$ ovviamente diminuisce;
- Quello che è importante adesso quindi è trovare un valore di $k$ adatto, anche se ovviamente non esiste un valore in assoluto perfetto (dipende dall'esperimento)
- Tutti i valori fuori dall'intervallo confinato da $A$