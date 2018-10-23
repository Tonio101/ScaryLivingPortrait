# ScaryLivingPortrait
RaspberryPi Halloween Project

## Parts needed:
- Raspberry Pi 2|3
- Raspberry Pi Camera module v2|v3
- Unliving portrait video(s): [AtmostFX] (https://atmosfx.com/collections/halloween/products/unliving-portraits)
- Spare TV or monitor
- Picture Frame (I created mine using wall molding)
- Speaker(s)
- Good ventilation on the CPUs of the Raspberry Pi

## Prereqs
I'm not going go over how to configure all the prereqs. There is
plenty of documentation out there to show you the way.
- Raspberry Pi version 2 or 3 running the latest Raspbian.
- OpenCV 3.4.3 (Any version should be ok).
- Python3.
- Omxplayer is pre-installed on Raspbian 9.4. (Stretch).
- Omxplayer-wrapper python library.
```bash
  sudo python3 -m pip install omxplayer-wrapper
```
<!-- TODO Insert Link for tutorial -->

You should now have everything you need to run the script.

### Scary Portrait Video:
Stitched up 3 different videos so that you can alternate between different
characters.
Video file: raspberrypi_halloween_video.mp4 (not included)
Total length = 3:25 min

Man:
Total Time: 0:00 -> 1:09
Initial scene: 0:00
Scene 1: 0:03 -> 0:13
Scene 2: 0:14 -> 0:36
Scene 3: 0:37 -> 0:56
Scene 4: 0:57 -> 1:09

Woman:
Total Time: 1:11 -> 2:09
Initial scene: 1:11
Scene 1: 1:11 -> 1:28
Scene 2: 1:28 -> 1:41
Scene 3: 1:41 -> 1:55
Scene 4: 1:56 -> 2:08

Girl:
Total Time: 2:10 -> 3:15
Initial scene: 2:10
Scene 1: 2:10 -> 2:37
Scene 2: 2:37 -> 2:51
Scene 3: 2:51 -> 3:01
Scene 4: 3:01 -> 3:12

The Result:
Essentially, it will iterate through all 3 videos in which
each video clip has 4 different scenes.
Take a look at the finish product.
[![Imgur](https://i.imgur.com/enEWNMx.png)](https://youtu.be/Ghp6V88iJZM)
