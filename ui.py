import pyglet

class TestPingMenu(pyglet.window.Window):
    def __init__(self,width=700, height=200,*args, **kwargs) -> None:
        super().__init__(width,height,*args, **kwargs)
        self.label = pyglet.text.Label('Window 1',font_name='Times New Roman',font_size=36,x=width//2, y=height//2,anchor_x='center', anchor_y='center')  

    def on_draw(self):
        self.clear()
        self.label.draw()

    def render(self):
        pass

window = TestPingMenu()

#window.render()
pyglet.app.run()