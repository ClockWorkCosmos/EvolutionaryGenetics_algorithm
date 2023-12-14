import math 
import sys
import random as r
import time as t
import pygame
from pygame.locals import *
pygame.init()

window_size = int(500)
window_bgcolor = [255,255,255]
window_caption = str("New")

map_size = int(250)
map_color = [000,000,000]
map_x = int(62)
map_y = int(200)

agent_size = int(16)
agent_color = [200,000,000]
agent_x = int(182)
agent_y = int(325)
agent_angle = int(0)
agent_speed = int(10)
traversed = int(0)
action = str("")

goal = int(200)

pause = float(0.00)

input_color = [000,255,000]
hidden_color = [000,000,255]
output_color_a = [000,255,000]
output_color_b = [000,255,000]
red = [255,000,000]

g = int(0)
h = int(0)
m = int(250)
n = int(100)
i = int(0)
j = int(0)
l = float(0.001)
c = float(0.00)
d = float(0.00)
o = float(0.00) 
s = float(0.00)
p = [0.00, 0.00, 0.00]
q = [0.00, 0.00, 0.00]
a = [0.00, 0.00, 0.00]
b = [0.00, 0.00, 0.00]
e = [0.00, 0.00]
f = [0.00, 0.00]

screen = pygame.display.set_mode([window_size+250,window_size])
screen.fill(window_bgcolor)
pygame.display.set_caption(window_caption)
pygame.display.update()

for x, _ in enumerate(b):
	b[x] = r.uniform(-1.00, 1.00)
d = r.uniform(-1.00, 1.00)

