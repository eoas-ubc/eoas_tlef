%
% Code associated with interpolation worksheet
% Background for week 11 lab.
%

% preliminaries
clear all;
close all;

% set up my demo function
x=0:0.1:9;
a=0.1;
b=-0.7;
t=x-2;
y=a*t.^3+b*t.^2;

% my unevenly sampled function:  used to produce figure on worksheet
xsamp=[0.3,1.1,3.5,3.9,5.8,8.0];
ksamp=dsearchn(x',xsamp');
ysamp=y(ksamp);

%% interpolate using various interpolation options

dx=1;       % interpolation interval
x2=0:1:9;  % x-vector onto which I want to interpolate my values
y2a=interp1(xsamp,ysamp,x2,'nearest');  % use nearest neighbor interpolation
y2b=interp1(xsamp,ysamp,x2,'linear');   % use linear interpolation
y2c=interp1(xsamp,ysamp,x2,'spline');   % use spline interpolation
y2d=interp1(xsamp,ysamp,x2,'pchip');    % use piecewise cubic interpolation

% figure for in-class demo
figure(2); 
hold on; 
    set(gca,'FontSize',21);
    % plot original points
    plot(xsamp,ysamp,'s-','MarkerFaceColor','k','MarkerSize',10,'LineWidth',2)
    xlim([0 10]); ylim([-6 2]);
    pause;
    children = get(gca, 'children');
    delete(children(1));
    plot(xsamp,ysamp,'s:','MarkerFaceColor','k','MarkerSize',10,'LineWidth',1)
    grid on; 
    xlim([0 10]); ylim([-6 2]);
    pause;
    % plot nearest neighbor interpolation
    plot(x2,y2a,'ro--');
    pause;
    % plot linear interpolation
    plot(x2,y2b,'go--'); 
    pause;
    % plot spline interpolation
    plot(x2,y2c,'bo--');
    pause;
    % plot piecewise cubic -(shape preserving)- interpolation
    plot(x2,y2d,'mo--');
    pause;
    legend('data','nearest','linear','spline','pchip','location','north');
    % plot my original function
    plot(x,y,'k-');
hold off;
pause;

%% Examples with overshoots in interpolated function

% spline - smoother results, i.e. is continuous; more accurate if data
% consists of values of a smooth functions

% shape-preserving piecewise cubic interpolation
% pchip, no overshoots and less oscillation if data are not smooth

x=-3:3;
y=[-1 -1 -1 0 1 1 1];
t=-3:0.01:3;            % interpolate onto finer sampling interval 
ps=interp1(x,y,t,'spline');
pc=interp1(x,y,t,'pchip');
pl=interp1(x,y,t,'linear');

% plot original data and interpolated values
figure(3);
    plot(t,pc,'b-',t,pl,'g--',t,ps,'r',x,y,'s','MarkerFaceColor','k','MarkerSize',10);
    legend('pchip','linear','spline','data','location','best');
    set(gca,'FontSize',21);
pause;

%% Example with overshoots in interpolated and extrapolated functions

% same example as previously, just now extrapolate beyond edges of x array
% so x (original) goes from -3 to 3 but t (interpolated/extrapolated) goes from from -4 to 4
x=-3:3;
y=[-1 -1 -1 0 1 1 1];
t=-4:0.01:4;        % interpolate onto finer sampling interval and extrapolate beyond [-3, +3]
ps=interp1(x,y,t,'spline');
pc=interp1(x,y,t,'pchip');
pl=interp1(x,y,t,'linear');

% plot original data and interpolated & extrapolated values
figure(4);
    plot(t,pc,'b-',t,pl,'g--',t,ps,'r',x,y,'s','MarkerFaceColor','k','MarkerSize',10);
    legend('pchip','linear','spline','data','location','best');
    set(gca,'FontSize',21);
% ================= end demo ===============