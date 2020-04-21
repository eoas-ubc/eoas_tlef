%
% Notice that in this lab we are doing pretty much the same thing, 4
% times in a row. 
%
%                LOOPLOOPLOOPLOOPLOOPLOOP!
%
% But how, you are asking! Here you go:

load commute.mat

% here's the secret - set up arrays for everything
modes=['R';    'B';  'C';  'W' ];
labels={'Bike','Bus','Car','Walk'};
lcol= ['m';    'b';  'g';  'r'];
lmark=['d';    's';  '^';  'o'];
 
% Compute what you need...and put it all into arrays
for k=1:length(modes),
  ival=md==modes(k);
  num(k)=sum(ival);
  meantim(k)=mean(mins(ival));  % mins
  meandis(k)=mean(km(ival));  % km
%  meanspd(k)=meandis(k)/meantim(k)*60;  % kmh
  meanspd(k)=nanmean(km(ival)./mins(ival))*60;  % kmh
end;

% Now, make the plot....
clf;
set(gcf,'defaultaxestickdir','out','defaultaxesfontsize',14);
for k=1:length(modes),
  ival=md==modes(k);
  line(km(ival),mins(ival),'marker',lmark(k),'color',lcol(k),'linestyle','none','markerfacecolor','w');  
end;

%....and pretty it up
title('2018 Commuting Stats');
xlabel('Distance/km');
ylabel('Time/mins');
set(gca,'tickdir','out');

% ...oh yeah, add the labels.
 
for k=1:4,
  line([0 meandis(k)],[0 meantim(k)],'linewi',2,'color',lcol(k));
  text(meandis(k),meantim(k),sprintf('speed = %.1f kmh',meanspd(k)));
end;
legend(labels,'location','southeast');
  
  
% Open file....
fid=fopen('commute.txt','w');

% ...write header
fprintf(fid,'%6s %10s %10s %10s %10s\n','Mode','# people','Time',  'Distance','Speed ');
fprintf(fid,'%6s %10s %10s %10s %10s\n',' ',   ' ',       '(mins)','(km)',    '(kmh)');
fprintf(fid,'%1s',repmat('=',1,6+10+10+10+10+4));
fprintf(fid,'\n');

% ...and data
for k=1:length(modes),
  fprintf(fid,'%6s %10d %10.1f %10.1f %10.1f\n',labels{k},num(k),meantim(k),meandis(k),meanspd(k));
end;

fclose(fid);
 
