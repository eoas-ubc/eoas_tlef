function southVImap(lon, lat, depth)
% SOUTHVIMAP draw a basic map of southern VI, 
%    Draw a map focusing on the region of Juan de Fuca Canyon 
%    where the FK009A cruise took place.
%

clf; hold on; box on; grid on;
%Need to set aspect ratio because longitudes converge towards the poles
set(gca, 'dataaspectratio', [1 cosd(48.5) 1], 'fontsize', 10)
%First contour the coastline and the 200 m contours separately
contour(lon, lat, depth, [0 0], 'k', 'linewidth', 2); 
contour(lon, lat, depth, [200 200], 'k'); 
%Then contour a few other isobaths
contour(lon, lat, depth, [100 300 400 500 600 700], ':k');
%Axis limits
axis([-126.75 -123.5 47.8 49.2]) 

set(gca,'tickdir','out','linewi',2);

% Make the labels more "map-like"

xlab=get(gca,'xticklabel');
for k=1:length(xlab)
    xlab{k}=sprintf('%5.1f\xB0W',abs(str2num(xlab{k})));
end    
set(gca,'xticklabel',xlab);

ylab=get(gca,'yticklabel');
for k=1:length(ylab)
    ylab{k}=sprintf('%5.1f\xB0N',abs(str2num(ylab{k})));
end    
set(gca,'yticklabel',ylab);
end