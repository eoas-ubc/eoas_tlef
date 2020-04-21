
%% Calculations from in-class demo
clear; 
close all;

load lab11_data


%SETUP MATRIX FOR TEMPR AT 10KM
sal0_pro = nan(length(depths), 10);
sal20_pro = nan(length(depths), 10);

% now make a plot that has profiles only where there are data to show
% uneven distribution of casts
 
%INITIALIZE OTHER FIGURES
figure(1); clf; 
figure(2); clf; 

for j=1:10
    
    ii=inds{j};
    subtemp=saln(:,ii); 
    xx=dist200(ii);

    % we want to have a (dist,depth) pair for every salinity measurement
    [mx,my]=meshgrid(xx,depths);
    
    %This is where we do the actual plotting - this uses the built-in function scatter 
    % scatter needs to be passed 1D arrays as arguments so we must flatten mx, my
    figure(1); %ADD TO LOOP TO CHOOSE CORRECT FIGURE ACTIVE
    makeScatterPlot(mx(:),my(:),subtemp(:),j,11-j)      %HAD TO MAKE POINTS BIGGER IN SCATTER....MATLAB RELEASE DIFFERENCE??
    caxis([32 34.2]);
    axis([-20 45 0 91]);  
    title(sprintf('Track %d Salinity',j)); 
    
    %We only want the xlabel on the bottom row of subplots
    if j==1 || j==2 
        xlabel('Distance from Shelf Break/km')
    else
        set(gca,'xticklabel', [])
    end
    
    %INTERPOLATED X AND Y AXES
    [intX,intY] = meshgrid(-20:0.5:40, depths);

    % LINEAR INTERPOLATION
    % change this to 'nearest', 'spline' to get figures 2, 4 of lab that are not turned in
    method = 'nearest';      
    %method = 'linear';        
    %method = 'spline';    
     
    intSalr = interp2(mx, my, subtemp, intX, intY, method);
   
  
    figure(2);
    jj=isfinite(intSalr(:));  %ignore nans because scatter colors nans
    makeScatterPlot(intX(jj), intY(jj), intSalr(jj), j, 11-j);
    caxis([32 34.2]);
    axis([-20 45 0 91]);  
    title(sprintf('Track %d Salinity',j)); 
    
    %We only want the xlabel on the bottom row of subplots
    if j==1 || j==2 
        xlabel('Distance from Shelf Break/km')
    else
        set(gca,'xticklabel', [])
    end
    
    %THE INDEX OF THE 10KM CASTS - FOR LAST PART OF LAB
    [~,ind0k]=min(abs(intX(1,:)-0));
    [~,ind20k]=min(abs(intX(1,:)-20));
    %ind10k=intX(1,:)>9.5 & intX(1,:)<10.5;
    %ind10k=intX(1,:)==10; % line above is better b/c of numerical issues but this works in this example
    %USE LINEAR INTERPOLATION FOR LAST PART OF LAB
    sal0_pro(:,j)=intSalr(:, ind0k);
    sal20_pro(:,j)=intSalr(:, ind20k);
    
end


%% NOW MAKE PLOT OF TEMPERATURES AT 10KM
figure(3); clf; 

zz = repmat(depths, 1, 10);  %Need repmat for quick plotting
subplot(131);  
% hold on;
plot(sal0_pro, depths)
%labels = num2str([1:10]'); %easy way to label the casts
%legend(labels)
set(gca,'FontSize',14);
xlabel('Salinity/(g/kg)');

ylabel('Depth (m)');
axis([31 34.2 0 91])
axis ij; %Remind students to invert y axis
title('a) 0 km');

subplot(132);  
% hold on;
plot(sal20_pro, depths)
%labels = num2str([1:10]'); %easy way to label the casts
%legend(labels)
set(gca,'FontSize',14);
xlabel('Salinity/(g/kg)');
ylabel('Depth (m)');
axis([31 34.2 0 91])
axis ij; %Remind students to invert y axis
title('b) 20 km');

subplot(133); 

meanval=nanmean(sal0_pro, 2);   %need mean of second dimension 
stdval = nanstd(sal0_pro, 2);  %std along second dimension
plot(meanval, depths, 'k', 'linewidth', 2); %one col of zz
hold on;
plot(meanval+stdval, zz, '-k');
plot(meanval-stdval, zz, '-k');

meanval=nanmean(sal20_pro, 2);   %need mean of second dimension 
plot(meanval, depths, '-r', 'linewidth', 2); %one col of zz
stdval = nanstd(sal20_pro, 2);  %std along second dimension
plot(meanval+stdval, zz, '--r');
plot(meanval-stdval, zz, '--r');
set(gca,'FontSize',14);
xlabel('Salinity/(g/kg)');
title('c)');
ylabel('Depth (m)');
axis([31 34.2 0 91])
 axis ij;

%figure(3);print -depsc finalfig

%figure(2);print -depsc interpsec


















