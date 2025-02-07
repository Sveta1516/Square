import pygame as pg 
import pymunk.pygame_util
from random import*
pymunk.pygame_util.positive_y_is_up = False

RES = WIDTH, HEIGHT = 800, 620
FPS = 60
pg.init()
surface = pg.display.set_mode(RES) 
clock = pg.time.Clock() 
draw_options = pymunk.pygame_util.DrawOptions(surface) 


space = pymunk.Space()
space.gravity = 0, 8000
def create_square(space, pos):
    square_mass, square_size = 1, (50, 60)
    square_moment = pymunk.moment_for_box(square_mass, square_size)
    square_body = pymunk.Body(square_mass, square_moment)
    square_body.position = pos 
    square_shape = pymunk.Poly.create_box(square_body, square_size)
    square_shape.elasticity = 1.8 
    square_shape.friction = 1.0
    square_shape.color = [randrange(256) for i in range(4)]
    space.add(square_body, square_shape)

segment_shape = pymunk.Segment(space.static_body, (10, HEIGHT), (WIDTH, HEIGHT), 30)
space.add(segment_shape)
segment_shape.elasticity = 0.5
segment_shape.friction = 1.5

segment_shape1 = pymunk.Segment(space.static_body, (10, HEIGHT), (600, 150), 10)
space.add(segment_shape1)
segment_shape1.elasticity = 0.5
segment_shape1.friction = 1.5

segment_shape2 = pymunk.Segment(space.static_body, (10, HEIGHT), (10,0), 10)
space.add(segment_shape2)
segment_shape2.elasticity = 1.5
segment_shape2.friction = 1.5
while True:
    surface.fill(pg.Color(178, 243, 247))
    for i in pg.event.get(): 
            if i.type == pg.QUIT: 
                exit()
            if i.type == pg.MOUSEBUTTONDOWN:
                if i.button == 1:
                    create_square(space, i.pos)
                    print(i.pos)
    space.step(1/ FPS)
    space.debug_draw(draw_options)
    pg.display.flip()
    clock.tick(FPS)

