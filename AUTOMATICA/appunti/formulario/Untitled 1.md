> $\displaystyle \underline{\text{Tempo}} \quad u(t)=\underbrace{K_{P}\bigg [y^{\text{o}}-y(t) \bigg]}_{\text{Retroazione Algebrica}} + \underbrace{K_{I} \int_{0}^{t} \bigg[ y^{\text{o}}(\tau)-y(\tau) \bigg] \,d\tau}_{\text{Anticipare il trend}} + \underbrace{K_{D} \frac{d}{dt}\bigg[y^{\text{o}}(t)-y(t)\bigg]}_{\text{Inseg. perfetto (no prefiltro, }H_{f}=1 \text{)}}  \quad , \quad \stackrel{\large \text{Parametri}}{\text{Progetto}} \begin{cases} K_{P} \\ K_{I} \\ K_{D} \end{cases}$
> $\displaystyle \underline{\text{Laplace}} \quad U(s)=\underbrace{\bigg(K_{P}+\frac{K_{I}}{s}+K_{D}\ s\bigg)}_{K(s)}\big[Y^{\text{o}}-Y(s)\big]  \quad \implies \begin{gather}\quad K(s)=\frac{K_{D}s^{2}+K_{P}\ s + K_{I}}{s} \quad \overbrace{\text{(PID ideale)}}^{\text{f. impropria}}\\ \quad K(s)=\frac{K_{D}s^{2}+K_{P}\ s + K_{I}}{s(1+s \tau)} \quad \underbrace{\text{(PID reale)}}_{\text{f. propria}}\end{gather}$

> $\underline{\text{Azione integrale:}} \quad K(s)\text{ ha almeno un polo in 0 } \implies p(0)=0$


>$\underline{\text{Funzioni trasferimento ciclo chiuso}} \quad$
>	$\displaystyle \text{riferimento-uscita}: \quad G^{*}_{y^\text{o}y}(s)=\frac{K(s)G(s)}{1+K(s)G(s)}=\frac{b(s)q(s)}{a(s)p(s)+b(s)q(s)}$
>	
>	$\displaystyle \text{disturbo-uscita}: \quad G^{*}_{y^\text{o}y}(s)=\frac{G(s)}{1+K(s)G(s)}=\frac{b(s)p(s)}{a(s)p(s)+b(s)q(s)}$


