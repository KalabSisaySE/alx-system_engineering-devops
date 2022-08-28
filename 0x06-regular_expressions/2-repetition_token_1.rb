#!/usr/bin/env ruby
regx = /hb?tn/
if ARGV.empty?
    return
else
    puts ARGV[0].scan(regx).join('')
end
