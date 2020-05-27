Exercise 1: Write MATLAB code to…

1.  Create a column (5x1) matrix **var1** with the elements 1.1, 2.2,
    3.3, 4.4, 5.5

2.  Create a row (1x3) matrix **var2** with the numbers 10 to 12.

3.  Create a 2x3 matrix **var3** with numbers 101-103 (first row) and
    201-203 (second row)

4.  Create an empty array **var4**

5.  Create a row (1x1000) vector **var5** containing the numbers 2400 to
    3399

6.  Create a string variable **str1** containing the word “class”.

Exercise 2: What are the results of the following (using variables from
Exercise 1)?

1.  bvar1=var1(3)

2.  bvar2=var2(2)

3.  bvar3=var1(\[1 2 3\])

4.  ii=\[1 2 5\]; bvar4=var1(ii)

5.  bvar5=var3(2,2)

6.  bvar6=var3(\[1 2\],2)

7.  bvar7=var3(\[1 2\],\[2 3\])

8.  bvar8=var3(4)

9.  bvar9=var2(:)

10. bstr1=str1(3:4)

11. bvar10=var1(var1(2))

12. bvar11=var1(3); bvar11=var1(4)

13. bvar12=var1(1,5)

14. bvar13=var1(5,1)

15. bvar14=var2(1,3)

16. bvar15=var2(3,1)

17. bvar16=\[ \]; bvar16(2:4)=var3(1, :)

Exercise 3: What is printed to the screen when you enter the following?

1.  B={'sky' , 3.4 , \[2 4 5\]}; B{1}(2)

2.  A.var1={8 , 30, 'R' }

> A.var2=2
> 
> A.var3=A.var1{A.var2}
