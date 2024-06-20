import json


def load_data():
    """
    Goes inside the file and loads the data from there
    if no data is found it returns empty list

    :return:
    """
    try:
        with open('youtube.txt', 'r') as file:
            # fetches all the data that is in the file and returns it in json formate
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    """
    will be called when ever we have to store the video
    :param videos: list of videos
    :return: None
    """
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video["name"]},"
              f"Duration: {video['time']}")
    print("\n")
    print("*" * 70)


def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be updated: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)

    else:
        print("Invalid video index selected")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))

    if 1 <= index <= len(videos):
        print(f"Selected Video for delete is:- {videos[index - 1]}")
        value = int(input("To continue delete press 1, to abort press 0: "))
        if value == 1:
            del videos[index - 1]
            save_data_helper(videos)
            print("Video deletion successful")
        else:
            print("Video not deleted")
            pass
    else:
        print("Invalid video index selected")


def main():
    videos = load_data()
    while True:
        print("\n YouTube Manager | Choose an option")
        print("1. List all the youtube video")
        print("2. Add a youtube video")
        print("3. Update a youtube video detail")
        print("4. Delete a youtube video detail")
        print("5. Exit the app")

        choice = input("Enter the choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Input")


if __name__ == "__main__":
    main()
