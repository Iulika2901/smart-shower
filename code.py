temp_target = int(input("Enter the target temperature: "))
temp_init = int(input("Enter the initial temperature: "))
time_shower = int(input("Enter the shower time (in minutes): "))
temp_obt = temp_init
stop = 1

while time_shower != 0 and stop != 0:
    time_shower_sec = time_shower * 60
    epsilon = pow(10, -1)

    print("Shower starting...")

    for i in range(time_shower_sec):
        media = abs(temp_obt - temp_target) / 2
        if temp_obt < temp_target:
            if media < epsilon:
                temp_obt = temp_target
            elif temp_target > temp_obt + media:
              temp_obt = temp_target
            else: temp_obt=temp_obt+media
        if temp_obt > temp_target:
            if media < epsilon:
                temp_obt = temp_target
            elif temp_target < temp_obt + media:
                temp_obt = temp_target
            else: temp_obt=temp_obt-media
        if  temp_obt == temp_target:  temp_obt=temp_obt+0.5
        
        print("Current temperature:", temp_obt)
        minutes_remaining = (time_shower_sec - i) // 60
        seconds_remaining = (time_shower_sec - i) % 60
        print("Time remaining:", minutes_remaining, "minutes and", seconds_remaining, "seconds")

    
    print("Final temperature:", temp_obt)
    time_shower = int(input("Enter the shower time in minutes (or 0 to stop): "))
    stop = int(input("Press 0 to stop the shower: "))
