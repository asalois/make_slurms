from mako.template import Template
my_tmpl = Template(filename='slurm_matlab_tmpl.txt')
my_scp_tmpl = Template(filename='cpy_hyalite_tmpl.txt')
memory = 5 * 1024
time = 40
partition = "defq"
mfile_name = "scan_dfe"
script_lines = "#!/bin/bash \n"
x_dir = "/mnt/lustrefs/scratch/v16b915/dfe_scan_new/"

end = 64
for i in range(end + 1): 
        ar_start = 1
        ar_end = 1000
        if i == end:
            ar_end = 600

        pl = 1000*i
        lines = my_tmpl.render(mem=memory,time=time,queue=partition,\
            start=ar_start,end=ar_end,limit=26,num=i,plus=pl) 
        lines += "\n"
        file_name = "dfe_ber_" + str(i).zfill(2) + ".slurm"
        file = open(file_name,"w+")
        file.writelines(lines)
        if i == 0:
            script_lines += "jb_id"+ str(i).zfill(2) +"=$((sbatch " + file_name + ") | cut -d \" \" -f 4 )\n"  
            script_lines += "echo $jb_id"+ str(i).zfill(2) + " && echo \"" + file_name + "\" \n"  
        else:
            script_lines += "jb_id"+ str(i).zfill(2) +"=$((sbatch --dependency=afterany:"+"$jb_id"+ str(i-1).zfill(2) + " " +file_name + ") | cut -d \" \" -f 4 )\n"  
            script_lines += "echo $jb_id"+ str(i).zfill(2) + " && echo \"" + file_name + "\" \n"  


file = open("launch.sh","w+")
file.writelines(script_lines)        

file = open("to_hyalite.sh","w+")
scp = my_scp_tmpl.render(path=x_dir)
file.writelines(scp)
