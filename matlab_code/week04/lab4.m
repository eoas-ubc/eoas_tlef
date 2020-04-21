% Inputs

press=90000.;     % Pa
Tc=[-30:40];      % deg C
RH=[10:20:90];    % percent
[RH,Tc]=meshgrid(RH,Tc);

%  Constants

e0   = 611.;      % Pa
Lvap = 2.5e6;     % J/kg
T0   = 273;       % K
Rv   = 461;       % J/kg/K
Rd   = 287.;      % J/kg/K
epsilon =0.622;   % g/g

% Calculations

Tk=273.15 + Tc;   % Kelvin 
esat=e0*exp(Lvap./Rv.*((1/T0) - (1./(Tk)) ) );
evap=esat.*(RH/100);
rvap=epsilon*evap./(press-evap);
rho=press./(Rd*(Tk).*(1+0.61*rvap));

% Outputs

clf
subplot(2,1,1)
plot(Tc,rvap);
xlabel('Temperature (^oC)');
ylabel('rvap (kg/kg)');
xlim([5 25]);
legend({'10%','30%','50%','70%','90%'},'Location','NorthEastOutside')
title('Mixing ratio for a range of relative humidities at press=90 kPa');

subplot(2,1,2)
plot(Tc,rho);
legend({'10%','30%','50%','70%','90%'},'Location','NorthEastOutside')
title('Density for a range of relative humidities at press=90 kPa');
axis([5 25 1 1.15]);
xlabel('Temperature (^oC)');
ylabel('rho (kg/m^3)');

