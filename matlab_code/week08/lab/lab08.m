% lab08 - CLJ 2017
% prelims 

clear all;
close all;


%% REAL GPS DATA
load aircraft_gps;

%% do the running median and running mean
figure(1)
winlen=7;
invec=gps.vel;
outvec = calcmedian(winlen, invec);
outvec2 = calcmean(winlen, invec);
plot(gps.mtime,gps.vel,'b:',gps.mtime,outvec,'.r',gps.mtime,outvec2,'k-')
legend('raw data', 'running median','running mean','Location','Best');
datetick('x',15)
xlabel('Time (UTC)')
ylabel('Speed (m/s)')
title('Median Filtered with winlen=5')

%% SYNTHETIC DATA
clear invec outvec;
y=[-1:.025:1];
x=1:length(y);
invec=-y.^2;
invec(40)=1;
invec([55:60])=1;
invec(1)=0;

M=11;
outvec=calcmedian(M, invec);
outvec2=calcmean(M, invec);
figure(2)
plot(x,invec,'b',x,outvec,'.r',x,outvec2,'k--')
legend('raw data', 'running median','running mean','Location','Best');
xlabel('x axis')
ylabel('y-axis - synthetic data')

%%  CHECKS
% Error checking - make square matrix for invec, make M even, M=1, M=length(y);
% clear invec;
% invec=-y'*y;
% M=7;
% outvec=calcmedian(M, invec);
