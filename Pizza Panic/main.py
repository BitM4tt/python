#Pizza Panic
import games, __init__, color, random
score=0
games.init(screen_width=800, screen_height=600, fps=100)
chefimage=games.load_image("Chef.gif")
bowlimage=games.load_image("Bowl.gif")
pizzaimage=games.load_image("Pizza.gif")
wallimage=games.load_image("wall.gif")
games.screen.background=wallimage
class Chef(games.Sprite):
    def update(self):
        if self.right>800:
            self.dx = -self.dx
            bounced_pos="right"
        if self.left<0:
            self.dx = -self.dx
            bounced_pos="left"
        if bounced_pos=='left':
            self.x+=3
        else:
            self.x-=3
        n=random.randint(1,3)
        if n==2:
            games.screen.add(Pizza, x=self.x+120, y=self.y)
    def __init__(self):
        super(Pan, self).__init__(image=bowlimage,
                                  x=games.mouse.x,
                                  bottom=games.screen.height)
class Pizza(games.Sprite):
    def update(self):
        image=games.load_image("Pizza.gif")
        if self.bottom>games.screen.height:
            gameovermessage=games.Message(value="GAME OVER", size=50, color=color.red, x=games.screen.width/2, y=games.screen.height/2, lifetime=5*games.screen.fps, after_death=games.screen.quit)
            games.screen.quit()
        self.y+=3
games.screen.add(Chef)
games.screen.mainloop()
