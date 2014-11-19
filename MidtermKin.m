l1 = .3;
l2 = .2;
l3 = .1;
l4 = .1;
l5 = .2;
l6 = .1;
l7 = .3;
l8 = .1;
l9 = .1;

O1 = .4;
O2 = .6;
O3 = 1.2;
O4 = .5;
O5 = .1;
O6 = .7;
O7 = .3;
O8 = .2;
O9 = .1;

x1=l1*cos(O1);
x2=x1+l2*cos(O1+O2);
x3=x2+l3*cos(O1+O2+O3);
x4=x3+l4*cos(O1+O2+O3+O4);
x5=x4+l5*cos(O1+O2+O3+O4+O5);
x6=x5+l6*cos(O1+O2+O3+O4+O5+O6);
x7=x6+l7*cos(O1+O2+O3+O4+O5+O6+O7);
x8=x7+l8*cos(O1+O2+O3+O4+O5+O6+O7+O8);
x9=x8+l9*cos(O1+O2+O3+O4+O5+O6+O7+O8+O9);

y1=l1*sin(O1);
y2=y1+l2*sin(O1+O2);
y3=y2+l3*sin(O1+O2+O3);
y4=y3+l4*sin(O1+O2+O3+O4);
y5=y4+l5*sin(O1+O2+O3+O4+O5);
y6=y5+l6*sin(O1+O2+O3+O4+O5+O6);
y7=y6+l7*sin(O1+O2+O3+O4+O5+O6+O7);
y8=y7+l8*sin(O1+O2+O3+O4+O5+O6+O7+O8);
y9=y8+l9*sin(O1+O2+O3+O4+O5+O6+O7+O8+O9);

disp("\nx: ");
disp(x9);

disp("\ny: ");
disp(y9);
