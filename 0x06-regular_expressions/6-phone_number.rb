#!/usr/bin/env ruby
regx = /\d{10, 10}/
if ARGV.empty?
    return
else
    puts ARGV[0].scan(regx).join('')
end
