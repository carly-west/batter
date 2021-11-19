from game.actor import Actor
from game.point import Point
from game import constants


class Ball(Actor):
    def __init__(self):
        super().__init__()
        self.set_height = constants.BALL_HEIGHT
        self.set_width = constants.BALL_WIDTH
        # for i in
        self.set_image(constants.IMAGE_BALL)
        self._velocity = Point(-4, -4)

    def set_position(self, position):
        self._position = position

    def get_position(self):
        return self._position
