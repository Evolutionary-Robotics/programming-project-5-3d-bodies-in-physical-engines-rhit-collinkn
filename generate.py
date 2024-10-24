import pyrosim.pyrosim as ps

# Global parameters
l = 1 # length
w = 1 # width 
h = 1 # height 

# x = 0
# y = 0
# z = 0.5
x = 0
y = 0
z = 1.5

def Create_World():
    ps.Start_SDF("box.sdf")
    for i in range(10):
        ps.Send_Cube(name="Box",pos=[x,y,z],size=[l,w,h])
        z += h
        l = 0.9 * l
        w = 0.9 * w
        h = 0.9 * h
    ps.End()

def Create_Robot1():
    ps.Start_URDF("body.urdf")
    ps.Send_Cube(name="Foot",pos=[x,y,z],size=[l,w,h]) # Parent
    ps.Send_Joint(name="Foot_Torso", parent="Foot", child="Torso", type="revolute", position = [0.5,0,1.0])
    ps.Send_Cube(name="Torso",pos=[0.6,0.4,0.1],size=[1.2,0.2,0.2]) # Child
    ps.Send_Joint(name="Foot_Torso2", parent="Foot", child="Torso2", type="revolute", position = [-0.5,0.0,1.0])
    ps.Send_Cube(name="Torso2",pos=[-0.6,0.4,0.1],size=[1.2,0.2,0.2]) # Child


    ps.Send_Joint(name="Foot_Torso3", parent="Foot", child="Torso3", type="revolute", position = [0.5,-0.8,1.0])
    ps.Send_Cube(name="Torso3",pos=[0.6,0.4,0.1],size=[1.2,0.2,0.2]) # Child
    ps.Send_Joint(name="Foot_Torso4", parent="Foot", child="Torso4", type="revolute", position = [-0.5,-0.8,1.0])
    ps.Send_Cube(name="Torso4",pos=[-0.6,0.4,0.1],size=[1.2,0.2,0.2]) # Child
    
    ps.End()

def Create_Robot2():

    ps.Start_URDF("body2.urdf")
    ps.Send_Cube(name="parent",pos=[2,2,1.5],size=[l,w,h]) # Parent
    
    ps.Send_Joint(name="parent_child2", parent="parent", child="child2", type="revolute", position = [1.5,1.2,1.0])
    ps.Send_Cube(name="child2",pos=[-0.6,0.4,0.1],size=[1.2,0.2,0.2]) # Child


    ps.Send_Joint(name="parent_child1", parent="parent", child="child1", type="revolute", position = [2.5,1.4,1.0])
    ps.Send_Cube(name="child1",pos=[0.6,0.4,0.1],size=[1.2,0.2,0.2]) # Child
    # ps.Send_Joint(name="parent_child4", parent="parent", child="child4", type="revolute", position = [1.5,1.4,1.0])
    # ps.Send_Cube(name="child4",pos=[-0.6,0.4,0.1],size=[1.2,0.2,0.2]) # Child


    ps.End()

Create_Robot1()
Create_Robot2()