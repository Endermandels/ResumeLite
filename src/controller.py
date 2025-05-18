from typing import NamedTuple

class Inputs(NamedTuple):
    quit: bool = False      # Quit the program if true
    help: bool = False      # Display help info if true
    skill: str = ''         # Skill to enter
    project: dict = None    # Project to enter (name, organizer, points)

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
        if uin.lower().startswith('s|'):
            # Skill
            return Inputs(skill=uin[2:].strip())
        if uin.lower().startswith('p|'):
            # Project
            details = uin.split('|')[1:]
            if len(details) < 3:
                print('Need name, project organizer, and descriptive points, split by \'|\'') 
                return Inputs()
            project = {
                'name': details[0],
                'organizer': details[1],
                'points': details[2:]
            }
            return Inputs(project=project)
        print(f"unknown command: {uin}")
        return Inputs(help=True)