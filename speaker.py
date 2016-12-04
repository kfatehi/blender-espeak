import subprocess
from os import path
import re
import bpy


class Speaker():
    def __init__(self):
        here = bpy.path.abspath("//")
        self.ESPEAK = path.join(here, 'eSpeak','command_line','espeak.exe')
        self.WAV_DIR = path.join(here, 'speech-clips')
        
        subPattern = re.compile("^(\d+) (.+)$")
        self.SPEECH_LIST = []
        rawSubs = bpy.data.texts['speech.txt'].as_string()
        for line in rawSubs.split("\n"):
            try:
                (start, txt) = re.search(subPattern, line).groups()
                item = (int(start), self.gen(start, txt))
                self.SPEECH_LIST.append(item)        
                print(item)
            except AttributeError:
                pass

    def getWav(self, id):
        return path.join(self.WAV_DIR, str(id)+'.wav')        

    def gen(self, id, text):
        wav = self.getWav(id)
        subprocess.run([self.ESPEAK, '-w', wav, text])
        print("generated "+wav)
        return wav

    def getSpeechList(self):
        return self.SPEECH_LIST
    
    def addStripsToChannel(self, ch):
        scene = bpy.data.scenes['Scene']
        seqs = scene.sequence_editor.sequences
        for (start, wav) in self.getSpeechList():
            name = "spk"+str(start)
            strip = seqs.new_sound(name, wav, ch, start)

Speaker().addStripsToChannel(4)