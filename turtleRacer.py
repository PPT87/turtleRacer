import turtle
import random

# Set screen size
WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'black',
          'purple', 'yellow', 'brown', 'cyan', 'pink']


def get_number_of_turtles():
    racers = 0
    while True:
        racers = input('Enter how many turtles will be racing (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Try again...Please enter a valid number')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Try again...Please enter a number 2 and 10...Try again!')


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    # enumerate gives the index and the value
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def race(colors):
    turtles = create_turtles()

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def init_turtle():
    # Set up turtle screen
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    # Rename window
    screen.title('Turtle Racer')


racers = get_number_of_turtles()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f'{winner} turtle wins!')
