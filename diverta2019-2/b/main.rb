N = gets.to_i
x, y = N.times.map{gets.split.map(&:to_i)}.transpose

hash = Hash.new

N.times do |i|
  N.times do |j|
    next if i == j
    new_x = x[i] - x[j]
    new_y = y[i] - y[j]
    hash["#{new_x},#{new_y}"] ||= 0
    hash["#{new_x},#{new_y}"] += 1
  end
end

puts N - (hash.values.max || 0)