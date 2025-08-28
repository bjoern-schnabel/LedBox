from ulib import graphics_library as gl
from ulib import input_library as il
import time
import numpy as np

# Game over screen as a compact string representation
GAME_OVER_PATTERN = [
    "0000000000000000",
    "00RRRRR00RRRRR00", 
    "00R000R00R000R00",
    "00R0RRR00RRRRR00",
    "0000000000000000",
    "00RRRRR00RRRR000",
    "00R00R000000R000",
    "00RRRRR00RRRR000",
    "0000000000000000",
    "00RRRRR00RRRRR00",
    "000RR0000R0R0R00",
    "00RRRRR00000000",
    "0000000000000000",
    "00RRRRR00RRR000",
    "00R0R0R00R0R000",
    "0000000000000000",
]

def create_game_over_screen():
    """Create game over screen from pattern."""
    screen = np.full((16, 16, 3), gl.colors["background"])
    for x, row in enumerate(GAME_OVER_PATTERN):
        for y, char in enumerate(row):
            if char == 'R':
                screen[x, y] = gl.colors["red"]
            elif char == 'G':
                screen[x, y] = (4, 4, 4)  # Gray pixels
    return screen

game_over_screen = create_game_over_screen()


class Game:
    def __init__(self):
        self.running = True
        self.is_game_over = False
        self.score = 0
        self.spt = 0.1  # seconds per tick
        self.tick = 0  # Game tick counter

    def initialise(self):
        """Initialize the game."""
        gl.clear()
        il.initialise()
        self.running = True
        self.is_game_over = False
        self.score = 0

    def play(self):
        """Start the game loop."""
        while self.running:
            if il.inputs["exit"]:
                self.stop()
            if il.inputs["escape"]:
                self.stop()
            if il.inputs["space"] or il.inputs["enter"]:
                if self.is_game_over:
                    self.initialise()
                    self.is_game_over = False
            if not self.is_game_over:
                self.update()
                self.render()
            il.reset_inputs()
            time.sleep(self.spt)
            self.tick += 1

    def set_difficulty(self, difficulty, default_mult):     # difficulty important for overloading
        # Geschwindigkeit setzen
        self.spt *= default_mult
        

    def update(self):
        """Update game state."""
        raise NotImplementedError("Update method must be implemented by subclasses.")

    def render(self):
        """Render the game state."""
        raise NotImplementedError("Render method must be implemented by subclasses.")

    def game_over(self):
        """Handle game over state."""
        self.is_game_over = True
        print(f"Game Over! Your score: {self.score}")
        time.sleep(1)
        for x in range(16):
            for y in range(16):
                gl.set_pixel(x, y, game_over_screen[x, y])
        gl.show()

    def stop(self):
        """Stop the game."""
        self.running = False
