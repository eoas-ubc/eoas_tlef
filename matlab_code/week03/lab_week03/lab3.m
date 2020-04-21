%% Now work with the salinity data
clear
close all

S=load('salt.txt');
load('Bathyfile.mat')

%First row gives longitude. First column gives depth. Everything else is S
sal.salinity = S(2:end, 2:end);
sal.depth = S(2:end, 1);
sal.long = S(1, 2:end);

%Find indices of 48N 51.5N and 55N
ii=[];
ii(1)=find(bath.lat==48);
ii(2)=find(bath.lat==51.5);
ii(3)=find(bath.lat==55);

figure(1), hold on;
    contourf(sal.long, sal.depth, sal.salinity, [31.5:.1:35])
    colorbar;
    set(gca,'FontSize',14);
    plot(bath.long, bath.height(ii,:))
    ylim([-5500 3000])
    xlabel('Longitude');
    ylabel('Latitude');
    legend('Salinity contours','48^o N','51.5^o N', '55^o N','Location','Best');
    title('Contours of Salinity with Bathymetry at 48^o N, 51.5^o N and 55^o N')
hold off;






























