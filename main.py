def is_even(n):
	return n % 2 == 0
	
def water():
	if get_water() < 0.75:
		use_item(Items.Water_Tank)
		
def muevase():
	if get_pos_y() == get_world_size()-1:
		move(East)
		move(North)
	else:
		move(North)
		
def tend():
	if can_harvest():
		harvest()
	water()
	if get_entity_type() == None and get_ground_type() == Grounds.Soil:
		till()
	muevase()
	
def checkmegapumpkin():
	a = get_world_size() ** 2
	while can_harvest() == True and get_entity_type() == Entities.Pumpkin:
		a -= 1
		quick_print(a)
		muevase()
		if a == 0:
			harvest()
			break
		
def tillifneeded():
	if get_ground_type() != Grounds.Soil:
		till()
		
while True:
	while num_items(Items.Hay) < 1000:
		tend()
	
	while num_items(Items.Wood) < 1000:
		if is_even(get_pos_y()) == True and is_even(get_pos_x()) == True:
			plant(Entities.Tree)
		elif  is_even(get_pos_y()) == False and is_even(get_pos_x()) == False:
			plant(Entities.Tree)
		tend()
	
	while num_items(Items.Carrot) < 1000:
		tillifneeded()
		if get_entity_type() != Entities.Carrots:
			trade(Items.Carrot_Seed)
			plant(Entities.Carrots)
		tend()
	
	while num_items(Items.Pumpkin) < 1000:
		tillifneeded()
		if get_entity_type() != Entities.Pumpkin:
			trade(Items.Pumpkin_Seed)
			plant(Entities.Pumpkin)
		checkmegapumpkin()
		
#while num_items(Items.Power) < 1000:
#	tillifneeded()
#	if get_entity_type() != Entities.Sunflower:
#		trade(Items.Sunflower_Seed)
#		plant(Entities.Sunflower)
#	if measure() != None:
#		tend()
