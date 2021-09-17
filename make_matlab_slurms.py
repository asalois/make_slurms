from mako.template import Template
my_tmpl = Template(filename='slurm_matlab_tmpl.txt')
my_scp_tmpl = Template(filename='cpy_hyalite_tmpl.txt')
memory = 6 * 1024
time = 120
partition = "defq"
mfile_name = "dfe_scan"
job_name = "ber_dfe"
script_lines = "#!/bin/bash \n"
x_dir = "/mnt/lustrefs/scratch/v16b915/dfe_scan/"
last = 3542

for i in range(1,5): 
        start = (i-1)*1000 + 1
        end = i*1000
        if end > last:
            end = last

        if i == 1:
            pl = 0
        else:
            pl = 1000

        lines = my_tmpl.render(mem=memory,time=time,queue=partition,\
            start_ar=start,end_ar=end,m_file=mfile_name,j_name=job_name,plus=pl) 
        lines += "\n"
        file_name = "dfe_ber_" + str(i) + ".slurm"
        script_lines += "sbatch " + file_name + "\n"  
        file = open(file_name,"w+")
        file.writelines(lines)


file = open("launch.sh","w+")
file.writelines(script_lines)        

file = open("to_hyalite.sh","w+")
scp = my_scp_tmpl.render(path=x_dir)
file.writelines(scp)
