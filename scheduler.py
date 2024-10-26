from __future__ import annotations
from protocols import Timeslot, DegreeProgram, Participant
    
class Interviewee:
    def __init__(self, name: str, capes_id: str, time_slots: list[Timeslot], degree_program: DegreeProgram):
        self._name = name
        self._capes_id = capes_id
        self._time_slots = time_slots
        self._degree_program = degree_program
        self._priority = len(time_slots)
    @property
    def name(self) -> str:
        return self._name
    @property
    def capes_id(self) -> str:
        return self._capes_id
    @property
    def time_slots(self) -> list[Timeslot]:
        return self._time_slots
    @property
    def degree_program(self) -> DegreeProgram:
        return self._degree_program
    @property
    def priority(self) -> int:
        return self._priority
    
class Interviewer:
    def __init__(self, name: str, capes_id: str, time_slots: list[Timeslot], degree_program_preference: list[DegreeProgram] | DegreeProgram | None):
        self._name = name
        self._capes_id = capes_id
        self._time_slots = time_slots
        self._degree_program_preference = degree_program_preference
        self._interviewee_list = []
    @property
    def name(self) -> str:
        return self._name
    @property
    def capes_id(self) -> str:
        return self._capes_id
    @property
    def time_slots(self) -> list[Timeslot]:
        return self._time_slots
    @property
    def degree_program_preference(self) -> list[DegreeProgram] | DegreeProgram | None:
        return self._degree_program_preference
    @property
    def interviewee_list(self) -> list[Interviewee]:
        return self.interviewee_list
    def add_to_interviewee_list(self, interviewee: Interviewee):
        self._interviewee_list.append(interviewee)
    