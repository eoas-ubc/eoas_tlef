**Exercise 1:** We have two input vectors, x which is distance and tpro
which is elevation in kilometers (say, along a survey line). Both are
1x99 arrays (ie a row vector with 99 entries). Use
<span class="underline">a loop and an if statement</span> to write out a
new variable tlow that contains only the values in tpro when the
elevation is less than -1.8km and NaN otherwise. Write your answer in
MATLAB code (or as close to it as you can).

What is the length of the new vector tlow?

**Exercise 2:** Turn the code snippet above into a function that returns
a vector tlow2 that is exactly the same as tlow, but that takes as input
(1) tproin and (2) a variable called cutoff that contains an arbitrary
cut-off for the elevation (ie, I might want to select elevations below
-2km or -1.8 km or -1.5km, so make this a variable). Start by writing
down what you think the function call from the main script should look
like if you want to process tpro with a cutoff of -1.8.

Function Call:

Now write down the function definition line:

Now write the H1 and help lines:

Now write down the body of the function:

**Exercise 3:** Now take the code snippet in Exercise 1 and adapt it to
return a vector tlow3 instead of tlow, where tlow3 contains ONLY the
elevation values that are less than -1.8km AND NOTHING ELSE. Make a
corresponding vector x3 that contains ONLY the distances corresponding
to the elevations in tlow3. Just write the code snippet, don’t write it
as a function yet.

**Exercise 4:** Now turn the code snippet in Exercise 3 into a function
that returns a vector tlow4 that is exactly the same as tlow3 in Ex. 3,
and a vector x4 that is the same as x3 in Ex. 3.

Input arguments:

Output arguments:

Function Call:

Now write down the function definition line:

Now write down the body of the function:

**Exercise 5:** Finally, I need not have used a loop and an “if”
statement in the function. How would I rewrite the body of the function
in Exercise 4 to use logical indexing? Note that the function call and
function definition line don’t need to be changed.
