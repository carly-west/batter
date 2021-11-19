import random
from game import constants
from game.action import Action
from game.point import Point
from game.actor import Actor


class HandleOffScreenAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

    Stereotype:
        Controller
    """

    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["balls"][0]

        position = ball.get_position()
        x = position.get_x()
        y = position.get_y()
        x_vel = ball._velocity.get_x()
        y_vel = ball._velocity.get_y()

        if x == 776 or x == 0:
            x_vel = x_vel * -1

        if y in range(575, 578):
            y_vel = y_vel * -1

        elif y in range(0, 4):
            y_vel = y_vel * -1

        ball.set_velocity(Point(x_vel, y_vel))
