class Button:
    dark_mode = False

    def __init__(self, imprint, spaces):
        self.imprint = imprint
        self.spaces = spaces

    @classmethod
    def toggle_dark_mode(cls):
        cls.dark_mode = not cls.dark_mode


buttons = [
    Button("0", 2),
    Button("1", 1),
    Button("=", 3)
]

mode_before = Button.dark_mode

Button.toggle_dark_mode()

mode_after = Button.dark_mode

pass