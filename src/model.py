from src.controller import Controller, TerminalController, Inputs
from src.view import View, TerminalView

class Model():
    def __init__(self, ct: Controller, vw: View) -> None:
        """
        Keeps track of the program state.
        Handles interactions between controller and view.

        Params:
            ct: Controller
            vw: View
        """
        self.running = False
        self.ct = ct
        self.vw = vw

    def handle_inputs(self, inputs: Inputs) -> None:
        if inputs.quit:
            self.running = False
        if inputs.help:
            self.vw.show_help()
        if inputs.pl:
            print(f"TODO: add '{inputs.pl}' to Proficient Languages")
        if inputs.fl:
            print(f"TODO: add '{inputs.fl}' to Familiar Languages")
        if inputs.tech:
            print(f"TODO: add '{inputs.tech}' to Technologies")
        if inputs.project:
            print(f"TODO: add '{inputs.project}' to Projects")
        if inputs.experience:
            print(f"TODO: add '{inputs.experience}' to Work Experience")
        if inputs.education:
            print(f"TODO: add '{inputs.education}' to Education")

    def run(self) -> None:
        """
        Runs the main while loop of the program.
        """
        self.running = True
        while self.running:
            self.handle_inputs(self.ct.update())
            self.vw.update()

class TerminalModel(Model):
    def __init__(self, ct: TerminalController, vw: TerminalView) -> None:
        Model.__init__(self, ct, vw)
    