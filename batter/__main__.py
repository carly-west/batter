import random
import raylibpy
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.ball import Ball
from game.paddle import Paddle
from game.draw_actors_action import DrawActorsAction
from game.move_actors_action import MoveActorsAction
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.handle_off_screen_action import HandleOffScreenAction

from game.brick import Brick
# from game.control_actors_action import ControlActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
# from game.handle_off_screen_action import HandleOffScreenAction
# from game.move_actors_action import MoveActorsAction


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["bricks"] = []
    # TODO: Create bricks here and add them to the list
    bricks = []

    # Loops through and creates bricks

    row = 1

    for new_column in range(1, 15):
        row *= -1
        for new_row in range(1, 8):
            brick = Brick()
            x = (constants.BRICK_WIDTH * new_column) + constants.BRICK_SPACE
            y = (constants.BRICK_HEIGHT * new_row) + constants.BRICK_SPACE
            position = Point(x, y)
            brick.set_position(position)

            if row == -1:
                image = constants.IMAGE_BRICK_RED

            else:
                image = constants.IMAGE_BRICK
            brick.set_new_image(image)

            bricks.append(brick)

    cast["bricks"] = bricks

    # output_service.draw_actors(bricks)

    # TODO: Create a ball here and add it to the list
    balls = []

    position_ball = Point(400, 450)
    ball = Ball()
    ball.set_position(position_ball)
    balls.append(ball)

    cast["balls"] = balls

    cast["paddle"] = []
    # TODO: Create a paddle here and add it to the list

    paddles = []
    paddle = Paddle()

    position_paddle = Point(400, 550)
    paddle.set_position(position_paddle)
    paddles.append(paddle)

    cast["paddle"] = paddles

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction(physics_service)
    draw_actors_action = DrawActorsAction(output_service)
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(
        physics_service, audio_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action,
                        handle_off_screen_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)

    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()


if __name__ == "__main__":
    main()
