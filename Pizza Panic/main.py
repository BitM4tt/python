#Pizza Panic
import games, __init__, color
score=0
games.init(screen_width=800, screen_height=600, fps=100)
chefimage=games.load_image("Chef.gif")
bowlimage=games.load_image("Bowl.gif")
pizzaimage=games.load_image("Pizza.gif")
wallimage=games.load_image("wall.gif")
games.screen.background=wallimage
class Chef(games.Sprite):
    def update(self):
        if self.right>800 or self.left<0:
            self.dx = -self.dx
class Pizza(games.Sprite):
    def update(self):
        image=games.load_image("Pizza.gif")
        if self.bottom>games.screen.height:
            gameovermessage=games.Message(value="GAME OVER", size=50, color=color.red, x=games.screen.width/2, y=games.screen.height/2, lifetime=5*games.screen.fps, after_death=games.screen.quit)
games.screen.mainloop()
