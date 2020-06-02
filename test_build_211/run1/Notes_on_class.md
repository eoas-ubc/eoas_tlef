**My Notes for Week 04:(Tuesday)**

1\) Move people into their GROUPS (have group list available)

2\) Quiz

3\) During quiz, hand back lab

**Computer math:**

On Laptop:

.1 \<ret\>

.1+.1\<ret\>

.1+.1-.2 \<ret\>

.1+.1+.1-.3 \<ret\> - 5.5511e-17\!

\- Computer math works on computer numbers

\- Computer numbers: each number has to fit into a finite nuimber of
bits:

e.g. for unsigned integers: \_ \_ \_ \_ \_ \_ \_ \_ each has 0 or 1, so
we have 2\*2\*...=2^8 = 256 possible numbers.

x=uint8(34); y=uint8(50)

x+y OK

x-y \<- 0\!

x=uint8(240)

x+y \<- 255.

\>\> help datatypes

Notice all the kinds of different integers – uint and int (with a
sign)...also logical....also “single” and “double”.

Double precision floating point:

Numbers re represented more or less as +/-(1+f) x2^e (sign, mantissa,
0\<=f\<1, exponent) so there are

still a finite number of patterns (numbers), spread unevenly throughout
the real number line

LARGEST NUMBER realmax

realmax\*2 -\> Inf

SMALLEST realmin (Note, not for class – realmin/2 is not zero, there are
so-called 'denormalized numbers represented as (f)x2^e the handle
underflows.

So...long decimal numbers are represented by the NEAREST number. But
this means

sqrt(2)\*sqrt(2)-2 \~= 0\!\!\!

and .1+.1+.1 \~= .3\!

Other stuff: what is the smallest number you can add to 1 to get \>1?
eps

Special numbers: 1/0 -\> Inf

What is 0/0? -\> NaN\! “Not-a-Number”.

WorkSheet

After doing part 1, perhaps do

\>\>help precendence
