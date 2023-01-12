#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Jan. 10, 2022


import stage
import ugame


# main game_scene
def game_scene():
    # imports image
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets the image(s) in a grid
    background = stage.Grid(image_bank_background, 10, 8)
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # displays the background ands it to a layer
    game = stage.Stage(ugame.display, 60)
    game.layers = [ship] + [background]
    game.render_block()

    # game loop
    while True:
        # get user input

        # update game logic

        # redraw the Sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
