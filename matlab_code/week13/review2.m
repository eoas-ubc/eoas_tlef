
%
% Review sheet 1: week 13:  Debugging

%% Math 1
A=[1 5 3 0 1]; B=[0 5 6 0 1];
C=A./B + 4

%% Math 2:
pause;

A=10-[1:4]*2;
C=sum(A/10)-2
D=C~=0

%% Debug 1

pause; 

x=1:10;
y=2*x;
sum=0;
while(sum1 + y(i) < 12)
    sum1=sum1+y(i);
    i=i+1;
end
fprintf('Sum=%3.1f, i=%3d\n',sum1,i-1);

pause;
% fix 1
x=1:10;
y=2*x;
sum1=0;
while(sum1 + y(i) < 12)
    sum1=sum1+y(i);
    i=i+1;
end
fprintf('Sum=%3.1f, i=%3d\n',sum1,i-1);

pause;
% fix 2
x=1:10;
y=2*x;
sum1=0;
i=1;
while(sum1 + y(i) < 12)
    sum1=sum1+y(i);
    i=i+1;
end
fprintf('Sum=%3.1f, i=%3d\n',sum1,i-1);


% general problem e.g. y=x./x;
pause;
x=1:10;
y=x./x;
sum1=0;
i=1;
while(sum1 + y(i) < 12)
    sum1=sum1+y(i);
    i=i+1;
end
fprintf('Sum=%3.1f, i=%3d\n',sum1,i-1);

%  fix for general problem
% general problem e.g. y=x./x;
pause;
x=1:10;
y=x./x;
sum1=0;
i=1;
while(i<=length(y) && (sum1 + y(i) < 12))
    sum1=sum1+y(i);
    i=i+1;
end
fprintf('Sum=%3.1f, i=%3d\n',sum1,i-1);

%% Debug 2

a=1:3:30;
b=sin(a);
c=tan(a);
d=(a.*b)./c;
plot(a,d)

%% Code writing 1

a(1)=0;
a(2)=1;
maxterm=5000;
i=2;

while(a(i)<maxterm)
    i=i+1;
    a(i)=a(i-1)+a(i-2);
end
fprintf('# terms < %d is %d\n',maxterm,i-1);
