% lab 3 2017 CLJ

clear all; 
close all;

%% Part2:  Ocean Color / SST

% type in these commands from lab instructions
[A,CMAP]=imread('V20181522018181.L3m_MO_SNPP_CHL_chlor_a_9km.nc.png');

figure(1)
image(A);
xlabel('Column index');
ylabel('Row index');
colormap(CMAP);

% how large?  use 'size' function
nA=size(A)

% % old version
% A=imread('ModisChlAJan2013.png');
% image(A);
% set(gca,'ydir','normal');
% nA=size(A)

% look at the colors
figure(2)
image(uint8(0:255))
colormap(CMAP);

A(1200,500,:)

figure(3)
WNA=A(300:650,1350:1700,:);
image(WNA);
colormap(CMAP);


nA=size(A)
lat=90-180*[1:nA(1)]/nA(1);
lon=-180+360*[1:nA(2)]/nA(2);

figure(4)
image(lon, lat,A);
set(gca,'ydir','normal');
xlabel('Longitude');
ylabel('Latitude');
colormap(CMAP);

% Vancouver area - note how we extract subarrays from lon and lat
figure(5)
VAN=A(400:600,550:750,:);
image(lon(550:750),lat(400:600),VAN);
colormap(CMAP);
set(gca,'ydir','normal');
xlabel('Longitude');
ylabel('Latitude');
title('Vancouver Area');

%% Part 3a: getting the bathy file and plotting

pause
clear all;
close all;

load Bathyfile.mat;
figure(1)
imagesc(bath.long,bath.lat,bath.height);
xlabel('Longitude');
ylabel('Latitude');
colorbar;
set(gca,'ydir','normal');
caxis([0 4200]);

%% Part 3b: using ginput

% make the fig with real lats and lons
figure(1)
imagesc(bath.long,bath.lat,bath.height);
set(gca,'ydir','normal');
colorbar;

% make the fig only with row and col indices so that it is ready for ginput
figure(2)
imagesc(bath.height);
colorbar;

[I,J]=ginput(1);    %remember [x,y]=ginput(1), so returns col index first, then row index
I=round(I);
J=round(J);
bath.height(J,I)
text(I,J,num2str(bath.height(J,I)));
% get the lat and lon of this point
bath.lat(J)
bath.long(I)

figure(3)
plot(bath.long,bath.height(256,:));

% get the latitude of this row
bath.lat(256)

title('Bathymetry profile at 51.5^oN');
xlabel('Longitude');
ylabel('Height (m)');
hold on;
plot([bath.long(1) bath.long(end)],[0 0],'k--');

%% Part 4: Ocean Salinity

pause
close all;

S=load('salt.txt');

% extract depth, longitude and salinity values into subfields of a structure
sal.long=S(1,2:42);
sal.depth=S(2:34,1);
sal.salinity=S(2:34,2:42);

figure(1)
subplot(211), plot(sal.long,sal.salinity);
subplot(212), plot(sal.salinity,sal.depth);

figure(2)
%imagesc(sal.long,sal.depth,sal.salinity); hold on
contourf(sal.long,sal.depth,sal.salinity,[31.5:.1:35]);
hold on
plot(bath.long,bath.height(256,:));
%hold off;

% The piece to turn in.......
figure(3)
contourf(sal.long,sal.depth,sal.salinity,[31.5:.1:35]);
hold on;
ii=find(bath.lat==48);    % = 361
plot(bath.long,bath.height(ii,:));
ii=find(bath.lat==51.5);  % =256
plot(bath.long,bath.height(ii,:));
ii=find(bath.lat==55);    % =151
plot(bath.long,bath.height(ii,:));
ylim([-5000 1000]);
colorbar
hold off;
xlabel('Longitude');
ylabel('Depth/m');


