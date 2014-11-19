l1 = .3;
l2 = .2;

O1 =0;
O2 =0;

de=[0.2;0.2];
%calculate initial conditions
R1 = [  cos(O1)    -sin(O1)   0   0;
        sin(O1)    cos(O1)    0   0; 
        0           0           1   0;
        0           0           0   1];
    
R2 = [  cos(O2)    -sin(O2)   0   0;
        sin(O2)    cos(O2)    0   0; 
        0           0           1   0;
        0           0           0   1];

D1 = [eye(4,3) [ l1; 0; 0; 1]];
D2 = [eye(4,3) [ l2; 0; 0; 1]];

T1 = R1*D1;
T2 = R2*D2;


Ti= T1*T2;
xi=Ti(1,4)
yi=Ti(2,4)
dtheta=.01
%calculate x and y if O1 changes
R1 = [  cos(O1+dtheta)    -sin(O1+dtheta)   0   0;
        sin(O1+dtheta)    cos(O1+dtheta)    0   0; 
        0           0           1   0;
        0           0           0   1];
    
R2 = [  cos(O2)    -sin(O2)   0   0;
        sin(O2)    cos(O2)    0   0; 
        0           0           1   0;
        0           0           0   1];

D1 = [eye(4,3) [ l1; 0; 0; 1]];
D2 = [eye(4,3) [ l2; 0; 0; 1]];

T1 = R1*D1;
T2 = R2*D2;


Td1= T1*T2;

%calculate x and y if O2 changes
R1 = [  cos(O1)    -sin(O1)   0   0;
        sin(O1)    cos(O1)    0   0; 
        0           0           1   0;
        0           0           0   1];
    
R2 = [  cos(O2+dtheta)    -sin(O2+dtheta)   0   0;
        sin(O2+dtheta)    cos(O2+dtheta)    0   0; 
        0           0           1   0;
        0           0           0   1];

D1 = [eye(4,3) [ l1; 0; 0; 1]];
D2 = [eye(4,3) [ l2; 0; 0; 1]];

T1 = R1*D1;
T2 = R2*D2;
Td2= T1*T2;
%Get the changes in y
xd1=Td1(1,4)
yd1=Td1(2,4)
disp("\n")
xd2=Td2(1,4)
yd2=Td2(2,4)

%Fill the Jacobian with values
J=[ ((xd1-xi)/dtheta) ((xd2-xi)/dtheta);
    ((yd1-yi)/dtheta) ((yd2-yi)/dtheta);
]

%multiply by J
dO=inverse(J)*de






