from mako.template import Template
my_tmpl = Template(filename='slurm_matlab_tmpl.txt')
my_scp_tmpl = Template(filename='cpy_hyalite_tmpl.txt')
memory = 8 * 1024
time = 400
partition = "defq"
mfile_name = "scan_dfe"
script_lines = "#!/bin/bash \n"
x_dir = "/mnt/lustrefs/scratch/v16b915/dfe_scan_new/"

end = 6
for i in range(end + 1): 
        ar_start = 1
        ar_end = 1000
        if i == end:
            ar_end = 460

        pl = 1000*i
        lines = my_tmpl.render(mem=memory,time=time,queue=partition,\
            start=ar_start,end=ar_end,limit=100,num=i,plus=pl) 
        lines += "\n"
        file_name = "dfe_ber_" + str(i).zfill(2) + ".slurm"
        file = open(file_name,"w+")
        file.writelines(lines)
        script_lines += "sbatch " + file_name + "\n"  


file = open("launch.sh","w+")
file.writelines(script_lines)        

file = open("to_hyalite.sh","w+")
scp = my_scp_tmpl.render(path=x_dir)
file.writelines(scp)
