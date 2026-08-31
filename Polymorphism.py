class AudioFile:
    def play(self):
        return "Playing MP3 stream..."
class VideoFile:
    def play(self):
        return "Rendering MP4 frames..."
# A single interface handling different types
def media_player(media_object): # media_player is a generic function.It accepts any object passed into it as the parameter media_object.
    print(media_object.play())
media_player(AudioFile())  
media_player(VideoFile())  

#Summary of Benefits
# This design uses a concept called Duck Typing ("If it walks like a duck and quacks like a duck, it's a duck"). 
# It allows you to expand your code easily. If you later add a GIFFile() or StreamLink() class, you will not need to change the media_player function at all. 
# You only need to ensure the new classes have a .play() method.
