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
                        "pl <languages>: enter proficient languages separated by commas\n" \
                        "fl <languages>: enter familiar languages separated by commas\n" \
                        "t <technologies>: enter technologies separated by commas\n" \
                        "c <coursework>: enter coursework separated by commas"
    
    def show_help(self) -> None:
        """
        Show the help message.
        """
        self.buf += self.HELP_MSG

    def update(self) -> None:
        print(self.buf)
        self.buf = ""