%
% code snippets for Week 12, Worksheet 2 for the file handling part.
%
% CLJ Nov 2017

clear all;
close all;
clc;

%% Part B:

strfil='mag001.dat';
%bdata=load(strfil);     % would uncomment this to load the file if it existed.

%% Part C:

for iday=100:365
    strfil=strcat('mag',num2str(iday),'.dat');
    fprintf('%s\n',strfil);
    %bdata=load(strfil);
end

%% Part D:

% setting up the strings: practice with an if, elseif, else statement and loop
fprintf('Part D');
for iday=1:365
    if (iday < 10)
        strfil=strcat('mag00',num2str(iday),'.dat');
    elseif (iday < 100)
        strfil=strcat('mag0',num2str(iday),'.dat');
    else
        strfil=strcat('mag',num2str(iday),'.dat');
    end
    fprintf('%s\n',strfil);         % note that I put this outside the if statement but inside the loop
    %bdata=load(strfil);            % ditto and again would uncomment this to load the files
end

%% an alternative to the above solution

% just doing this for a few days, chosen to show it works for all 3 cases above

fprintf('\n\n Alternative using sprintf - format specifier is %%03d\n');
for iday=[1:3:12,100:100:365]
    strfil=sprintf('mag%03d.dat',iday);
    fprintf('%s\n',strfil); 
end