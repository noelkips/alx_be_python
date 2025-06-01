# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case for priority handling
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unknown priority"

# Check if time-sensitive
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if "Reminder" in message:
        message += ". Try to complete it soon."
    else:
        message += ". Consider completing it when you have free time."

# Output the final message
print("\n" + message)
