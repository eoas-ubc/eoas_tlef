function sumn = addn(n,summax,maxiter)
% sumn(n,summax,maxiter) adds the n to itself until one of the two is
% reached:
% 1. The sumn reaches summax, or
% 2. maxiter iterations is reached
%
counter = 0;
sumn = n;
while sumn <=(summax-n) && (counter <= maxiter-1)
    sumn = sumn+n;
    counter = counter+1;
end