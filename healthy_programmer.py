from pygame import mixer
import datetime
from time import time
def gettime():
    return datetime.datetime.now()
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if(a==stopper):
            mixer.music.stop()
            break
def log(mssg):
    with open("logs.txt","a") as f:
        f.write(f"{mssg} {gettime()}\n")
if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water_sec=5
    eyes_sec=10
    exercise_sec=20
    while True:
        if time()-init_water>water_sec:
            print("Drink water...Print 'drank' to stop.")
            musiconloop("pani.mp3","drank")
            init_water=time()
            log("Drank water at ")
        if time()-init_eyes>eyes_sec:
            print("Start doing eyes exercise...Print 'Done' to stop.")
            musiconloop("aakh.mp3","Done")
            init_eyesdr=time()
            log("Done eyes exercise  at ")
        if time()-init_exercise>exercise_sec:
            print("Start doing workout...Print 'Done' to stop.")
            musiconloop("wk.mp3","Done")
            init_exercise=time()
            log("Done workout at ")
