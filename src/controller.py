from typing import NamedTuple

class Inputs(NamedTuple):
    quit: bool = False          # Quit the program if true
    help: bool = False          # Display help info if true
    pl: list[str] = None        # Proficient languages to enter
    fl: list[str] = None        # Familiar languages to enter
    t: list[str] = None         # Technologies to enter
    c: list[str] = None         # Coursework to enter
    project: dict = None        # Project to enter (name, organizer, points)

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
            t = list(map(str.strip, uin[2:].split(',')))
            return Inputs(t=t)
        if uin.lower().startswith('c '):
            # Coursework
            c = list(map(str.strip, uin[2:].split(',')))
            return Inputs(c=c)
        # if uin.lower().startswith('p|'):
        #     # Project
        #     # TODO: Read files/project.json and add those project settings
        #     return Inputs(project=project)
        print(f"unknown command: {uin}")
        return Inputs(help=True)