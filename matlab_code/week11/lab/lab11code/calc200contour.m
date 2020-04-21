function [lon200, lat200] = calc200contour(lon, lat, depths)
%USE:  [lon200, lat200] = calc200contour(lon, lat, depths)
%
%Calculates a smoothed version of the 200m contour given lat, long, and
%depth. Removes canyons from contours. Array sizes:
%lat:    Mx1
%lon:    1xN
%depths: MxN

%Calculate the contour matrix
c3 = contourc(lon, lat, depths, [200 200]);

%We are interested in the first 200 m contour only. Contour level given in
%c3(1,1) and number of points given in c3(2,1).
numPts=c3(2,1);
cols = 2:numPts-1;

%Lats and Lons of the 200 m isobath
lon200raw = c3(1, cols); 
lat200raw = c3(2, cols);

%Remove JdF canyon
ii = lon200raw > -125.4 & lat200raw>48;
lon200cut = lon200raw(~ii); 
lat200cut = lat200raw(~ii);

%Do the running mean to remove wiggles
winlen = 21 ;  
lon200 = runmean(lon200cut, winlen);
lat200 = runmean(lat200cut, winlen);

end



function out=runmean(invec, winlen)
%Calculate the running mean. Shrink the window near the endpoints.

N=length(invec);
for i=1:N,
    W=min([i-1, N-i, (winlen-1)/2]); %clever way to deal with the endpoints
    out(i)=mean(invec(i-W:i+W));     %and calculate the mean  %BUG
end

end