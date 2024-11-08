import sched
from classes import Interviewer, Interviewee
from protocols import Times, DegreeProgram
from scheduler import Scheduler
import heapq
import pandas as pd
def set_interviewer_priorities(input : list[Interviewer], appointment_type):
    pq = []
    input = list(filter(lambda x : x.appointment_type == appointment_type, input))
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
        'BS Mining Engineering' : DegreeProgram.MiningEngg,
        'ChE' : DegreeProgram.ChemicalEngg,
        'CE' : DegreeProgram.CivilEngg,
        'CoE' : DegreeProgram.ComputerEngg,
        'CS' : DegreeProgram.ComputerScience,
        'EE' : DegreeProgram.ElectricalEngg,
        'ECE' : DegreeProgram.ElectronicsEngg,
        'GE' : DegreeProgram.GeodeticEngg,
        'IE' : DegreeProgram.IndustrialEngg,
        'MatE' : DegreeProgram.MaterialsEngg,
        'ME' : DegreeProgram.MechEngg,
        'MetE' : DegreeProgram.MetalEngg,
        'EM' : DegreeProgram.MiningEngg
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
                    time_slots.append(result)
        interviewee_list.append(Interviewee(row["Name"], row["Email"], "0000", time_slots, index, get_degree_program(row["Degree Program"])))
    return interviewee_list
def company_time_block_cases(time_block: str, appointment_type: str) -> list[Times]:
    switch = {
        ("Second Half (1:45 PM - 5:45 PM)", "RC") : [Times.Time1400_1445, Times.Time1500_1545, Times.Time1600_1645],
        ("Second Half (1:45 PM - 5:45 PM)", "IS") : [Times.Time1415_1515, Times.Time1530_1630]        
    }
    return switch[(time_block, appointment_type)]



if __name__ == "__main__":

    # Mount data sets
    #company_df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTNYcUyx1PVU1V0SA0wnDULnewFxUiHUC7ldZdiUtWcWsHMFHJxvuW1Sv5WFDcdTp7u-u7ZzQjRUpFd/pub?gid=0&single=true&output=csv", converters={'Timeslot': str})
    #interviewee_df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRa3mG_GWUj4kBkaLQRwj8W5_XS8BOVyJ9uAYxjI6L8TgALXcfN5ad4cFnOhLMOlUQ76aTJz3By79-W/pub?gid=883177446&single=true&output=csv", converters={'RC Nov 21 B': str})

    company_df = pd.read_csv("./test_company_data.csv",converters={'Timeslot': str} )
    interviewee_df = pd.read_csv("./test_interviewee_data.csv")

    # Interviewee Data cleaning
    initial_clean = interviewee_df.loc[:, ~interviewee_df.columns.str.contains('^Unnamed')]
    dropped_null = initial_clean.dropna()
    clean_interview_truth_value(dropped_null, True)
    clean_interview_truth_value(dropped_null, False)

    upskill_days = [("RC", "1"), ("RC", "2"), ("IS", "1"), ("IS", "2")]

    # Company Data Cleaning
    company_df.columns = company_df.iloc[4]
    for _ in range(5):
        company_df.drop(company_df.index[0], axis=0, inplace=True)
    company_df = company_df.loc[:, company_df.columns.notna()]
    company_df = company_df.dropna()

    # Interviewer Object Creation
    interviewer_list = []
    for index, row in company_df.iterrows():
        time_slots = company_time_block_cases(row['Timeslot'], row['RC/IS'])
        preferred_program_list = row["Preferred Degree Program"].split(", ")
        preferred_program_list = [get_degree_program(x) for x in preferred_program_list]
        interviewer_list.append(Interviewer(row["Company Name"], time_slots, preferred_program_list, row['RC/IS']))
    
    # Interviewee Allocation
    prev_type = None
    unallocated_interviewees = []
    allocated_interviewees = []
    for _, (type, day) in enumerate(upskill_days):
        interviewee_list = create_interviewee_list_per_day(dropped_null, type, day)
        interviewer_pq = set_interviewer_priorities(interviewer_list, type)
        if prev_type == None or prev_type == type:
            print(type)
            interviewee_list += unallocated_interviewees
            interviewee_list = list(set(interviewee_list))
            interviewee_list = list(set(interviewee_list).difference(allocated_interviewees))
        else:
            print("Next Type")
            unallocated_interviewees = []
            allocated_interviewees = []
        pq_empty = False
        print(f"Interviewee List: {list(map(lambda x : x.name, interviewee_list))}")

        while len(interviewee_list) != 0:
            if len(interviewer_pq) == 0:
                break
            else:
                current_company = heapq.heappop(interviewer_pq)
            schedule = Scheduler(interviewee_list, current_company[1])
            schedule.prio_queue_algorithm()
            schedule.add_to_interviewer_schedule(1)
            unallocated_interviewees = schedule.not_allocated_interviewees
            allocated_interviewees += schedule.allocated_interviewees
            print(f"Allocated List: {list(map(lambda x : x.name, allocated_interviewees))}")

        prev_type = type
        print("Next Day \n")
