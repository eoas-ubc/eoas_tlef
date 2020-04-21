% load GPS data structure

load lab08/aircraft_gps;

% run to check implements running median correctly
% winlen=5;
% mymedian = calcmedian(gps.vel,winlen);
% plot(gps.mtime,gps.vel,'b',gps.mtime,outvec,'.r')
% legend('raw data', 'running median','Location','Best');
% datetick('x',15)
% xlabel('Time (UTC)')
% ylabel('GPS Speed')
% 
% % run to check for error messages
% winlen=8;
% mymedian = calcmedian(gps.vel,winlen);
% 
% winlen=1;
% mymedian = calcmedian(gps.vel,winlen);
% 
% winlen=2;
% mymedian = calcmedian(gps.vel,winlen);
% 
% winlen=3;
% mymedian = calcmedian(gps.vel,winlen);
% 
% winlen=15;
% mymedian = calcmedian(gps.vel(1:15),winlen);

% winlen=7;    % window length - odd
% for i=1:length(gps.vel),
%     w1=min([i-1,length(gps.vel)-i,(winlen-1)/2]);  %window length smaller near ends of array
%     outvec(i)=median(gps.vel(i-w1:i+w1));
% end
% 
% plot(gps.mtime,gps.vel,'b',gps.mtime,outvec,'.r')
% datetick('x',15)
% xlabel('Time (UTC)')
% ylabel('Speed')

clear invec;
y=[-1:.025:1];
x=1:length(y);
invec=-y.^2;
invec(40)=1;
invec([55:60])=1;
invec(1)=0;
winlen=83;

checkinputs(winlen,invec)
% if (mod(winlen,2)==0)
%     error('winlen should be even')
% elseif (winlen < 3)
%     error('winlen should be greater than 2')
% elseif (length(invec)<winlen+1)
%     str=sprintf('invec needs to be bigger than %d',winlen);
%     error(str)    
% end

clear outvec;
N=length(invec);
for i=1:N,
    w1=min([i-1,N-i,(winlen-1)/2]);  %window length smaller near ends of array
    outvec(i)=median(invec(i-w1:i+w1));
end

figure(2)
plot(x,invec,'b',x,outvec,'.r')