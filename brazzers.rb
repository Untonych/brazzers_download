#!/usr/bin/env ruby
require 'mechanize'
mechanize = Mechanize.new
page = mechanize.get('http://www.brazzers.com/videos/')
scenes = page.images_with(:src => /scenes/)
titles = []
scenes.each do |s|
  if title = s.alt.split('-').first 
    titles << title.strip
  end
end
titles.uniq!.compact!
base = 'http://oldpiratebay.org/search.php?q'
titles.first(2).each do |title|
  begin
  search = mechanize.get("#{base}#{title.gsub(' ','%20')}")
  puts "#{base}#{title.gsub(' ','%20')}"
  magnet_link = search.link_with(href: /magnet/).href
  system("open #{magnet_link}")  
  rescue NoMethodError
    puts "No encontrado: #{title}"
  end
end
