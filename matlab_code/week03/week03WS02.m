%
% Worksheet #1, Week 03
%
clear all;
close all;
%% Exercise 1

lats=[1:20]; lats=[10:15]
pause

L2 = lats([2 4])
pause

%L3 = lats([1 0])

%L4 = lats([1 1 0 0 1 1])

L5 = lats(logical([1 1 0 0 1 1]))
pause

L6 = lats(end-2:end)
pause

L7 = lats(length(lats))
pause

ii=lats>12; lats(ii)

%% Exercise 2
clear all

lats = [10:20]
pause

lat_table = [lats(1:5); lats(6:10)]
pause

lat_table(2,[1,2])
pause

lat_table([1,2],2)
pause

%lat_table([1,0],2)

lat_table(logical([1,0]),2)
pause

lat_table(5)
pause

lat_table(1:4)

%% Exercise 3

clear all

mystruc.name='Joe Lunchbucket'   % field 1 is a string
mystruc.date=datenum(2000,8,15)  % field 2 is a number
mystruc.marks={10,8,'A','C',87}  % field 3 is a cell array

mystruc.name(1:3)

mystruc.marks(1)

mystruc.marks{1}

mystruc.name = 'Jim bulldozer'  % replaces the contents of the name field in structure mystruc.

mystruc

%% Exercise 4

A = 1:10;
X = rem(A,2)
B = A(logical(~X))
