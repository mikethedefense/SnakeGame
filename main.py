import arcade 
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Snake Game"
PLAYER_MOVEMENT_SPEED = 5
PLAYER_SCALING = 0.2
FOOD_SCALING = 0.2



class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.BEIGE)
        self.player_list = None
        self.food = None
        self.player_sprite = None
        self.score = 0
    
    def setup(self):
        self.player_list = arcade.SpriteList()
        sprite_image= "snake (2).png"
        food_image = "chick.png"
        
        self.player_sprite = arcade.Sprite(sprite_image, PLAYER_SCALING)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 320
        self.player_list.append(self.player_sprite)

        self.food_sprite = arcade.Sprite(food_image, FOOD_SCALING)
        self.food_sprite.center_x = random.uniform(self.food_sprite.height/2, SCREEN_WIDTH - self.food_sprite.height/2)
        self.food_sprite.center_y = random.uniform(self.food_sprite.height/2,SCREEN_HEIGHT - self.food_sprite.height/2)
    
    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.food_sprite.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)
    
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
        self.food_sprite.update()
        
        if self.player_sprite.center_x < self.player_sprite.height / 2:
            self.player_sprite.center_x = self.player_sprite.height / 2

        elif self.player_sprite.center_x > SCREEN_WIDTH - self.player_sprite.height / 2:
            self.player_sprite.center_x = SCREEN_WIDTH - self.player_sprite.height / 2

        elif self.player_sprite.center_y < self.player_sprite.height/2:
            self.player_sprite.center_y = self.player_sprite.height/2

        elif self.player_sprite.center_y > SCREEN_HEIGHT - self.player_sprite.height/2:
            self.player_sprite.center_y = SCREEN_HEIGHT - self.player_sprite.height/2
        
        collision = arcade.check_for_collision(self.player_sprite, self.food_sprite)
        if collision:
            self.food_sprite.center_x = random.uniform(self.food_sprite.height/2, SCREEN_WIDTH - self.food_sprite.height/2)
            self.food_sprite.center_y = random.uniform(self.food_sprite.height/2, SCREEN_HEIGHT- self.food_sprite.height/2)
            self.score += 1
    

def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()