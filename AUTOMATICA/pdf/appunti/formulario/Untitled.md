$\displaystyle \lim_{t \to \infty} g(t)$ quando viene data $G(s)$
- Poli tutti con $\text{Re}<0$ e/o polo in $0$ con $m=1$ $\stackrel{TVF}{\Rightarrow}$ $\displaystyle \lim_{t \to \infty} g(t)=\lim_{t \to 0} s G(s)$
- Viene dato anche $u(t)$ $\Rightarrow$ $Y_{f}(s)=G(s)U(s)$
	- $\mathcal{L}\{u(t)\}$
	- Se $u(t)$ ha più addendi $\Rightarrow$ distributiva tra $G(s)$ e $U_{i}(s)$ e guardo poli di ogni addendo
		- Se ci sono poli che danno modi divergenti $\Rightarrow$ $y_f(t)$ diverge
		- Altrimenti faccio $\mathcal{L}^{-1}$ e vedo a quali residui $K_{i}$ tende

Modi naturali per sistemi ingresso uscita
- Vale $\varphi(s)=m(s)=s^{2}-\alpha_{1}s-\alpha_{0}$
- Esempio: $\ddot y = -2 \dot y - 5y + 3u \to$ $m(s)=s^{2}+2s+5 \to \lambda_{1,2}=-1\pm j \to \text{modi associati}$
	- Modi: $e^{\sigma_{1}t}\sin(\omega_{1}t) \ , \ e^{\sigma_{1}t}\cos(\omega_{1}t)$ con $\sigma_{1}=-1 \ , \ \omega_{1}=2$  

Ingressi limitati tali da far divergere la risposta forzata $y_{f}(t) \iff$ non esternamente stabile
- Dato sistema ingresso uscita: passo alla $G(s)$ (formula)
	- $\displaystyle \ddot y = \alpha_{1}\dot y+\alpha_{0}y+\beta_{2}\ddot u+\beta_{1}\dot u+\beta_{0}u \implies G(s)=\frac{\beta_{2}s^{2}+\beta_{1}s + \beta_{0}}{s^{2}-\alpha_{1}s -\alpha_0}$
	- Se esternamente stabile: non esistono modi adatti
		- Altrimenti esistono (si trovano con la risonanza)
				- Poli pur. immaginari: si prende $u(t)=\sin(\omega_{0}t)1(t)$ si fa $\mathcal{L}\{u(t)\} = U(s)$ e $Y_{f}(s)=G(s)U(S)$
				- Poli reali: si stimola con un ingresso avente lo stesso modo (e quindi stesso polo in $U(s)$)

Calcola punti di equilibrio e studia stabilità
- Monodimensionale
	- $\dot x=2-ux \to (x_{e},u_{e}) \text{equilibrio} \iff f(x_{e},u_{e})=0 \iff 2-u_{e}x_{e}=0$ 
		- $\displaystyle x_{e}=\frac{2}{u_{e}} \to u_{e}=0 \text{ no eq.} \quad u_{e} \neq 0 \text{ stato eq. } x_{e}= \frac{2}{u_{e}}$
			- $\displaystyle A_{e}=\frac{\partial f}{\partial x}= \frac{\partial}{\partial x}(2-ux)=-u|_{x=x_{e},u=u_{e}}=-u_{e}$
				- $u_{e}>0 \iff  u_{e}<0 \to \text{ eq. asintotic. stabile (autov. con Re)<0}$
- Multidimensionale
	- $\begin{cases} \dot x_{1}=x_{2}-x_{1} \\ \dot x_{2}=(x_1-2)(1-x_{2}) \\ y=x_{1}+2x_{2} \end{cases} \to x_{e}=\begin{bmatrix} x_{e1} \\ x_{e2} \end{bmatrix} \text{ equilibrio } \iff \begin{cases} x_{e2}-x_{e1}=0 \\ (x_{e1}-2)(1-x_{e2})=0 \end{cases}$
	- $\begin{cases} x_{e1}=2 \text{ oppure } x_{e2}=1 \\ x_{e1}=x_{e2} \end{cases} \to \ 1) \  x_{e}=\begin{bmatrix} 1 \\ 1 \end{bmatrix} \quad 2) \ x_{e}=\begin{bmatrix} 2 \\ 2 \end{bmatrix}$
	- Costruisci $A_{e}=\frac{\partial f}{\partial x}$, quindi studia $\varphi_{e}(s)=\det(sI-A_{e})$

