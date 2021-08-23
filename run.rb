require 'yaml'
require 'erb'


# you can define this in a sep. file, or inline here the heredoc (<<-HEREDOC_MARKER) syntax allows us to do it inline.
# https://infinum.com/the-capsized-eight/multiline-strings-ruby-2-3-0-the-squiggly-heredoc
template_run = ERB.new(<<-ERB
#!/bin/bash

ERB
)

template_slurm = ERB.new(<<-ERB
#!/bin/bash
#SBATCH -J <%= job.test_cv%><%= job.sample%> # Name for your job
#SBATCH --array=5-35
#SBATCH -n 16 # Number of tasks when using MPI. Default is 1, and SLURM assumes the usage of 1 cpu per task.
#SBATCH -N 1 # Number of nodes to spread cores across - default is 1 - if you are not using MPI this should likely be 1
#SBATCH --mem <%= job.mem %> # Megabytes of memory requested. Default is 2000/task.
#SBATCH -t <%= job.time%> # Runtime in minutes
#SBATCH -p <%= job.partition%> # Partition to submit to the standard compute node partition(defq) or the express node partition(express)
#SBATCH --mail-user alexander.salois@student.montana.edu # this is the email you wish to be notified.
#SBATCH --mail-type FAIL,END # this specifies what events you should get an email about ALL will alert you of job beginning, completion, failure, etc.
#SBATCH -o nnEq_<%= job.test_cv%>_%A_%2a.out.txt # Standard output
#SBATCH -e nnEq_<%= job.test_cv%>_%A_%2a.err.txt # Standard error

date
echo "Hello from $(hostname)."
echo "${SLURM_ARRAY_TASK_ID}"
lscpu

module load Anaconda3
source activate $HOME/condatf2
export HDF5_USE_FILE_LOCKING='FALSE' 
echo "Run a Python script"
python3 <%= job.py_filename %> ${SLURM_ARRAY_TASK_ID} <%=job.sample%>
echo "Ended batch processing at `date`.
ERB
)

# this give you property access
# https://ruby-doc.org/core-3.0.2/Struct.html
Job = Struct.new( :sample, :filename, :py_filename, :test_cv, :mem, :time, :partition, keyword_init: true)

# data is stored in a lightweight markup file, read into ruby as a basic hash data structure:
# https://ruby-doc.org/stdlib-2.5.1/libdoc/yaml/rdoc/YAML.html
# https://medium.com/@kristenfletcherwilde/saving-retrieving-data-with-a-yaml-file-in-ruby-the-basics-e45232903d94
data = YAML.load(File.read("data.yml"))

# each job is a k,v pair:
# {"deep_nnEq"=>{"filename"=>"deep_nnEq_test_hpc.py", "sample"=>445, "mem"=>4000, "time"=>60, "partition"=>"defq"}
# but we just want the values (not the key) so we destructure with the (key, value) in the proc arguments
# https://pragmaticstudio.com/tutorials/ruby-block-syntax

jobs = data["jobs"].map {|(key, values)| Job.new(values) }

# now just make the files
jobs.each do |job|
  binding.local_variable_set(:job, job)
  File.open(job.filename, "w") { |f| f.write template_slurm.result(binding) }
end


