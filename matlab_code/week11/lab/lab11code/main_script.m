% Script to load and plot data in preparation for interpolation lab
%
% The script loads a data set of lat, lons for Southern Vancouver Island
% and also some oceanographic data from one leg of a cruise in August 2013.
%
% It computes a smoothed version of the 200m bathymetry contour and the
% perpendicular distance of each point along the individual ship tracks
% from this contour.  The 200m contour is a proxy for the shelf break.
%
% In the second part of the script the salinity as a function of
% distance from the shelf break and water depth is plotted.  Because data
% was not taken evenly along the tracks and because the tracks are not
% taken with at same orientation with respect to the shelf break the
% resulting plots are unevenly spaced in terms of distance from shelf break.
%
% In the lab you will interpolate these data onto an even grid.

clear; 
close all;

% Temperature, salinity, density, and pressure for first half of 
% leg E of FK009A cruise, August 2013
load FK009A_demo.mat

%calculates a smooth version of the 200 m contour. 
[lon200,lat200] = calcsmoothcontour; 

%Make a basic map showing the track and a few depth contours
figure(1); hold on;
%All contours
southVImap;
%Now the "smoothed" 200m contour - pink
plot(lon200, lat200, 'm', 'linewidth', 2);
%The ship track
plot(lon, lat, 'b.', 'markersize', 10);

%get the shortest distance of each datapoint from the smoothed 200m contour
dist200 = shortest_dist(lon, lat, lon200, lat200);
%Isolate indices for individual tracks. Output variable is a cell array.
inds=setupInds;

for k=1:length(inds)
    text(lon(inds{k}(1)),lat(inds{k}(1)),sprintf('Track %d',k),'fontweight','bold');
end    

%% Now plot temperature - one track per subfigure
%
% MAKE SURE YOU UNDERSTAND WHAT meshgrid AND scatter do.  You've seen meshgrid
% already this term.

% just extract the shallowest 91m of depth and temperature arrays because 
% there are measurements at these depths on all tracks
saln=saln(1:91,:);
depths=depths(1:91);


%% save this to a file for lab 11

save lab11_data.mat lon lat dist200 depths saln inds

%%  If you load lab11_data.mat you can run the code below.

%% now make a plot that has profiles only where there are data to show
% uneven distribution of casts
figure(2); clf; k=0;

%Loop backwards because track 10 is northernmost - we want it at the top of
%the figure. Track numbers should decrease top to bottom in the figure. Ie.
%subplot 1 should contain plot for track 10; subplot 2 the plot for track 9; etc...
for j=1:10
   
    % extract salinities and distances
    ii=inds{j};
    subtemp=saln(:,ii); 
    xx=dist200(ii);
    
    % we want to have a (dist,depth) pair for every temp measurement
    [mx,my]=meshgrid(xx,depths);
    
    % Our plots of salinity as a function of depth and distance use the built-in 
    % function scatter.  Scatter needs to be passed 1D arrays as arguments so we must flatten
    % mx, my
    
    makeScatterPlot(mx(:),my(:),subtemp(:),j,11-j);
   
    caxis([32 34.2]);
    axis([-20 45 0 91]);  
    title(sprintf('Track %d Salinity',j)); 
    
    %We only want the xlabel on the bottom row of subplots
    if j==1 || j==2 
        xlabel('Distance from Shelf Break/km')
    else
        set(gca,'xticklabel', [])
    end

end

%figure(1);print -depsc mapfig
