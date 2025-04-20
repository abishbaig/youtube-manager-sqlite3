import os
import time
import getpass  # Used for secure input, typically hides input text in console
import sqlite3

# DB Intialization
conn = sqlite3.connect("youtube.db")
cur = conn.cursor()

# Creating Table to Store Values
cur.execute('''
            
    CREATE TABLE IF NOT EXISTS videos(
        video_id INTEGER PRIMARY KEY,
        video_title TEXT NOT NULL,
        video_duration INT NOT NULL        
    );
''')


# Global Variables
sleep_time = 2         # Delay (in seconds) used between transitions and interactions
sub_sign_count = 50    # Length for separator lines to improve console UI readability

# --------------------- Video Listing ---------------------

# Displays all videos stored in the db in a clean tabular format
def list_all_Videos():
    print("-" * sub_sign_count)
    print("\tVIDEOS LIST MENU")
    print("-" * sub_sign_count)
    print("ID\tName\t\tDuration(min)")
    print("-" * sub_sign_count)

    data = cur.execute("SELECT * FROM VIDEOS")
    for row in data:
        print(f"{row[0]}\t{row[1]}\t\t{row[2]}")
        
    
    print("-" * sub_sign_count)

# --------------------- Utility Functions ---------------------

# Checks if a video with the same name (case-insensitive) already exists in the database
def video_already_present(video_name):
    data = cur.execute("SELECT * FROM VIDEOS")
    for vid in data:
        if vid[1].upper() == video_name.upper():
            return True
    return False

# --------------------- Core Functionalities ---------------------

# Handles user input for adding a new video and add to database if not already present
def add_video():
    print("-" * sub_sign_count)
    print("\tADD VIDEO MENU")
    print("-" * sub_sign_count)
    
    video_name = input("Enter Video Title: ")
    video_duration = input("Enter Video Duration: ")

    if video_already_present(video_name):
        print("-" * sub_sign_count)
        print("Video with this Name Already Present!!!\nFailed to Add!!!")
        print("-" * sub_sign_count)
        return

    print("-" * sub_sign_count)

    # Add new video as a dictionary
    cur.execute("INSERT INTO videos(video_title,video_duration) VALUES (?,?)",(video_name,video_duration))
    conn.commit()
    
    print("Video Added Successfully...")
    print("-" * sub_sign_count)

# Updates the name and duration of an existing video using its ID
def update_video():
    list_all_Videos()
    print("-" * sub_sign_count)
    print("\tUPDATE VIDEO MENU")
    print("-" * sub_sign_count)

    video_index = int(input("Enter Video ID: "))
    
    isFound = False
    data = cur.execute("SELECT * FROM videos")

    for row in data:
        if row[0] == video_index:
            isFound = True
            break
            
    if isFound:
        print("-" * sub_sign_count)
        video_name = input("Enter Video's New Title: ")
        video_duration = input("Enter Video's New Duration: ")
        if video_already_present(video_name):
            print("-" * sub_sign_count)
            print("Video with this Name Already Present!!!\nFailed to Add!!!")
            print("-" * sub_sign_count)
            return
        # Update the corresponding video entry
        cur.execute("UPDATE videos SET video_title=?, video_duration=? WHERE video_id=?",(video_name,video_duration,video_index))
        conn.commit()

        print("-" * sub_sign_count)
        print("Video Updated Successfully...")
        print("-" * sub_sign_count)
    else:
        print("-" * sub_sign_count)
        print("ID Not Found!!!\nFailed to Update Video!!!")
        print("-" * sub_sign_count)
       

# Removes a video from the db
def delete_video():
    list_all_Videos()
    print("-" * sub_sign_count)
    print("\tDELETE VIDEO MENU")
    print("-" * sub_sign_count)

    video_index = int(input("Enter Video ID: "))
    
    isFound = False
    data = cur.execute("SELECT * FROM videos")

    for row in data:
        if row[0] == video_index:
            isFound = True
            break
            
    if isFound:
        print("-" * sub_sign_count)
        cur.execute("DELETE FROM videos WHERE video_id=?",(video_index,))
        conn.commit()

        print("-" * sub_sign_count)
        print("Video Deleted Successfully...")
        print("-" * sub_sign_count)
    else:
        print("-" * sub_sign_count)
        print("ID Not Found!!!\nFailed to Delete Video!!!")
        print("-" * sub_sign_count)
# --------------------- Application Entry Point ---------------------

def main():
    option = '0'

    while option != '5':
        time.sleep(sleep_time)        # Simulates a pause before displaying UI
        os.system('cls')              # Clears the terminal screen (works for Windows)

        print("-" * sub_sign_count)
        print("\tYoutube Videos Manager (SQLite3)")
        print("-" * sub_sign_count)
        print("[1] List All Videos")
        print("[2] Add a Video")
        print("[3] Update a Video")
        print("[4] Delete a Video")
        print("[5] Exit")
        print("-" * sub_sign_count)

        option = input("Enter Option: ")
        print("-" * sub_sign_count)

        match option:
            case '1':
                time.sleep(sleep_time)
                os.system('cls')
                list_all_Videos()
                print("\n" + "-" * sub_sign_count)
                getpass.getpass("Press Enter Key to Continue ")  # Waits for user input securely
            case '2':
                time.sleep(sleep_time)
                os.system('cls')
                add_video()
            case '3':
                time.sleep(sleep_time)
                os.system('cls')
                update_video()
            case '4':
                time.sleep(sleep_time)
                os.system('cls')
                delete_video()
            case '5':
                print("-" * sub_sign_count)
                print("\tApp Exiting...")
                print("-" * sub_sign_count)
                break
            case _:
                print("Wrong Option Entered!!!")
                time.sleep(sleep_time)
                os.system('cls')
    
    conn.close()

# Ensures this script only runs when directly executed (not when imported as a module)
if __name__ == "__main__":
    main()