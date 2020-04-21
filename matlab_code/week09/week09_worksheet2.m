%
%  

% what does the following code snippet do?
clear all;
close all;

n=3;
fid=fopen('filenames.txt','w');

for ii=1:n
    myfile=sprintf('f%1d.txt',ii);   
end

%%
% what line of code should be added to the code above to write out 
% the content(s) of variable "myfile" to the file "filenames.txt"
% Now write the line of code to close the file

n=3;
fid=fopen('filenames.txt','w');

for ii=1:n
    myfile=sprintf('f%1d.txt',ii);   
    fprintf(fid,'%s\n',myfile);
end

fclose(fid);

%%

x = 1:3:11;

% What does the following code snippet do?
y=sum(x);

fprintf('The sum of the values in x is %4d\n',y);

% How would you output the result of computing half the mean value of x to a
% file called "xdata.txt"?  You can use the built-in matlab function ?mean?

f34=fopen('xdata.txt','w');
fprintf(f34,'Half the mean value of x is %4.2f\n',mean(x)/2);
fclose(f34);

% Now write a line of code that will also write the values contained in x to the
% file xdata.txt.  Output this information in the first line of the file.
% Format your output as follows: e.g. if x = 1:4, the first line should read
% x = [1, 2, 3, 4]

fprintf(2,'x = [ %d %d %d %d ]\n',x);
% not this
fprintf(2,'x = [ %d ]\n',x);
% but this is ok
fprintf(2,'x = [');
for ii=1:length(x)
    fprintf(2,'%d ',x(ii))
end
fprintf(2,']\n');
fprintf(2,'Half the mean value of x is %4.2f\n',mean(x)/2);


f35=fopen('xdata2.txt','w');
fprintf(f35,'x = [ %d %d %d %d ]\n',x);
fprintf(f35,'Half the mean value of x is %4.2f\n',mean(x)/2);
fclose(f35);

% can discuss the fact that this is ok for small x where we know how many
% elements of x there are.  
