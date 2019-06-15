N =gets.to_i
balls = N.times.map do
  gets.split.map(&:to_i)
end

distances = {}

index = 0
while(balls.count != index)
  target_ball = balls[index]

  balls.each do |ball|
    dif_pos = [
        ball.first - target_ball.first,
        ball.last - target_ball.last
    ]
    # puts "#{dif_pos[0]}, #{dif_pos[1]}"
    distances[dif_pos] = (distances[dif_pos] || 0) + 1
  end
  index += 1
end
distances[[0, 0]] = 0
puts "#{distances}"
puts N - (distances.values.max || 0)
