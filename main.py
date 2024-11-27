clear()
nrfields = get_world_size() ** 2

def is_even(n):
	return n % 2 == 0
	
def harvestif():
	if can_harvest():
		harvest()
	
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
	if get_entity_type() != Entities.Pumpkin and get_entity_type() != Entities.Sunflower:
		harvestif()
	water()
	if get_entity_type() == None and get_ground_type() == Grounds.Soil:
		till()
	muevase()
	
def tillifneeded():
	if get_ground_type() != Grounds.Soil:
		till()
		
def checkmegapumpkin():
	b = nrfields
	while can_harvest() == True and get_entity_type() == Entities.Pumpkin:
		b -= 1
		quick_print(b)
		if b == 0:
			harvestif()
		muevase()
		
def harvestSF():
	a = num_items(Items.Power)
	quick_print("Petals to be harvested:", measure())
	harvestif()
	trade(Items.Sunflower_Seed)					
	plant(Entities.Sunflower)
	b = num_items(Items.Power)
	quick_print("Energy harvested:", b-a)	
		
#######################################		
		
while True:
	while num_items(Items.Hay) < 1000:
		tend()
	
	while num_items(Items.Wood) < 2000:
		tend()
		if is_even(get_pos_y()) == True and is_even(get_pos_x()) == True:
			plant(Entities.Tree)
		elif  is_even(get_pos_y()) == False and is_even(get_pos_x()) == False:
			plant(Entities.Tree)

	
	while num_items(Items.Carrot) < 2000:
		tend()
		tillifneeded()
		if get_entity_type() != Entities.Carrots:
			trade(Items.Carrot_Seed)
			plant(Entities.Carrots)


	while num_items(Items.Pumpkin) < 3000:
		if get_entity_type() != Entities.Pumpkin:
			trade(Items.Pumpkin_Seed)
			tillifneeded()
			plant(Entities.Pumpkin)
		tend()
		checkmegapumpkin()
		
		
	while num_items(Items.Power) < 1500:
		tillifneeded()
		if get_entity_type() != Entities.Sunflower:	
			trade(Items.Sunflower_Seed)
			plant(Entities.Sunflower)
		tend()
		if get_entity_type() == Entities.Sunflower:
			fieldPower = []
			for i in range(nrfields):
				if get_entity_type() == Entities.Sunflower:
					fieldPower.append(measure())
				muevase()
				if measure() == 15:
					harvestSF()
					break
			if len(fieldPower) == nrfields:
				for i in range(nrfields):
					if measure() == max(fieldPower) or measure() == 15:
						harvestSF()
						break
					else:
						muevase()