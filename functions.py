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
	
def makeSoil():
	if get_ground_type() != Grounds.Soil:
		till()

def makeTurf():
	if get_ground_type() != Grounds.Turf:
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
	harvestif()
	trade(Items.Sunflower_Seed)					
	plant(Entities.Sunflower)
	b = num_items(Items.Power)
	quick_print("Energy harvested:", b-a)
	
def limHay():
	if num_items(Items.Hay) < 6800:
		return
	else:
		return False
		
def limWood():
	if num_items(Items.Wood) < 3000:
		return
	else:
		return False

def limCarrot():
	if num_items(Items.Carrot) < 7000:
		return
	else:
		return False

def limPumpkin():
	if num_items(Items.Pumpkin) < 3000:
		return
	else:
		return False
		
def limPower():
	if num_items(Items.Power) < 1600:
		return
	else:
		return False

def demand():
	if limHay() or limWood() or limCarrot() or limPumpkin() or limPower():
		return 