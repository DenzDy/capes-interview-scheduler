from __future__ import annotations
from protocols import Times, DegreeProgram, Participant
from classes import Interviewee, Interviewer
import queue
class Scheduler:
    def __init__(self, interviewee_data: list[Interviewee], interviewer_data: Interviewer):
        self._interviewee_data = interviewee_data
        self._interviewer_data = interviewer_data
        self._not_allocated_interviewees : list[Interviewee] = []

    def prio_queue_algorithm(self):
        pq = queue.PriorityQueue()
        for interviewee in self._interviewee_data:
            pq.put((interviewee.priority, interviewee))
        self.pq = pq

    def add_to_interviewer_schedule(self, interviewee_allotment_per_timeslot: int):
        # I have yet to figure out how to make this more efficient
        while self.pq.get() == None:
            item : Interviewee = self.pq.get()[1]
            matching_timeslots = set(item.time_slots).intersection(self._interviewer_data.time_slots)
            if len(matching_timeslots) != 0: # check if matches occur
                for time_slot in matching_timeslots:
                    if self._interviewer_data.add_to_interviewee_list(item, time_slot, interviewee_allotment_per_timeslot) == 0: # checks if time slot is full
                        self._not_allocated_interviewees.append(item)


                    
    