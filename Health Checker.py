# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:38:06 2024

@author: gabeg
"""

def health_check():
    print("Welcome to the Health Check Program!")
    
    # Input for sleep hours
    sleep_hours_per_day = float(input("How many hours do you sleep per night? "))
    total_sleep_per_week = sleep_hours_per_day * 7

    # Input for water intake
    water_intake_liters = float(input("How many liters of water do you drink per day? "))

    # Input for exercise
    exercise_minutes_per_day = int(input("How many minutes do you exercise per day? "))
    total_exercise_per_week = exercise_minutes_per_day * 7

    # Input for screen time
    screen_time_hours_per_day = float(input("How many hours do you spend on screens (computer, phone, TV) per day? "))

    # General Health Recommendations
    recommended_sleep = 7 * 7  # 7 hours per night
    recommended_water_intake = 2  # Liters per day
    recommended_exercise = 150  # 150 minutes per week
    max_screen_time = 2  # Recommended maximum screen time in hours per day

    # Check against recommendations
    print("\nHealth Assessment Report:")

    # Sleep Assessment
    if total_sleep_per_week == recommended_sleep:
        print("✅ You are meeting the recommended amount of sleep.")
    elif total_sleep_per_week >= recommended_sleep:
            print("✅✅✅ You really like to sleep, what kind of dreams do you have XD")
    else:
        print("⚠️ You may need more sleep. Aim for at least 7 hours per night.")

   
    # Water Intake Assessment
    if water_intake_liters == recommended_water_intake:
        print("✅ Your water intake meets the daily recommendation.")
    elif water_intake_liters >= recommended_water_intake:
         print("✅✅✅ Wow, you are super hydrated, you probably don't get any cramps!")
    else:
        print("⚠️ Consider drinking more water. Aim for at least 2 liters per day.")

   
        
    # Exercise Assessment
    if total_exercise_per_week == recommended_exercise:
        print("✅ Great job on exercise! You're meeting the weekly recommendation.")
    elif total_exercise_per_week >= recommended_exercise:
           print("✅✅✅ Work Hard, Play Hard. The grind never stops. Massive respect!!!")
    else:
        print("⚠️ You may need more exercise. Aim for at least 150 minutes per week.")

    # Screen Time Assessment
    if screen_time_hours_per_day == max_screen_time:
        print("✅ Your screen time is within a healthy range.")
    elif screen_time_hours_per_day == 0:
        print("✅Looks like you wanted to enjoy nature today? ")
    else:
        print("⚠️ Consider reducing screen time. Try to limit it to 2 hours or less per day.")

    # Final message
    print("\nThank you for using the Health Check Program. Remember, these are general recommendations. Always consult a healthcare professional for personalized advice.")

# Run the health check
health_check()
