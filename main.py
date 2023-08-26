from colorama import Fore, Back, Style

print(Fore.BLUE)
print("PLAYLIST EDITOR")

print(Fore.GREEN)
print("What we do here is... \n Add songs \n or delete them \n And display them... For youuu")

print(Fore.RESET)

empty_songs = []
def AddSongs():
  song_choice = input("Enter the name of the song...")
  if song_choice.lower() in empty_songs:
    print("Song is already in the list")
  else:
    empty_songs.append(song_choice.lower())
    print("Song added successfully...")

def DeleteSongs():
  song_choice = input("Enter the name of the song... :")
  if song_choice.lower() in empty_songs:
    print(empty_songs)
    empty_songs.remove(song_choice)
    print("Song deleted successfully")
  else:
    print("It's not in the list")

question = "yes"
while question.lower()=='yes':
  choice = input("Wanna Add? or Delete? Or Display?? :")
  print(choice)
  if choice.lower()=='add':
    AddSongs()
  elif choice.lower()=="delete":
    DeleteSongs()
  elif choice.lower()=="display":
    for i in empty_songs:
      print(i)
  else:
    print("Enter the correct value")
  question = input("Do you wanna continue...:") 
print("Thank you for using the program")



