import matplotlib.pyplot as plt
plt.style.use('ggplot')
#################
#Init Population#
#################

rabbits = [100]
foxes = [10]
grass = [400]

########################
#Init birth death rates#
########################
rabbit_birth_rate = 0.5
rabbit_death_rate = 0.015

fox_birth_rate = 0.015
fox_death_rate = 0.5

grass_birth_rate = 2
grass_death_rate = 0.06



###########
#CONSTANTS#
###########
dt = 0.01
cycles = 5000
GC_list = []
factor = 1
for t in range(0, cycles):
	updated_rabbits = (rabbits[t] + dt * (rabbit_birth_rate * rabbits[t]*grass[t]/20  - rabbit_death_rate * foxes[t] * rabbits[t]))*factor   
	updated_foxes = foxes[t] + dt * (-fox_death_rate * foxes[t] + fox_birth_rate * foxes[t] * rabbits[t])
	updated_grass = grass[t] + dt * (grass_birth_rate * grass[t]  - grass_death_rate * grass[t] * rabbits[t])



	#if t >= 3000:
		#updated_foxes = 0
		#factor = 1
		#updated_rabbits = (rabbits[t] + dt * (rabbit_birth_rate * rabbits[t]*grass[t]/20-rabbit_death_rate * rabbits[t]*2))

	if round(updated_rabbits,6) == 0:
		updated_rabbits = 0
	if round(updated_foxes,6) == 0:
		updated_foxes = 0
	if round(updated_grass,6) == 0:
		updated_grass = 0

	rabbits.append(updated_rabbits)
	foxes.append(updated_foxes)
	grass.append(updated_grass)

time_points = range(cycles + 1)
plt.plot(time_points, foxes, label = 'Fox', c = 'orange')  
plt.plot(time_points, rabbits, label = 'Rabbit') 
plt.plot(time_points, grass, label = 'Grass', c = 'green')
#plt.xlim(-1,500)
plt.ylim(-1, 1000)
plt.xlabel('Time', size = 30)
plt.ylabel('Population Count', size = 30)
plt.legend(prop = {'size':20}, loc = 'upper right')
plt.show()


#plt.plot(rabbits, foxes, label = 'fox')  
#plt.show()