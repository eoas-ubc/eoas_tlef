% review sheet for week 13:  solutions/code snippets for questions 1,2,5,6,7
% consult your notes from class for the solutions for questions 3 and 4
% question 8 is for you to do!  it's very similar to some from earlier in
% term

clear all
close all
%% QUESTION 1:

fprintf('\nQUESTION 1 dimensions and element-wise versus matrix algebra \n\n')
a = [1 2; 3 -1; 0 1];
b = [3:-2:-2]';
c = ones(3);

fprintf('Dimensions of a are %d rows by %d cols \n', size(a))
fprintf('Dimensions of b are %d rows by %d cols \n', size(b))
fprintf('Dimensions of c are %d rows by %d cols \n', size(c))
fprintf('Dimensions of b''.*a are %d rows by %d cols \n', size(b'*a))
fprintf('Dimensions of a.^2 are %d rows by %d cols \n', size(a.^2))
fprintf('Dimensions of a*a'' are %d rows by %d cols \n', size(a*a'))
fprintf('a^2 is not defined: MATLAB Error using ==> mpower,  Matrix must be square.\n')

%% QUESTION 2

A=[1 5 3 0 1];
B = [0 5 6 0 1];

fprintf('\n --- Question 2\n');
C=A./B + 4


%%  QUESTION 3 AND QUESTION 4

%
% We went over these in class - see your class notes
%

%% QUESTION 5: 

fprintf('\nQUESTION 3: precedence \n\n')
a=3;
x1=[2^a+a*2+1,a^sum([2:-1:0, -4])];
x2=a^3-2^a;
fprintf('Qn1: x1 = [%d, %f] \nQn2: x2 = %d\n',x1,x2);

%% QUESTION 6: writing to a string (also practice with repetition and conditional statements)

fprintf('\nQUESTION 6:  writing to a string \n\n')

n=11;
for i=1:n
    if (i<10)
        fname=sprintf('file0%1d.dat',i);
    else
        fname=sprintf('file%2d.dat',i);
    end
    fprintf('Filename %d is %s\n',i, fname);
end


%  play around with incorrect fprintf statements also, or ones like
f=1:6;
fprintf('\n playing with formatting some more \n');
fprintf('\ncount f is %d\n',f);

%% QUESTION 7:

fprintf('\nQUESTION 5: opening files to read/ write \n\n')

str='myfile.dat';

% NONE OF THESE WORK BECAUSE "myfile.dat" has  been passed 
% as a variable which is undefined.
%     fid1 = fopen(myfile.dat, 'r');
%     fid2 = fopen(myfile.dat);
%     fid3 = fopen(myfile.dat, 'w');

%These will all work and open a file - 1 and 2 only open for read access
fid1 = fopen('myfile.dat', 'r');
fid2 = fopen('myfile.dat');
fid3 = fopen('myfile.dat', 'w');
% test #3 - if you test #s 1 and 2 with these two lines you'll get an error
fprintf(fid3,'stuff');
fclose(fid3);

%% QUESTION 8 
%
% this one is for you to do!!!
%

%%
clear
clc
fprintf('\n\n**************************************************\n\n')
fprintf('*** you''re on your own now - Good Luck & Happy Holidays! ***\n\n')
fprintf('**************************************************\n\n')