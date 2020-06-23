from datetime import datetime
def solution(m, musicinfos):
    answer = None
    def tone_change(m):
        m = m.replace('C#', 'H')
        m = m.replace('D#', 'I')
        m = m.replace('F#', 'J')
        m = m.replace('G#', 'K')
        m = m.replace('A#', 'L')
        return m

    m = tone_change(m)
    my_dict = {}

    for info in musicinfos:
        info_list = info.split(',')
        start = datetime.strptime(info_list[0],'%H:%M')
        end = datetime.strptime(info_list[1],'%H:%M')
        title = info_list[2]
        tones = tone_change(info_list[3])

        music_length = (end - start).seconds//60
        tone_actuality = (music_length//len(tones))*tones + tones[0:music_length%len(tones)]

        my_dict[tone_actuality] = title

        for song in my_dict.keys():
            if m in song:
                if answer == None:
                    answer = song
                else:
                    if len(answer) < len(song):
                        answer = song

    if answer == None:
        return "(None)"
    else :
        return my_dict[answer]