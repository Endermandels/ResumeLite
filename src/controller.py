from typing import NamedTuple
import json

class Inputs(NamedTuple):
    quit: bool = False          # Quit the program if true
    help: bool = False          # Display help info if true
    pl: list[str] = None        # Proficient languages to enter
    fl: list[str] = None        # Familiar languages to enter
    tech: list[str] = None      # Technologies to enter
    course: list[str] = None    # Coursework to enter
    project: dict = None        # Project to enter
    experience: dict = None     # Experience to enter

class Controller():
    def __init__(self) -> None:
        """
        Prompts user for inputs.
        Molds inputs and return them to model.
        """
        pass

    def update(self) -> Inputs:
        """
        Steps through the next update cycle.

        Returns:
            User inputs
        """
        pass

class TerminalController(Controller):
    def __init__(self) -> None:
        super().__init__()

    def update(self) -> Inputs:
        uin = input('>> ').strip()
        if uin.lower() == 'h' or uin.lower() == 'help':
            # Help
            return Inputs(help=True)
        if uin.lower() == 'q' or uin.lower() == 'quit':
            # Quit
            return Inputs(quit=True)
        if uin.lower() == 'p' or uin.lower() == 'project':
            # Project
            with open('files/project.json', "r") as file:
                project = json.load(file)
            return Inputs(project=project)
        if uin.lower() == 'e' or uin.lower() == 'experience':
            # Experience
            with open('files/experience.json', "r") as file:
                experience = json.load(file)
            return Inputs(experience=experience)
        if uin.lower().startswith('pl '):
            # Proficient Languages
            pl = list(map(str.strip, uin[2:].split(',')))
            return Inputs(pl=pl)
        if uin.lower().startswith('fl '):
            # Familiar Languages
            fl = list(map(str.strip, uin[2:].split(',')))
            return Inputs(fl=fl)
        if uin.lower().startswith('t '):
            # Technologies
            tech = list(map(str.strip, uin[2:].split(',')))
            return Inputs(tech=tech)
        if uin.lower().startswith('c '):
            # Coursework
            course = list(map(str.strip, uin[2:].split(',')))
            return Inputs(course=course)
        print(f"unknown command: {uin}")
        return Inputs(help=True)