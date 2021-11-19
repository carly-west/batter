from game.point import Point
from game.action import Action
from game import constants
import random
from abc import abstractmethod
from abc import ABC


class Person(ABC):
    def __init__(self):
        self._first = ""
        self._last = ""

    def print_names(self):
        print(f"First: {self._first}, Last: {self._last}")

    def set_first_name(self, name):
        self._first = name

    def set_last_name(self, name):
        self._last = name

    def get_first_name(self):
        return self._first

    def get_last_name(self):
        return self._last


class Student(Person):
    def __init__(self):
        super().__init__()
        self._gpa = ""

    def set_gpa(self, gpa):
        self._gpa = gpa

    def get_gpa(self):
        return self._gpa


def mainPerson():

    person1 = Person()
    person1.set_first_name("Carly")
    person1.set_last_name("West")

    person2 = Person()
    person2.set_first_name("Leonardo")
    person2.set_last_name("Correa")

    person3 = Person()
    person3.set_first_name("Ellie")
    person3.set_last_name("West")

    people = []

    people.append(person1)
    people.append(person2)
    people.append(person3)

    for person in people:
        print(
            f"First: {person.get_first_name()}, Last: {person.get_last_name()}")


def mainStudent():

    student1 = Student()
    student1.set_first_name("Carly")
    student1.set_last_name("West")
    student1.set_gpa("3.8")

    student2 = Student()
    student2.set_first_name("Leonardo")
    student2.set_last_name("Correa")
    student2.set_gpa("4.0")

    student3 = Student()
    student3.set_first_name("Ellie")
    student3.set_last_name("West")
    student3.set_gpa("2.5")

    people = []

    people.append(student1)
    people.append(student2)
    people.append(student3)

    for student in people:
        print(
            f"First: {student.get_first_name()}, Last: {student.get_last_name()}, GPA: {student.get_gpa()}")


mainPerson()
mainStudent()


# class Shutter(ABC):
#     def __init__(self):
#         self._color = ""
#         self._room = ""
#         self._louverCount = 0

#     def print_shutter_info(self):
#         print(
#             f"Color: {self._color}, Room: {self._room}, Louvers: {self._louverCount}")

#     @abstractmethod
#     def get_area(self):
#         pass


# class SquareShutter(Shutter):
#     def __init__(self):
#         super().__init__()
#         self._width = 0
#         self._height = 0

#     def print_shutter_info(self):
#     print(
#         f"*SQUARE* Color: {self._color}, Room: {self._room}, Louvers: {self._louverCount}, Width: {self._width}, Height: {self._height}")

#     def get_area(self):
#         return self._width * self._height


# class SunburstShutter(Shutter):
#     def __init__(self):
#         super().__init__()
#         self._radius = 0

#     def print_shutter_info(self):
#         print(
#             f"*SUNBURST* Color: {self._color}, Room: {self._room}, Louvers: {self._louverCount}, Radius: {self._radius}")

#     def get_area(self):
#         return (self._radius ** 2) * 3.14 / 2


# def print_cut_ticket(shutter):
#     pass


# def main():
#     s1 = Shutter()
#     s1._color = "White"
#     s1._room = "Living Room"
#     s1._louverCount = 25
#     s1.print_shutter_info()
#     s2 = SquareShutter()
#     s2._color = "Off White"
#     s2._room = "Kitchen"
#     s2._louverCount = 38
#     s2._width = 60
#     s2._height = 48
#     s2.print_shutter_info()
#     s3 = SunburstShutter()
#     s3._color = "Snow White"
#     s3._room = "Dungeon"
#     s3._louverCount = 20
#     s3._radius = 12
#     s3.print_shutter_info()
#     shutters = []
#     shutters.append(s1)
#     shutters.append(s2)
#     shutters.append(s3)
#     print("Using the list...")
#     total_area = 0
#     for shutter in shutters:
#         shutter.print_shutter_info()
#         total_area += shutter.get_area()
#         print(f"Total area: {total_area}")


# main()


class HandleCollisionsAction(Action):
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
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]

        ball_position = ball.get_position()
        ball_x = ball_position.get_x()
        ball_y = ball_position.get_y()

        x_vel = ball._velocity.get_x()
        y_vel = ball._velocity.get_y()

        paddle_position = paddle.get_position()
        paddle_x = paddle_position.get_x()
        paddle_y = paddle_position.get_y()

        if ball_x + 24 in range(paddle_x, paddle_x + 96) and ball_y + 24 in range(paddle_y, paddle_y + 24):
            if x_vel >= 0 and y_vel <= 0:
                y_vel = y_vel * -1
            if x_vel <= 0 and y_vel <= 0:
                y_vel = y_vel * -1

            if x_vel >= 0 and y_vel >= 0:
                y_vel = y_vel * -1

            if x_vel <= 0 and y_vel >= 0:
                y_vel = y_vel * -1

            ball.set_velocity(Point(x_vel, y_vel))

        for brick in bricks:
            position = brick.get_position()
            brick_x = position.get_x()
            brick_y = position.get_y()

            if ball.get_top_edge in range(brick_x, brick_x + 48) and ball_y in range(brick_y, brick_y + 24):
                y_vel = y_vel * -1

            if ball_x in range(brick_x, brick_x + 48) and ball_y in range(brick_y, brick_y + 24):

                if brick_x >= 0 and brick_y <= 0:
                    y_vel = y_vel * -1

                if brick_x <= 0 and brick_y <= 0:
                    y_vel = y_vel * -1

                if brick_x >= 0 and brick_y >= 0:
                    y_vel = y_vel * -1

                if brick_x <= 0 and brick_y >= 0:
                    y_vel = y_vel * -1

                if brick_x >= 0 and brick_y >= 0:
                    x_vel = x_vel * -1

                if brick_x <= 0 and brick_y <= 0:
                    y_vel = y_vel * -1

                if brick_x >= 0 and brick_y >= 0:
                    y_vel = y_vel * -1

                if brick_x <= 0 and brick_y >= 0:
                    y_vel = y_vel * -1

                # x_vel = x_vel * -1
                # y_vel = y_vel * -1
                ball.set_velocity(Point(x_vel, y_vel))
