#!/usr/bin/env ruby
regx = /hbt+n/
if ARGV.empty?
    return
else
    puts ARGV[0].scan(regx).join('')
end
