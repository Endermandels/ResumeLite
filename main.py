from src.view       import TerminalView
from src.model      import TerminalModel
from src.controller import TerminalController

def main():
    vw = TerminalView()
    ct = TerminalController()
    model = TerminalModel(ct, vw)
    model.run()

if __name__ == '__main__':
    main()