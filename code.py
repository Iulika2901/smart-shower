import requests
import time
import json

c3p0={"name": "Luke Skywalker",
			"height": "172",
			"mass": "77",
			"hair_color": "blond",
			"skin_color": "fair",
			"eye_color": "blue",
			"birth_year": "19BBY",
			"gender": "male"}
c1p0=json.loads(c1p0)
print(c1p0['name'])

c3p0=json.loads(c3p0)
c3p0['name']="Popescu"
c3p0_str=json.dumps(c3p0)
print(c3p0_str)

while True:
 req = requests.get("https://swapi.dev/api/people/2/")
 print(req.status_code)
 if req.status_code!=200:
   pass
   time.sleep(300)
 print(f"User name is \t\t{user['name']}")
 print(f"User name is \t\t{user['birth_year']}")
 for each in person['each']:
    req=requests(each)
    each = req.json()
    print("Person is: " ,person['name'])





filename=input("what is the filename?")
with open(filename,'r') as file:
    file = file.readlines()
for content in file:
    file.write(content)
print(file[2])
if file[2] in ['cardiac problems', 'avc','hart atack','temperature']:
    ok=True
    print("pbbbb")


with open('out.txt','a') as file:
     file.write("output files\n")


def temperature():
 temp_target = int(input("Enter the target temperature: "))
 if ok==True: temp_target = int(input("Enter the target temperature below 32: "))
 temp_init = int(input("Enter the initial temperature: "))
 time_shower = int(input("Enter the shower time (in minutes): "))
 temp_obt = temp_init
 stop = 1
 def shower(**key):
 print(key)
  while time_shower != 0 and stop != 0:
    time_shower_sec = time_shower * 60
    epsilon = pow(10, -1)

    file.write("Shower starting...")
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
        
        file.write("Current temperature:", temp_obt)
        minutes_remaining = (time_shower_sec - i) // 60
        seconds_remaining = (time_shower_sec - i) % 60
        file.write("Time remaining:", minutes_remaining, "minutes and", seconds_remaining, "seconds")

    if  time_shower != 0 and stop != 0: shower()
    file.write("Final temperature:", temp_obt)
    
    time_shower = int(input("Enter the shower time in minutes (or 0 to stop): "))
    stop = int(input("Press 0 to stop the shower: "))
   
class Shower:
    water = True

    def __init__(self, mode, temp, color1, music): 
        self._mode = mode
        self.temp = temp
        self.color1 = color1
        self.music = music

    def run(self):
        file.write(f'run on {self._mode} mode')
        if self._mode == 'rain':
            self.color1 = 'blue'
        else:
            self.color1 = 'red'

    @classmethod
    def colorlight(cls, mode, color1):
        return cls(mode, 31, color1, None)


class Boobles(Shower):
    def __init__(self, mode, temp, color, music):
        super().__init__(mode, temp, color, music)
        if mode == 'massage':
            self.boobles = True
        else:
            self.boobles = False

    def __str__(self):
        return f"boobles are on {self.temp} degrees"


class full_bath(Shower,Boobles):
    def __init__(self,mode,color,temp):
        Shower.__init__(self,mode,temp,color,music)
        Boobles.__init__(self,mode,temp,color,music)


    file.write("full bath\n")

full_bath1 = full_bath("massage",31,"jazz")
boobles1 = Boobles('massage', 31, 'blue', 'pop')
shower2 = Shower('massage', 31, 'blue', 'rock')

class music_playlist(list):
    def __init__(self, name):
        self.name = name

    def __getitem__(self, index):
        return self.name[index]



class playlist2(list):
  def __len__(self):
    return 10
m_playlist=playlist();
file.write(len(m_playlist))
m_playlist.append('blues')

my_list = music_playlist(["classic jazz", "pop", "latino"])

for music in my_list:
    file.write(music)

for char in [shower2, boobles1]:
    char.run()

mode = input("Enter shower mode: ")
while mode != 'rain' and mode != 'massage':
    mode = input("Enter shower mode: ")
file.write('starting shower')
shower1 = Shower(mode, 31, 'blue', 'pop')
shower1.run()
shower1.colorlight('rain', 'blue').run()
boobles1 = Boobles('rain', 31, 'red', 'rock')
file.write(boobles1.colorlight('rain', 'red').run())
file.write(isinstance(boobles1, Boobles))
temperature()



#setting shower temperature



#MRO resolution order
class sh1: pass
class sh2: pass
class sh3: pass
class sh4(sh1,sh3): pass
class sh5(sh2,sh1): pass
class sh6(sh5,sh4,sh3): pass
