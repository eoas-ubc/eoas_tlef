load commute

%Bus
minsB=mins(md=='B');
kmB=km(md=='B');

%Bike
minsM=mins(md=='R');
kmM=km(md=='R');

%Walk
minsW=mins(md=='W');
kmW=km(md=='W');

%Car
minsC=mins(md=='C');
kmC=km(md=='C');

%Plotting a graph distance vs. time
hold on;
plot(kmB,minsB,'bs'); 
plot(kmM,minsM,'md'); 
plot(kmW,minsW,'ro'); 
plot(kmC,minsC,'g^'); 
xlabel('Distance (km)');
ylabel('Time (mins)');
title('Distance vs. Time');

%Bus
MDB=mean(kmB);
MTB=mean(minsB);
SB=kmB./(minsB./60);
MSB=mean(SB);
strB=sprintf('speed = %0.2f kmh.',MSB);

%Bike
MDM=mean(kmM);
MTM=mean(minsM);
SM=kmM./(minsM./60);
MSM=mean(SM);
strM=sprintf('speed = %0.2f kmh.',MSM);

%Walk
MDW=mean(kmW);
MTW=mean(minsW);
SW=kmW./(minsW./60);
SW(isnan(SW))=0;
MSW=mean(SW);
strW=sprintf('speed = %0.2f kmh.',MSW);

%Car
MDC=mean(kmC);
MTC=mean(minsC);
SC=kmC./(minsC./60);
MSC=mean(SC);
strC=sprintf('speed = %0.2f kmh.',MSC);

plot([0 MDB],[0 MTB],'b');
plot([0 MDM],[0 MTM],'m');
plot([0 MDW],[0 MTW],'r');
plot([0 MDC],[0 MTC],'g');
lgd=legend('Bus','Bike','Walk','Drive');
title(lgd,'Mode of Commuting');

%Labeling endpoints
text(MDB,MTB,strB);
text(MDM,MTM,strM);
text(MDW,MTW,strW);
text(MDC,MTC,strC);

%Defining new vectors for txt writing
BUS=[length(minsB),MTB,MDB,MSB];
BIKE=[length(minsM),MTM,MDM,MSM];
WALK=[length(minsW),MTW,MDW,MSW];
CAR=[length(minsC),MTC,MDC,MSC];

%Writing a txt file
fid=fopen('commute.txt','w');
fprintf(fid,'%20s %20s %30s %25s %25s\n','Transportation mode','Number of people','Average commute time (mins)','Average distance (km)','Average speed (kmh)');
fprintf(fid,'%20s %20.0f %30.1f %25.1f %25.1f\n','Bus',BUS);
fprintf(fid,'%20s %20.0f %30.1f %25.1f %25.1f\n','Bike',BIKE);
fprintf(fid,'%20s %20.0f %30.1f %25.1f %25.1f\n','Walk',WALK);
fprintf(fid,'%20s %20.0f %30.1f %25.1f %25.1f\n','Drive',CAR);
fclose(fid);

%partner.name='XXXXXXXXXX';
%Time_spent=04hours



