from mako.template import Template
my_tmpl = Template(filename='slurm_tmpl.txt')
test_cv = ["cv","test"]
script_lines = "#!/bin/bash \n"

for i in range(1,6):
    for test_or_cv in test_cv: 
        py_file = "deep_nn_" + test_or_cv +"_hpc.py"
        lines = my_tmpl.render(test_cv=test_or_cv,sample=str(i),py_file=py_file) 
        lines += "\n"
        file_name = test_or_cv + str(i).zfill(2) + ".slurm"
        script_lines += "sbatch " + file_name + "\n"  
        file = open(file_name,"w+")
        file.writelines(lines)


file = open("launch_nns.sh","w+")
file.writelines(script_lines)        

