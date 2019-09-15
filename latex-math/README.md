## Common Templates for editing latex document, along with math notations

> Use overleaf as online latex editor. 


### Summation and Product
```latex
\sum\limits_{}^{}
\prod\limits_{}^{}
```

### Write down math equations with steps and explanation
```latex
\begin{align*} % equations are aligned at &
A &= B + C && (exaplantion 1) \\
  &= D + E && (explanation 2}) \\
  &= F &&
\end{align*}
```

### Table
```latex
\begin{tabular}{ l | c || r } 
% l, c, r, means to align the column to left, center, or right.
% lines bewtween 
  \hline
  1  & 2  & 3 \\
  4  & 5  & 6 \\
  \hline
  7  & 8  & 9 \\
  10 & 11 & 12\\
  \hline  
\end{tabular}


\begin{center} % cneter the table.
\begin{tabular}{ | l | l | l | p{5cm} |} % if content is text and need wrapping.
  \hline
  Day & Min Temp & Max Temp & Summary \\ \hline
  Monday & 11C & 22C & A clear day with lots of sunshine.  
  However, the strong breeze will bring down the temperatures. \\ \hline
  Tuesday & 9C & 19C & Cloudy with rain, across many northern regions. Clear spells 
  across most of Scotland and Northern Ireland, 
  but rain reaching the far northwest. \\ \hline
  Wednesday & 10C & 21C & Rain will still linger for the morning. 
  Conditions will improve by early afternoon and continue 
  throughout the evening. \\
  \hline
  \end{tabular}
\end{center}

```

### Insert image
```latex
\begin{figure}[h]
  \centering
  \includegraphics[width=0.8\linewidth]{<filename>.png}
\end{figure}
```

### ordered/unordered list
```latex
\begin{enumerate}
  \item item1
  \item item2
  \item item3
\end{enumerate}

\begin{itemize}
  \item item1
  \item item2
  \item item3
\end{itemize}
```

### use text mode in math mode
```latex
$p(rv=\text{readable value})$
```

---
 
### Probability Notations (latex)


---

### (TODO) Deep Learning Math Notations (latex)

##### 1 Layer of NN

##### LSTM

##### GRU

##### Attention

##### represent sentence, word
