function outvec=calcmedian(winlen, invec)

% CALCMEDIAN:  Function to compute a running median
%      Inputs:  invec (1D array), winlen (must be odd, >=3 or
%               <=length(invec))
%      Output:  outvec - contains running median
%
%      Various error checks implemented

checkinputs(winlen,invec)

N=length(invec);
for i=1:N,
    w1=min([i-1,N-i,(winlen-1)/2]);  %window length smaller near ends of array
    outvec(i)=median(invec(i-w1:i+w1));
end
%y=outvec(i)

%  checkinputs function
function checkinputs(winlen,invec)

[N,M]=size(invec);
if (mod(winlen,2)==0)
    error('winlen should be odd')
elseif (winlen < 3)
    error('winlen should be >= 3')
elseif (length(invec)<winlen+1)
%     str=sprintf('invec needs to be bigger than %d',winlen);
%     error(str)    
    error('invec needs to be bigger than winlen');
elseif  (N ~= 1 && M ~= 1)
    error('invec is not a row or column vector')
end