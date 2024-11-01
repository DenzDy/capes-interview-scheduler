import sched
from sqlite3 import Time
from classes import Interviewee, Interviewer
from protocols import Times, DegreeProgram
from scheduler import Scheduler

def test_class_initialization():
    company = Interviewer("DCS", [Times.Time0915_1015, Times.Time1030_1130, Times.Time1415_1515, Times.Time1530_1630], [DegreeProgram.ComputerScience])
    interviewees = [Interviewee("A", "a@gmail.com", 'C0001', [Times.Time0915_1015], 1, DegreeProgram.ComputerScience), Interviewee("B", "b@gmail.com", 'C0002', [Times.Time0915_1015, Times.Time1030_1130], 2, DegreeProgram.ComputerScience), Interviewee("C", "c@gmail.com", 'C0003', [], 3, DegreeProgram.ComputerScience)]
    assert company.name == "DCS"
    x = list(map(lambda x : x.name,interviewees))
    assert x == ['A','B','C']

def test_pq_algorithm():
    company = Interviewer("DCS", [Times.Time0915_1015, Times.Time1030_1130, Times.Time1415_1515, Times.Time1530_1630], [DegreeProgram.ComputerScience])
    interviewees = [Interviewee("A", "a@gmail.com", 'C0001', [Times.Time0915_1015], 1, DegreeProgram.ComputerScience), Interviewee("B", "b@gmail.com", 'C0002', [Times.Time0915_1015, Times.Time1030_1130], 2, DegreeProgram.ComputerScience), Interviewee("C", "c@gmail.com", 'C0003', [], 3, DegreeProgram.ComputerScience)]
    x = map(lambda x : x.name,interviewees)
    scheduler_algo = Scheduler(interviewees, company)
    scheduler_algo.prio_queue_algorithm()
    y = []
    y.append(scheduler_algo.get_pq_elem()[2])
    y.append(scheduler_algo.get_pq_elem()[2])
    y.append(scheduler_algo.get_pq_elem()[2])
    y = list(map(lambda x : x.name, y))
    assert y == ['C', 'A', 'B']

def test_scheduling_algorithm_basic():
    company = Interviewer("DCS", [Times.Time0915_1015, Times.Time1030_1130, Times.Time1415_1515, Times.Time1530_1630], [DegreeProgram.ComputerScience])
    interviewees = [Interviewee("A", "a@gmail.com", 'C0001', [Times.Time0915_1015], 1, DegreeProgram.ComputerScience), Interviewee("B", "b@gmail.com", 'C0002', [Times.Time0915_1015, Times.Time1030_1130], 2, DegreeProgram.ComputerScience), Interviewee("C", "c@gmail.com", 'C0003', [], 3, DegreeProgram.ComputerScience)]
    x = map(lambda x : x.name,interviewees)
    scheduler_algo = Scheduler(interviewees, company)
    scheduler_algo.prio_queue_algorithm()
    scheduler_algo.add_to_interviewer_schedule(1)
    assert ['A'] == list(map(lambda x : x.name, company.interviewee_list[Times.Time0915_1015]))
    assert ['B'] == list(map(lambda x : x.name, company.interviewee_list[Times.Time1030_1130]))
    assert ['C'] == list(map(lambda x : x.name, scheduler_algo.not_allocated_interviewees))

def test_scheduling_algorithm_first_come_first_serve():
    company = Interviewer("DCS", [Times.Time0915_1015, Times.Time1030_1130, Times.Time1100_1145, Times.Time1300_1345], [DegreeProgram.ComputerScience])
    interviewees = [Interviewee("A", "a@gmail.com", 'C0001', [Times.Time0915_1015, Times.Time1030_1130, Times.Time1100_1145], 1, DegreeProgram.ComputerScience), 
                    Interviewee("B", "b@gmail.com", 'C0002', [Times.Time0915_1015], 2, DegreeProgram.ComputerScience), 
                    Interviewee("C", "c@gmail.com", 'C0003', [Times.Time1030_1130], 3, DegreeProgram.ComputerScience),
                    Interviewee("D", "d@gmail.com", 'C0004', [Times.Time1100_1145], 4, DegreeProgram.ComputerScience),
                    ]
    x = map(lambda x : x.name,interviewees)
    scheduler_algo = Scheduler(interviewees, company)
    scheduler_algo.prio_queue_algorithm()
    scheduler_algo.add_to_interviewer_schedule(1)
    assert ['A'] == list(map(lambda x : x.name, company.interviewee_list[Times.Time1100_1145]))
    assert ['C'] == list(map(lambda x : x.name, company.interviewee_list[Times.Time1030_1130]))
    assert ['B'] == list(map(lambda x : x.name, company.interviewee_list[Times.Time0915_1015]))
    assert ['D'] == list(map(lambda x : x.name, scheduler_algo.not_allocated_interviewees))



if __name__ == '__main__':
    test_scheduling_algorithm_first_come_first_serve()

