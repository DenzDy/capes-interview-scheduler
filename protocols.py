from datetime import datetime
from typing import NewType, Protocol
from enum import StrEnum

class DegreeProgram(StrEnum):
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

class Timeslot:
    def __init__(self, start_time: datetime, end_time: datetime):
        self._start_time = start_time
        self._end_time = end_time
    @property
    def start_time(self) -> datetime:
        return self._start_time
    @property
    def end_time(self) -> datetime:
        return self._end_time

class Participant(Protocol):
    @property
    def name(self) -> str:
        # Return str that is the name of the participant (could be interviewee/interviewer)
        ...
    @property
    def time_slots(self) -> list[Timeslot]:
        # Returns time slots of participant
        ...