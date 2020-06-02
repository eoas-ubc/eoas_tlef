**EXERCISE 1:** Practice with loops and logical indexing. Assume
**x1=\[1 8 -7 2 -9 -3\] to help you test your answers.**

**a) Write the following without loops:**

for i=1:length(x1)

if x1(i)\>0

x2(i)=1;

else

x2(i)=0;

end;

end;

**b) Write the following using a loop**

x2=x1(1:end-1)\>x1(2:end);

**  
**

**c) What is in x2 after executing this piece of code? Use x1=\[1 8 -7 2
-9 -3\]**

x2=x1(x1(1:end-1)\>x1(2:end))

**d) Write the following using a loop**

ix=find(x1(1:end-1)\>x1(2:end))

x2=x1(ix);

**  
**

**EXERCISE 2:** The points on a circle, radius R, centered at an x,y
position (x<sub>C</sub>, y<sub>C</sub>) are given by their x,y
positions.

x = x<sub>C</sub> + R cosθ

y = y<sub>C</sub> + R sinθ

θbetween the x-axis and the line from the center of
the circle to any given point on the circle. i.e., θ goes from 0 to 2π.

Write a function called getcirc that will take as input the variables
xc, yc, R and the number of points on the circle (N) in that order and
return a vector x and a vector y in that order containing the x and y
coordinates of the N points on the circle.

Add a subfunction called checkRN that checks that the radius R is
positive and that the number of points is at least 20 (for a reasonably
smooth circle).

**EXERCISE 3.** The following script is supposed to call the function
getcirc to calculate a circle that has radius 15, is centered at (π,1)
and then plot the resulting circle. You can assume the subfunction
checkRN has been correctly implemented inside getcirc. What are the bugs
in this script?

% test script to call getcirc

close all;

clear all;

N=15;

Rp=100;

xc=1;

yc=pi;

\[yp,xp\]=getcirc(xc,yc,R,N);

figure(1), set(gca, 'FontSize',18);

plot(xp,xp,'k-');

xlabel('X (km)');

ylabel('Y (km)');

title('Testing my circle function');

axis('equal');

**EXERCISE 4.** Add some code to your debugged version of the script
above that will write the (x,y) coordinates of the points on the circle
to a file called mycirc.dat. Write out the x,y positions as 2 columns
(col 1 = x positions, col 2 = y positions). Add a header line that
contains the numerical values for (xc,yc), R and N. Format any real
numbers so that e.g. the number 101.254 is written in the form
1.013e+02.
