from classes import Interviewer, Interviewee
from protocols import Times, DegreeProgram
from scheduler import Scheduler
import heapq
import pandas as pd
def set_interviewer_priorities(input : list[Interviewer]):
    pq = []
    for interviewer in input:
        heapq.heappush(pq, (interviewer.priority, interviewer))
    return pq

def clean_interview_truth_value(input : pd.DataFrame | pd.Series, RC_or_IS : bool):
    for col in (['RC Nov 21 B', 'RC Nov 22 B'] if RC_or_IS else ['IS Nov 21 B', 'IS Nov 22 B']):
        saved = input[col].map(lambda x : str(int(x)).zfill(8 if RC_or_IS else 6))
        input[col] = saved

def get_day_and_type_of_appointment(appointment_type : str, day: str):
    switch = {
        ('RC', '1') : "RC Nov 21 B",
        ('RC', '2') : "RC Nov 22 B",
        ('IS', '1') : "IS Nov 21 B",
        ('IS', '2') : "IS Nov 22 B"  
    }
    return switch[(appointment_type, day)]

def get_timeslot(time_id : int, appointment_type : str):
    switch = {}
    if appointment_type == 'RC':
        switch = {
            "1" : Times.Time0915_0945,
            "2" : Times.Time1000_1045,
            "3" : Times.Time1100_1145,
            "4" : Times.Time1300_1345, 
            "5" : Times.Time1400_1445,
            "6" : Times.Time1500_1545, 
            "7" : Times.Time1600_1645,
            "8" : None
        }
    else:
        switch = {
            "1" : Times.Time0915_1015,
            "2" : Times.Time1030_1130,
            "3" : Times.Time1300_1400,
            "4" : Times.Time1415_1515,
            "5" : Times.Time1530_1630,
            "6" : None
        }
    return switch[str(time_id)]

def get_degree_program(input):
    switch = {
        'BS Chemical Engineering' : DegreeProgram.ChemicalEngg,
        'BS Civil Engineering' : DegreeProgram.CivilEngg,
        'BS Computer Engineering' : DegreeProgram.ComputerEngg,
        'BS Computer Science' : DegreeProgram.ComputerScience,
        'BS Electrical Engineering' : DegreeProgram.ElectricalEngg,
        'BS Electronics Engineering' : DegreeProgram.ElectronicsEngg,
        'BS Geodetic Engineering' : DegreeProgram.GeodeticEngg,
        'BS Industrial Engineering' : DegreeProgram.IndustrialEngg,
        'BS Materials Engineering' : DegreeProgram.MaterialsEngg,
        'BS Mechanical Engineering' : DegreeProgram.MechEngg,
        'BS Metallurgical Engineering' : DegreeProgram.MetalEngg,
        'BS Mining Engineering' : DegreeProgram.MiningEngg
    }
    return switch[input]
def create_interviewee_list_per_day(df : pd.DataFrame | pd.Series, appointment_type : str, day : str):
    # input is a row in the dataframe, output is the list of interviewee time slots for only one option (RC or IS)
    interviewee_list : list[Interviewee] = []
    for index, row in df.iterrows():
        truth_value = [int(bit) for bit in row[get_day_and_type_of_appointment(appointment_type, day)]]
        time_slots = []
        for index, digit in enumerate(truth_value): # guys this isn't O(n) I swear!!!
            if digit == 1:
                result = get_timeslot(index + 1, appointment_type)
                if result is not None:
                    time_slots += result
        interviewee_list.append(Interviewee(row["Name"], row["Email"], "0000", time_slots, index, get_degree_program(row["Degree Program"])))
    return interviewee_list


if __name__ == "__main__":
    df = pd.read_csv("./test_interviewee_data.csv", converters={'RC Nov 21 B': str})
    initial_clean = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    dropped_null = initial_clean.dropna()
    clean_interview_truth_value(dropped_null, True)
    upskill_days = [("RC", "1"), ("RC", "2"), ("IS", "1"), ("IS", "2")]
    prev_day = None
    interviewer_pq = set_interviewer_priorities([])
    unallocated_interviewees = []
    for _, (type, day) in enumerate(upskill_days):
        interviewee_list = create_interviewee_list_per_day(dropped_null, type, day)
        if prev_day == None or prev_day == day:
            unallocated_interviewees += interviewee_list
        else:
            unallocated_interviewees = []
        pq_empty = False
        while pq_empty == False or len(interviewee_list) == 0:
            current_company = heapq.heappop(interviewer_pq)
            schedule = Scheduler(interviewee_list, current_company)
            schedule.add_to_interviewer_schedule(8)
            unallocated_interviewees = schedule.not_allocated_interviewees


                
            



    



