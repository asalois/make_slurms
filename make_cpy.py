script_lines = "#!/bin/bash \n"
to_dir = "/mnt/lustrefs/scratch/v16b915/make_ber_mats/"
from_dir_path = "/mnt/lustrefs/scratch/v16b915/pof_nns/fiber100/"
from_dirs =[
    "e10_12linear",
    "e10_12relu_12tanh", 
    "e10_12relu_12tanh_10tanh_8tanh_6tanh_4tanh",
    "e10_12relu_12tanh_12tanh_12tanh_12tanh_12tanh",
    "e10_12relu_12tanh_8tanh_4tanh_8tanh_12tanh",
    "e10_12relu_4tanh_6tanh_8tanh_10tanh_12tanh",
    "e10_12tanh_12relu" 
    ]

for r_dir in from_dirs: 
        script_lines += "cp " + from_dir_path + r_dir + "/*berDNNTF.mat " + to_dir + r_dir + "_berDNNTF.mat\n"
        script_lines += "cp " + from_dir_path + r_dir + "/*bernn.png " + to_dir + r_dir + "_bernn.png\n"

file = open("cpy_mats.sh","w+")
file.writelines(script_lines)
