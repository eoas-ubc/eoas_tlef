% lab 3 2015

clear all; 
close all;

%% Part2:  Ocean Color / SST

A=imread('T20151822015212.L3m_MO_NSST_sst_9km.nc.png');
A=imread('T20151822015212.L3m_MO_CHL_chl_ocx_9km.nc.png');
image(A);
%set(gca,'ydir','normal');
nA=size(A)

% % old version
% A=imread('ModisChlAJan2013.png');
% image(A);
% set(gca,'ydir','normal');
% nA=size(A)

A(1200,500,:)

WNA=A(300:650,1350:1700,:);
figure(2),
image(WNA);

lat=90-180*[1:nA(1)]/nA(1);
lon=-180+360*[1:nA(1)]/nA(1);

figure(99)
image(lon, lat,A);
set(gca,'ydir','normal');

%% Part 3a: getting the bathy file and plotting

pause
clear all;
close all;

load Bathyfile.mat;
figure(1)
imagesc(bath.long,bath.lat,bath.height);
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
plot(bath.long,bath.height(256,:));
ylim([-5000 1000]);
colorbar
hold off;


