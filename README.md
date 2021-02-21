# Brick Breaker Game in Python using OOPs concepts

## Components
- Ball
- Bricks:
    - Level bricks : Bricks of value 1,2,3 whose value reduce by 1 on hitting and vanish on becoming 0
    - Unbreakable bricks `X`: Can't be broken by ball hits
    - Exploding bricks `*` : Hitting these break bricks adjacent to them (diagonally, vertically, horizontally) irrespective of the value or kind.
- Paddle

## Run
- `python3 main.py`

## Play
- `w` : releasing ball at the start
- `a` : move paddle to the left
- `d` : move paddle to the right
- `q` : quit game

OOPS concepts used:

• Inheritance: Object class with different types of objects like Brick, Ball, Paddle etc. inherited from it.

• Polymorphism: Methods show(), clear() are present in ball, paddle, brick etc. classes but they perform different function according to the class they belong to.

• Encapsulation: Class and object based approach for all the functionality implemented.

• Abstraction: Intuitive functionality like move_balls(), shoot_ball(), move_paddle(), etc, showing away inner details from the end user.