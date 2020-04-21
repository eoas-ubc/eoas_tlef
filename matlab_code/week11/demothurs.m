% Worksheet for class, week 11

clear all;
clc;

Mmerc=3.3e23;
bigG=6.67e-011;
Rmerc=2440e03; 

vx=0;
vy=7000;
sx=-3050e03;
sy=-3*Rmerc;

dt=60;

% line 1
fprintf(' vx = %.3e  vy= %.3e \t  sx = %.3e  sy = %.3e\n',vx,vy,sx,sy);

%% rest of line 1
s=sqrt(sx.^2+sy.^2);
a=bigG*Mmerc/s^2;
ax=-a*sx/s;
ay=-a*sy/s;

fprintf('  s = %.3e\t a = %.3e\t  ax = %.3e\t ay = %.3e\n\n', s,a,ax,ay);

%% line 2

dvx=vx+ax*dt;
dvy=vy+ay*dt;
dsx=vx+ax*dt^2/2;
dsy=vy+ay*dt^2/2;

vx=vx+dvx;
vy=vy+dvy;
sx=sx+dsx;
sy=sy+dsy;

s=sqrt(sx.^2+sy.^2);
a=bigG*Mmerc/s^2;
ax=-a*sx/s;
ay=-a*sy/s;

fprintf('dvx = %.3e dvy= %.3e \t dsx = %.3e  dsy = %.3e\n',dvx,dvy,dsx,dsy);
fprintf(' vx = %.3e  vy= %.3e \t  sx = %.3e   sy = %.3e\n',vx,vy,sx,sy);
fprintf('  s = %.3e\t a = %.3e\t  ax = %.3e\t ay = %.3e\n\n', s,a,ax,ay);