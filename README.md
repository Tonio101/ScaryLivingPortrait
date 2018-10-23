# ScaryLivingPortrait
RaspberryPi Halloween Project<br/>

## Parts needed:
- Raspberry Pi 2|3<br/>
- Raspberry Pi Camera module v2|v3<br/>
- Unliving portrait video(s): [AtmostFX]: https://atmosfx.com/collections/halloween/products/unliving-portraits<br/>
- Spare TV or monitor<br/>
- Picture Frame (I created mine using wall molding)<br/>
- Speaker(s)<br/>
- Good ventilation on the CPUs of the Raspberry Pi<br/>

## Prereqs
I'm not going go over how to configure all the prereqs. There is<br/>
plenty of documentation out there to show you the way.<br/>
- Raspberry Pi version 2 or 3 running the latest Raspbian.<br/>
- OpenCV 3.4.3 (Any version should be ok).<br/>
- Python3.<br/>
- Omxplayer is pre-installed on Raspbian 9.4. (Stretch).<br/>
- Omxplayer-wrapper python library.<br/>
```bash
  sudo python3 -m pip install omxplayer-wrapper
```
<!-- TODO Insert Link for tutorial -->

You should now have everything you need to run the script.<br/>

### Scary Portrait Video:
Stitched up 3 different videos so that you can alternate between different<br/>
characters.<br/>
Video file: raspberrypi_halloween_video.mp4 (not included)<br/>
Total length = 3:25 min<br/>

Man:<br/>
Total Time: 0:00 -> 1:09<br/>
Initial scene: 0:00<br/>
Scene 1: 0:03 -> 0:13<br/>
Scene 2: 0:14 -> 0:36<br/>
Scene 3: 0:37 -> 0:56<br/>
Scene 4: 0:57 -> 1:09<br/>

Woman:<br/>
Total Time: 1:11 -> 2:09<br/>
Initial scene: 1:11<br/>
Scene 1: 1:11 -> 1:28<br/>
Scene 2: 1:28 -> 1:41<br/>
Scene 3: 1:41 -> 1:55<br/>
Scene 4: 1:56 -> 2:08<br/>

Girl:<br/>
Total Time: 2:10 -> 3:15<br/>
Initial scene: 2:10<br/>
Scene 1: 2:10 -> 2:37<br/>
Scene 2: 2:37 -> 2:51<br/>
Scene 3: 2:51 -> 3:01<br/>
Scene 4: 3:01 -> 3:12<br/>

The Result:<br/>
Essentially, it will iterate through all 3 videos in which<br/>
each video clip has 4 different scenes.<br/>
Take a look at the video here:<br/>
[![Imgur](https://i.imgur.com/enEWNMx.png)](https://youtu.be/Ghp6V88iJZM)
