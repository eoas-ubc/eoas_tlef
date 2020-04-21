% cjscript.m
% Sample script to calculate runnning mean and running median - from lab06
% Inputs:  gps.vel, winlen_mean, winlen_median
% Outputs: z (running mean), zm (running median)

% do the running mean and median - window length must be odd
% loop sets window length to be smaller near ends of array

winlen_mean=7;    
winlen_med=7;
N=length(gps.vel);
for i=1:N,
    w1=min([i-1,N-i,(winlen_mean-1)/2]);  % or use results from worksheet in week 5 for min of 3 numbers
    z(i)=mean(gps.vel(i-w1:i+w1));	% running mean
    w1m=min([i-1,N-i,(winlen_med-1)/2]);  
    zm(i)=median(gps.vel(i-w1m:i+w1m));	%running median
end
