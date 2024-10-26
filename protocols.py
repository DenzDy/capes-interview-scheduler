from datetime import datetime
from typing import NewType, Protocol
from enum import StrEnum

class DegreeProgram(StrEnum):
    ComputerScience = 'BS Computer Science'
    IndustrialEngg = 'BS Industrial Engineering'
    ComputerEngg = 'BS Computer Engineering'
    MechEngg = 'BS Mechanical Engineering'
    CivilEngg = 'BS Civil Engineering'

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