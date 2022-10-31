w = 200fx
h = 400fx
pewpew.set_level_size(w, h)
local location_x = fmath.random_fixedpoint(0fx, w)
local location_y = fmath.random_fixedpoint(0fx, 400fx)
pewpew.new_player_ship(location_x, location_y, 0)
for i = 0, 20 do
  pewpew.new_rolling_cube(100.1024fx, 50.2048fx)
end
for i = 0fx, 5fx do
  pewpew.new_rolling_cube(15.2048fx, 200.1024fx)
end
return pewpew.print_debug_info()
