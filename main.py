nrfields = get_world_size() ** 2

while demand():
	while limHay():
		makeTurf()
		tend()
	
	while limWood():
		tend()
		if is_even(get_pos_y()) == True and is_even(get_pos_x()) == True:
			makeTurf()
			plant(Entities.Tree)
		elif  is_even(get_pos_y()) == False and is_even(get_pos_x()) == False:
			makeTurf()
			plant(Entities.Tree)

	
	while limCarrot():
		tend()
		makeSoil()
		if get_entity_type() != Entities.Carrots:
			trade(Items.Carrot_Seed)
			plant(Entities.Carrots)


	while limPumpkin():
		if get_entity_type() != Entities.Pumpkin:
			trade(Items.Pumpkin_Seed)
			makeSoil()
			plant(Entities.Pumpkin)
		tend()
		checkmegapumpkin()
		
		
	while limPower():
		makeSoil()
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