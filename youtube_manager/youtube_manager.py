import json


def load_data(): 
    try : 
        with open('youtube.txt', 'r') as file : 
            test = json.load(file)
            return test
    except FileNotFoundError : 
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file :
        json.dump(videos, file)


def main():
    videos = load_data()
    while True: 
        print("\n Youtube Manager | Choose an option ")
        print("1. List all Youtube Videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

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
                print("Invalid Choice")

if __name__ == "__main__" :
    main()