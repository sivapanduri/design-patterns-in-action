class Button: pass
class WindowsButton(Button):
    def click(self): print("Windows Button clicked")
class MacButton(Button):
    def click(self): print("Mac Button clicked")

class UIFactory:
    def create_button(self): pass

class WindowsUIFactory(UIFactory):
    def create_button(self): return WindowsButton()

class MacUIFactory(UIFactory):
    def create_button(self): return MacButton()

if __name__ == "__main__":
    factory = MacUIFactory()
    button = factory.create_button()
    button.click()
