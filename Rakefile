require 'erb'
require_relative 'cv_slurm'

desc "make a HPC cluster file"

task :config do
  Rake::Task["clean"].invoke
 
  slurm = CvSlurm.new do |h|
    h.sample = 4
  end

  template = File.read("hpc.slurm.erb")

  File.open("hpc.slurm", "w") do |f|
    f.write ERB.new(template).result(binding)
  end
end

desc "remove written file"
task :clean do
  File.delete("hpc.slurm")
end
