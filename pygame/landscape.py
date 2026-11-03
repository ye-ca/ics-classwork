# pygame landscape
import pygame
import math

pygame.display.init() # changed to pygame.display.init() to avoid initializing the audio module that prevented this from closing on my linux computer

WIDTH = 1280
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initalize polygon positions
grass_positions = [
    (0, 400),
    (0, 400),
    (0, 400),
    (0, 328),
    (369, 326),
    (359, 346),
    (342, 404),
    (374, 434),
    (495, 454),
    (642, 483),
    (763, 482),
    (1067, 470),
    (1300, 431),
    (1368, 421),
    (1378, 726),
    (0, 728),
]

hills_positions = [
    (0, 400),
    (0, 400),
    (0, 328),
    (1, 235),
    (12, 243),
    (26, 246),
    (41, 263),
    (64, 269),
    (79, 271),
    (89, 278),
    (97, 283),
    (116, 287),
    (140, 297),
    (150, 293),
    (172, 280),
    (191, 274),
    (209, 268),
    (219, 276),
    (237, 278),
    (248, 282),
    (266, 290),
    (281, 296),
    (311, 306),
    (328, 309),
    (366, 316),
    (387, 312),
    (445, 312),
    (466, 315),
    (517, 321),
    (548, 323),
    (606, 321),
    (648, 318),
    (678, 318),
    (717, 321),
    (763, 322),
    (801, 308),
    (819, 303),
    (868, 306),
    (883, 303),
    (920, 306),
    (951, 303),
    (980, 309),
    (999, 311),
    (1042, 309),
    (1078, 310),
    (1117, 295),
    (1158, 287),
    (1178, 278),
    (1202, 271),
    (1231, 278),
    (1259, 291),
    (1280, 300),
    (1280, 309),
    (1280, 327),
    (1280, 335),
    (1280, 344),
    (1280, 357),
    (1280, 376),
    (1232, 367),
    (1218, 360),
    (1200, 351),
    (1168, 353),
    (1139, 349),
    (1104, 349),
    (1065, 336),
    (1019, 338),
    (970, 337),
    (924, 336),
    (853, 344),
    (793, 339),
    (737, 342),
    (679, 342),
    (624, 341),
    (546, 344),
    (508, 348),
    (494, 351),
    (471, 363),
    (400, 371),
    (355, 380),
]

water_positions = [
    (0, 400),
    (0, 400),
    (0, 400),
    (248, 405),
    (426, 334),
    (549, 333),
    (963, 328),
    (1161, 323),
    (1241, 350),
    (1280, 359),
    (1280, 391),
    (1280, 425),
    (1286, 461),
    (1248, 468),
    (1026, 505),
    (725, 517),
    (462, 499),
]

hillshade1_positions = [
    (0, 325),
    (0, 319),
    (67, 344),
    (99, 361),
    (94, 341),
    (143, 368),
    (164, 385),
    (177, 388),
    (197, 394),
    (218, 405),
    (187, 405),
    (152, 397),
    (120, 385),
    (129, 400),
    (161, 410),
    (128, 406),
    (100, 401),
    (65, 388),
    (72, 406),
    (90, 416),
    (54, 410),
    (28, 397),
    (29, 410),
    (40, 424),
    (66, 428),
    (93, 442),
    (76, 446),
    (39, 437),
    (0, 439),
    (0, 434),
]

hillshade2_positions = [
    (166, 312),
    (166, 312),
    (166, 312),
    (162, 303),
    (149, 301),
    (166, 296),
    (176, 300),
    (182, 296),
    (193, 303),
    (203, 311),
    (213, 315),
    (215, 308),
    (227, 317),
    (241, 326),
    (254, 330),
    (267, 330),
    (278, 333),
    (287, 344),
    (298, 350),
    (286, 350),
    (273, 346),
    (281, 354),
    (289, 358),
    (302, 364),
    (321, 363),
    (338, 368),
    (349, 371),
    (333, 374),
    (326, 381),
    (306, 377),
    (278, 372),
    (254, 358),
    (265, 372),
    (279, 378),
    (258, 375),
    (241, 369),
    (223, 355),
    (193, 342),
    (169, 326),
    (161, 320),
    (171, 320),
    (157, 311),
]

