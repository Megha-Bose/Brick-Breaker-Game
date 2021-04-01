# Brick Breaker Game in Python using OOPs concepts

## Overview

- This a terminal-based arcade game in Python3, inspired by the classic brick-breaker game. 
- The player uses a paddle with a bouncing ball to smash a wall of bricks. 
- The objective of the game is to break all the bricks as fast as possible. You lose a life when the ball touches the ground below the paddle. 
- Different sounds are played when different events (like life lost, brick collision, wall collision, laser shoot, etc.) occur.

## Components

- Ball
- Bricks:
- Level bricks: Bricks of value 1,2,3 whose value reduce by 1 on hitting and vanish on becoming 0
- Unbreakable bricks `X`: Can't be broken by ball hits
- Exploding bricks `*` : Hitting these break bricks adjacent to them (diagonally, vertically, horizontally) irrespective of the value or kind.
- Colour changing rainbow bricks till hit by a ball
- Falling bricks: Bricks move down by 1 unit on the ball, hitting the paddle. The game ends if the lowest brick present touches the paddle.
- Paddle
- Boss Enemy in the last level:
	- The final level of the game has the boss enemy along with a few unbreakable bricks.
	- The boss enemy flies at the top of the screen and follows the paddle (moves along with it).
	- The enemy drops bombs `*` in regular intervals onto the paddle (which travels linearly downwards); on being hit by these bombs, the paddle loses one life.
	- The enemy has health which reduces on hitting it directly with a ball (shown on health bar).
- Shoot paddle power-up:
	- Activates when paddle catches `^` that falls down from the point ball/bullet destroys a brick.
	- This power-up enables the paddle to shoot bullets in order to break the bricks. The strength of each of these bullets is the same as the ball.
	- Taking the power-up enables the paddle to shoot lasers continuously until time for the power-up runs out.
	- This power-up is active for a limited time. The remaining time of usage of the power-up is displayed.
	- Small cannons appear on both ends of the paddle from which the bullets are shot.

## Run
- Open the terminal in full screen
- `python3 main.py`

## Play
- `w` : releasing ball
- `a` : move paddle to the left
- `d` : move paddle to the right
- `n` : Move to next level
- `q` : quit game

## Details

### Startup
	
- Initially, the ball appears randomly on any part of the paddle (top). The player can move and release the ball at their will.

### Collision Handling

- Handles elastic collisions as follows:
	- Ball and bricks:
		- Handles collisions with four sides of the brick. The reflections are based on the side the ball hits the brick.
		- Each time a collision happens, the strength of brick decreases by one unit (except for unbreakable bricks), and when the strength becomes zero, the brick disappears.
	- Ball and paddle:
		- Handles collisions with only the top face of the paddle.
		- The direction of movement of the ball after collision with the paddle depends on the distance from the center of the paddle and the collision point.
	- Ball and wall(5 points):
		- Handles collisions with 3 sides of the walls (except the bottom one).
		- The reflections are based on the side the ball hits the wall.
		- The ball is lost when it hits the bottom wall (missing the paddle).

### Levels
- 3 levels, with each level having different layouts.
- The scores and lives of each level carried forward to the next one. 
- Power-ups lost at the start of the new level.
- `n` key to skip the levels (for easier testing). If the key is pressed in the last level, the game is over.

## OOPS concepts used:

- Inheritance: Object class with different types of objects like Brick, Ball, Paddle, etc. inherited from it.

- Polymorphism: Methods show(), clear() are present in the ball, paddle, brick, etc. classes, but they perform different functions according to the class they belong to.

- Encapsulation: Class and object-based approach for all the functionality implemented.

- Abstraction: Intuitive functionality like move_balls(), shoot_ball(), move_paddle(), etc, showing away inner details from the end user.
