class KeyboardHandler:
    def __init__(self):
        self.pressed = []

    def get_key_pressed(self, key):
        return self.pressed[key]

    def key_pressed(self, key):
        self.pressed.append(key)

    def key_released(self, key):
        self.pressed.remove(key)
