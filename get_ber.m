%% Proakis Synthetic Channel Equilization with Deep NNs

% Montana State University
% Electrical & Computer Engineering Department
% Created by Alexander Salois

% prelim comands
function get_ber(mat_name)
tic
ber = zeros(10,31);
labels = cell(1,10);
mat_name = mat_name + "_berDNNTF"
save('berDNNTF','ber')
toc
