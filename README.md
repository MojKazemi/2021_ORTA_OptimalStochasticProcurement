# Introduction

​	This project is about "Optimal stochastic procurement" for the Operational research course in Poltecnico di Torino


## Run the code:
Run the code by writing in the terminal
```
python3 main.py
```
## Project

In the project we want to solve the following problem with the constraints:

The Capacitated Supplier Selection Problem with Total Quantity Discount Policy and Activation Costs (CTQD_AC) and under uncertainty ($CTQD\_AC_u$)



There are two approch :

​											1- only product price stochastic ($CTQD\_AC_{up}$)

​											2- only product demand is stochastic ($CTQD\_AC_{ud}$)



M : Set of suppliers index by i - it was defined in code by "num_Suppliers" = [5, 10, 15]

K : Set of products index by k - it was defined in code by "num_products" = [10, 20, 30]

$F_{ik}$ : Basic price of product " i " of supplier " k " - It was defined in code by " B_price_low = 10 and B_price_high = 200"

$\lambda$ : It was defined in code by " lambda " = [0.1, 0.8]



we consider the following problem:
$$
\min \sum_{i \in \mathcal{M}} a_i x_i + \sum_{\in \mathcal{S}} p_s \big[\sum_{k \in K} \sum_{i \in M_k}\sum_{r \in R_i}(1-\delta_{ir})f_{ik}(z_{ikr}+z^+_{ikrs}=z^-_{ikrs})+\sum_{k \in K}F_kw_{ks} \big]
$$
subject to:
$$
\sum_{i\in \mathcal{I}} w_i x_i \leq W
$$

$$
\sum_{i\in \mathcal{I}} v_i y_i^s \leq V\ \ \ \forall\ s\ \in\ \mathcal{S}
$$

$$
y_i \leq x_i
$$

$$
x_i, y_i \in \{0, 1\}\ \ \ \forall\ i \in \mathcal{I}
$$

