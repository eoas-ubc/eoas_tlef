clear all
close all

% Part 1
fprintf('\nUsing exponential notation\n')
fprintf('1234567890\n');  % This will label the columns
fprintf('%8.0e\n',100*pi)
fprintf('%8.1e\n',100*pi)
fprintf('%8.3e\n',100*pi)
%fprintf('%8.5e\n',pi)
fprintf('%8.10e\n',100*pi)

fprintf('\nUsing floating point notation\n')
fprintf('1234567890\n');  % This will label the columns
fprintf('%8.0f\n',100*pi)
fprintf('%8.1f\n',100*pi)
fprintf('%8.3f\n',100*pi)
%fprintf('%8.5f\n',pi)
fprintf('%8.10f\n',100*pi)

fprintf('\nUsing exponential notation\n')
fprintf('1234567890\n');  % This will label the columns
fprintf('%.0e\n',100*pi)
fprintf('%.1e\n',100*pi)
fprintf('%.3e\n',100*pi)
%fprintf('%8.5e\n',pi)
fprintf('%.10e\n',100*pi)

fprintf('\nUsing floating point notation\n')
fprintf('1234567890\n');  % This will label the columns
fprintf('%.0f\n',100*pi)
fprintf('%.1f\n',100*pi)
fprintf('%.3f\n',100*pi)
%fprintf('%8.5f\n',pi)
fprintf('%.10f\n',100*pi)

fprintf('\nUsing g notation\n')
fprintf('1234567890\n');  % This will label the columns
fprintf('%8.0g\n',100*pi)
fprintf('%8.1g\n',100*pi)
fprintf('%8.3g\n',100*pi)
%fprintf('%8.5g\n',pi)
fprintf('%8.10g\n',100*pi)

%% Part 2
% Demonstrating that format specifiers are vectorized

fprintf('\nDemonstrating that format specifiers are vectorized - I\n');
fprintf('%10.2f\n',exp(1:10));
fprintf('\nDemonstrating that format specifiers are vectorized - II\n');
fprintf('%10.2f %10.2f\n',exp(1:10));

% Part 3
% printing to a string for plotting

n=3;
x=cumsum(randn(50,n));
plot(x);
ylim([-20 20])
str=sprintf('we are showing %d lines',n);
text(1,10,str);


