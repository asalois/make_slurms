class Slurm
  attr_accessor :interface

  def initialize
    yield self if block_given?
  end

  def mem
    4000
  end

  def time
    60
  end

  def sample
    6
  end

  def partition
    'defq'
  end

  def file_name
    'deepNNEq_cv_hpc.py'
  end

end