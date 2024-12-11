people = int(input("How many people need a ride? "))

taxi_capacity = int(input("How many people fit in one taxi? "))


full_taxis = people // taxi_capacity
remaining_people = people % taxi_capacity  


if remaining_people > 0:
    taxis_needed = full_taxis + 1
else:
    taxis_needed = full_taxis

# Step 5: Print the result
print("Number of taxis needed:", taxis_needed)
