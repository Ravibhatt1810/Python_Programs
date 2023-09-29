import pygame

# Initialize pygame
pygame.mixer.init()

# Create a playlist of songs
playlist = [
    "song1.mp3",
    "song2.mp3",
    "song3.mp3",
]

# Function to play a song
def play_song(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

# Main loop
while True:
    print("Music Player Menu:")
    print("1. Play Song")
    print("2. Pause")
    print("3. Resume")
    print("4. Stop")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        song_choice = int(input("Enter the song number (1, 2, 3): "))
        if 1 <= song_choice <= len(playlist):
            play_song(playlist[song_choice - 1])
        else:
            print("Invalid song number.")
    elif choice == "2":
        pygame.mixer.music.pause()
    elif choice == "3":
        pygame.mixer.music.unpause()
    elif choice == "4":
        pygame.mixer.music.stop()
    elif choice == "5":
        pygame.mixer.quit()
        break
    else:
        print("Invalid choice. Please select a valid option.")
