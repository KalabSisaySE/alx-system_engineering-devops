#!/usr/bin/env ruby
regx = /h.n/
if ARGV.empty?
    return
else
    puts ARGV[0].scan(regx).join('')
end
