class Slurm
  attr_accessor :sample

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
    raise "implement me in subclass"
  end

  def partition
    'defq'
  end

  def file_name
    raise "implement me in subclass"
  end

end