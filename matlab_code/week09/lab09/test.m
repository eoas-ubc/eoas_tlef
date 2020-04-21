n=3;
    x=cumsum(randn(50,n));
    plot(x);
    ylim([-20 20]);
    str=sprintf('we are showing %d lines',n);
    text(1,10,str);