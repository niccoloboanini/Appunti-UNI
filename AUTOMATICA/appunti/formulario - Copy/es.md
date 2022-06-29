### RETROAZIONE USCITA (ALGEBRICA)
$\text{a) }\quad \varphi(s),G(s) \text{ al variare di } \alpha$
	$\varphi(s)=\underbrace{(s-\lambda_{1})(s-\lambda_{2}),\dots,(s-\lambda_{n})}_{\det(sI-A) \ \& \ \text{scomposizione}} \ \to  G(s)=\frac{1}{\varphi(s)}C \text{Adj}(sI-A)B+D = \frac{a(s)}{b(s)}=\frac{\alpha[\dots]}{a(s)}\to \alpha \text{ che semplifica } \longleftrightarrow \lambda_{i} \text{ nascosto}$
$\text{b) }\text{Ben posto} \iff \text{TUTTI autovalori con Re}\geq 0 \text{ compaiono come poli di }G(s)$
$\text{c) }\alpha=x \to \text{è ben posto?} \to (sì) \to \begin{gather}a(s)=\dots \\ b(s)=\dots \end{gather} \to G(s) \to \varphi^{*}(s)=a(s)+Kb(s) \to \text{stabilità ciclo chiuso} \longleftrightarrow \underbrace{\text{TUTTI poli con Re}<0}_{\text{A occhio || Routh}}$
$\text{d) }\underbrace{K=x}_{\text{stabile}} \to G^{*}_{y^{\text{o}}y}(s)=\frac{G(s)}{1+KG(s)}H=\frac{b(s)}{a(s)+K b(s)}H\to \text{inseguimento perfetto: }G^{*}_{y^{\text{o}}y}(0)=1 \text{ per qualche }H \text{ (se possibile)}$
---
### RETROAZIONE USCITA (SCHEMA)

$\boxed{\text{Dati }K(s) \text{ e } G(s)}$

 $K(s)=K_{P} \quad \text{ (retroazione statica)}$ 
> $\text{a)} \quad \varphi^{*}(s) \to G(s)=\frac{b(s)}{a(s)},K(s)=\frac{q(s)}{p(s)}\to \varphi^{*}(s)=a(s)p(s)+b(s)q(s)$
> $\quad G^{*}_{y^{\text{o}}y}(s)=\frac{b(s)q(s)}{a(s)p(s)+b(s)q(s)} \quad G^{*}_{dy}(s)=\frac{b(s)p(s)}{a(s)p(s)+b(s)q(s)}$
> $\text{b)} \quad \text{instabilita' } \forall K_{P} \text{: } \varphi^{*}(s) \text{ con qualche radice con Re}\geq 0 \text{ (cfr. cond. necessaria/Cartesio/Routh)}$

$\text{Retroazione dinamica con certa } K(s)$
> $\text{c) } \quad \text{individua: } q(s),p(s) \text{ in } K(s)=\frac{q(s)}{p(s)} \quad \text{e} \quad b(s),a(s) \text{ in } G(s)=\frac{b(s)}{a(s)}$
> $\quad \quad  \varphi^{*}(s), G^{*}_{y^{\text{o}}y}(s), G^{*}_{dy}(s)\quad\to \text{ cfr. a)}$
> $\text{d)}\quad \text{stabilità } \varphi^{*}(s) \text{ variando } K \quad \to \text{tutte radici con Re}<0 \to \text{(Cartesio,Routh,etc..)}$
> $\quad \quad \quad \text{Nota: se } \exists \lambda_{i} \text{ non dipendenti da }K \to \text{ devono avere Re}<0 \text{ (già stabili)}$
> $\quad \quad \quad \text{Risultato: }K=\dots$
> $\text{e)} \quad \text{K (da scegliere) per stabilità e } y^{\text{o}}(t),d(t) \text{ a gradino} \to ? \text{ RP uscita ed errore inseguimento}$
> $\quad \quad Y(s)=G^{*}_{y^{\text{o}}y}(s)Y^{\text{o}}(s)+G^{*}_{dy}(s)D(s)\stackrel{\text{teo fond.}}{\longleftrightarrow} y_{f}^{Y^{\text{o}}}+y_{f}^{D}(t)=G^{*}_{y^{\text{o}}y}(0)y^{\text{o}}(t)+G^{*}_{dy}(0)d(t)$
> $\quad \quad \text{errore inseguimento: } y_{f}^{Y^{\text{o}}}+y_{f}^{D}(t)-y^{\text{o}}(t) \quad \text{(nullo se }\exists \text{ azione integrale)}$

---
$\boxed{\mathcal{P} \text{ in rappr. ingresso-uscita e legge controllo }u(t) \text{ con azione integrale}}$

