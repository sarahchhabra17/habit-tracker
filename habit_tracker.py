import json
import datetime

DATA_FILE = "data.json"

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_habit(data, name):
    for h in data["habits"]:
        if h["name"] == name:
            print(f"'{name}' already exists!")
            return
    habit = {
        "name": name,
        "created": str(datetime.date.today()),
        "streak": 0,
        "last_done": None
    }
    data["habits"].append(habit)
    save_data(data)
    print(f"✅ Habit '{name}' added!")

def mark_done(data, name):
    today = str(datetime.date.today())
    for h in data["habits"]:
        if h["name"] == name:
            if h["last_done"] == today:
                print(f"Already marked '{name}' as done today!")
                return
            h["last_done"] = today
            h["streak"] += 1
            save_data(data)
            print(f"🔥 '{name}' done! Streak: {h['streak']} days")
            return
    print(f"Habit '{name}' not found.")

def view_habits(data):
    if not data["habits"]:
        print("No habits yet. Add one!")
        return
    print("\n--- Your Habits ---")
    for h in data["habits"]:
        done_today = h["last_done"] == str(datetime.date.today())
        status = "✅" if done_today else "❌"
        print(f"{status} {h['name']} | Streak: {h['streak']} days")
    print("-------------------\n")

def main():
    data = load_data()
    while True:
        print("\nWhat do you want to do?")
        print("1. View habits")
        print("2. Add a habit")
        print("3. Mark a habit as done")
        print("4. Quit")
        choice = input("Enter 1-4: ")

        if choice == "1":
            view_habits(data)
        elif choice == "2":
            name = input("Habit name: ")
            add_habit(data, name)
        elif choice == "3":
            name = input("Which habit did you complete? ")
            mark_done(data, name)
        elif choice == "4":
            print("See you tomorrow 👋")
            break
        else:
            print("Invalid choice, try again.")

main()