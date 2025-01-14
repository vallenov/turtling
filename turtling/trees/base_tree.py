import turtle
import random


class Tree:
    
    def __init__(self, position: tuple):
        self.position = position
        self.axiom = "22220"
        self.axiom_tmp = ""
        self.itr = 9
        self.angl = 14
        self.dl = 10
        self.level = 0
        self.stc = []
        self.thick = None

        self.grow_map = {
            '0': self.grow_leaf,
            '1': self.grow_branch,
            '2': self.random_leaf,
            '[': self.grow_save_position,
            ']': self.grow_load_position
        }

        self.draw_map = {
            '+': self.right_angle,
            '-': self.left_angle,
            '^': self.add_random_angle,
            '[': self.save_position,
            ']': self.load_position,
            '0': self.draw_leaf
        }
    
    def grow_up(self):
        turtle.hideturtle()
        turtle.tracer(0)
        turtle.penup()
        turtle.setposition(self.position)
        turtle.setheading(0)
        turtle.left(90)
        turtle.pendown()
        
        for k in range(self.itr):
            self.next_step(k)
        self.draw()
        turtle.update()

    def next_step(self, iteration):
        self.thick = int(iteration * 1.5)
        turtle.pensize(self.thick)
        for ch in self.axiom:
            f = self.grow_map.get(ch)
            f() if callable(f) else self.grow_other(ch)
        self.axiom = self.axiom_tmp
        self.axiom_tmp = ""

    def draw(self):
        for ch in self.axiom:
            f = self.draw_map.get(ch, self.draw_branch)
            f()
        turtle.setposition(self.position)

    def grow_other(self, ch):
        self.axiom_tmp += ch

    def grow_save_position(self):
        self.axiom_tmp += '['
        self.level += 1

    def grow_load_position(self):
        self.axiom_tmp += ']'
        self.level -= 1

    def grow_leaf(self):
        self.axiom_tmp += '1[-20][+20]'

    def grow_branch(self):
        self.axiom_tmp += '21'

    def save_position(self):
        self.level += 1
        self.stc.append(self.thick)
        self.stc.append(turtle.xcor())
        self.stc.append(turtle.ycor())
        self.stc.append(turtle.heading())
        self.thick = self.thick * 0.75
        turtle.pensize(self.thick)

    def load_position(self):
        self.level -= 1
        turtle.penup()
        turtle.setheading(self.stc.pop())
        turtle.sety(self.stc.pop())
        turtle.setx(self.stc.pop())
        self.thick = self.stc.pop()
        turtle.pensize(self.thick)
        turtle.pendown()

    def draw_leaf(self):
        self.stc.append(turtle.pensize())
        turtle.pensize(4)
        r = random.randint(0, 10)
        if r < 3:
            turtle.pencolor('#009900')
        elif r > 6:
            turtle.pencolor('#667900')
        else:
            turtle.pencolor('#20BB00')
        turtle.forward(self.dl - 2)
        turtle.pensize(self.stc.pop())
        turtle.pencolor('#000000')

    def random_leaf(self):
        if random.randint(0, 100) < 7 and self.level > 2:
            self.axiom_tmp += '3[^30]'
        else:
            self.axiom_tmp += '2'

    def draw_branch(self):
        if random.randint(0, 10) > 4:
            turtle.forward(self.dl)

    @staticmethod
    def add_random_angle():
        ug = random.randint(-30, 30)
        if ug < 0:
            turtle.left(ug - 25)
        else:
            turtle.left(ug + 25)

    def left_angle(self):
        turtle.left(self.angl - random.randint(-13, 13))

    def right_angle(self):
        turtle.right(self.angl - random.randint(-13, 13))


class Forrest:

    def __init__(self):
        self.position_x_list = list(range(-500, 500))
        self.position_y_list = list(range(-500, 100))

    def get_new_tree_position(self):
        x = random.choice(self.position_x_list)
        y = random.choice(self.position_y_list)
        pos = (self.position_x_list.pop(self.position_x_list.index(x)),
               self.position_y_list.pop(self.position_y_list.index(y)))
        return pos

    def grow_up(self):
        while True:
            tree = Tree(self.get_new_tree_position())
            tree.grow_up()
