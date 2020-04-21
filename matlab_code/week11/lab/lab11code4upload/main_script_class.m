% Code to load some oceanograhic data, display data as scatter plots,
% compute a smoothed contour for 200m depth. This version shows the casts 
% at their actual distance taken rather than a pretty contour plot. This is 
% in preparation for the week 11 lab in which we will interpolate these
% data onto an even perpendicular distance spacing and compute some
% statistics.
%
%  Updated CLJ 11/2018

clear; 
close all;

% Southern Vancouver Island (SVI) Grid of lats/lons
load SouthVI.mat

% Put South VI grid into easier variables
lonMap = SouthVI.lon;    % longitude vector for the SVI map
latMap = SouthVI.lat;    % latitude vector for the SVI map
zMap = -SouthVI.depth;   % 2D array of depths: 
                         % d=0 is the coastline, we will be interested in d=200m
clear SouthVI;           % don't need this any more

%% Temperature, salinity, density, and pressure for first half of 
% % leg E of FK009A cruise, August 2013

load FK009A_demo.mat

%%  Do some preliminary calcs and make a nice plot

% Calculate a smooth version of the 200 m contour. 
[lon200 lat200] = calc200contour(lonMap, latMap, zMap); 

% Make a basic map showing the track and a few depth contours
figure(1); hold on;
% Plot all contours - does this in function for tidiness of main script.
southVImap(lonMap, latMap, zMap);
% Now the "smoothed" 200m contour - pink
plot(lon200, lat200, 'm', 'linewidth', 2);
% Plot ship track - blue
plot(lon, lat, 'b.', 'markersize', 10);

% Compute shortest distance of each ship point with data from the smoothed 200m depth contour
dist200 = shortest_dist(lon, lat, lon200, lat200);

% Get the indices for individual tracks. Output variable is a cell array.
inds=setupInds;


%% Make scatter plots to show temperature as function of distance and depth

% -----------------------
% MAKE SURE YOU UNDERSTAND WHAT meshgrid AND scatter do.  We saw meshgrid
% earlier in the term
% -----------------------
% just extract the shallowest 90m of depth and salinity arrays because 
% there are measurements at these depths on all tracks
saln=saln(1:91,:);       
depths=depths(1:91);

% now make a plot that has profiles only where there are data to show
% uneven distribution of casts
figure(2); clf; k=0;


for j=10:-1:1
    %pause;
    
    % extract temps and distances
    ii=inds{j};
    subsal=saln(:,ii);     
    xx=dist200(ii);
    
    % we want to have a (dist,depth) pair for every temp measurement
    [mx,my]=meshgrid(xx,depths);
    
    %This is where we do the actual plotting - this uses the built-in function scatter 
    % scatter needs to be passed 1D arrays as arguments so we must flatten mx, my
    k=k+1; 
    figure(2);         %ADD TO LOOP TO CHOOSE CORRECT FIGURE ACTIVE - not essential here but important in lab
    makeScatterPlot(mx(:),my(:),subsal(:),j,k);
    colorbar;   
    caxis([31 34]);    % add after plotting once to see range of salinities      
    xlim([-20 45]);  
    ylabel('Depth (z)');  title(['Track' num2str(j) ' Temperature']) 
        
    %We only want the xlabel on the bottom row of subplots
    if k==9 | k==10 
        xlabel('Distance from Shelf Break (km)')
    else
        set(gca,'xticklabel', [])
    end

end

%% save this to a file for lab 11

save lab11_data.mat lon lat dist200 depths saln inds   

