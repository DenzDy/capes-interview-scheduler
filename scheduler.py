from __future__ import annotations
from protocols import Times, DegreeProgram, Participant
from classes import Interviewee, Interviewer
import queue
from typing import Tuple
class Scheduler:
    def __init__(self, interviewee_data: list[Interviewee], interviewer_data: Interviewer):
        self._interviewee_data = interviewee_data
        self._interviewer_data = interviewer_data
        self._not_allocated_interviewees : list[Interviewee] = []

    def prio_queue_algorithm(self):
        pq = queue.PriorityQueue()
        i = 1
        for interviewee in self._interviewee_data:
            pq.put((interviewee.priority, i, interviewee))
            i+=1 
        self._pq = pq
    def get_pq_elem(self) -> Tuple[int, int, Interviewee]:
        return self._pq.get()
    def add_to_interviewer_schedule(self, interviewee_allotment_per_timeslot: int):
        # I have yet to figure out how to make this more efficient
        not_empty = True
        while not_empty == True:
            item = self.get_pq_elem()[2]
            print(item.name)
            matching_timeslots = set(item.time_slots).intersection(self._interviewer_data.time_slots)
            if len(matching_timeslots) != 0: # check if matches occur
                for time_slot in matching_timeslots:
                    print(time_slot)
                    if self._interviewer_data.add_to_interviewee_list(item, time_slot, interviewee_allotment_per_timeslot) == 1: # checks if time slot is full
                        break
            else:
                self._not_allocated_interviewees.append(item)
            if self._pq.empty() == True:
                not_empty = False
    @property
    def not_allocated_interviewees(self):
        return self._not_allocated_interviewees