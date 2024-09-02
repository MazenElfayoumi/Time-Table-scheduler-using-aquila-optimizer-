import random
from datetime import datetime, timedelta
 
def initialize_population(population_size, num_exams, num_timeslots):
    population = []
    for _ in range(population_size):
        solution = random.sample(range(num_timeslots), num_exams)
        population.append(solution)
    return population
 
def calculate_fitness(solution):
    conflicts = 0
    for i in range(len(solution)):
        for j in range(i+1, len(solution)):
            if solution[i] == solution[j]:  # Exams scheduled on the same day
                conflicts += 1
    return -conflicts  # Return negative conflicts to maximize fitness
 
def update_mean_value(solution):
    # Code to update the mean value of the current solution XM(t)
    # Modify the solution in-place or return the updated solution
    # Add your specific logic here
    return solution
 
def expanded_exploration(solution):
    # Code to perform expanded exploration (Step 1)
    # Update the solution using Eq. (3)
    # Add your specific logic here
    return solution
 
def narrowed_exploration(solution):
    # Code to perform narrowed exploration (Step 2)
    # Update the solution using Eq. (5)
    # Add your specific logic here
    return solution
 
def expanded_exploitation(solution):
    # Code to perform expanded exploitation (Step 3)
    # Update the solution using Eq. (13)
    # Add your specific logic here
    return solution
 
def narrowed_exploitation(solution):
    # Code to perform narrowed exploitation (Step 4)
    # Update the solution using Eq. (14)
    # Add your specific logic here
    return solution
 
def time_scheduler(num_exams, num_timeslots, population_size, max_generations):
    population = initialize_population(population_size, num_exams, num_timeslots)
    best_solution = None
 
    for t in range(max_generations):
        for i in range(len(population)):
            solution = population[i]
 
            solution = update_mean_value(solution)
            # Update any other variables or parameters if necessary
 
            if t <= (2/3) * max_generations:
                if random.random() <= 0.5:
                    solution = expanded_exploration(solution)
                else:
                    solution = narrowed_exploration(solution)
            else:
                if random.random() <= 0.5:
                    solution = expanded_exploitation(solution)
                else:
                    solution = narrowed_exploitation(solution)
 
            population[i] = solution
 
            if calculate_fitness(solution) < calculate_fitness(best_solution):
                best_solution = solution
 
    return best_solution
 

# Exam information
exams = ["Climate Change and Sustainability - GEO217","History of Civilizations – HIS111","Introduction to Law and Human Rights - PSC011","English 1 - LAN020","Arabic Language - LAN010","English 2 - LAN022","Critical Thinking -LAN028","History of Art – VIA121","History of Science & Technology – UNR040","Entrepreneurship & Innovation - MGT031","Introduction to Statistics – MAT010","First Aid – ADL123""Research and Analysis Skills - LIB116","Japanese Language - LAN051","Communication Skills -COM011","Introduction to Architecture – ARC013","Advanced Physical Chemistry (CHE341)","Structure Programming (CSE014)","ELE 437 DSP","Mechanics (MAT123)","Chemistry for Arts (CHE101","ASU General Biology I (BIO181)","Plant Biotechnology (BIO341)","Laboratory Safety (GES119)","Lab Safety (CHE119)","Synthesis of Nanomaterials (CHE323)","Dynamics (MAT121)","Optimization Tech","Discrete Mathematics(CSE 315)","Computer Architecture (CSE 132)","Computer Vision (CSE 383)","Mathematics II (MAT112)","Differential Equations and Numerical Analysis (MAT313)","Organic Chemistry (CHE111)","Journal Club (CHE 319)", "Molecular Biology II  (BIO321)",
"Economic Geology (GES312)",
"Embedded Systems (CSE 272)",
"OOP (CSE 015) + OOP and DS ASU (CSE 205)",
"Precalculus (MAT170)",
"Calculus for Engineering I (MAT113)",
"Calculus for Engineering II (MAT115)",
"Engineering Chemistry (CHE142)",
"Renewable Energy (CHE241)",
"Intro to Nanoscience (PH211)",
"Biophysics (PHY261)",
"CHE434 Pharmaceutical Nanotechnology",
"Petrophysics and Well Logging (GES321)",
"Design and Analysis of Alg/ (CSE 112)",
"Brief Calculus (MAT235)",
"Modern Physics (PHY232)",
"Physical Chemistry (CHE141)",
"Elec. And Elect. Circuits (CSE 113)",
"RB Dynamics (MAT221)",
"Bio farming (BIO332)",
"General Biology (BIO102)",
"Molecular Genetics (BIO221)",
"Engineering Geology (GES316)",
"Statistics (MAT131)",
"Machine Learning (AIE 121)",
"Database Systems (CSE 221)",
"Environmental Biotechnology (ENV311)",
"Introduction to Biotechnology (BIO311)",
"BIO101 Medicinal Plants",
"Electricity and Magnetism (Phy 211)",
"EM waves & optics (PHY231)",
"University Physics I (PHY121)",
"Probability and Statistics (MAT231)",
"Molecular Materials (CHE322)",
"Mineralogy (GES112)",
"Knowledge-Based Systems (AIE 212)",
"Software Engineering (CSE 251)",
"Cell Biology (BIO223)",
"Analytical Chemistry (CHE232)",
"Lab Safety (BIO119)",
"Geophysical Exploration (GES423)"]

num_exams = len(exams)

# Define the available timeslots
timeslots = ['10:30 AM - 12:30 PM', '1:30 PM - 3:30 PM']
num_timeslots = len(timeslots)

# Specify the start date for the exams
exam_start_date = datetime.strptime('2023-06-03', '%Y-%m-%d')
exam_end_date = datetime.strptime('2023-06-21', '%Y-%m-%d')

# Calculate the number of days needed for all exams (1 day per exam + 2 days gap)
num_days = num_exams * 2 - 1

# Generate the date-time schedule for exams (randomized within timeslots)
exam_schedule = []
current_date = exam_start_date
days_added = 0

while current_date <= exam_end_date and len(exam_schedule) < num_exams:
    if current_date.weekday() != 4:  # Skip Fridays (weekday() returns 4 for Friday)
        for timeslot in timeslots:
            if len(exam_schedule) < num_exams:
                exam_index = len(exam_schedule)
                exam = exams[exam_index]
                exam_schedule.append((exam, current_date.strftime('%Y-%m-%d'), timeslot))
    next_date = current_date + timedelta(days=1)
    if exam_start_date <= next_date <= exam_end_date:
        current_date = next_date
    else:
        break

# If there are remaining exams, schedule them randomly within the available dates and time slots
remaining_exams = num_exams - len(exam_schedule)
remaining_dates = [date for _, date, _ in exam_schedule if date >= '2023-06-12']

if remaining_exams > 0:
    for _ in range(remaining_exams):
        date = random.choice(remaining_dates)
        timeslot = random.choice(timeslots)
        exam = exams[len(exam_schedule)]
        exam_schedule.append((exam, date, timeslot))

# Sort the exam schedule by date
sorted_exam_schedule = sorted(exam_schedule, key=lambda x: x[1])

# Print the exam schedule
for exam_info in sorted_exam_schedule:
    exam, date, timeslot = exam_info
    print(f"Date-Time: {date} {timeslot}")
    print(f"Exam: {exam}")
    print()