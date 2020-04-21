function [y1,y2] = sqrtsum(x1,x2)

%
% Example of function that takes 2 input variables and returns 2 output variables
%   computes y1 = sum of x1 and x2, and y2 = sqrt of sum of x1 and x2
%
% Inputs: x1, x2
% Outputs: y1, y2
%
%=======================================================================

checkinputs(x1,x2);

y1 = x1 + x2;
y2 = sqrt(y1);

end                 % end the function

% note that this sub function goes AFTER the "end" of the main function 
function checkinputs(c1,c2)

if (c1+c2 < 0)      % variables c1 and c2 are local to the subfunction "checkinputs"
    error('hello')
end                 % end the "if" statement

end                 % end the subfunction