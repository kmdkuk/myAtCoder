N, L = gets.chomp.split.map(&:to_i)

azi = Array.new(N)

N.times do |i|
  azi[i] = L + i
end

n_py = azi.inject(:+)
min = nil
min_i = nil
N.times do |i|
  eat_py = n_py - azi[i]
  abs = (n_py - eat_py).abs
  if (min.nil? || min > abs)
    min = abs
    min_i = i
  end
end

puts n_py - azi[min_i]