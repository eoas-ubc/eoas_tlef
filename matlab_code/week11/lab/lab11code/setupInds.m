function ind=setupInds
%   SETUPINDS Indices of succesive transects for FK0009A cruise
%   This sets up a 1x10 cell array 'ind' where each cell contains the 
%   indices of successive tracks of Survey E of FK009A cruise.

%Initialize
ind=cell(1,10);

%The indices for tracks 1 through 10
ind{1}=[1:20 22:28];
ind{2}=83:-1:29;
ind{3}=84:132;  
ind{4}=176:-1:133;
ind{5}=177:225;
ind{6}=262:-1:226;
ind{7}=265:318;
ind{8}=362:-1:319;
ind{9}=365:426;
ind{10}=483:-1:426;

end