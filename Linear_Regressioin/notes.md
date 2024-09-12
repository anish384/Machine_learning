# Scores 

- For example 
    following are the actual scores
        [2, 3, 4] => truth
    following are the scores that our algo have predicted
        [1.8, 2.5, 3.5] => prediction
- We use coefficient of determination 
    $$1 - \frac{u}{v}$$
- Where 
$$u = \sum_{i = 0}^{n} (y_{i}^{t} - y_{i}^{p})^2$$
- and 
$$v = \sum_{i = 0}^{n} (y_{i}^{t} - y_{mean}^{t})^2$$
- And higher the score the better the algorithm
- Scikit-learn provides us the function called .score() for actually calculating these values

---

# Error function

- following is not a great error function as it cancel out's 
$$\sum_{i = 0}^{n} y_{i} - (m * x_{i} + c)$$
- we just have to take the mode
$$\sum_{i = 0}^{n} |y_{i} - (m * x_{i} + c)|$$
- we have to square 
$$\sum_{i = 0}^{n} |y_{i} - (m * x_{i} + c)|^2$$