while True:
	a = [0.00, 0.00, 0.00]
	c = 0.00
	e = [0.00, 0.00]
	f = [0.00, 0.00]
	action = ""
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			pause = 0.25
		else:
			pause = 0.00

	if i >= goal:
		pause = 0.1
		
	if i < goal:
		if g >= m:
			if j <= 10 and h >= 10:
				for x, _ in enumerate(p):
					p[x] = r.uniform(-0.99, 0.99)
					q[x] = r.uniform(-0.99, 0.99)
					b[x] = r.uniform(-0.99, 0.99)
					d = r.uniform(-0.99, 0.99)
					o = r.uniform(-0.99, 0.99)
					s = r.uniform(-0.99, 0.99)
			i = 0
			g = 0
			for x, _ in enumerate(b):
				b[x] = ((q[x] + p[x])/2) + r.uniform(-l, l)	
			d = ((o + s)/2) + r.uniform(-l, l)
			a = [0.00, 0.00, 0.00]
			e = [0.00, 0.00]
			action = ""	
			agent_x = 182
			agent_y = 325
			h += 1
			traversed = 0
		else:
			g += 1
		
	if agent_angle == 0 or agent_angle == 360:
		for x, _ in enumerate(a):
			a[x] = abs((map_y - agent_y)) / 100
			if a[x] > 0.99:
				a[x] = 0.99
			if a[x] < 0.00:
				a[x] = 0.00	
	elif agent_angle == 90:
		for x, _ in enumerate(a):
			a[x] = abs((map_x+map_size) - (agent_x + agent_size)) / 100
			if a[x] > 0.99:
				a[x] = 0.99
			if a[x] < 0.00:
				a[x] = 0.00
	elif agent_angle == 180:
		for x, _ in enumerate(a):
			a[x] = abs(((map_size+map_y) - (agent_y+agent_size))) / 100
			if a[x] > 0.99:
				a[x] = 0.99
			if a[x] < 0.00:
				a[x] = 0.00
	elif agent_angle == 270:
		for x, _ in enumerate(a):
			a[x] = abs((map_x - agent_x)) / 100
			if a[x] > 0.99:
				a[x] = 0.99
			if a[x] < 0.00:
				a[x] = 0.00
						
	for x, _ in enumerate(a):
		c += a[x] * b[x]
		
	if c > 0.99:
		c = 0.99
	elif c < -0.99:
		c = -0.99
		
	if c >= d:
		hidden_color = red
		e = [1.00, 0.00]
	if c < d:
		hidden_color = [000,000,255]
		e = [0.00, 1.00]
		
	if e == [1.00, 0.00]:
		if r.randint(0,1) > 0:
			action = "move_right"
			output_color_a = [255,000,000]
			output_color_b = [000,255,000]
			if agent_angle < 360:
				agent_angle += 90
			elif agent_angle == 360:
				agent_angle = 90
		else:
			action = "move_left"
			output_color_a = [255,000,000]
			output_color_b = [000,255,000]
			if agent_angle == 0:
				agent_angle = 270
			elif agent_angle >= 0:
				agent_angle += -90 
					
		if agent_angle <= 0 or agent_angle >= 360:
			agent_angle = 0	
		if agent_angle == 90:
			agent_x += agent_speed
		if agent_angle == 180:
			agent_y += agent_speed	
		if agent_angle == 270:
			agent_x += 0-(agent_speed)			
		if agent_angle == 360 or agent_angle == 0:
			agent_y += 0-(agent_speed)
			
	if e == [0.00, 1.00]:
		action = "move_forward"
		traversed += 1
		if action == "move_forward" and agent_angle == 90:
			agent_x += agent_speed
			output_color_a = [000,255,000]
			output_color_b = red
		if action == "move_forward" and agent_angle == 180:
			agent_y += agent_speed	
			output_color_a = [000,255,000]
			output_color_b = red
		if action == "move_forward" and agent_angle == 270:
			agent_x += 0-(agent_speed)
			output_color_a = [000,255,000]
			output_color_b = red			
		if action == "move_forward" and agent_angle == 360 or agent_angle == 0:
			agent_y += 0-(agent_speed)	
			output_color_a = [000,255,000]
			output_color_b = red
			
	for x, _ in enumerate(a):
		if a[x] < 0.3:
			f = [1.00, 0.00]
		else:
			f = [0.00, 1.00]
				
	if i > j - (j/4) and i < j:
		p = b
		s = d
	elif i >= j:
		j = i
		q = b
		o = d	
			
	if agent_x <= map_x+1 or agent_x >= (map_x+map_size)-(agent_size+1) or agent_y >= (map_y+map_size)-(agent_size+1) or agent_y <= map_y+2:
		t.sleep(pause)	
		if i != goal:
			for x, _ in enumerate(b):
				if r.randint(0,1):
					b[x] += r.uniform(0.00, 0.02)
				else:
					b[x] += r.uniform(-0.02, 0.00)		
					
			if r.randint(0,1):
				d += r.uniform(-0.02, 0.00)
			else:
				d += r.uniform(0.00, 0.02)
					
			a = [0.00, 0.00, 0.00]
			e = [0.00, 0.00]
			action = ""	
			agent_x = 182
			agent_y = 325
			i = 0
		else:
			i = i
			a = [0.00, 0.00, 0.00]
			e = [0.00, 0.00]
			action = ""	
			agent_x = 182
			agent_y = 325	
					
	elif traversed < 1:
		action = "move_forward"
		agent_angle = 180
		if action == "move_forward" and agent_angle == 90:
			agent_x += agent_speed
		if action == "move_forward" and agent_angle == 180:
			agent_y += agent_speed	
		if action == "move_forward" and agent_angle == 270:
			agent_x += 0-(agent_speed)			
		if action == "move_forward" and agent_angle == 360 or agent_angle == 0:
			agent_y += 0-(agent_speed)
			
	if e == f and i != goal:
		i += 1		
				
	for x, _ in enumerate(b):
		if b[x] >= 0.99:
			b[x] = 0.99
		elif b[x] <= -0.99:
			b[x] = -0.99	
			
	if d >= 0.99:
		d = 0.99
	elif d <= -0.99:
		d = -0.99
		
	if i <= 0:
		i = 0
		
	font = pygame.font.Font('freesansbold.ttf', 12)
	
	ACTION = "Action:" + str(action) + " ~ Output:" + str(e) + " ~ Correct Output:" + str(f)
	ANGLE = "Angle:" + str(agent_angle) + "*"
	INPUT_LAYER = "Input Layer:" + str(a)
	WEIGHTS = "Weights:" + str(b) 
	HIDDEN_LAYER = "Hidden Unit:" + str(c)
	THRESHOLD = "Threshold:" + str(d)
	SCORE = "Score:" + str(i)
	HIGH_SCORE = "High Score:" + str(j)
	ITERATION = "Episode:" + str(g) 
	GENERATION = "Generation:" + str(h)
	
	action_display = font.render(ACTION, True, (0,0,0),(255,255,255))
	angle_display = font.render(ANGLE, True, (0,0,0),(255,255,255))
	il_display = font.render(INPUT_LAYER, True, (0,0,0),(255,255,255))
	w_display = font.render(WEIGHTS, True, (0,0,0),(255,255,255))
	h_display = font.render(HIDDEN_LAYER, True, (0,0,0),(255,255,255))
	t_display = font.render(THRESHOLD, True, (0,0,0),(255,255,255))
	s_display = font.render(SCORE, True, (0,0,0),(255,255,255))
	hs_display = font.render(HIGH_SCORE, True, (0,0,0),(255,255,255))
	i_display = font.render(ITERATION, True, (0,0,0),(255,255,255))
	g_display = font.render(GENERATION, True, (0,0,0),(255,255,255))
	
	pygame.draw.rect(screen,(window_bgcolor),[0,0,window_size+250,window_size],0)
	pygame.draw.rect(screen,(map_color),[map_x,map_y,map_size,map_size],2)
	pygame.draw.rect(screen,(agent_color),[agent_x, agent_y, agent_size, agent_size],0)
	
	pygame.draw.line(screen, (0,0,0),[450,225], [550,325], 3)
	pygame.draw.line(screen, (0,0,0),[450,325], [550,325], 3)
	pygame.draw.line(screen, (0,0,0),[450,425], [550,325], 3)
	pygame.draw.line(screen, (0,0,0),[550,325], [650,275], 3)
	pygame.draw.line(screen, (0,0,0),[550,325], [650,375], 3)

	pygame.draw.circle(screen, (input_color),[450,225], 20, 0)
	pygame.draw.circle(screen, (input_color),[450,325], 20, 0)
	pygame.draw.circle(screen, (input_color),[450,425], 20, 0)
	pygame.draw.circle(screen, (hidden_color),[550,325], 25, 0)
	pygame.draw.circle(screen, (output_color_a),[650,275], 20, 0)
	pygame.draw.circle(screen, (output_color_b),[650,375], 20, 0)
	
	screen.blit(action_display, (220,60))
	screen.blit(angle_display, (220,75))
	screen.blit(w_display, (220,15))
	screen.blit(h_display, (220,30))
	screen.blit(t_display, (220,45))
	screen.blit(il_display, (220,0))
	screen.blit(s_display, (map_x,map_y - 20))
	screen.blit(hs_display, (map_x + map_size - (map_size / 4),map_y - 20))
	screen.blit(i_display, (0,0))
	screen.blit(g_display, (0,15))
	
	t.sleep(pause)
	pygame.display.flip()
input(">>")
pygame.exit()
exit()
