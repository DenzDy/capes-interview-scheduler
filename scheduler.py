from __future__ import annotations
from protocols import Times, DegreeProgram, Participant
from classes import Interviewee, Interviewer
from typing import Tuple
import heapq

class Scheduler:
    def __init__(self, interviewee_data: list[Interviewee], interviewer_data: Interviewer):
        self._interviewee_data = interviewee_data
        self._interviewer_data = interviewer_data
        self._not_allocated_interviewees : list[Interviewee] = []
        self._allocated_interviewees: list[Interviewee] = []
    def prio_queue_algorithm(self):
        pq = []
        i = 1
        for interviewee in self._interviewee_data:
            heapq.heappush(pq, (interviewee.priority, i, interviewee))
            i+=1 
        self._pq = pq
    def get_pq_elem(self) -> Tuple[int, int, Interviewee]:
        return heapq.heappop(self._pq)
    def add_to_interviewer_schedule(self, interviewee_allotment_per_timeslot: int):
        # I have yet to figure out how to make this more efficient
        not_empty = True
        while not_empty == True:
            item = self.get_pq_elem()[2]
            matching_timeslots = set(item.time_slots).intersection(set(self._interviewer_data.time_slots))
            #print(f"Interviewee Timeslot: {item.time_slots}\nInterviewer Timeslot: {self._interviewer_data.time_slots}\nSet Intersection: {matching_timeslots}")
            if len(matching_timeslots) != 0: # check if matches occur
                checker = False
                for time_slot in matching_timeslots:
                    if self._interviewer_data.add_to_interviewee_list(item, time_slot, interviewee_allotment_per_timeslot) == 1: # checks if time slot is full
                        # check if any of the items in the list can be replaced (this is probably very slow)
                        self._interviewee_data.remove(item)
                        self._allocated_interviewees.append(item)
                        checker = True
                        break
                if checker == False:
                    result = self._interviewer_data.resolve_first_come_first_serve_conflict(item, time_slot)
                    if result != None:
                        self._not_allocated_interviewees.append(result)
                        break
                    else:
                        self._interviewee_data.remove(item) # TODO: refactor such that both instances of this line of code are merged into one
                        self._allocated_interviewees.append(item)
            else:
                self._not_allocated_interviewees.append(item)
            if not self._pq:
                not_empty = False
    @property
    def not_allocated_interviewees(self):
        return self._not_allocated_interviewees
    @property
    def allocated_interviewees(self):
        return self._allocated_interviewees