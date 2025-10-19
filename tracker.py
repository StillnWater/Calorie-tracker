# Meal Calorie Tracker:This program tracks meals and their calorie counts.
#Name- Manas Bhasker , Date- 11/10/2025
print("Welcome to the Meal Calorie Tracker!")
print("You can log your meals and their calorie counts here.")
print("Let's get started!")


meal=[]
calories=[]

num_meals=int(input("Enter number of meals you Had: "))
for i in range(num_meals):
    meal_name=input("Enter the name of the meal: ")
    meal.append(meal_name)
    calorie_count=int(input(f"Enter the calories for {meal_name}: "))
    calories.append(calorie_count)

total_calories=sum(calories)
print("\nMeal Name","\t", " Calories")
underline="-"*30
print(underline)
for i in range(num_meals):
    print(f"\n{meal[i]}: \t {calories[i]} calories")
print(f"\nTotal Calories Consumed: {total_calories} calories")
avg_calories=total_calories/num_meals
print(f"Average Calories per Meal: {avg_calories:.2f} calories")
high_calorie_meals=[meal[i] for i in range(num_meals) if calories[i]>500]
if high_calorie_meals:
    print("\nMeals with more than 500 calories:")
    for meal_name in high_calorie_meals:
        print(meal_name)