hillshade3_positions = [
    (257, 327),
    (257, 327),
    (257, 327),
    (281, 329),
    (293, 333),
    (299, 340),
    (306, 341),
    (329, 342),
    (345, 338),
    (351, 344),
    (362, 346),
    (378, 341),
    (368, 337),
    (337, 327),
    (365, 328),
    (392, 332),
    (415, 335),
    (420, 344),
    (446, 342),
    (476, 336),
    (509, 341),
    (539, 339),
    (560, 329),
    (586, 332),
    (609, 330),
    (627, 324),
    (660, 332),
    (681, 333),
    (707, 335),
    (731, 329),
    (752, 327),
    (780, 318),
    (798, 313),
    (789, 323),
    (785, 329),
    (801, 327),
    (826, 322),
    (838, 334),
    (839, 338),
    (853, 333),
    (866, 330),
    (885, 323),
    (881, 311),
    (897, 311),
    (906, 321),
    (923, 325),
    (940, 327),
    (970, 320),
    (959, 327),
    (985, 327),
    (1006, 331),
    (1012, 335),
    (1038, 330),
    (1052, 335),
    (1034, 338),
    (1007, 338),
    (962, 336),
    (939, 338),
    (909, 338),
    (887, 340),
    (875, 344),
    (839, 346),
    (819, 342),
    (789, 341),
    (749, 341),
    (716, 341),
    (688, 340),
    (633, 342),
    (569, 342),
    (539, 342),
    (520, 344),
    (502, 348),
    (489, 354),
    (461, 354),
    (464, 361),
    (441, 365),
    (408, 365),
    (391, 362),
    (375, 366),
    (383, 372),
    (356, 372),
    (340, 369),
    (303, 358),
    ]

hillshade4_positions = [
    (1145, 320),
    (1145, 320),
    (1145, 320),
    (1145, 339),
    (1157, 344),
    (1174, 344),
    (1186, 337),
    (1207, 324),
    (1207, 339),
    (1234, 325),
    (1258, 314),
    (1268, 313),
    (1258, 322),
    (1257, 333),
    (1256, 341),
    (1267, 335),
    (1287, 332),
    (1289, 341),
    (1277, 356),
    (1289, 367),
    (1287, 378),
    (1288, 376),
    (1273, 374),
    (1241, 371),
    (1232, 367),
    (1216, 359),
    (1203, 354),
    (1196, 353),
    (1184, 352),
    (1166, 352),
    (1153, 349),
    (1140, 347),
    (1129, 348),
    (1119, 348),
    (1106, 349),
    (1103, 348),
    (1116, 331),
    (1127, 335),
]

path_positions = [
    (951, 720),
    (890, 687),
    (831, 672),
    (781, 668),
    (674, 660),
    (568, 654),
    (532, 642),
    (508, 613),
    (451, 583),
    (418, 576),
    (370, 563),
    (309, 543),
    (276, 501),
    (274, 473),
    (257, 456),
    (251, 437),
    (260, 426),
    (287, 415),
    (315, 410),
    (329, 412),
    (344, 406),
    (360, 424),
    (349, 423),
    (338, 424),
    (316, 427),
    (305, 425),
    (289, 428),
    (281, 436),
    (287, 453),
    (308, 464),
    (308, 474),
    (307, 490),
    (319, 505),
    (344, 516),
    (388, 528),
    (416, 525),
    (449, 526),
    (475, 534),
    (517, 535),
    (571, 547),
    (585, 562),
    (626, 574),
    (657, 565),
    (710, 568),
    (754, 571),
    (817, 569),
    (887, 576),
    (923, 589),
    (987, 604),
    (1026, 608),
    (1099, 631),
    (1157, 654),
    (1210, 675),
    (1231, 693),
    (1244, 728),
]
# ---------------------------

# ---------------------------
# Initialize global variables

speed = 1  


water_colour = (89, 141, 176)
grass_colour = (95, 123, 59)
hillshade_colour = (13, 85, 0)
path_colour = (173, 148, 89)

flower_colour = (234, 137, 89)
flower_size = 20

sun_position = (640, 0)
moon_x = 2000 # start off screen
moon_y = 2000 

sky_colour_start = (0, 0, 0) # fill in just to have defined variables, will be changed in the game loop
sky_colour_end = (0, 0, 0) # same as above

sky1_time_begin = 0
sky1_colour1 = (253, 244, 150)
sky1_colour2 = (166, 222, 253)

sky2_time_begin = 170
sky2_colour1 = (185, 121, 91)
sky2_colour2 = (217, 113, 41)

sky3_time_begin = 270
sky3_colour1 = (0, 0, 0)
sky3_colour2 = (0, 0, 0)

sky4_time_begin = 520
sky4_colour1 = (0, 0, 0)
sky4_colour2 = (0, 0, 0)

sky5_time_begin = 600
sky5_colour1 = (253, 244, 150)
sky5_colour2 = (166, 222, 253)


sky_reset = 800 # reset the sky to the beginning of the cycle after this many frames


# debug
frames = 1

# ---------------------------

# ---------------------------
# Drawing Functions

def draw_background(start, end):
    # draw a gradient background from start to end
    for i in range(HEIGHT):
        r = start[0] + ((end[0] - start[0]) / HEIGHT) * i # first find the delta between start and end, then divide by height of screen to make it a ratio, then multiply by current index to get current value
        g = start[1] + ((end[1] - start[1]) / HEIGHT) * i 
        b = start[2] + ((end[2] - start[2]) / HEIGHT) * i 
        pygame.draw.line(screen, (int(r), int(g), int(b)), (0, i), (WIDTH, i)) # draw a line with the colours, starting at the edge ending at the other edge of the screen
        

