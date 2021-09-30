script_lines = "#!/bin/bash \n"

for snr in range(5,36): 
    rm_dir = "snr" + str(snr).zfill(2)    
    script_lines += "cd " + rm_dir + "\n"
    script_lines += "rm cv0*.mat\n"
    script_lines += "cd ../\n"

file = open("rm_mats.sh","w+")
file.writelines(script_lines)
