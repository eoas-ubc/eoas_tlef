function checkinputs(winlen,invec)

if (mod(winlen,2)==0)
    error('winlen should be even')
elseif (winlen < 3)
    error('winlen should be greater than 2')
elseif (length(invec)<winlen+1)
    str=sprintf('invec needs to be bigger than %d',winlen);
    error(str)    
end