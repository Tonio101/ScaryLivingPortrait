'''
Moving portrait with haar cascade face detection with OpenCV
'''
from time import sleep
from omxplayer.player import OMXPlayer
from subprocess import PIPE, Popen
from pathlib import Path
import numpy as np
import sys
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
CASCADE_PATH = Path('haarcascade_frontalface_default.xml')
VIDEO_PATH = Path('raspberrypi_halloween_video.mp4')
# Adjust the dimensions according to you monitor
VIDEO_DIMENSIONS = '0 0 {LENGTH} {WIDTH}' \
                   .format(LENGTH='1920', WIDTH='1080')
OMX_PLAYER_ARGS = ['--no-osd', '--loop', '--win', VIDEO_DIMENSIONS]
KILL_OMXPLAYER_PROCESS = 'sudo pkill omxplayer.bin'

START_OF_SCENE = [0, 71, 130]

MAN_SCENE_TIMES = {
  0 : [0, 13],
  1 : [14, 36],
  2 : [37, 56],
  3 : [57, 69]
}

WOMAN_SCENE_TIMES = {
  0 : [71, 88],
  1 : [88, 101],
  2 : [101, 115],
  3 : [116, 128]
}

GIRL_SCENE_TIMES = {
  0: [130, 157],
  1: [157, 171],
  2: [171, 181],
  3: [181, 192],
}

LIST_OF_SCENES = [MAN_SCENE_TIMES, WOMAN_SCENE_TIMES, GIRL_SCENE_TIMES]

def cmdline(command):
  process = Popen(args=command,
                  stdout=PIPE,
                  shell=True)
  return process.communicate()[0]

def main():
    """
      Insert 'python3 <YOUR_PATH>/LivingPortraitFaceDetection.py &'
      to /etc/rc.local in order for the script to run
      during boot.
    """
  try:
    sleep(30) # Allow plenty of time for everything to load
    if not CASCADE_PATH.exists() or not VIDEO_PATH.exists():
      print("{0}|{1} File(s) not found!" \
            .format(CASCADE_PATH.name, VIDEO_PATH.name))
      exit(2)
    faceCascade = cv2.CascadeClassifier(CASCADE_PATH._str)
    player = OMXPlayer(VIDEO_PATH, args=OMX_PLAYER_ARGS)
    sleep(1)
    player.set_position(0.0)
    player.pause()
    sleep(1)

    # sudo modprobe bcm2835-v4l2 you may need to run this command
    # or add bcm2835-v4l2 to /etc/modules, then reboot
    capture = cv2.VideoCapture(0)
    sleep(1)
    #capture.set(3,640) # set Width
    #capture.set(4,480) # set Height
    capture.set(cv2.CAP_PROP_BUFFERSIZE, 3)

    face_detected = False
    face_detected_count = 0
    scene_count = 0
    is_face_on_first_pass = False
    is_face_on_second_pass = False

    while True:
        if face_detected:
          for i in range(5): #Flush any buffered images.
            capture.grab()
          face_detected = False

        ret, img = capture.read()

        if ret == True:
          gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
          faces = faceCascade.detectMultiScale(gray,
                                               scaleFactor=1.1,
                                               minNeighbors=5,
                                               minSize=(30, 30))
          if len(faces) > 0:
            if not is_face_on_first_pass:
              is_face_on_first_pass = True
              face_detected = True
              continue
            if not is_face_on_second_pass:
              is_face_on_second_pass = True
            if is_face_on_first_pass and is_face_on_second_pass:
              is_face_on_first_pass = False
              is_face_on_second_pass = False
              face_detected = True
          if is_face_on_first_pass or is_face_on_second_pass:
            is_face_on_first_pass = False
            is_face_on_second_pass = False
            face_detected = False
            # No faces detected, clearing flags
            continue

          if face_detected:
            # Face detected. Start video
            face_detected = True
            selected_scene = LIST_OF_SCENES[scene_count]
            scary_scene = selected_scene[face_detected_count]
            player.set_position(scary_scene[0])
            player.play()
            sleep(scary_scene[1] - scary_scene[0])
            player.pause()
            face_detected_count += 1
            if face_detected_count % 4 == 0:
              face_detected_count = 0
              scene_count += 1
              if scene_count % 3 == 0:
                scene_count = 0
              player.set_position(START_OF_SCENE[scene_count])
              player.play()
              sleep(1)
              player.pause()
    # End while loop

    capture.release()
    cv2.destroyAllWindows()
    cmdline(KILL_OMXPLAYER_PROCESS)
    sys.exit(2)
  except KeyboardInterrupt as error:
    capture.release()
    cv2.destroyAllWindows()
    cmdline(KILL_OMXPLAYER_PROCESS)
    print(error)
    sys.exit(2)
  except Exception as error:
    capture.release()
    cv2.destroyAllWindows()
    cmdline(KILL_OMXPLAYER_PROCESS)
    print(error)
    sys.exit(2)

if __name__ == '__main__':
  main()
