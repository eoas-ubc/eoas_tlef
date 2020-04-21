function distance = shortest_dist(lon, lat, lineLon, lineLat)
% SHORTEST_DIST finds shortest distance from a point to a line.
%      DISTANCE = SHORTEST_DIST(LON,LAT, LINELON, LINELAT) Loops 
%      through each element in LAT and LON and finds the minimum 
%      distance from that point to the line given by LINELAT and 
%      LINELON. For example, if LINELON and LINELAT specify the 
%      200 m contour, SHORTEST_DIST finds the shortest distance of 
%      each point given by lon and lat to that contour.


if length(lat)~=length(lon)  
    error('Inputs Lat and Long must be the same length')
end

%Initialize new variable
distance = nan(size(lat)); 

%Loop through each measurement
for i = 1:length(lat)
    
    %Minimize the square-root of the square of the difference
    [distance(i) ind]= min( sqrt( ((lineLat-lat(i))*111).^2 + ...
                                  ((lineLon-lon(i))*111*cosd(48.5)).^2) );
    
    %If the point is to the LEFT of the 200 m contour, write the distance
    %as negative value
    if lon(i)<lineLon(ind)
        distance(i) = -distance(i); 
    end
end

end





