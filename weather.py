import random

day = 0
chars = "☀️","⛅","🌦️","🌩️","🌧️","☁️"

while True:
   day += 1
   print(f"Day {day}: " + random.choice(chars))
   