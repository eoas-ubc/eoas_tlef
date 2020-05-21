**Exercise 1**: a) You have a cash register with $20, $10, $5, $2, $1,
$0.25, $0.10, $0.05 and $0.01 bills or coins. Write a program to make
change – so that, for example, if someone gives you a $10 bill for
something costing $6.55 the program will calculate that you get back
$3.45 in change consisting of a $2, and $1, a $0.25, and 2 $0.10

It may be useful to use the fix() function, which rounds its (\>0) input
to the nearest positive integer less than or equal to the input.

Store the denominations in a variable denom=\[20 10 5 2 1 0.25 0.10 0.05
0.01\] , the item cost in cost, the money provided in payment, and store
the change in a vector change of the same size as denom.

b) Now we remove pennies, so costs are rounded to the nearest 0.05. How
can we use the round() function to take this into account?
