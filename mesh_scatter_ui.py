from functools import partial

import maya.cmds as mc

import mesh_scatter




def generate_mesh(mesh_type_option, mesh_count_field, *args):
	
	mesh_type = mc.optionMenu(mesh_type_option, q=True,value= True)
	mesh_count = mc.intField(mesh_count_field, q=True,value= True)
	
	mesh_scatter.mesh_scatter(mesh_count, mesh_type)
	
	
def create_ui():
	window= mc.window(title='Randomize', width=300)
	layout = mc.formLayout()
	
	mesh_type_option = mc.optionMenu(label='Mesh Count',parent=layout )
	mc.menuItem(label='cube')
	mc.menuItem(label='sphere')
	mc.menuItem(label='cylinder')
	mc.menuItem(label='random')
	
	mesh_count_label=mc.text(label='Mesh Count', parent=layout)
	mesh_count_field=mc.intField(value=20, minValue=1, parent=layout)
	
	generate_btn = mc.button(label='Generate',parent=layout,command=partial(generate_mesh ,mesh_type_option, mesh_count_field))
	
	
	mc.formLayout(layout,e=True, af=[(mesh_type_option, "left", 4), (mesh_type_option, "top", 4)])
	mc.formLayout(layout,e=True,af=[(mesh_count_label, "left", 4)],ac=[(mesh_count_label, "top", 6, mesh_type_option), (mesh_count_field, "top", 4, mesh_type_option), (mesh_count_field, "left", 4, mesh_count_label)])
	mc.formLayout(layout, e=True,af=[(generate_btn, "left", 4), (generate_btn, "right", 0), (generate_btn, "bottom", 10)],ac=[(generate_btn, "top", 10, mesh_count_label)])

	
	
	mc.showWindow(window)
	
if __name__=='__main__':
	create_ui()



	
