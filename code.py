#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Jan. 10, 2022
# space aliens game


import constants
import stage
import ugame


# main menu_scene
def menu_scene():
    # imports all images needed
    image_bank_background = stage.Bank.from_bmp16("Assets/space_aliens_background.bmp")

    # adds text objects
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # sets the image(s) in a grid
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # creates a stage for the background to be displayed
    # and sets the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # sets layers, items show up in order
    game.layers = text + [background]
    # renders background + original location of the sprite
    game.render_block()

    # game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # start button pressed
        if keys & ugame.K_START != 0:
            game_scene()

        # redraws the Sprites
        game.tick()


# main game_scene
def game_scene():
    # imports all images needed
    image_bank_background = stage.Bank.from_bmp16("Assets/space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("Assets/space_aliens.bmp")

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("Assets/pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # sets the image(s) in a grid
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # sprites
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )
    alien = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # creates a stage for the background to be displayed
    # and sets the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # sets layers, items show up in order
    game.layers = [ship] + [alien] + [background]
    # renders background + original location of the sprite
    game.render_block()

    # game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # A button pressed to fire
        if keys & ugame.K_X != 0:
            # makes the sound of a
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # B button pressed
        if keys & ugame.K_O != 0:
            pass
        # start button pressed
        if keys & ugame.K_START != 0:
            pass
        # select button pressed
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
            # moves ship
            if ship.x <= (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
            # sets boundaries for the right side
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)

        if keys & ugame.K_LEFT != 0:
            # moves ship
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            # sets boundaries for the left side
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        # updates game logic
        # plays a sound if A button was button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # redraws the Sprites
        game.render_sprites([ship] + [alien])
        game.tick()


if __name__ == "__main__":
    menu_scene()
