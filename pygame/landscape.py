# pygame template
import math
import pygame


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


water_colour = (89, 141, 176)
grass_colour = (95, 123, 59)
hillshade_colour = (13, 85, 0)
path_colour = (173, 148, 89)

sun_position = (640, 0)

sky1_colour1 = (253, 244, 150)
sky1_colour2 = (166, 222, 253)

sky2_time_begin = 120
sky2_colour1 = (185, 121, 91)
sky2_colour2 = (217, 113, 41)

sky3_time_begin = 215
sky3_colour1 = (0, 0, 0)
sky3_colour2 = (0, 0, 0)


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
        pygame.draw.line(screen, (r, g, b), (0, i), (WIDTH, i)) # draw a line with the colours, starting at the edge ending at the other edge of the screen
        

def draw_sun(position):
    pygame.draw.circle(screen, (253, 132, 0), position, 90)
    pygame.draw.circle(screen, (253, 201, 5), position, 50)
    pygame.draw.circle(screen, (255, 228, 0), position, 30)
    pygame.draw.circle(screen, (245, 235, 156), position, 20)
   


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
    if sun_position[1] < -100:
        frames -= 1
    elif sun_position[1] > -100:
        frames += 1
    print(frames)
        
    # DRAWING
    
    if frames < sky2_time_begin:
        draw_background(sky1_colour1, sky1_colour2)
    elif frames < sky3_time_begin:
        draw_background(sky2_colour1, sky2_colour2)
    else:
        draw_background(sky3_colour1, sky3_colour2)

    # Draw the sun
    draw_sun(sun_position)
    sun_position = (sun_position[0], sun_position[1] + 2)
    


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


    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()