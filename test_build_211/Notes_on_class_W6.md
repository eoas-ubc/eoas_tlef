**Tuesday class**

1\) prequiz on loops

2\) hand back labs

3\) Comments on lab 5

\- longitude is 'long(ix)” NOT ix\!\!\! (ix is an INDEX into array of
longitudes)

\- the point we are dealing with is long(ix),lat(iy), NOT X,Y. The
latter is just the ginput point. Note if we wanted slope at X,Y we would
have to INTERPOLATE

Have to deal with “wrap around” correctly: (draw on “grid” to
illustrate)

x x x x x

x x x x x

x x x x x

\- Note that the EARTH IS ROUND, so points that go off the right come
back on the left. Reducing THIS to a 2-point upwind difference is
INCORRECT.

\- points are ALWAYS 2 degrees apart (not -358 degrees) –
long(irighht)-long(ileft) is WRONG.

\- 111e3 is 111x10<sup>3</sup> NOT 111\*exp(3)

\- Not really worth any marks (or none deducted either) but

\- we can write 10N for 10 North, -10N for 10 south, but NOT -10S for 10
degrees south.
