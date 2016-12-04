# blender-espeak

text to speech audio strip creator for blender (last used on blender v2.78)

reads a text file containing a very simple format for text to speech

```
50 hey what's up dude?
100 is this working?
150 i need to know!
```

the script depends on eSpeak:

http://espeak.sourceforge.net/

when run, the script will generate wav files first using the espeak command line interface, and then create the audio strips for you
