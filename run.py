from mako.template import Template
my_tmpl = Template(filename='slurm_tmpl.txt')
test_cv = ["cv","test"]
script_lines = "#!/bin/bash \n"
py_file_path = "/mnt/lustrefs/scratch/v16b915/pof_nns/"
memory = 6 * 1024
time_limit = 15 * 60

for i in range(1,11):
    py_file_0 = py_file_path + "deep_nnEq_cv_hpc.py"
    py_file_1 = py_file_path + "deep_nnEq_test_hpc.py"
    lines = my_tmpl.render(sample=str(i),py_file_0=py_file_0,\
    py_file_1=py_file_1, mem=str(memory),time=str(time_limit),queue="defq") 
    lines += "\n"
    file_name = str(i).zfill(2) + "_samples.slurm"
    script_lines += "sbatch " + file_name + "\n"  
    file = open(file_name,"w+")
    file.writelines(lines)


file = open("launch_nns.sh","w+")
file.writelines(script_lines)        

