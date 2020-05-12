################################################################################
## DATA COLLECTIONS ############################################################
################################################################################
# list of exercise dictionaries
# dictionary keys: values:
# - name: name of the exercise
# - types: lower-push, lower-pull, upper-push, upper-pull, total-body
# - level: 1 = beginner, 2 = intermediate, 3 = advanced
# IDEAS
# - group make different exercise dictionary lists for each block?

import random as rand

primary_block_exercises = [
    {'name': 'squats', 'type': ['lower push'], 'level': 1, 'reps': '10'},
    {'name': 'split squats', 'type': ['lower push'], 'level': 2, 'reps': '10'},
    {'name': 'single leg glute bridge', 'type': ['lower pull'], 'level': 1, 'reps': '10'},
    {'name': 'v up reaches', 'type': ['anterior core'], 'level': 2, 'reps': '10'},
    {'name': 'reverse sit ups', 'type': ['anterior core'], 'level': 1, 'reps': '10'},
    {'name': 'pavlov press', 'type': ['rotational core'], 'level': 1, 'reps': '10'},
    {'name': 'offset resistance band rows', 'type': ['upper pull'], 'level': 2, 'reps': '10'},
    {'name': 'seated resistance band rows', 'type': ['upper pull'], 'level': 1, 'reps': '10'},
    {'name': 'eccentric push ups', 'type': ['upper push',], 'level': 3, 'reps': '10'},
    {'name': 'windshield wipers', 'type': ['rotational core',], 'level': 2, 'reps': '10'},
    {'name': 'russian twists', 'type': ['rotational core',], 'level': 1, 'reps': '30'},
]

special_block_exercises = [
    {'name': 'rapid response drills', 'type': ['speed',], 'level': 2, 'reps': '10'},
    {'name': 'long jump', 'type': ['power',], 'level': 2, 'reps': '10'},
    {'name': 'seated arm sprints', 'type': ['speed',], 'level': 1, 'reps': '10'},
    {'name': 'vertical jump', 'type': ['power',], 'level': 2, 'reps': '10'},
    {'name': 'stationary sprints', 'type': ['speed',], 'level': 1, 'reps': '10'},
    {'name': 'lateral jumps', 'type': ['power',], 'level': 3, 'reps': '10'},
    {'name': 'single leg jump', 'type': ['',], 'level': 3, 'reps': '10'},
    {'name': 'depth drop', 'type': ['',], 'level': 1, 'reps': '10'},
]

accessory_block_exercises = [
    {'name': 'adductor lifts', 'type': ['lower',], 'level': 1, 'reps': '10'},
    {'name': 'glute bridge leg lifts', 'type': ['lower pull',], 'level': 1, 'reps': '10'},
    {'name': 'IYTWs', 'type': ['upper',], 'level': 2, 'reps': '10'},
    {'name': 'hollow hold', 'type': ['anterior core',], 'level': 2, 'reps':'30secs'},
    {'name': 'HE to CC', 'type': ['core','upper','lower'], 'level': 3, 'reps': '10'},
    {'name': 'Iso Deadbug', 'type': ['core','upper','lower'], 'level': 1, 'reps': '10'},
    {'name': 'glute bridge hip fallouts', 'type': ['core','lower'], 'level': 2, 'reps': '10'},
    {'name': 'supermans', 'type': ['core','upper'], 'level': 1, 'reps': '10'},
    {'name': 'blackburns', 'type': ['upper',], 'level': 1, 'reps': '10'},
    {'name': 'split squat iso', 'type': ['lower',], 'level': 2, 'reps': '10'},
    {'name': 'plank', 'type': ['core',], 'level': 1, 'reps': '30secs'},
    {'name': 'glute bridge heel walkouts', 'type': ['lower',], 'level': 2, 'reps': '10'},
    {'name': 'side plank hip ups', 'type': ['core',], 'level': 2, 'reps': '10'},
    {'name': 'glute bridge marches', 'type': ['lower',], 'level': 1, 'reps': '30'},
    {'name': 'prone floor sweeps', 'type': ['core','upper'], 'level': 1, 'reps': '10'},
    {'name': 'hydrants to kick backs', 'type': ['lower',], 'level': 1, 'reps': '10'},
    {'name': 'high plank shoulder taps', 'type': ['core','upper'], 'level': 2, 'reps': '20'},
]
    # Dictionary template
    # {'name': '', 'type': ['',], 'level': ,},

################################################################################
## RANDOM WORKOUT GENERATOR CORE CODE ##########################################
################################################################################

# temporary storage for exercises already selected for the workout. used to avoid repeats
# referenced inside of
selected_exercises = []

def random_primary_block_exercise(type, level):
    """
    prints a random exercise from the 'primary_block_exercises' list
    """
    global selected_exercises
    exercise_bank = []

    for exercise in primary_block_exercises:
        if type in exercise['type'] and exercise not in selected_exercises and exercise['level'] == level:
            exercise_bank.append(exercise)

    ex = exercise_bank[rand.randint(0,len(exercise_bank)-1)]
    selected_exercises.append(ex)
    workout_sheet.write(ex['name'].title() + "   x" + ex['reps'] + "\n")

def random_special_block_exercise(type):
    """
    prints a random exercise from the 'special_block_exercises' list
    """
    global selected_exercises
    # selects only exercises of a certain type and puts those into a temporary list
    exercise_bank = []
    for exercise in special_block_exercises:
        if type in exercise['type'] and exercise not in selected_exercises:
            exercise_bank.append(exercise)

    # randomly selects an exercise and adds it to a temporary list
    ex = exercise_bank[rand.randint(0,len(exercise_bank)-1)]
    selected_exercises.append(ex)
    workout_sheet.write(ex['name'].title() + "   x" + ex['reps'] + "\n")

def random_accessory_block_exercise(type, level):
    """
    prints a random exercise from the 'random_accessory_block_exercises' list
    """
    global selected_exercises
    exercise_bank = []

    for exercise in accessory_block_exercises:
        if type in exercise['type'] and exercise not in selected_exercises and exercise['level'] == level:
            exercise_bank.append(exercise)

    ex = exercise_bank[rand.randint(0,len(exercise_bank)-1)]
    selected_exercises.append(ex)
    workout_sheet.write(ex['name'].title() + "   x" + ex['reps'] + "\n")

workout_sheet = open("workout_sheet.txt","w")
workout_sheet.write("Today's Workout: ")
workout_sheet.close()

workout_sheet = open("workout_sheet.txt","a")

# creates a random workout block with the 'type' and the 'level of each exercise specified'
accessory_block_template = [['upper',1],['lower',1],['core',1],['upper',2],['lower',2],['core',2]]
workout_sheet.write('\n\nACCESORY BLOCK: x3\n\n')
for i in accessory_block_template:
    random_accessory_block_exercise(i[0],i[1])
# resets the 'selected_exercises' temporary list
selected_exercises = []

primary_block_template = [['upper pull',1],['anterior core',1],['lower push',2],['rotational core',2]]
workout_sheet.write('\nACCESORY BLOCK: x3\n\n')
for i in primary_block_template:
    random_primary_block_exercise(i[0],i[1])

selected_exercises = []

workout_sheet.close()
