% EOSC 211.    October 2017

% Week 09: Tuesday class
% Script containing demos for formatted output
% 
% Demos:  sprintf, fprintf, fopen, fclose, text
% Various format specifiers for use with fprintf, sprintf

clc;
clear;
close all;

%  EXAMPLE 1:  PRINTING A STRING TO THE SCREEN, USING \n
fprintf('Example of printing to the screen')    % no \n at end - see what happens
pause
fprintf('perhaps I forgot something for more printing\n') % now the \n
pause
fprintf('like a special character \\n to do a carriage return\n') % how to write \n in the string
pause
fprintf('Or I could have just left a space ')
pause
% note that I can also print to the screen by setting fid=1 as follows:
fid=1;
fprintf(fid,'like this or a tab \t like this \n\n')
pause
fprintf(fid,'********************************************\n')
% and fid=2 prints to standard error
fid=2;
fprintf(fid,'setting fid=2 prints to standard error (the screen, but in RED)\n')
fprintf(fid,'********************************************\n\n')
pause
%%
% EXAMPLE 2: DEMOS OF FORMATTED OUTPUT OF INTEGER OR REAL NUMBER
clc
fprintf('Demos for formatted output of the variable x = 53\n\n')
x=53;
fprintf('printing an integer, x = %2d\n', x)
fprintf('printing a real # using fixed point format, x = %4.1f\n', x)
fprintf('printing a real # using exponential format, x = %7.1e\n', x)
fprintf('printing a real # using integer format, x = %2d\n', x)
pause

%%
% FORMATTING NUMBER DEMOS IN GORY DETAIL.....
% TRY OTHERS IN THE LAB

clc
fprintf('More Demos for formatted output of the variable x = 53\n\n')
fprintf('printing a real # using integer format, x = %1d\n', x)
fprintf('printing a real # using integer format, x = %2d\n', x)
fprintf('printing a real # using integer format, x = %3d\n', x)
fprintf('printing a real # using integer format, x = %4d\n', x)

pause;
fprintf('********************************************\n')
fprintf('\nFormatted output using the variable pi = %10.8f\n\n',pi)

fprintf('1234567890 \t\t column numbers \n');  % This will label the columns
fprintf('%7.1f \t\t output using %%7.1f \n',pi);
fprintf('%9.1f \t\t output using %%9.1f \n',pi);  % two more columns
fprintf('%2.1f \t\t\t output using %%2.1f \n\n',pi);  % one less column
pause

fprintf('1234567890 \t\t column numbers \n');  % This will label the columns
fprintf('%7.2e \t\t output using %%7.2e \n',pi);
fprintf('%9.1e \t\t output using %%9.1e \n',pi);  % two more columns
fprintf('%4.1e \t\t output using %%4.1e \n',pi);  % one less column
fprintf('%4.0e \t\t\t output using %%4.0e \n\n',pi);  % one less column
pause

%%
% DEMO:   PRINTING TO A STRING
stringpi=sprintf('%3.1f',pi);


%%
% DEMO: OUTPUTTING TO A TEXT FILE

fid=fopen('ClassExample.txt','w');
fprintf(fid,'Mode   Time    Distance \n');
fclose(fid);


% we could also have checked this by printing to the screen
fid=1;
fprintf(fid,'\n\n Mode   Time    Distance \n\n');



