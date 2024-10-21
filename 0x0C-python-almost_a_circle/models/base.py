#!/usr/bin/python3
"""base.py module
Provides the class definition of Base
"""
import json
import csv
import turtle


class Base:
    """Base class definiton
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate base object with id
        """

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        """
        if (list_dictionaries is None):
            return ("[]")
        if len(list_dictionaries) < 1:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        """
        if (json_string is None) or (len(json_string) < 1):
            return ([])
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of list_objs to a file
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.writelines("[]")
            else:
                objs = [obj.to_dictionary() for obj in list_objs]
                f.writelines(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            dummy.update(**dictionary)
        if cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = cls.from_json_string(f.read())
                instances = [cls.create(**instance) for instance in content]
                return (instances)
        except FileNotFoundError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes the object to CSV format
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            if list_objs is None:
                writer.writerow([])
            else:
                objs = [obj.to_dictionary() for obj in list_objs]
                for obj in objs:
                    writer.writerow(obj.values())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes the object from CSV format
        """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.reader(f, delimiter=",", lineterminator="\n")
                contents = [item for item in reader]
                keys = cls(1, 1).to_dictionary().keys()
                instance_dictionaries = []
                for values in contents:
                    values = [int(value) for value in values]
                    instance_dictionaries.append(dict(zip(keys, values)))
                instances = [cls.create(**dictionary) for dictionary in
                             instance_dictionaries]
                cls.__nb_objects -= 1
                return (instances)
        except FileNotFoundError:
            return ([])

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares
        """
        turtle.Turtle()
        turtle.bgcolor("white")
        turtle.pensize(4)
        turtle.pencolor("blue")
        turtle.shape("classic")
        turtle.title("Draw Object")
        turtle.speed(1)

        for rectangle in list_rectangles:
            turtle.showturtle()
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            for i in range(2):
                turtle.forward(rectangle.width)
                turtle.right(90)
                turtle.forward(rectangle.height)
                turtle.right(90)
            turtle.hideturtle()

        for square in list_squares:
            turtle.showturtle()
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for i in range(4):
                turtle.forward(square.size)
                turtle.right(90)
            turtle.hideturtle()
        turtle.penup()
        turtle.goto(90, 90)
        turtle.write("Click here to exit")
        turtle.exitonclick()
