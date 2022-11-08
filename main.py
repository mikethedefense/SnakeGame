import arcade 
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Snake Game"
PLAYER_MOVEMENT_SPEED = 5
SCALING = 0.2


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.BEIGE)
        self.player_list = None
        self.collectables = None
        self.player_sprite = None
    
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.collectables = arcade.SpriteList()
        main_sprite = "snake (2).png"
        self.player_sprite = arcade.Sprite(main_sprite, SCALING)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 325
        self.player_list.append(self.player_sprite)
    
    def on_draw(self):
        self.clear()
        self.player_list.draw()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
            self.player_sprite.change_x = 0
            self.player_sprite.angle = 180
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
            self.player_sprite.change_x = 0
            self.player_sprite.angle = 360
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            self.player_sprite.change_y = 0
            self.player_sprite.angle = -90
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
            self.player_sprite.change_y = 0
            self.player_sprite.angle = 90
    
    def on_update(self, delta_time):
        self.player_sprite.update()
        
        if self.player_sprite.center_x < self.player_sprite.height / 2:
            self.player_sprite.center_x = self.player_sprite.height / 2

        if self.player_sprite.center_x > SCREEN_WIDTH - self.player_sprite.height / 2:
            self.player_sprite.center_x = SCREEN_WIDTH - self.player_sprite.height / 2

        if self.player_sprite.center_y < self.player_sprite.height/2:
            self.player_sprite.center_y = self.player_sprite.height/2

        if self.player_sprite.center_y > SCREEN_HEIGHT - self.player_sprite.height/2:
            self.player_sprite.center_y = SCREEN_HEIGHT - self.player_sprite.height/2

def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()