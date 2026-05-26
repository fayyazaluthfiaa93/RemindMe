import mysql.connector
from tabulate import tabulate

# Database Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="remindme"
)
cursor = db.cursor()

def generate_auto_tags(text):
    """Automatically generates tags based on keywords found in the input text."""
    keywords = {
        "#coding": ["python", "script", "code", "logic", "mysql"],
        "#materi": ["kuliah", "modul", "bab", "belajar", "dosen", "materi"],
        "#task": ["tugas", "proyek", "deadline", "due", "kerjakan", "latihan", "kumpul"],
        "#reminder": ["jangan lupa", "ingat", "besok", "jadwal", "kuis"],
        "#notes": ["catatan", "ide", "tanya"]
    }

    found_tags = []
    text = text.lower()
    
    for tag, words in keywords.items():
        for word in words:
            if word in text:
                found_tags.append(tag)
                break  

    return found_tags


while True:
    print("\n=== REMIND ME MENU ===")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Update Task")
    print("4. Show Tasks")
    print("5. Exit")

    choice = input("Select an option: ")

   
    if choice == "1":
        user_input = input("What's on your mind?: ")
        detected_tags = generate_auto_tags(user_input)
        tags_string = ", ".join(detected_tags)  

        sql = "INSERT INTO metadata_assets(title, tags) VALUES (%s, %s)"
        values = (user_input, tags_string)

        try:
            cursor.execute(sql, values)
            db.commit()
            print("Successfully added task!")
        except Exception as e:
            db.rollback()
            print(f"Failed to add task: {e}")

    
    elif choice == "2":
        id_to_delete = input("\nEnter the ID you want to delete: ")
        sql_delete = "DELETE FROM metadata_assets WHERE id = %s"

        try:
            cursor.execute(sql_delete, (id_to_delete,))
            db.commit()
            print("Successfully deleted task!")
        except Exception as e:
            db.rollback()
            print(f"Failed to delete task: {e}")
    
   
    elif choice == "3":
        id_to_update = input("Enter the ID you want to update: ")
        new_title = input("Enter new notes: ")
        updated_tags = generate_auto_tags(new_title)
        tags_string = ", ".join(updated_tags)

        sql_update = "UPDATE metadata_assets SET title = %s, tags = %s WHERE id = %s"
        values = (new_title, tags_string, id_to_update)

        try:
            cursor.execute(sql_update, values)
            db.commit()
            print(f"Task ID {id_to_update} successfully updated!")
        except Exception as e:
            db.rollback()
            print(f"Failed to update task: {e}")
    

    elif choice == "4":
        print("\n--- MY REMINDERS LIST ---")
        sql_view = "SELECT id, title, tags FROM metadata_assets"

        try:
            cursor.execute(sql_view)
            result = cursor.fetchall()

            if not result:
                print("Your reminder list is empty.")
            else:
                headers = ["ID", "Title", "Tags"]
                print(tabulate(result, headers=headers, tablefmt="fancy_grid"))
        except Exception as e:
            print(f"Failed to fetch data: {e}")

    
    elif choice == "5":
        print("Thank you for using RemindMe! Goodbye.")
        break
        
    else:
        print("Invalid option. Please choose between 1-5.")