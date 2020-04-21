function makeScatterPlot(dist,depth,z,track,jplot)

%USE: makeScatterPlot(dist,depth,z,track,jplot)
%
%Makes scatter plot of the variable 'z', with x-coordinates given by
%dist and y-coordinates by depth. Variable track is an integer, giving
%the track number. Variable jplot is an integer giving the plot # (1-10)

    %This is where we do the actual plotting - scatter needs 1D arrays
    subplot(5,2,jplot);
    scatter(dist, depth, 8, z, 'filled');
    set(gca, 'fontsize', 10, 'ydir', 'reverse','tickdir','out','box','on') 
    ylabel('Depth/m');  
end