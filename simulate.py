import pybullet as p
import pybullet_data
import pyrosim.pyrosim as ps
import numpy as np
import time 
import math
import matplotlib.pyplot as plt

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
# p.loadSDF("box.sdf")

def sim1():
    duration = 500000
    robotId = p.loadURDF("body.urdf")
    ps.Prepare_To_Simulate(robotId)

    x = np.linspace(0,10000*np.pi, duration)
    y1 = np.sin(x)*np.pi/16 + math.pi/16
    y2 = np.sin(x)*np.pi/8 + math.pi/8
    y3 = np.cos(x)*np.pi/16 + math.pi/16
    y4 = np.cos(x)*np.pi/8 + math.pi/8

    for i in range(duration):
        ps.Set_Motor_For_Joint(bodyIndex = robotId, 
                            jointName = b'Foot_Torso',
                            controlMode = p.POSITION_CONTROL,
                            targetPosition = y1[i],
                            maxForce = 50)
        ps.Set_Motor_For_Joint(bodyIndex = robotId, 
                            jointName = b'Foot_Torso2',
                            controlMode = p.POSITION_CONTROL,
                            targetPosition = -y2[i],
                            maxForce = 500)
        
        ps.Set_Motor_For_Joint(bodyIndex = robotId, 
                            jointName = b'Foot_Torso3',
                            controlMode = p.POSITION_CONTROL,
                            targetPosition = y3[i],
                            maxForce = 50)
        ps.Set_Motor_For_Joint(bodyIndex = robotId, 
                            jointName = b'Foot_Torso4',
                            controlMode = p.POSITION_CONTROL,
                            targetPosition = -y4[i],
                            maxForce = 500)
        p.stepSimulation()
        time.sleep(1/500)

    p.disconnect()



def sim2():
    duration = 5000000
    robot2Id = p.loadURDF("body2.urdf")
    ps.Prepare_To_Simulate(robot2Id)

    x = np.linspace(0,100000*np.pi, duration)
    y1 = np.sin(x)*np.pi/16 + math.pi/16
    y2 = np.sin(x)*np.pi/8 + math.pi/8
    y3 = np.sin(x)*np.pi/4 + math.pi/8
    y4 = np.cos(x)*np.pi/4 + math.pi/8

    for i in range(duration):
        ps.Set_Motor_For_Joint(bodyIndex = robot2Id, 
                               jointName = b'parent_child1',
                               controlMode = p.POSITION_CONTROL,
                               targetPosition = y3[i],
                               maxForce = 100)
        ps.Set_Motor_For_Joint(bodyIndex = robot2Id, 
                            jointName = b'parent_child2',
                            controlMode = p.POSITION_CONTROL,
                            targetPosition = -y4[i],
                            maxForce = 100)
        p.stepSimulation()
        time.sleep(1/500)

    p.disconnect()

sim1()
#  sim2()
    
duration = 100  
# x = np.linspace(0,10000*np.pi, duration)
# y1 = np.sin(x)*np.pi/16 + math.pi/16
# y2 = np.sin(x)*np.pi/8 + math.pi/8
# y3 = np.cos(x)*np.pi/16 + math.pi/16
# y4 = np.cos(x)*np.pi/8 + math.pi/8


# x = np.linspace(0,100000*np.pi, duration)
# y1 = np.sin(x)*np.pi/16 + math.pi/16
# y2 = np.sin(x)*np.pi/8 + math.pi/8
# y3 = np.sin(x)*np.pi/4 + math.pi/8
# y4 = np.cos(x)*np.pi/4 + math.pi/8

# plt.plot(x.T, y1.T)
# plt.plot(x.T, y2.T)
# plt.plot(x.T, y3.T)
# plt.plot(x.T, y4.T)
# plt.title("Signals")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()