$\text{a) } \quad \text{funzione trasf. controllore}$
$\quad \quad \quad u(t) \stackrel{\mathcal{L}}{\to}U(s) \text{ ricordando che: } K_{P}[\dots] \to K_{P}[\dots] \text{ \& } K_{I}\int_{0}^{t} [\dots] \to \frac{K_{I}}{s}[\dots]$
$\quad \quad \quad K(s)=U(s) \text{ senza }[\dots]=\frac{q(s)}{p(s)}$
$\text{b) } \quad \mathcal{P} \to \text{forma standard: } \ddot y=\alpha_{1}\dot y+\alpha_{0}y+\beta_{2}\ddot u+\beta_{1}\dot u+\beta_{0}u$
$\quad \quad \quad \varphi(s)=s^{2}-\alpha_{1}s-\alpha_{0} \quad \text{ (da fattorizzare)}$
$\displaystyle \quad \quad \quad G(s)=\frac{b(s)}{a(s)} =\frac{\beta_{2}s^{2}+\beta_{1}s+\beta_{0}}{s^{2}-\alpha_{1}s-\alpha_{0}} \quad \quad \to \text{individua: } b(s),a(s),\underbrace{\varphi_{h}(s)}_{\text{controlla stabilità}}$
$\quad \quad  \quad \varphi^{*}(s), G^{*}_{y^{\text{o}}y}(s), G^{*}_{dy}(s)\quad\to \text{ cfr. a es. prec.)}$
$\text{c) } \quad \text{stabilità asintotica variando } K_{P}, K_{I}$
$\quad \quad \quad \varphi_{h}(s) \text{ stabile?} \Rightarrow a^{*}(s)=a(s)p(s)+b(s)q(s) \text{ con tutte radici con Re}<0$
$\text{e)} \quad K_{P},K_{I}\text{ (da scegliere) per stabilità e } y^{\text{o}}(t),d(t) \text{ a gradino} \to ? \text{ RP uscita ed errore inseguimento}$
$\quad \quad \quad \text{cfr. e) es. prec.}$

---
### RETROAZIONE - PROGETTO CON CONTROLLORE
$\text{a)} \quad \text{ben posto:}$
- $\varphi(s) \text{ per trovare tutti gli autovalori}$
- $G(s)=C(sI-A)^{-1}B=C \frac{1}{\varphi(s)}Adj(sI-A)B$
- $\text{ben posto } \iff \text{ tutti } \lambda_{i} \text{ con Re }\geq 0 \text{ compaiono come poli di }G(s)$
	- $\text{discuto al variare di } \alpha$

$\text{b)} \quad \text{PROGETTO} \to \text{parametri: } F,H,L$
- $F \text{ t.c }A-BF \text{ asintoticamente stabile}$
	- $A-BF \quad \quad \to \text{ricorda: } \begin{bmatrix} b_{11} \\ b_{21} \end{bmatrix} \begin{bmatrix} f_{1} & f_{2} \end{bmatrix} = \begin{bmatrix} b_{11}\cdot f_{1} & b_{11}\cdot f_{2} \\ b_{21}\cdot f_{1} & b_{21} \cdot f_{2}  \end{bmatrix}$
	- $\text{calcola } \det(sI-A+BF)$
		- $\text{scegli }f_{1},f_{2} \text{ adatti per stabilità asintotica}$
		-  $\text{riscrivi } \det(sI-A+BF) \text{ con i nuovi } f_{1},f_{2} \text{ e razionalizza}$  
- $H \text{ t.c. } G^{*}_{y^{\text{o}}y}(0)=1$
	- $\text{ trova } G^{*}_{y^{\text{o}}y}(s)=C(sI-A+BF)^{-1}=\frac{1}{\det(sI-A+BF)}C \ \text{Adj}(sI-A+BF)\cdot BH \text{ , lasciando H incognito}$
	- $\text{ricava }H \text{ da } G^{*}_{y^{\text{o}}y}(0)=1 \text{ (inseguimento perfetto)}$
- $L \text{ t.c }A-LC \text{ asintoticamente stabile}$
	- $A-LC \quad \quad \to \text{ricorda: } \begin{bmatrix} \ell_{1} \\ \ell_{2} \end{bmatrix} \begin{bmatrix} c_{11} & c_{12} \end{bmatrix} = \begin{bmatrix} \ell_{1}\cdot c_{11} & \ell_{1}\cdot c_{12} \\ \ell_{2}\cdot c_{11} & \ell_{2} \cdot c_{12}  \end{bmatrix}$
	- $\text{calcola } \det(sI-A+LC)$
		- $\text{scegli }\ell_{1},\ell_{2} \text{ adatti per stabilità asintotica}$
		- $\text{riscrivi } \det(sI-A+LC) \text{ con i nuovi } \ell_{1},\ell_{2} \text{ e razionalizza}$
- $\text{esplicita } \varphi^{*}(s)=\det(sI-A+BF)\det(sI-A+LC) \text{ coi polinomi trovati}$





