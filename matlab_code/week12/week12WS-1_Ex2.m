x1=[1 7 -8 2 -3 -9]


k=0;
y2=[];
for i=1:length(x1),
  if x1(i)<0,
    k=k+1;
    y2(k)=x1(i);
  end;
end;

  -8    -3    -9

y2=x1;
k=0;
for i=1:length(x1),
  if x1(i)<0,
    k=k+1;
    y2(k)=x1(i);
  end;
end;

    -8    -3    -9     2    -3    -9

y2=[];
for i=1:length(x1),
  if x1(i)<0,
    y2=[y2, x1(i)];
  end;
end;

  -8    -3    -9
