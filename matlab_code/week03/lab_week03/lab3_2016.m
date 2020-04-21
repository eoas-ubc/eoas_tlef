% lab 3 2015

clear all; 
close all;

%% Part2:  Ocean Color / SST

%A=imread('T20151822015212.L3m_MO_NSST_sst_9km.nc.png');
%A=imread('T20151822015212.L3m_MO_CHL_chl_ocx_9km.nc.png');
[A,CMAP]=imread('V20152442015273.L3m_MO_SNPP_CHL_chlor_a_9km.nc.png');
image(A);
xlabel('Column index');
ylabel('Row index');
colormap(CMAP);
%set(gca,'ydir','normal');
nA=size(A)

% % old version
% A=imread('ModisChlAJan2013.png');
% image(A);
% set(gca,'ydir','normal');
% nA=size(A)

image(0:255)

A(1200,500,:)

WNA=A(300:650,1350:1700,:);
figure(2),
image(WNA);


nA=size(A)
lat=90-180*[1:nA(1)]/nA(1);
lon=-180+360*[1:nA(2)]/nA(2);

%figure(99)
image(lon, lat,A);
set(gca,'ydir','normal');
xlabel('Longitude');
ylabel('Latitude');


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

figure(2)
imagesc(bath.height);
colorbar;

[I,J]=ginput(1);
I=round(I);
J=round(J);
bath.height(J,I)
text(I,J,num2str(bath.height(J,I)));

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

sal.long=S(1,2:42);
sal.depth=S(2:34,1);
sal.salinity=S(2:34,2:42);

figure(1)
subplot(211), plot(sal.long,sal.salinity);
subplot(212), plot(sal.salinity,sal.depth);

figure(2)
%imagesc(sal.long,sal.depth,sal.salinity); hold on
contour(sal.long,sal.depth,sal.salinity,[31.5:.1:35]);
%hold off;

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


