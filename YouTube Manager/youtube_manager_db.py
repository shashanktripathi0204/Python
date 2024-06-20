import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
""")


def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("No data in table")
    else:
        for row in rows:
            print(row)
    print("\n")


def add_video(name, time):
    cursor.execute("INSERT INTO VIDEOS (name, time) VALUES (?, ?)", (name, time))
    conn.commit()


def update_video(video_id, new_name, new_time):
    print("\n")
    cursor.execute("UPDATE VIDEOS SET NAME = ?, TIME = ?"
                   "WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()


def delete_video(video_id):
    print("\n")
    print("Select Video from the list")
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    conn.commit()


def main():
    while True:
        print("\nYouTube Manager | Choose an option")
        print("1. List video")
        print("2. Add video")
        print("3. Update video detail")
        print("4. Delete video")
        print("5. Exit the app\n")
        choice = input("Enter the choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            print("\nFrom the video list:-")
            list_videos()
            video_id = input("Enter video id to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            print("\nFrom the video list:-")
            list_videos()
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")
    conn.close()


if __name__ == "__main__":
    main()
