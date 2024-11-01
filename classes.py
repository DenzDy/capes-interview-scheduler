from __future__ import annotations
from protocols import Times, DegreeProgram, Participant
import heapq
    
class Interviewee:
    def __init__(self, name: str, email: str, capes_id: str, time_slots: list[Times], registration_order: int, degree_program: DegreeProgram):
        self._name = name
        self._email = email
        self._capes_id = capes_id
        self._time_slots = time_slots
        self._degree_program = degree_program
        self._priority = len(time_slots)
        self._registration_order = registration_order
        self._granted_slot: Times
    @property
    def name(self) -> str:
        return self._name
    @property
    def email(self) -> str:
        return self._email
    @property
    def capes_id(self) -> str:
        return self._capes_id
    @property
    def time_slots(self) -> list[Times]:
        return self._time_slots
    @property
    def degree_program(self) -> DegreeProgram:
        return self._degree_program
    @property
    def priority(self) -> int:
        return self._priority
    @property
    def registration_order(self) -> int:
        return self._registration_order
    @property
    def granted_slot(self) -> Times:
        return self._granted_slot
    
    def set_granted_slot(self, time: Times):
        self._granted_slot = time
class Interviewer:
    def __init__(self, name: str, time_slots: list[Times], degree_program_preference: list[DegreeProgram] | DegreeProgram | None):
        self._name = name
        self._time_slots = time_slots
        self._degree_program_preference = degree_program_preference
        self._interviewee_list : dict[Times, list[Interviewee]] = {}
    @property
    def name(self) -> str:
        return self._name
    @property
    def time_slots(self) -> list[Times]:
        return self._time_slots
    @property
    def degree_program_preference(self) -> list[DegreeProgram] | DegreeProgram | None:
        return self._degree_program_preference
    @property
    def interviewee_list(self) -> dict[Times, list[Interviewee]]:
        return self._interviewee_list
    def add_to_interviewee_list(self, interviewee: Interviewee, time : Times, max_alloc: int):
        if time not in self._interviewee_list.keys():
            self._interviewee_list[time] = []
        elif len(self._interviewee_list[time]) >= max_alloc:
            return 0
        interviewee.set_granted_slot(time)
        self._interviewee_list[time].append(interviewee)
        return 1    
    def resolve_first_come_first_serve_conflict(self, interviewee: Interviewee, time: Times) -> Interviewee | None:
        list_of_timeslots: list[Interviewee] = []
        for item in interviewee.time_slots:
            list_of_timeslots += self._interviewee_list[item]
        list_of_timeslots.sort
        if any(interviewee.registration_order < item.registration_order for item in list_of_timeslots):
            index = self._interviewee_list[list_of_timeslots[-1].granted_slot].index(list_of_timeslots[-1])
            self._interviewee_list[list_of_timeslots[-1].granted_slot][index] = interviewee
            return list_of_timeslots[-1]
        
        
