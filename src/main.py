import argparse
# from pathlib import Path
import getApps
import os
import openApps
import questionary as quest
from rich.table import Table
from rich.console import Console
from rich import print as richPrint

# handling paths ?
SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__)) #returns script path
SAVES_DIRECTORY = os.path.join(SCRIPT_DIRECTORY, "saves") #append saves folder to the path

#if folder does not exist, create it
if not os.path.exists(SAVES_DIRECTORY):
    os.makedirs(SAVES_DIRECTORY)


def printWorkspace(workspace_name):
    console = Console()
    table = Table(title="Apps Saved currently")

    table.add_column("S. No.", style="magenta", justify="center")
    table.add_column("Application Name", justify="left", style="cyan", no_wrap=True)


    for idx,n in enumerate(getApps.getNamesFromFile(os.path.join(SAVES_DIRECTORY, f"{workspace_name}.txt")),1):
        table.add_row(str(idx),n)
    console.print(table)


def saveWorkspace(app_names, app_paths):
    workspaceName = input("Enter Name of workspace").strip()

    filepath = os.path.join(SAVES_DIRECTORY, f"{workspaceName}.txt")

    with open(filepath, "w") as file:
        for name, path in zip(app_names, app_paths):
            file.write(f"{name} : {path}\n")

def getAllWorkspaces():
    """Returns list of names of all saved workspaces"""

    files = os.listdir(SAVES_DIRECTORY)

    workspaces = []
    for f in files:
        if f.endswith(".txt"):
            workspaces.append(f.replace(".txt", ""))
    return workspaces

def editSavedWorkspace(workspace_name):
    """Makes changes in currently saved workspace

        Returns: 'x' >= 0, if 'x' changes made

        Returns: -1 if error
    """

    filepath = os.path.join(SAVES_DIRECTORY, f"{workspace_name}.txt")

    lines = None

    with open(filepath,"r") as f:
        lines = f.readlines()

    unstage = input("Enter S. No(s). of App to unstage(comma separated) : ").strip()

    #if no input, leave
    if not unstage:
        print("No changes")
        return 0

    try:
        toRemove = []
        for num in unstage.split(","):
            toRemove.append(int(num.strip()))
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        return -1
    
    keepLines = []
    for idx,line in enumerate(lines, 1):
        if idx not in toRemove:
            keepLines.append(line)
    
    #rewrite file
    with open(filepath, "w") as f:
        f.writelines(keepLines)

    print(f"{len(toRemove)} changes made ✅")
    return len(toRemove)

def checkSavedWorkspace():
    """Returns 1 : File found and opened
       Returns 0 : File found but not opened
       Returns -1 : File not found
    """

    choices = ["Launch Workspace 🚀",
                "See 👁️ or edit saved workspace(s) ✏️",
                "Eat 5-⭐ Do Nothing."]
    
    option = quest.select(message="",choices=choices).ask()

    savedWorkpaces = getAllWorkspaces()
    print(savedWorkpaces)
    if option == choices[0]:
        if(len(savedWorkpaces) > 0):
            # print("previous saved workspace exists. Do you wish to..\n")

            ch = quest.select(
                message="Select the workspace you wish to launch..\n",
                choices=savedWorkpaces
            ).ask()

            pathsFromWorkspace = getApps.getPathsFromFile(os.path.join(SAVES_DIRECTORY,f"{ch}.txt"))
            for path in pathsFromWorkspace:
                openApps.openApp(path)
        else:
            print("No previous workspace exists 🥺, create one!")

    elif option == choices[1]:
        if(len(savedWorkpaces)>0):
            ch = quest.select(
                message="Select the workspace you wish to edit..\n",
                choices=savedWorkpaces
            ).ask()

            printWorkspace(ch)

            editSavedWorkspace(ch)
    else:
        print("LOL 🍫")
         


        


parser = argparse.ArgumentParser()

# parser.add_argument("path")
parser.add_argument("name")

args = parser.parse_args()

# print(args)

print(f"Welcome! {args.name}")
# richPrint("[bold italic yellow on red blink]This text is impossible to read")

while True:
    
    #get current apps
    names, paths = getApps.getRunningApps()


    initialChoices = ["Save Current Workspace 🔥",
                      "Launch 🚀 or Check Saved Workspace(s) 🔍",
                      "Exit 👋"]

    initchoice = quest.select(message="", choices=initialChoices).ask()

    if initchoice == initialChoices[0]:
        print("Apps currently opened :- ")
        for n in names:
            print(f"    --> {n}")

        choice = quest.confirm(message="Save these apps into workspace?", default=True).ask()
        # print(choice)
        if choice:
            saveWorkspace(names, paths)
            print(f"    --> ✅ saved")
        else:
            print(f"    --> ❌ not saved")

    elif initchoice == initialChoices[1]:
        checkSavedWorkspace()
      
    else:
        break
    
