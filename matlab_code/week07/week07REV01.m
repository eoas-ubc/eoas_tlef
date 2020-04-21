%
% week 7 - review worksheet
%
%% EXERCISE1:If a=[7654321];,what would be the values of b,c, d, and e if:

a=[7 6 5 4 3 2 1]

b=a(1:3:7)

c=[a/2;-a]

d=a(1:2).*a(6:7)

e=[1 1;2 2]'.*[a([1 2]);a([2 3])]


%% EXERCISE 2: What is the result of the following expressions? 

1:6==2+3*1

1>6:2*3+1

3^0/4--3/4:3

3^0/4-(-3/4:3)

%% EXERCISE 3: This piece of matlab code is supposed to find local minimums in the input time series, 
% i.e. points that have values less than their neighbours on either side, and return their indices in x. 
% But it has some bugs in it. Explain what they are and fix them.
% y is a 1x100 vector given as input
% % k=1;
% % while k<100,
% %    if y(k)<y(k+1) & y(k)>y(k-1),
% %       x(k)=k;
% % k=k-1 end;

ipts=1:100;
y = rand(1,length(ipts));
k=2;                                % need to start at 2nd point
i = 0;                              % need second counter
                                    % could start this with i=1: if so
                                    % line 45 (i=i+1) should go after x(i) = k
while k<100                         % , not needed
   if y(k)<y(k+1) && y(k)<y(k-1)	% (1) &&, (2) second > should be <  (3) , not needed
      i = i+1;                      % increment local minimum counter
      x(i)=k;                       % x(i) = k
   end                              % missing end
   k=k+1;                           % should be k=k+1;  semicolon nice, not reqd 
end                                 % don't need the ; but not critical

% plot it to check
plot(ipts,y,'ko-',x,y(x),'r*');
set(gca,'FontSize',24);
legend('original data','local minima')