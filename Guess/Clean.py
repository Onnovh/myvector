import time
import os
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps
import random

x = (random.randint(0, 100))
anim_fout = 'anim_pounce_success_02'
current_directory = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(current_directory, "wrong.jpg")
image_file = Image.open(image_path)
screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)
duration_s = 2.0


with anki_vector.Robot() as robot:
    print(x)
    robot.behavior.drive_off_charger()
    robot.anim.play_animation_trigger("GreetAfterLongTime")
    robot.behavior.set_head_angle(degrees(45.0))
    robot.behavior.set_lift_height(0.0)
    robot.behavior.say_text("I want to play the game guess the number!")
    robot.behavior.say_text("Type a number between 0 and 100.")
    while True:
        y = int(input('Guess a number between 0 and 100: '))
        if y == x:
            robot.behavior.set_head_angle(degrees(45.0))
            robot.behavior.set_lift_height(1.0,duration=0.1)
            robot.audio.stream_wav_file("win.wav", 100)
            robot.behavior.set_lift_height(0.0)
            robot.behavior.say_text("Yes, the right number was")
            robot.behavior.say_text(str(x))
            robot.behavior.say_text("Well done!")
            robot.anim.play_animation("anim_reacttocliff_wheely_03")
            robot.behavior.drive_straight(distance_mm(100), speed_mmps(255))
            robot.behavior.drive_on_charger()
            break
        elif x > y:
            robot.behavior.set_head_angle(degrees(45.0))
            robot.behavior.set_lift_height(0.0)
            robot.screen.set_screen_with_image_data(screen_data, duration_s)
            robot.audio.stream_wav_file("wrong.wav", 100)
            robot.behavior.say_text("You guessed too low. Guess again!")
            robot.anim.play_animation(anim_fout)
            robot.behavior.drive_straight(distance_mm(50), speed_mmps(255))
            robot.behavior.set_head_angle(degrees(20.0))
        elif x < y:
            robot.behavior.set_head_angle(degrees(45.0))
            robot.behavior.set_lift_height(0.0)
            robot.screen.set_screen_with_image_data(screen_data, duration_s)
            robot.audio.stream_wav_file("wrong.wav", 100)
            robot.behavior.say_text("You guessed too high. Guess again!")
            robot.anim.play_animation(anim_fout)
            robot.behavior.drive_straight(distance_mm(50), speed_mmps(255))
            robot.behavior.set_head_angle(degrees(20.0))
   

