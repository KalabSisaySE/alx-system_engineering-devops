#!/usr/bin/env ruby
regx = /hbt{2,5}n/
if ARGV.empty?
    return
else
    puts ARGV[0].scan(regx).join('')
end
