#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Jan. 10, 2022
# space aliens game


import constants
import stage
import ugame


# main game_scene
def game_scene():
    # imports all images needed
    image_bank_background = stage.Bank.from_bmp16("Assets/space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("Assets/space_aliens.bmp")

    # sets the image(s) in a grid
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # creates a stage for the background to be displayed
    # and sets the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # sets layers, items show up in order
    game.layers = [ship] + [background]
    # renders background + original location of the sprite
    game.render_block()

    # game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # A button pressed
        if keys & ugame.K_X:
            pass
        # Button pressed
        if keys & ugame.K_O:
            pass
        # start button pressed
        if keys & ugame.K_START:
            pass
        # select button pressed
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            # moves ship
            if ship.x <= constants.SCREEN_X:
                ship.move(ship.x + 1, ship.y)
            # sets boundaries for the right side
            else:
                ship.move(constants.SCREEN_X, ship.y)

        if keys & ugame.K_LEFT:
            # moves ship
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            # sets boundaries for the left side
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

        # update game logic

        # redraw the Sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
