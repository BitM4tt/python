from pygame import *
import __init__, color, games
games.init(screen_width=1000, screen_height=700, fps=50)
image=games.load_image("pic.jpg")
image2=games.Sprite(image=image, x=games.screen.width/2, y=games.screen.height/2)
games.screen.add(image2)
games.screen.mainloop()
