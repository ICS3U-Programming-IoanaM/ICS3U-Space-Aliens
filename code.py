#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Jan. 10, 2022


import ugame
import stage


# main game_scene
def game_scene():
    # imports background image and allows it to be displayed
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background)

    # displays the background ands it to a layer
    game - stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()

    # game loop
    while True:
        pass

if __name__ == "__main__":
    game_scene()
