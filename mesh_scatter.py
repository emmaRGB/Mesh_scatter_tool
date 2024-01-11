import random
import maya.cmds as mc


def set_random_position(transform_node):
	tx = random.randint(-10,10)
	ty = random.randint(-10,10)
	tz = random.randint(-10,10)
	mc.setAttr(f"{transform_node}.translate", tx,ty,tz, type= "double3")
	
	

def mesh_scatter(num_mesh, mesh_type = 'cube', size= 1 ):
	mesh_transform =[]
	lista_mesh =['cube','sphere','cylinder']
	is_random = mesh_type == 'random'
	is_random_size = size == 'random'
	if not is_random_size:
		for p in range(num_mesh):
			if is_random:
				mesh_type = random.choice(lista_mesh)
			if mesh_type == 'sphere' :
				transform_node = mc.polySphere( r = size)[0]
			elif mesh_type == 'cylinder' :
				transform_node = mc.polyCylinder(r=size, h= size*2)[0]
			else:
				transform_node = mc.polyCube(h= size, d= size, w= size)[0]	
			set_random_position(transform_node)
			mesh_transform.append(transform_node)
	if is_random_size:	
		for p in range(num_mesh):
			size_random = random.randint(1,4)
			if is_random:
				mesh_type = random.choice(lista_mesh)
			if mesh_type == 'sphere' :
				transform_node = mc.polySphere( r = size_random)[0]
			elif mesh_type == 'cylinder' :
				transform_node = mc.polyCylinder(r=size_random, h= size_random*2)[0]
			else:
				transform_node = mc.polyCube(h= size_random, d= size_random, w= size_random)[0]	
			set_random_position(transform_node)
			mesh_transform.append(transform_node)
		
		
	mc.group(mesh_transform , name = 'scattered_mesh')
	
	
if __name__ == '__main__':
	####mc.file(new= True , force = True )
	mesh_scatter(20, 'random', 'random')
	
	
	
	

