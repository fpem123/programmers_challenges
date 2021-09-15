def timeCalc(start, end): 
    shour, smin = map(int, start.split(":"))
    ehour, emin = map(int, end.split(":"))
    
    start = shour * 60 + smin
    end = ehour * 60 + emin
    
    return end - start
    
def soundTransform(soundmap, sound):
    for before, after in soundmap.items():
        sound = sound.replace(before, after)
    
    return sound
    
def getSong(time, sound):
    n, r = divmod(time, len(sound))
    
    return sound * n + sound[:r]
    

def solution(m, musicinfos):
    answer = '(None)'
    longestTime = 0
    soundmap = {'A#': '0',
                'B#': '1',
                'C#': '2',
                'D#': '3',
                'E#': '4',
                'F#': '5',
                'G#': '6'}
    m = soundTransform(soundmap, m)
    
    for musicinfo in musicinfos:
        start, end, name, sound = musicinfo.split(",")
        playTime = timeCalc(start, end)
        sound = soundTransform(soundmap, sound)
        sound = getSong(playTime, sound)
        
        if m in sound and playTime > longestTime:
            answer = name
            longestTime = playTime
        
    return answer