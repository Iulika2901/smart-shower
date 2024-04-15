class Shower:
  water=True
  def __init__(self, mode,temp): 
      self._mode=mode
      self.temp=temp
  def run(self):
    print('run on {self.mode} mode')
  @classmethod
  def colorlight(cls, color1):
    return cls(color1,'rain')

class Boobles(Shower):
    def __init__(self, mode, temp, color):
        super().__init__(mode, temp)
        if mode == 'massage':
            self.boobles = True
        else:
            self.boobles = False

mode = input("Enter shower mode: ")
while mode != 'rain' and mode != 'massage':
    mode = input("Enter shower mode: ")
print('starting shower')
shower1 = Shower(mode, 31)
shower1.run()
shower1.colorlight('rain').run()
boobles1 = Boobles('rain', 31, 'red')
print(boobles1.colorlight('rain').run())
print(isinstance(boobles1,Shower))



#setting shower temperature


temp_target = int(input("Enter the target temperature: "))
temp_init = int(input("Enter the initial temperature: "))
time_shower = int(input("Enter the shower time (in minutes): "))
temp_obt = temp_init
stop = 1

while time_shower != 0 and stop != 0:
    time_shower_sec = time_shower * 60
    epsilon = pow(10, -1)

    print("Shower starting...")
    shower1.temp=temp_obt
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




