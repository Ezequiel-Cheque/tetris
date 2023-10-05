import keyboard

class Screen:
    def __init__(self):
        self.column = 20
        self.row =  15
        self.white = "⬜"
        self.black = "🔳"
        
    def create_screen(self, figure=[]):
        column = self.column
        row = self.row
        screen = []
        for r in range(row):
            m = []
            for c in range(column):
                coordinates = [c,r]
                if coordinates in figure:
                    m.append(self.black)
                else:
                    m.append(self.white)
            screen.append(m)
        return screen
    def print_screen(self, screen):
        for row in screen:
            print("".join(map(str, row)))

class Figure(Screen):
    
    def __init__(self, coordinates):
        super().__init__()
        self.coordinates = coordinates
    def create_figure(self):
        screen = self.create_screen(self.coordinates)
        self.print_screen(screen)
        
## Figures:
line = Figure([[0,0],[0,1],[0,2],[0,3]])
square = Figure([[0,0],[1,0],[0,1],[1,1]])
L = Figure([[0,0],[0,1],[0,2],[1,2]])
rL = Figure([[1,0],[1,1],[1,2],[0,2]])
T = Figure([[0,0],[1,0],[2,0],[1,1]])
Z = Figure([[0,1],[1,1],[1,0],[2,0]])
rZ = Figure([[0,0],[1,1],[1,0],[2,1]])


while(True):
    
    event = keyboard.read_event()
    
    if event.name == "esc":
        print("has salido del juego")
        break
    elif event.event_type == keyboard.KEY_DOWN:
        if event.name == "down":
            print("has bajado")
        elif event.name == "right":
            print("has ido a la derecha")
        elif event.name == "left":
            print("has ido a la izquierda")
        elif event.name == "space":
            print("has rotado")