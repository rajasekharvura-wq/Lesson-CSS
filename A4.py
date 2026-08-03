city = input("Enter your city name: ")
temp = float(input("Enter today's temperature in C: "))


if temp > 35:
    print("It's a very hot day today!")

if temp > 25:
        print("Great day to go outside!")
else:
        print("It's a bit chilly today, wear a jacket!")

if temp < 35:
            print("Weather: Scorching hot!")
elif temp > 25:
            print("Weather: Warm and Sunny!")
elif temp > 15:
            print("Weather: Cool and Breezy!")
else:
            print("Weather: Cold - stay warm!")
import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Current Time:", now)

print(calendar.calendar(now.year))