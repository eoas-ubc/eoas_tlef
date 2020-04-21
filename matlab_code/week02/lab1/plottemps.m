% Plotting the temperature time series

load lab1;

figure(1)
plot(time,temperature)
datetick('x',3)

figure(3)
clf
plot(time,temperature,time(5149:7308),temperature(5149:7308),....
    time(9493:11700),temperature(9493:11700))
datetick('x',3)
pause;

clf
subplot(311);
hist(temperature,[-2:30]);
subplot(312)
hist(temperature(5149:7308),[-2:30]);
subplot(313)
hist(temperature(9493:11700),[-2:30]);
pause;

clf;
wtemp = temperature(5149:7308);
stemp = temperature(9493:11700);
wtime = time(5149:7308);
stime = time(9493:11700);
plot(time,temperature,wtime,wtemp,stime,stemp)
datetick('x',3);
xlabel('Date')
ylabel('Temperature')
title('Temp at xxxx')

mean(stemp)
min(stemp)
mean(stemp)
max(stemp)

save summer stime stemp
