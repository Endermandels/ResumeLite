class View():
    def __init__(self) -> None:
        """
        Handles displaying information to the user.
        """
        pass

    def update(self) -> None:
        """
        Step through the next update cycle.
        """
        pass

class TerminalView(View):
    def __init__(self) -> None:
        super().__init__()
        self.buf = ''
        self.HELP_MSG = "--- Commands ---\n" \
                        "q: quit\n" \
                        "h: help\n" \
                        "s <skill>: enter skill"
    
    def show_help(self) -> None:
        """
        Show the help message.
        """
        self.buf += self.HELP_MSG

    def update(self) -> None:
        print(self.buf)
        self.buf = ""