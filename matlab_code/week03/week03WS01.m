%
% Worksheet #1, Week 03
%
clear all;
close all;

%% Exercise 1

var1=[1.1; 2.2; 3.3; 4.4; 5.5]

var2 = [10, 11, 12]
var2=10:12

var3=[101:103; 201:203];

var4=[]

var5=2400:3399;
% var5(end-3:end)
% 
% var6=var5';
% size(var6)

str1='class'

%% Exercise 2

bvar1=var1(3)
pause; 

bvar2=var2(2)
pause; 

bvar3=var1([1 2 3])
pause; 

ii=[1 2 5]; bvar4=var1(ii)
pause; 

bvar5=var3(2,2)
pause; 

bvar6=var3([1 2],2)
pause; 

bvar7=var3([1 2], [2,3])
pause; 

bvar8=var3(4)
pause; 

bvar9=var2(:)
pause; 

bvar9=var3(:)
pause; 

bstr1=str1(3:4)
pause; 

bvar10=var1(var1(2))
pause; 
%%
bvar11=var1(3); bvar11=var1(4);
pause; 

bvar12=var1(1,5);
pause; 
%%
bvar13=var1(5,1)
pause; 

bvar14=var2(1,3)
pause; 

bvar16=[]; bvar16(2:4)=var3(1,:)
pause; 

%% Excercise 3
clear all

B={'sky', 3.4, [2 4 5]}; B{1}(2)

A.var1={8, 30, 'R'}
A.var2=2
A.var3=A.var1{A.var2}
