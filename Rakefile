require 'erb'
require_relative 'slurm'

desc "make a config file"

task :config do
  Rake::Task["clean"].invoke
 
  slurm = Slurm.new do |h|
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
