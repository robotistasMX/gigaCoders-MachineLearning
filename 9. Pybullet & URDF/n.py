import pybullet as p
import pybullet_data
import time 
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #used by loadURDF
p.setGravity(0,0,-9.8)
p.setTimeStep(0.0001)       # this slows everything down, but let's be accurate...
p.setRealTimeSimulation(0)  # we want to be faster than real time :)
planeId = p.loadURDF("plane.urdf")

robot = p.loadURDF("opera_description/urdf/tao.urdf", [0, 0, .07])

def forward(t,k):
    p.setJointMotorControl2(
            robot,
            0,
            p.VELOCITY_CONTROL,
            targetVelocity=k,
            force=t
        )

    p.setJointMotorControl2(
            robot,
            1,
            p.VELOCITY_CONTROL,
            targetVelocity=k,
            force=t
        )
    p.setJointMotorControl2(
            robot,
            2,
            p.VELOCITY_CONTROL,
            targetVelocity=k,
            force=t
        )

    p.setJointMotorControl2(
            robot,
            3,
            p.VELOCITY_CONTROL,
            targetVelocity=k,
            force=t
        )

    

while True:
    
    for _ in range(100000):   
        p.stepSimulation()
        forward(1.5, 1.50)

    for _ in range(100000):   
        p.stepSimulation()
        forward(1.5, -1.50)