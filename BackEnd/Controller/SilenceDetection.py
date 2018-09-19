
import shutil
import os

def silence_detect1():
    from pydub import AudioSegment, silence
    path = 'D:/New Research/SmartInterviewer-Code/BackEnd/Database/Audio'
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    oldest = files[0]
    print(oldest)
    path1 = path + '/' + oldest
    print(path1)
    myaudio = intro = AudioSegment.from_wav(path1)  # 'audio/output14.wav'

    silence = silence.detect_silence(myaudio, min_silence_len=1000, silence_thresh=-60)
    # start and the end point of silence and display number of silent part in brackets
    # convert to sec
    silence = [((start / 1000), (stop / 1000)) for start, stop in silence]
    # Start and end points of silence parts in milliseconds
    print(silence)
    # Gap between start and the end point of the each silent part of the audio
    silence_gap = [(((stop) - (start)) / 1000) for start, stop in silence]
    # Silence gaps display in list
    print(silence_gap)
    # identify silence parts with more than 5 milliseconds
    silence_gap2 = sorted(i for i in silence_gap if i >= 0.005)
    print(silence_gap2)

    silence_gap_list = [i * 1000 for i in silence_gap2]
    # silence gaps with three decimal places
    myFormattedList2 = ['%.3f' % elem for elem in silence_gap_list]
    print(myFormattedList2)
    # Number of silence gaps with morethan 5 milliseconds
    print(len(myFormattedList2))

#After detecting the silence part of the audio clip it willmove to another folder vikum shold get the audio clip from that new folder.
    # path2 = 'D:/New Research/SmartInterviewer-Code/BackEnd/Database/movedAudio'
    # shutil.move(path1, path2)

