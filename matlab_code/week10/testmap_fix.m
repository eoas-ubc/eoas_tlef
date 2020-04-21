clear;

% Get the Dec/Jan/Feb averaged currents
% Each data file consists of lines, written in fortran free format,
% in the form of
% 15000., longitude, latitude, e-w velocity u, s-n velocity v, std. dev u, std. dev v


clf;
subplot(211);

plotarrows_fix('mgsva_MJJ.csv',5,10);

title('Whole world');

subplot(212);

plotarrows_fix('mgsva_MJJ.csv',1,7);

axis([-85 -50 20 45]);
title('Gulf Stream');
 
