from mako.template import Template
my_tmpl = Template(filename='slurm_matlab_tmpl.txt')
my_scp_tmpl = Template(filename='cpy_hyalite_tmpl.txt')
memory = 6 * 1024
time = 12 * 60
partition = "defq"
script_lines = "#!/bin/bash \n"
x_dir = "/mnt/lustrefs/scratch/v16b915/make_ber_mats/"
data_dir_path = "/mnt/lustrefs/scratch/v16b915/pof_nns/fiber100/"
data_dirs =[
    "e10_12linear",
    "e10_12relu_12tanh", 
    "e10_12relu_12tanh_10tanh_8tanh_6tanh_4tanh",
    "e10_12relu_12tanh_12tanh_12tanh_12tanh_12tanh",
    "e10_12relu_12tanh_8tanh_4tanh_8tanh_12tanh",
    "e10_12relu_4tanh_6tanh_8tanh_10tanh_12tanh",
    "e10_12tanh_12relu" 
    ]

for r_dir in data_dirs: 
        data = data_dir_path + r_dir
        lines = my_tmpl.render(mem=memory,time=time,queue=partition,data_dir=data,exe_dir=x_dir,mat_name=r_dir) 
        lines += "\n"
        file_name = r_dir + ".slurm"
        script_lines += "sbatch " + file_name + "\n"  
        file = open(file_name,"w+")
        file.writelines(lines)


file = open("launch.sh","w+")
file.writelines(script_lines)        

file = open("cpy_hyalite.sh","w+")
scp = my_scp_tmpl.render(path=x_dir)
file.writelines(scp)
