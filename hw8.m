load('meanvariance.mat')
O = ones(100,1);
M_inv=O'*inv(S)*O; %scalar
M = 1/M_inv;
u=2*M;
x = .5*inv(S)*O*u;
O'*x
x'*S*x
r_min = mu'*x

N_inv=[mu';O']*inv(S)*[mu O];
N = inv(N_inv);
v = 2*N*[.05665; 1]
y = 0.5*[inv(S)*mu inv(S)*O]*v;
O'*y
y'*S*y
r_min11 = mu'*y

a = (r_min:.0001:.12);
phi = zeros(100,size(a,2));
var = zeros(1,size(a,2));

for i=1:size(a,2)
    phi(:,i) = g + h*a(i);
    var(i) = phi(:,i)'*S*phi(:,i);
end
vol = sqrt(var);
plot(vol,a)

q = mu - .04*O;
P_inv = q'*inv(S)*q;
P = 1/P_inv;
z = 2*P;
x_sharpe_pos = .5*inv(S)*mu*z;
x_sharpe_port = x_sharpe_pos/(O'*x_sharpe_pos);

O'*x_sharpe_port
x_sharpe_port'*S*x_sharpe_port
mu'*x_sharpe_port



