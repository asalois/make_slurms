from mako.template import Template
my_tmpl = Template(filename='slurm_matlab_tmpl.txt')
my_scp_tmpl = Template(filename='cpy_hyalite_tmpl.txt')
script_lines = "#!/bin/bash \n"
x_dir = "/mnt/lustrefs/scratch/v16b915/dfe_scan_new/"

end = 64
for i in range(end + 1): 
        job_name = "berDFE" + str(i).zfill(2) 
        script_lines += "scancel -n " + job_name + "\n"  


file = open("cancel.sh","w+")
file.writelines(script_lines)        

file = open("to_hyalite.sh","w+")
scp = my_scp_tmpl.render(path=x_dir)
file.writelines(scp)
