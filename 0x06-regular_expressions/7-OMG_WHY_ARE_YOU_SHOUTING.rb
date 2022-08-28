#!/usr/bin/env ruby
regx = /[A-Z]+/
if ARGV.empty?
    return
else
    puts ARGV[0].scan(regx).join('')
end
