$$
\begin{align*}
& \textbf{Algorithm: Trajectory Generation (One Episode)} \\
& \begin{alignedat}{2}
    & \textbf{Input} &&: \mathcal{D},\ \pi_{\theta},\ V_{\psi},\ R_{\phi},\ \pi_{\text{ref}},\ \gamma,\ \beta,\ \lambda \\
    & \textbf{Output} &&: \tau \\
\end{alignedat} \\
& \begin{alignedat}{3}
    & x && \sim \mathcal{D} && \quad\quad\quad\quad\scriptstyle{\text{// Sample prompt}} \\
    & s_1 && \gets x && \quad\quad\quad\quad\scriptstyle{\text{// Init State}} \\
    & y && \gets \text{""} && \quad\quad\quad\quad\scriptstyle{\text{// Init Response}} \\
    & \mathbf{\tau} && \gets \left\lbrack\ \right\rbrack && \quad\quad\quad\quad\scriptstyle{\text{// Init Trajectory list}} \\
\end{alignedat} \\
& terminal \gets False && \scriptstyle{\text{// Terminal Signal}} \\
& \textbf{for } t = 1 \dots \ \textbf{do} \\
    & \quad\quad \begin{alignedat}{2}
        & \text{probs}^{\pi_{\theta}}_{t} && =\ \pi_{\theta}(\cdot | s_t) \\
        & \text{probs}^{\pi_{\text{ref}}}_{t} && =\ \pi_{\text{ref}}(\cdot | s_t) \\
    \end{alignedat} \\
    & \quad\quad a_t,\ \log{p}^{a_t} \sim \text{Categorical}(\text{probs}^{\pi_{\theta}}_{t}) && \scriptstyle{\text{// Sample Action from a Categorical Distribution}} \\
    & \quad\quad \begin{alignedat}{3}
        & s_{t+1} = s_t + a_t \\
        & y = y + a_t
    \end{alignedat} \\
    & \quad\quad \textbf{if }\ a_t == \text{\lbrack EOS\rbrack} \ \ \textbf{then} && \scriptstyle{\text{// At this time t=T}} \\
        & \quad\quad\quad\quad \begin{alignedat}{2}
            & r_t && = -\beta \, D_{\scriptscriptstyle\text{KL}}({\text{probs}^{\pi_{\theta}}_{t}}\ \|\ {\text{probs}^{\pi_{\text{ref}}}_{t}}) + R_\phi(x,y) \\
        \end{alignedat} \\
        & \quad\quad\quad\quad terminal \gets \textbf{True} \\
    & \quad\quad \textbf{else} \\
        & \quad\quad\quad\quad r_t = -\beta \, D_{\scriptscriptstyle\text{KL}}({\text{probs}^{\pi_{\theta}}_{t}}\ \|\ {\text{probs}^{\pi_{\text{ref}}}_{t}}) \\
    & \quad\quad \textbf{end if} \\[4pt]
    & \quad\quad \text{Append}\big(\tau, \left\lbrack{s_t,a_t,r_t,\log{p}^{a_t}}\right\rbrack\big) \\[4pt]
    & \quad\quad \textbf{if }\ terminal \ \ \textbf{then} \\
        & \quad\quad\quad\quad \textbf{break} \\
    & \quad\quad \textbf{end if} \\
& \textbf{end for}

\\[6pt]
& \begin{alignedat}{3}
    & T && \gets \text{Length}(\tau) \\
    & \hat{A}_{T+1} && \gets 0 && \quad\quad\quad\quad\scriptstyle{\text{// Bootstrap final advantage}} \\
\end{alignedat} \\
& \textbf{for } t = T \dots 1 \ \textbf{do} \\
    & \quad\quad s_t,\ a_t,\ r_t,\ \_ = \tau\lbrack t \rbrack \\
    & \quad\quad s_{t+1} = s_t + a_t \\
    & \quad\quad \begin{alignedat}{3}
        & \delta_{t} && = r_t + \gamma V_{\psi}(s_{t+1}) - V_{\psi}(s_t) \\
        & \hat{A}_t && = \delta_{t} + \gamma\lambda{\cdot}{\hat{A}_{t+1}} && \quad\quad\scriptstyle{\text{// GAE}} \\
        & \hat{R}_t && = \hat{A}_t + V_{\psi}(s_t) && \quad\quad\scriptstyle{\text{// Return estimate}} \\
    \end{alignedat} \\
    & \quad\quad \text{Extend}\big(\tau\lbrack t \rbrack, \ \lbrack \hat{A}_t, \hat{R}_t \rbrack \big) && \scriptstyle{\text{// One time step: } \left\lbrack\ s_t,\ a_t,\ r_t,\ \log{p}^{a_t},\ \hat{A}_t,\ \hat{R}_t \ \right\rbrack} \\
& \textbf{end for}
\end{align*}
$$