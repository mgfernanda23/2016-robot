from robotpy_ext.autonomous import state, timed_state, StatefulAutonomous
from components import intake, drive as Drive
import wpilib
from networktables import NetworkTable 

class Charge(StatefulAutonomous):
    MODE_NAME = "Charge"
    DEFAULT = False
    
    intake = intake.Arm
    drive = Drive.Drive
    
    @timed_state(duration = 4.5, first = True)
    def charge(self, initial_call):
        self.drive.move(1,0)