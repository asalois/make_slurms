from mako.template import Template
my_tmpl = Template(filename='slurm_process_tmpl.txt')
memory = 2 * 1024
time = 1 * 60
partition = "defq"
script_lines = "#!/bin/bash \n"
x_dir = "/mnt/lustrefs/scratch/v16b915/pof_data_process/"
p_file = 'process.py'
script_file = "make_csv.sh"
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
        lines = my_tmpl.render(mem=memory,time=time,queue=partition,\
            dir=data,exe_dir=x_dir,py_file=p_file,script=script_file) 
        lines += "\n"
        file_name = r_dir + ".slurm"
        script_lines += "sbatch " + file_name + "\n"  
        file = open(file_name,"w+")
        file.writelines(lines)


file = open("launch.sh","w+")
file.writelines(script_lines)        

