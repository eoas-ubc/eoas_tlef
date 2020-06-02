Exercise 1: What are the results of the following:

1.  lats=\[1:20\];lats=\[10:15\]

2.  L2=lats(\[2 4\])

3.  L3=lats(\[1 0\])

4.  L4=lats(\[1 1 0 0 1 1\])

5.  L5=lats(logical(\[1 1 0 0 1 1\]))

6.  L6 = lats(end-2:end)

7.  L7 = lats(length(lats))

8.  ii=lats\>12; lats(ii)

Exercise 2: What are the results of the following:

1.  lats=\[10:20\];

2.  lat\_table=\[lats(1:5) ; lats(6:10)\]

3.  lat\_table(2,\[1 2\])

4.  lat\_table(\[1 2\],2)

5.  lat\_table(\[1 0\],2)

6.  lat\_table(logical(\[1 0\]),2)

7.  lat\_table(5)

8.  lat\_table(1:4)

Exercise 3: Evaluate the following

Do the following:

> mystruc.name='Joe Lunchbucket';
> 
> mystruc.date=datenum(2000,8,15);
> 
> mystruc.marks={10,8,'A','C',87};

1.  > What does the data structure 'mystruc' look like?

2.  > mystruc.name(1:3)

3.  > mystruc.marks(1)

4.  > mystruc.marks{1}

If you evaluate the following:

mystruc.name='Jim bulldozer'

5.  > Now what does the data structure 'mystruc' look like?

Exercise 4: Combining concepts

The function rem(x,y) returns the remainder of x./y. For example,
rem(\[6 7 8 9\], 3) returns \[0 1 2 0\].

Using logical indexing in conjunction with this function, write one or
two lines of code to create the array B, containing only the even-valued
elements of the array A.

Assume that the array A is of size 1xN and contains only integers, but
you don’t know the values stored in A.