Per quali condizioni iniziali $y_{\ell}(t)$ è limitata
- Matrici $A,C \to (sI-A)^{-1}\to Y_{\ell}(s)=C(sI-A)^{-1}x(0)$, con $x(0)=\begin{bmatrix}x_{1}(0) \\ x_{2}(0) \\ \cdots\end{bmatrix}$
- Vedo se c'è un addendo con modo divergente

---

### RETROAZIONE SULLO STATO
-  $\varphi_{c}(s)$ al variare di $\alpha$
	- $\varphi(s)$ per vedere tutti gli autovalori
	- $\det(\mathcal{R})\neq 0$ $\Rightarrow$ completamente raggiungibile (quindi controllabile): $\varphi_{c}(s) =\varphi(s)$ 
		- Else: trovo autov. non controllabili: metto valore ad $\alpha$ e faccio m.c.m. denominatori di $(sI-A)^{-1}B$ 
- $X_{r}$ per certi valori di $\alpha$
	- $\mathbb{R}^n$ se completamente controllabile, altrimenti $\mathcal{R}$ e quindi $\text{Im}\{R\}$
- $\alpha$ per cui esiste legge di controllo tale da rendere il sistema asintoticamente stabile
	- se $\exists$ autovalori non controllabili $\implies$ devono essere asintoticamente stabili
- $\alpha$ per cui esiste legge di controllo tale da posizionare gli autovalori in $\lambda_{i}^{*}$
	- se tutti i $\lambda_{i}^{*} \neq \text{autovalori sistema}$ si può fare solo se completamente controllabile
		- se $\exists \lambda_{i}^{*}=\lambda_{i}$ allora devo spostare solo un $\lambda_{j}$ e lo posso fare se tale autovalore è controllabile
- Dato $\alpha$ fare legge di controllo per garantire stabilità asintotica in ciclo chiuso e inseguimento perfetto di $y^\text{o}$ costante
	- $A^{*}=A-BF$, $\varphi^{*}(s)=\det(sI-A^{*}) \text{ avente poli con Re}<0 \stackrel{\text{ricavare}}{\to}$ $f_{i}$ adatti e relativi autovalori $\lambda_{i}^{*}$ 
	- Inseguimento perfetto: $G^{*}_{y^\text{o}y}(0)=\frac{r(0)}{\varphi^{*}(0)}H=1$ da cui si individua $H$ (nota: $r(s)=C \text{Adj}(sI-A)B$)
- Risposta forzata (transitorio e permanente - $\exists$ se asintotic. stabile) per riferimento a gradino dato
	- $Y_{f}(s)=G^{*}_{y^\text{o}y}(s)\underbrace{Y^\text{o}(s)}_{\text{ingresso}}$ $\to$ se poli distinti tra i fattori $\Rightarrow$ $Y_{f}(s)=\underbrace{\frac{K_{i}}{s-p_{i}}}_{\text{transitorio}}+\underbrace{\frac{\tilde K_{i}}{s-p_{i}}}_{\text{permanente}}$ 
		- Permanente: teorema risposta in frequenza (+ sovrapposizione effetti se serve)
			- $\text{gradino: }\to \ y_{f}^{Y^{o}}(t)=\cancelto{1}{G^{*}_{y^{\text{o}}y}(0)}y^{\text{o}}(t)=y^{\text{o}}(t)$
			- $\text{sinusoide } (y^{\text{o}}(t)=Y_{0}\sin(\omega_0))  \to \text{Re}\{G^{*}_{y^{\text{o}}y}(j \omega_{0})\}Y_0(t)\sin(\omega_{0}t)+\text{Im}\{G^{*}_{y^{\text{o}}y}(j \omega_{0})\}Y_{0}(t)\cos(\omega_{0}t)$
		- Transitorio: teorema residui $\left( \lim_{s \to p_{i}} (s-p_{i})Y_{f}(s) \right) \  \forall i)$ e antitrasformata per avere nel tempo $(y_{f}^{G^{*}_{y^\text{o}y}}(t)=(\sum_{i=1^{}} K_{i}e^{p_{i}t})1(t)$
- Tracciare andamento $y_{f}(s)=\mathcal{L}^{-1}\{Y_{f}(s)\}=  \mathcal{L}^{-1}\{G^{*}_{y^{\text{o}}y}(s)Y^{\text{o}}(s)\}$
	- $G^{*}_{y^{\text{o}}y}(s)$ del secondo ordine $\displaystyle  \to = \frac{\omega_{n}^{2}}{\to \boxed{s^{2}+2 \ \zeta \ \omega_{n}s+\omega_{n}^{2}}}\to \omega_{n}=\dots\quad \zeta=\dots \to$ grafico
---

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