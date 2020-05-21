## EOSC 211: Interpolation 

**Group \#: \_\_\_\_\_\_\_ Name:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**Interpolation:**

![](week11WS01_figs/media/image1.png)

The figure above contains estimates, f<sub>i</sub>, of a function f(x)
taken at data points x<sub>i</sub>. The values of x<sub>i</sub>,
f<sub>i</sub> are given in Table 1 below.

Table 1:

| x<sub>i</sub> | 0.3   | 1.1   | 3.5   | 3.9   | 5.8   | 8.0   |
| ------------- | ----- | ----- | ----- | ----- | ----- | ----- |
| f<sub>i</sub> | \-2.5 | \-0.6 | \-1.2 | \-1.8 | \-4.6 | \-3.6 |

1.  **Using the graph only** estimate the values of f(x) at evenly
    spaced points x=1,2,3,…8. Plot the points on the graph and enter the
    estimated values of f(x) from the graph in table 2 below

| x<sub>i</sub> | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| ------------- | - | - | - | - | - | - | - | - |
| f<sub>i</sub> |   |   |   |   |   |   |   |   |

2.  Now we will use math and find an “exact” value of f(x) at the point
    x=7 by linearly interpolating between the 2 nearest points.
    
    1.  What are the two x values in Table 1 that are closest to x=7?
        Call these two points x<sub>j</sub> and x<sub>j+1</sub>.

> x<sub>j</sub> =
> 
> x<sub>j+1</sub> =

2.  What is the slope of the line joining these two points? Call this
    *m*

> *m =*

3.  How would you estimate the value f<sub>new</sub> of f(x) at a point
    x<sub>new</sub> that is part way between x<sub>i</sub> and
    x<sub>i+1.</sub> Write down the formula you would use to estimate
    f<sub>new</sub> and calculate its value at x<sub>new</sub> = 7.
