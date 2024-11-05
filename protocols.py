from datetime import datetime
from typing import NewType, Protocol
from enum import Enum

class DegreeProgram(str, Enum):
    ChemicalEngg = 'BS Chemical Engineering'
    CivilEngg = 'BS Civil Engineering'
    ComputerEngg = 'BS Computer Engineering'
    ComputerScience = 'BS Computer Science'
    ElectricalEngg = 'BS Electrical Engineering'
    ElectronicsEngg = 'BS Electronics Engineering'
    GeodeticEngg = 'BS Geodetic Engineering'
    IndustrialEngg = 'BS Industrial Engineering'
    MaterialsEngg = 'BS Materials Engineering'
    MechEngg = 'BS Mechanical Engineering'
    MetalEngg = 'BS Metallurgical Engineering'
    MiningEngg = 'BS Mining Engineering'

class Times(str, Enum): # not ideal, but I don't really want to deal with datetime right now
# Resume Consultations
    Time0915_0945 = "09:00 AM - 09:45 AM"
    Time1000_1045 = "10:00 AM - 10:45 AM"
    Time1100_1145 = "11:00 AM - 11:45 AM"
    Time1300_1345 = "01:00 PM - 01:45 PM"
    Time1400_1445 = "02:00 PM - 02:45 PM"
    Time1500_1545 = "03:00 PM - 03:45 PM"
    Time1600_1645 = "04:00 PM - 04:45 PM"
    Time1700_1745 = "05:00 PM - 05:45 PM"

# Interview Simulations
    Time0915_1015 = "09:15 AM - 10:15 AM"
    Time1030_1130 = "10:30 AM - 11:30 AM"
    Time1300_1400 = "01:00 PM - 02:00 PM"
    Time1415_1515 = "02:15 PM - 03:15 PM"
    Time1530_1630 = "03:30 PM - 04:30 PM"
    Time1645_1745 = "04:45 PM - 05:45 PM"

class Participant(Protocol):
    @property
    def name(self) -> str:
        # Return str that is the name of the participant (could be interviewee/interviewer)
        ...
    @property
    def time_slots(self) -> list[Times]:
        # Returns time slots of participant
        ...