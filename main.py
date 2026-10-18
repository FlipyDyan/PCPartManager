# A PC part manager.
import pyttsx3
import csv

engine = pyttsx3.init()

def speak(words):
    # Use this to add speech to your methods
    engine.say(words)
    engine.runAndWait()

def removeParts():
    #Most likely needs an index
    speak("Remove a Part")
    print("Remove") #add some code here remove what you want
    return main()

def addParts():
    # Most likely needs cost,name,ram_storage,quantity
    speak("Add a Part")
    print("Add") #add some code here remove what you want
    return main()

def listParts():
    # Needs CSV
    speak("Listing all Parts")
    print("List")  #add some code here remove what you want
    return main()

def updatePartListing():
    # Most likely needs cost,name,ram_storage,quantity
    speak("Update your Parts")
    print("Update") #add some code here remove what you want
    return main()

def listCommands():
    print(f"list - List Parts\n"
          f"update - Update Parts\n"
          f"add - Add Parts\n"
          f"remove - Remove Parts\n")

def main():
    print(f"PC Part Manager:\n")
    listCommands()
    speak("PC Part Manager")

    entry = input("Enter in a command: ")
    match entry.lower():
        #Added shortened alternatives for faster testing.
        case "add" | "a":
            addParts()

        case "list" | "l":
            listParts()

        case "update" | "u":
            updatePartListing()

        case "remove" | "r":
            removeParts()

        case _:
            # Made error red showing in terminal
            print(f"Invalid command: \033[31m{entry}\033[0m:\n"
                  f"Try Again\n\n\n")
            speak(f"{entry} is an invalid command. Try Again ")
            return main()


if __name__ == '__main__':
    main()