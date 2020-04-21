function fancyprint(Str)
%
% Print the string Str with * at the beginning and end of 
% the string.
% 
WrappedStr = wrapstr(Str);
disp(WrappedStr);

function Newstr = wrapstr(Str)

Newstr(1) = '*';
Newstr(2:length(Str)+1) = Str;
Newstr(end+1) = '*'; 
