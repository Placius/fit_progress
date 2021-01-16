import time, os
import winsound

all_infos = []
exercises = []

with open("exercises/warm-up.txt") as file:
    lines = file.read().split("\n")
    line_num = 1
    for line in lines:
        all_infos.append(line)
        if line_num > 2:
            exercises.append(line)
        line_num += 1
t = 5
for i in range(0,6):
    os.system("cls")
    print("Warm up starting in " + str(t) + "...")
    time.sleep(1)
    t -= 1

winsound.Beep(800, 1000)

for exercise in exercises:
    length = int(all_infos[1])
    sec = length
    while sec != 0:
        os.system("cls")
        print(all_infos[0].upper())
        print("\n\nExercise:", exercise)
        print("Time for this exercise - " + str(sec))
        time.sleep(1)
        sec -= 1
    
    winsound.Beep(800, 1000)
    print("Next exercise....")
    time.sleep(3)