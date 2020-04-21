%
% Week 09:  Thursday - left-over stuff from Tuesday class

clear;
close all;
clc

% Part 3 of Lab7.  NOW USE PRINTING TO A STRING TO ADD A TEXT LABEL
% TO A FIGURE

fprintf(2,'Making a plot now...and using sprintf......\n');
n=3;
x=cumsum(randn(50,n));
plot(x,'*-');
ylim([-20 20])
str=sprintf('we are showing %d lines',n);
text(1,15,str);
str2=sprintf('label the 10th point along the 1st line');
text(10,x(10,1),str2);

pause

%%  
%  VECTORIZED O/P - what can go wrong

fprintf('Things that can go wrong....\n\n');
fprintf('%9.4e',pi,pi,pi);
fprintf('\n\n');

pause

%%
x=2:2:10;
y=3*x;
fprintf('\n\n');
fprintf('%2d',x);  %this isnot quite right for the last 2 numbers

pause;

fprintf('\n\n Want to now print pairs of x,y values\n');
x
y

pause;
fprintf(2,'Not quite correct...\n');
fprintf(2,' x y\n');
fprintf(2,'-----\n');
fprintf(2,'%2d%2d\n',x,y);

fprintf('\n\n Better.....\n');
M=[x;y];
fprintf(' x  y\n');
fprintf('------\n');
fprintf('%2d %2d\n',M);

