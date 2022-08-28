#!/usr/bin/env ruby

sender_regx = /from:[+]*\d*\w*/
reciever_regx = /to:[+]*\d*\w*/
flag_regx = /(1|0|-1):(1|0|-1):(1|0|-1):(1|0|-1):(1|0|-1)/

arr = []
if ARGV.empty?
    return
else
    sender = ARGV[0].scan(sender_regx)
    arr << sender[0].slice(5..-1)
    reciever = ARGV[0].scan(reciever_regx)
    arr << reciever[0].slice!(3..-1)
    arr << ARGV[0].scan(flag_regx).join(':') 
    
    puts arr.join(',')
end
