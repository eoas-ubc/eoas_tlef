function plotarrows(filename,decfac,scfac)
% PLOTARROWS  Plots mean currents
%    PLOTARROWS(DECFAC,SCFAC) takes the gridded
%    current climatology provided by the 
%    Mariano Global Surface Velocity Analysis (MGSVA) 1.0
%    available by anonftp to ftp://jerry.rsmas.miami.edu/pub/MGSVA/
%    and makes a nice plot. You can subsample the
%    complete dataset by a decimation factor DECFAC,
%    and scale the arrows by a scaling SCFAC (which
%    has units of 'degrees per m/s')



% Info on data

% This code is supposed to make a map showing ocean current vectors
% as arrows, superimposed on a gray-scaled image of the current
% magnitudes.

%EDIT - move load coastline further down

csvdata=load(filename);   % Load the data in the arrow file

% They are in a long list, so insert them into
% rectangular matrices of the right dimensions

[LG,LT,U,V]=move_to_grid(csvdata); % This is a subfunction (bottom of this file)

%EDIT
% Now, we want to smooth the data matrices by taking
% a running mean in both dimensions. We choose the window length to be
% the same size as our subsampling interval 'decfac'
Um=mean2d_fix(U, decfac);
Vm=mean2d_fix(V, decfac);

%EDIT
% Now we subsample, or decimate, by taking only a subset of points
% using increments of 'decfac'.
rLG=LG(1:decfac:end,1:decfac:end);
rLT=LT(1:decfac:end,1:decfac:end);
rUM=Um(1:decfac:end,1:decfac:end);
rVM=Vm(1:decfac:end,1:decfac:end);

tic
% Draw the image. Use the MAGNITUDE of the velocity for the colour scale
imagesc(LG(1,:), LT(:,1), sqrt(Um.^2+Vm.^2)); %FIX
% imagesc(LG(1,:), LT(:,1), (Um+Vm)); %original - buggy
handle=colorbar('eastoutside');
set(get(handle,'ylabel'),'string','Current speed (m/s)');
caxis([0 .5]);
toc

tic
load m_coasts;  %load a coastline
line(ncst(:,1),ncst(:,2),'color', 'w'); % draw the coastline FIX
set(gca,'ydir','normal','tickdir','out');
colormap(gray);
xlabel('Longitude');
ylabel('Latitude');
toc

%EDIT

% Draw velocity vectors at each location of our subsampled
% grid. Use linear indexing in place of a double loop!
%
% Draw lines at a particular lat/long in
% the direction of U/V. However, degrees of longitude get closer
% together as we get nearer to poles, so we compensate in our drawing
% by dividing the U-component by the cosine of the latitude.

%EDIT - comments
ii=isfinite(rUM(:)); %find indeces (linear indexing) where vels exist
x=rLG(ii); %longitudes
y=rLT(ii); %latitudes
%multiplying by scaling factor determines relative length of arrows
dx=rUM(ii)./cosd(rLT(ii))*scfac; 
dy=rVM(ii)*scfac;

%plotting a thin red line ontop of a thick white line 
% enhances the contrast. 
line([x x+dx]',[y y+dy]','color','w','linewidth',2);
line([x x+dx]',[y y+dy]','color','r');

end

function [mLG,mLT,U,V]=move_to_grid(csvdata);
% MOVE_TO_GRID    Puts data into a grid
%
% Each data file consists of lines, written in fortran free format,
% in the form of
% 15000., longitude, latitude, e-w velocity u, s-n velocity v, std. dev u, std. dev v
% They are in 1 degree boxes, centered on the integer lat/long

% Set up the grid on which the data was created.
LONG=[-179:180];
LAT=[-89:89];
[mLG,mLT]=meshgrid(LONG,LAT);     

%EDIT
%Initializing with NaNs also automatically deals with points where there is
%no data (eg. on land) because those locations will simply contain NaNs
U=NaN(179,360);
V=NaN(179,360);

% Loop through all points in .csv file.
%
% For each, calculate the row/col indices
% from the lat/longs.  Lats get converted
% into row indices 'i', and longs into column
% indices 'j'. Since we have a 1 degree spacing
% we just have to add the right offset
% to make this work - for example, for latitudes
% latitude of -89 goes to row 1,
% latitude of -88 goes to row 2, etc.
%
% Then write the
% corresponding u/v data for that lat/long
% into the right place (i.e. index (i,j) )
% in the U/V matrices 
%
A=csvdata; %FIX
for k=1:length(A),
   i=A(k,3)+90;    %row index EDIT FIX
   j=A(k,2)+180;     %column index EDIT FIX
   U(i,j)=A(k,4);
   V(i,j)=A(k,5);   %FIX
end
    
end
    
    
    
      
