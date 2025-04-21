import os
import time
import getpass  # For secure input without echoing in terminal
import sqlite3  # For SQLite database operations

# --------------------- Database Initialization ---------------------

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("youtube.db")
cur = conn.cursor()

# Create a table for storing video details if it doesn't exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        video_id INTEGER PRIMARY KEY,
        video_title TEXT NOT NULL,
        video_duration INT NOT NULL        
    );
''')

# --------------------- Global Configurations ---------------------

sleep_time = 2         # UI delay (in seconds) for better user experience
sub_sign_count = 50    # UI separator length for cleaner console display

# --------------------- Video Listing ---------------------

# Display all stored videos in a tabular format
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

# Check if a video with the same title (case-insensitive) already exists
def video_already_present(video_name):
    data = cur.execute("SELECT * FROM VIDEOS")
    for vid in data:
        if vid[1].upper() == video_name.upper():
            return True
    return False

# --------------------- Core Functionalities ---------------------

# Add a new video entry if it doesn't already exist
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

    # Insert the new video into the database
    cur.execute("INSERT INTO videos(video_title,video_duration) VALUES (?,?)", (video_name, video_duration))
    conn.commit()
    
    print("Video Added Successfully...")
    print("-" * sub_sign_count)

# Update an existing video’s title and duration by its ID
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
        
        # Update the selected video in the database
        cur.execute("UPDATE videos SET video_title=?, video_duration=? WHERE video_id=?", (video_name, video_duration, video_index))
        conn.commit()

        print("-" * sub_sign_count)
        print("Video Updated Successfully...")
        print("-" * sub_sign_count)
    else:
        print("-" * sub_sign_count)
        print("ID Not Found!!!\nFailed to Update Video!!!")
        print("-" * sub_sign_count)

# Delete a video by its ID
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
        # Delete the video from the database
        cur.execute("DELETE FROM videos WHERE video_id=?", (video_index,))
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
        time.sleep(sleep_time)        # Add delay for smoother transitions
        os.system('cls')              # Clear terminal screen (Windows only)

        # Display main menu
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

        # Match user option to corresponding function
        match option:
            case '1':
                time.sleep(sleep_time)
                os.system('cls')
                list_all_Videos()
                print("\n" + "-" * sub_sign_count)
                getpass.getpass("Press Enter Key to Continue ")  # Wait for user input
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
    
    # Close DB connection on exit
    conn.close()

# Run the main function only if the script is executed directly
if __name__ == "__main__":
    main()
