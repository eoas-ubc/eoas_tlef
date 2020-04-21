
% first cat all the commute.m files into 1:  cat */*/commute.m >
% alldata_raw.dat and edit out all comments by hand -> alldata_edt.txt
% for loop goes through length of file

clear all;
close all;

 fid=fopen('alldata_edt.dat');
 N=105;
 
 km=NaN(N,1);
 mins=km;
 md=char(zeros(N,1));
 
 
 for k=1:N,
     l=fgetl(fid);
     [vals]=sscanf(l(1:end),'%f %f %s')
     km(k)=vals(1);
     mins(k)=vals(2);
     md(k)=upper(vals(3));
 end
 fclose(fid);

%stuff=importdata('alldata_edt.dat');
%[N,m]=size(stuff);
%
%km=NaN(N,1);
%mins=km;
%md=char(zeros(N,1));
%
%for k=1:length(stuff)
%    vals=sscanf(stuff{k},'%f %f %s');
%    km(k)=vals(1);
%    mins(k)=vals(2);
%    md(k)=vals(3);
%end

%%
save commute.mat km mins md

%%

clear all;
load commute.mat
   
md=upper(char(md));

ibus=(md=='B');
icar=(md=='C');
iwalk=(md=='W');
ibike=(md=='R');

% Check if all possibilities
bad_mode_id=length(km)-(sum(ibus)+sum(icar)+sum(iwalk)+sum(ibike))

figure(1)
set(gcf,'defaultaxestickdir','out');
plot(km(ibus),mins(ibus),'bo');
line(km(icar),mins(icar),'marker',  'd','linest','none','color',[0 .5 0],'linewi',1);
line(km(iwalk),mins(iwalk),'marker','s','linest','none','color','r');
line(km(ibike),mins(ibike),'marker','p','linest','none','color','c');

line([0 50],[0 50]*mean(mins(ibus))./mean(km(ibus)));
line([0 50],[0 50]*mean(mins(icar))./mean(km(icar)),'color',[0 .5 0],'linewi',1);
line([0 50],[0 50]*mean(mins(iwalk))./mean(km(iwalk)),'color','r');
line([0 50],[0 50]*mean(mins(ibike))./mean(km(ibike)),'color','c');
xlabel('Distance/km');
ylabel('Time/minutes'); title('211 Commute Times to School: Fall 2018');
axis([0 50 0 150]);
set(gca,'tickdir','out');

legend({'Bus','Car','Walk','Ride'},'location','southeast');

print -dpng commute18
%% the plot I ask them to make with no point labels yet

figure(2)
plot(km(ibus),mins(ibus),'ob'); hold on
plot(km(icar),mins(icar),'dm');
plot(km(iwalk),mins(iwalk),'sr');
plot(km(ibike),mins(ibike),'vg');
xlabel('Distance (km)');
ylabel('Time (mins)');
legend('Bus','Car','Walk','Ride','Location','SouthEast');
title('211 Class Commuting Data:  Fall 2018');
