**Week 5 Tuesday class**

(no prequiz this week)

1\) Hand Back Lab

2\) Discuss lab 4

\- show my example SHOW INPUTS AT TOP\!\!

\- redundancy – don't have it\! Eg:

TC = -30:40;

RH =10:20:90

\[RH,TC\]=meshgrid(10:20:90,-30:40)

\- add whitespace

\- organization

\- use of 'clear' before running:

\- code like

...

TempK=TempC+273.15

\[RH,TempC\]=meshgrid(...)

...

only works if you forget to CLEAR

\- legends: at least 3 ways to get a title:

lgd=legend(....'\_

1\) title(lgd,'legend title');

2\) lgd.Title.String='legend title';

3\) title(legend,'legend title');

More info in first 10 pages of CHAPTER 11 of textbook.

Note – my favourite graphics property is 'tickdir','out'\!

\-For degrees: Don't use weird characters (extended charactersets)

For example, use

xlabel('Temperature/^oC'); % Tex mapping

xlabel('Temperature/\\circC'); % Tex mapping

xlabel(\['Temperature/' char(176) 'C'\]); % MATLAB codes

( look for 'title' in documentation window upper right)

3\) Do “selection exercise”

4\) Hand out worksheet.

**Thursday class**

Notes on lab:

\- Explain the issue with latitude – conversion from degrees to
distance.

Delta LON \* 111e3 \*cos(LAT)

2\*pi\*6370/360 = 111 (earth radius = 6370)

cos(LAT) because lines of longitude come closer together near the poles
(spherical geometry)

\- make sure you understand it is the grid point lat you need, not the
point you select\!
