import random
from game import constants
from game.action import Action
from game.point import Point


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

    Stereotype:
        Controller
    """

    def __init__(self, physics_service, audio_service):
        super().__init__()
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast):
        """Executes the action using the given actors.

            Args:
                cast (dict): The game actors {key: tag, value: list}.
            """
        ball = cast["balls"][0]  # there's only one
        paddle = cast["paddle"][0]  # there's only one
        bricks = cast["bricks"]

        ball_position = ball.get_position()
        ball_x = ball_position.get_x()
        ball_y = ball_position.get_y()

        x_vel = ball._velocity.get_x()
        y_vel = ball._velocity.get_y()

        paddle_position = paddle.get_position()
        paddle_x = paddle_position.get_x()
        paddle_y = paddle_position.get_y()

        if ball_x + 12 in range(paddle_x, paddle_x + 96) and ball_y + 24 in range(paddle_y, paddle_y + 24):
            y_vel = y_vel * -1

            self._audio_service.play_sound(constants.SOUND_BOUNCE)

            ball.set_velocity(Point(x_vel, y_vel))

        for brick in bricks:
            position = brick.get_position()
            brick_x = position.get_x()
            brick_y = position.get_y()

            # if ball_x in range(brick_x, )
            if ball_x in range(brick_x, brick_x + 48) and ball_y in range(brick_y, brick_y + 24):

                if ball_x in range(brick_x + 48, brick_y - 24):
                    x_vel = x_vel * -1

                elif ball_x + 24 in range(brick_x, brick_y - 24):
                    x_vel = x_vel * -1

                # elif ball_x + 24 in range(brick_x, brick_y + 48):
                #     y_vel = y_vel * -1
                else:
                    y_vel = y_vel * -1

                ball.set_velocity(Point(x_vel, y_vel))
                bricks.pop(bricks.index(brick))

                self._audio_service.play_sound(constants.SOUND_BOUNCE)

                # if ball_position.get_

                # if ball_y - 24 <= 0:
                #     print("GAME OVER")
