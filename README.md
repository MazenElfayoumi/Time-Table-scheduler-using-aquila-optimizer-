# Timetable Scheduler using Aquila Optimizer

This project is a Python-based timetable scheduler that uses the Aquila Optimizer, a nature-inspired algorithm modeled after the hunting behavior of the Aquila bird, to efficiently schedule exams. The scheduler takes into account various constraints, such as available timeslots, the number of exams, and potential conflicts, to create an optimized exam timetable.

## Features:
- **Population Initialization**: Generates an initial population of possible schedules.
- **Fitness Calculation**: Evaluates the number of conflicts in a schedule to determine its fitness.
- **Aquila Optimizer Steps**:
  - **Expanded Exploration**: Diversifies the search for optimal solutions.
  - **Narrowed Exploration**: Focuses on promising regions of the search space.
  - **Expanded Exploitation**: Intensifies the search around good solutions.
  - **Narrowed Exploitation**: Fine-tunes the best solutions to reach the optimal schedule.
- **Customizable Parameters**: Allows setting the number of exams, timeslots, population size, and maximum generations for optimization.
- **Date and Timeslot Assignment**: Automatically assigns dates and timeslots to exams based on the optimized schedule.

## How to Use:
1. Define the number of exams and available timeslots.
2. Set the start and end dates for the exam period.
3. Run the code to generate and optimize the exam schedule.
4. The optimized schedule will be printed, showing each exam's assigned date and timeslot.

## Example Usage:
```python
num_exams = len(exams)
timeslots = ['10:30 AM - 12:30 PM', '1:30 PM - 3:30 PM']
exam_start_date = datetime.strptime('2023-06-03', '%Y-%m-%d')
exam_end_date = datetime.strptime('2023-06-21', '%Y-%m-%d')

best_solution = time_scheduler(num_exams, num_timeslots, population_size=50, max_generations=100)
```
## Sample of the Output:

![output](https://github.com/user-attachments/assets/856cc9f4-7e97-4330-9a8a-ac56b2702644)


