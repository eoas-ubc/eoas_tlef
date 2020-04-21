
X=[0.3	1.1	3.5	3.9	5.8	8.0];
Y=[-2.5	-0.6	-1.2	-1.8	-4.6	-3.6];

plot(X,Y,'sk','linewi',2);
set(gca,'tickdir','out');
axis([0 10 -6 2]);grid;
xlabel('x');
ylabel('f(x)');

print -dpng ws1_fig
