


% now make a plot that has profiles only where there are data to show
% uneven distribution of casts
figure(1); clf; k=0;
hold on;

for j=10:-1:1
    %pause;
    
    % extract temps and distances
    ii=inds{j};
    subsal=saln(:,ii);     
    xx=dist200(ii);
      
    % we want to have a (dist,depth) pair for every temp measurement
    [mx,my]=meshgrid(xx,depths);
    [newx,newy]=meshgrid(0,depths);
    [newx2,newy2]=meshgrid(20,depths);
    subsal2=interp2(mx,my,subsal,newx,newy,'linear');
    subsal3=interp2(mx,my,subsal,newx2,newy2,'linear');
    %This is where we do the actual plotting - this uses the built-in function scatter 
    % scatter needs to be passed 1D arrays as arguments so we must flatten mx, my
    k=k+1; 
    figure(1);         %ADD TO LOOP TO CHOOSE CORRECT FIGURE ACTIVE - not essential here but important in lab
    makeScatterPlot(newx(:),newy(:),subsal2(:),j,k);
    figure(2)
    makeScatterPlot(newx2(:),newy2(:),subsal3(:),j,k);
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

sal0_pro(:,j) = subsal2;
sal20_pro(:,j) = subsal3;

if k==9 | k==10 
        xlabel('Distance from Shelf Break (km)')
    else
        set(gca,'xticklabel', [])
end



% Plotting depth profiles at a common distance X--------------------------

figure(3);

% Plotting depth profiles at X = 0km
subplot(1,3,1);
plot(sal0_pro,depths);
set(gca,'ydir','reverse');
xlabel('Salinity/(g/kg)');
ylabel('Depth (m)');
title('Depth Profile at X = 0 km','fontsize',8);

% Plotting depth profiles at X = 20km
subplot(1,3,2);
plot(sal20_pro,depths);
set(gca,'ydir','reverse');
xlabel('Salinity/(g/kg)');
ylabel('Depth (m)');
title('Depth Profile at X = 20 km','fontsize',8);

% Calculating mean salinity and its standard deviation
for a = 1:length(depths)
sal0_mean(a) = nanmean(sal0_pro(a,:));
sal0_std(a) = nanstd(sal0_pro(a,:));
sal20_mean(a) = nanmean(sal20_pro(a,:));
sal20_std(a) = nanstd(sal20_pro(a,:));
end

sal0_mean_plus = sal0_mean + sal0_std;
sal0_mean_minus = sal0_mean - sal0_std;
sal20_mean_plus = sal20_mean + sal20_std;
sal20_mean_minus = sal20_mean - sal20_std;

% Plotting mean and standard deviation lines

subplot(1,3,3);
plot(sal0_mean,depths,'k','Linewidth',2);
hold on;
plot(sal0_mean_plus,depths,'k');
plot(sal0_mean_minus,depths,'k');

plot(sal20_mean,depths,'r','Linewidth',2);
plot(sal20_mean_plus,depths,'r--');
plot(sal20_mean_minus,depths,'r--');

xlabel('Salinity/(g/kg)');
ylabel('Depth (m)');
title('Mean depth Profile at X = 0km and X = 20km','fontsize',8);
set(gca,'ydir','reverse');

% Print to screen

fprintf('Yes, the two mean profiles differ by more than the standard deviation in the data');
