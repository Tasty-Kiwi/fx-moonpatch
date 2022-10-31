export w, h
w = 200fx
h = 400fx

pewpew.set_level_size w, h

location_x = fmath.random_fixedpoint 0fx, w
location_y = fmath.random_fixedpoint 0fx, 400fx

pewpew.new_player_ship location_x, location_y, 0

for i = 0, 20
    pewpew.new_rolling_cube 100.1024fx, 50.2048fx

for i = 0fx, 5fx
    pewpew.new_rolling_cube 15.2048fx, 200.1024fx

pewpew.print_debug_info!