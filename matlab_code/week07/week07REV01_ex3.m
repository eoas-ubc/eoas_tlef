%% Review, EXERCISE 3: This piece of matlab code is supposed to find local minimums in the input time series, 
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

%%  Week 06 Worksheet 03, Exercise 2

% Here is one solution
total = 1;          % start the sum 
num = 1;            % j'th term in the series referred to by "num" here
term = (1+2*num)^(-2);      % first term in the series - this has the value 1/9 which is > 0.0001;
while (term >= 0.0001)
    total = total + term;
    num = num + 1;          % this could go before previous line of code
    term = (1+2*num)^(-2);
end
num = num-1;        % need to adjust num at end
[num total]   
 
% -------------------------------------------------------------
% Here is another
total = 1;          % start the sum 
num = 0;            
term = (1+2*(num+1))^(-2);      % first term in the series - this has the value 1/9 which is > 0.0001;
while (term >= 0.0001)
    total = total + term;
    num = num + 1;
    term = (1+2*(num+1))^(-2);
end
[num total]
    
        
    