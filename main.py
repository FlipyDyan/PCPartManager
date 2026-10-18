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
    speak("Add a Part")
    print("\nAdd a PC Part")

    category = input(
        "Enter PC part category (Power Supply, GPU, Motherboard, CPU, Ram): "
    ).strip()

    while category == "":
        print("Category cannot be blank.")
        category = input("Enter PC part category: ").strip()
    match category.lower():
        case "cpu":
            example = "AMD Ryzen 5 7500F"
        case "gpu":
            example = "NVIDIA GeForce RTX 4060"
        case "motherboard":
            example = "Gigabyte B650 AORUS Elite AX"
        case "power supply" | "powersupply" | "psu":
            example = "Corsair RM750e"
        case "ram":
            example = "Corsair Vengeance 32GB DDR5"
        case "storage" | "ssd" | "hdd":
            example = "Samsung 990 PRO 1TB"
        case _:
            example = "brand and model"

    name = input(
        f"Enter component name (e.g., {example}): "
    ).strip()

    while name == "":
        print("Component name cannot be blank.")
        name = input("Enter component name: ").strip()

    with open("partDatabase.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, name])

    print(f"\nAdded: {category} - {name}\n")
    speak(f"{name} has been added.")

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