def draw_sun(position):
    pygame.draw.circle(screen, (253, 132, 0), position, 90)
    pygame.draw.circle(screen, (253, 201, 5), position, 50)
    pygame.draw.circle(screen, (255, 228, 0), position, 30)
    pygame.draw.circle(screen, (245, 235, 156), position, 20)

def draw_moon(x, y):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 90)
    pygame.draw.circle(screen, (197, 209, 234), (x + 45, y - 27), 20)
    pygame.draw.circle(screen, (197, 209, 234), (x + 50, y + 10), 15)
    pygame.draw.circle(screen, (197, 209, 234), (x - 10, y - 40), 35)
    pygame.draw.circle(screen, (197, 209, 234), (x - 40, y + 10), 25)
    pygame.draw.circle(screen, (197, 209, 234), (x + 76, y + 0), 12)
    pygame.draw.circle(screen, (197, 209, 234), (x - 50, y - 30), 30)
   
def change_sky_colour(start, end, total_frames, current_frame):
    t = current_frame / total_frames
    r = start[0] + (end[0] - start[0]) * t
    g = start[1] + (end[1] - start[1]) * t
    b = start[2] + (end[2] - start[2]) * t
    return (int(r), int(g), int(b))

def draw_flower(x, y, size, colour):
    pygame.draw.rect(screen, (89, 103, 52), (x - 5, y, 10, 50)) # stem
    pygame.draw.circle(screen, colour, (x, y), size) # flower
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                print(f"{event.pos},")
                path_positions.append(event.pos) 
    
    # GAME STATE UPDATES
    # All game math and comparisons happen here

    frames += speed # i named this frames but ive linked this to everything that changes. 

    if frames < sky3_time_begin:  # sun going down, shoo the moon off the screen
        sun_position = (sun_position[0], frames * 2 - 90)
        moon_y = 9999


    elif frames < sky4_time_begin: # moon going down, shoo the sun off the screen
        sun_position = (sun_position[0], 9999)
        moon_x = 640
        moon_y = (frames - sky3_time_begin) * 2 - 90
    
    elif frames < sky5_time_begin: # both moon and sun shooed off the screen
        sun_position = (sun_position[0], 9999)
        moon_y = 9999


    elif frames < sky_reset: # bring sun down, moon go bye bye 
        frames = 1


    
    print(frames)
    # DRAWING
    
    # background colour changes based on frames
    if frames < sky2_time_begin:
        current = frames - sky1_time_begin
        total   = sky2_time_begin - sky1_time_begin
        sky_colour_start = change_sky_colour(sky1_colour1, sky2_colour1, total, current)
        sky_colour_end   = change_sky_colour(sky1_colour2, sky2_colour2, total, current)

    elif frames < sky3_time_begin:
        current = frames - sky2_time_begin
        total   = sky3_time_begin - sky2_time_begin
        sky_colour_start = change_sky_colour(sky2_colour1, sky3_colour1, total, current)
        sky_colour_end   = change_sky_colour(sky2_colour2, sky3_colour2, total, current)

    elif frames < sky4_time_begin:
            current = frames - sky3_time_begin
            total   = sky4_time_begin - sky3_time_begin
            sky_colour_start = change_sky_colour(sky3_colour1, sky4_colour1, total, current)
            sky_colour_end   = change_sky_colour(sky3_colour2, sky4_colour2, total, current)

    elif frames < sky5_time_begin:
            current = frames - sky4_time_begin
            total   = sky5_time_begin - sky4_time_begin
            sky_colour_start = change_sky_colour(sky4_colour1, sky5_colour1, total, current)
            sky_colour_end   = change_sky_colour(sky4_colour2, sky5_colour2, total, current)
            
    # Draw the background
    draw_background(sky_colour_start, sky_colour_end)

    # Draw the sun
    draw_sun(sun_position)
    draw_moon(moon_x, moon_y)
    

    


    # Draw the Water
    pygame.draw.polygon(screen, water_colour, water_positions)

    # Draw Grass/hills
    pygame.draw.polygon(screen, grass_colour, grass_positions)
    pygame.draw.polygon(screen, grass_colour, hills_positions)
    # draw hillshades
    pygame.draw.polygon(screen, hillshade_colour, hillshade1_positions)
    pygame.draw.polygon(screen, hillshade_colour, hillshade2_positions)
    pygame.draw.polygon(screen, hillshade_colour, hillshade3_positions)
    pygame.draw.polygon(screen, hillshade_colour, hillshade4_positions)

    # draw path
    pygame.draw.polygon(screen, path_colour, path_positions)

    # draw flowers
    for i in range(WIDTH - 990):
        if i % 20 == 0:
            draw_flower(i, math.sin(i * 0.2) * 140 + 600, flower_size, flower_colour)

    for i in range(600, WIDTH):
            if i % 50 == 0:
                draw_flower(i, math.sin(i * 0.2) * 30 + 485, flower_size, flower_colour)


    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
