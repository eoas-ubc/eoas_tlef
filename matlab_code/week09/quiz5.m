%% Mini Quiz #5, Week 10 based on posted reading

clear all;
clc;

x=20;
% What is the result of the following lines of code?

% Q1: (1 point - to screen, text, format)
fprintf(1,'x = 20');

% Q2: (1 point - to screen in red, text, format)
fprintf(2,'x = %2d\n',x);

% Q3: (1 point)
fprintf(1,'%2d divided by 2 is %2d\n',x,x/2);

% Q4: (3 points - open file, write to file, close file)
fid=fopen('results.dat','w');
fprintf(fid,'Here are my results');
fclose(fid);


%% not included
% Q4: (bonus)
fprintf(1,'x = %4.2f\n',x);