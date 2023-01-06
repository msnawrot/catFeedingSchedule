# I want a schedule for feeding my cats 10 small meals a day.
# take in two datetimes, wakeUpTime and bedTime, and an integer
# mealsPerDay.  Output datetimes for each feeding.

from datetime import datetime, timedelta
from typing import List

def mealScheduler(wakeUpTime: datetime, bedTime: datetime, mealsPerDay: int) -> List[datetime]:
    dayTime = bedTime - wakeUpTime
    print("Daytime is", dayTime.seconds//3600, "hours", (dayTime.seconds//60)%60, "minutes")
    timeBetweenMeals = dayTime / mealsPerDay
    print(f"Time between {mealsPerDay} meals is", timeBetweenMeals.seconds//3600, "hour(s)", (dayTime.seconds//60)%60, "minute(s)")

    mealSchedule = []
    for i in range(mealsPerDay):
        mealSchedule.append(wakeUpTime + timeBetweenMeals * i)

    return mealSchedule



def mealScheduleTest():
    ini_time_for_now = datetime.now()
    print("initial_date", str(ini_time_for_now))
    new_final_time = ini_time_for_now + timedelta(days = 2)
    print("new_final_time", str(new_final_time))
    print('Time difference:', str(new_final_time - ini_time_for_now))

wakeUpTime = datetime(2022, 12, 25, 7, 30)
bedTime = datetime(2022, 12, 25, 23, 00)

mealSchedule = mealScheduler(wakeUpTime, bedTime, 8)
for i, mealTime in enumerate(mealSchedule):
    print(f"Meal {i+1} : {mealTime.strftime('%I:%M %p')}" )
