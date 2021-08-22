class Host
  attr_accessor :interface

  def initialize
    yield self if block_given?
  end

  def channel
    11
  end

  def ssid
    raise "implement me in subclass"
  end

  def alex
    "#{interface}**#{channel}"
  end

  def os_name
    `uname`
  end
end
