from xml.etree.ElementTree import *
import os
from moviepy.editor import VideoFileClip

def videoclipitem(video, timein, timeout, start, end, videoend, linknumber, current_path):
    clipitem = Element('clipitem')
    name = Element('name')
    name.text= video
    clipitem.append(name)
    enabled = Element('enabled')
    enabled.text= 'true'
    clipitem.append(enabled)
    rate = Element('rate')
    clipitem.append(rate)
    timebase = Element('timebase')
    timebase.text= '60'
    rate.append(timebase) 
    ntsc = Element('ntsc')
    ntsc.text= 'false'
    rate.append(ntsc)
    tin = Element('in')
    tin.text= timein
    clipitem.append(tin)
    tout = Element('out')
    tout.text= timeout
    clipitem.append(tout)
    st = Element('start')
    st.text= start
    clipitem.append(st)
    en = Element('end')
    en.text= end
    clipitem.append(en)
    file = Element('file')
    file.attrib['id']= video
    clipitem.append(file)

    name = Element('name')
    name.text= video
    file.append(name)
    pathurl = Element('pathurl')
    pathurl.text= current_path+"\\"+"inputvideo"+"\\"+video
    file.append(pathurl)
    media = Element('media')
    file.append(media)
    vi = Element('video')
    media.append(vi)
    samplecharacteristics = Element('samplecharacteristics')
    vi.append(samplecharacteristics)
    width = Element('width')
    width.text= '1920'
    samplecharacteristics.append(width)
    height = Element('height')
    height.text= '1080'
    samplecharacteristics.append(height)    
    anamorphic = Element('anamorphic')
    anamorphic.text= 'true'
    samplecharacteristics.append(anamorphic)    
    pixelaspectratio = Element('pixelaspectratio')
    pixelaspectratio.text= 'square'
    samplecharacteristics.append(pixelaspectratio)    
    fielddominance = Element('fielddominance')
    fielddominance.text= 'square'
    samplecharacteristics.append(fielddominance)    

    audio = Element('audio')
    media.append(audio)
    tin = Element('in')
    tin.text='0'
    audio.append(tin)
    tout = Element('out')
    tout.text=videoend
    audio.append(tout)  
    channelcount = Element('channelcount')
    channelcount.text='2'
    audio.append(channelcount)  
    duration = Element('duration')
    duration.text=videoend
    audio.append(duration)  

    link1 = Element('link')
    clipitem.append(link1)
    mediatype = Element('mediatype')
    mediatype.text='video'
    link1.append(mediatype)   
    trackindex = Element('trackindex')
    trackindex.text='1'
    link1.append(trackindex)   
    clipindex = Element('clipindex')
    clipindex.text=linknumber
    link1.append(clipindex)   

    link2 = Element('link')
    clipitem.append(link2)
    mediatype = Element('mediatype')
    mediatype.text='audio'
    link2.append(mediatype)   
    trackindex = Element('trackindex')
    trackindex.text='1'
    link2.append(trackindex)   
    clipindex = Element('clipindex')
    clipindex.text=linknumber
    link2.append(clipindex)
    groupindex = Element('groupindex')
    groupindex.text=linknumber
    link2.append(groupindex)

    link3 = Element('link')
    clipitem.append(link3)
    mediatype = Element('mediatype')
    mediatype.text='audio'
    link3.append(mediatype)   
    trackindex = Element('trackindex')
    trackindex.text='2'
    link3.append(trackindex)   
    clipindex = Element('clipindex')
    clipindex.text=linknumber
    link3.append(clipindex)
    groupindex = Element('groupindex')
    groupindex.text=linknumber
    link3.append(groupindex)

    return clipitem
def audioclipitem1(video, timein, timeout, start, end):
    clipitem = Element('clipitem')
    clipitem = Element('clipitem')
    name = Element('name')
    name.text= video
    clipitem.append(name)
    enabled = Element('enabled')
    enabled.text= 'true'
    clipitem.append(enabled)
    tin = Element('in')
    tin.text= timein
    clipitem.append(tin)
    tout = Element('out')
    tout.text= timeout
    clipitem.append(tout)
    st = Element('start')
    st.text= start
    clipitem.append(st)
    en = Element('end')
    en.text= end
    clipitem.append(en)
    file = Element('file')
    file.attrib['id']= video
    clipitem.append(file)
    sourcetrack = Element('sourcetrack')
    clipitem.append(sourcetrack)
    mediatype = Element('mediatype')
    mediatype.text='audio'
    sourcetrack.append(mediatype)
    trackindex = Element('trackindex')
    trackindex.text='1'
    sourcetrack.append(trackindex)
    return clipitem
def audioclipitem2(video, timein, timeout, start, end):
    clipitem = Element('clipitem')
    clipitem = Element('clipitem')
    name = Element('name')
    name.text= video
    clipitem.append(name)
    enabled = Element('enabled')
    enabled.text= 'true'
    clipitem.append(enabled)
    tin = Element('in')
    tin.text= timein
    clipitem.append(tin)
    tout = Element('out')
    tout.text= timeout
    clipitem.append(tout)
    st = Element('start')
    st.text= start
    clipitem.append(st)
    en = Element('end')
    en.text= end
    clipitem.append(en)
    file = Element('file')
    file.attrib['id']= video
    clipitem.append(file)
    sourcetrack = Element('sourcetrack')
    clipitem.append(sourcetrack)
    mediatype = Element('mediatype')
    mediatype.text='audio'
    sourcetrack.append(mediatype)
    trackindex = Element('trackindex')
    trackindex.text='2'
    sourcetrack.append(trackindex)
    return clipitem
def videotransitionitem(centerframe, duration):
    transition = Element('transitionitem')
    start = Element('start')
    start.text=str(centerframe-duration)
    transition.append(start)
    end = Element('end')
    end.text=str(centerframe+duration)
    transition.append(end)
    alignment = Element('alignment')
    alignment.text='center'
    transition.append(alignment)
    rate = Element('rate')
    transition.append(rate)
    timebase = Element('timebase')
    timebase.text='60'
    rate.append(timebase)
    ntsc = Element('ntsc')
    ntsc.text='FALSE'
    rate.append(ntsc)  
    effect = Element('effect')
    transition.append(effect)
    name = Element('name')
    name.text='Cross Dissolve'
    effect.append(name)
    effectid = Element('effectid')
    effectid.text='Cross Dissolve'
    effect.append(effectid)
    effectcategory = Element('effectcategory')
    effectcategory.text='Dissolve'
    effect.append(effectcategory)    
    effecttype = Element('effecttype')
    effecttype.text='transition'
    effect.append(effecttype)
    mediatype = Element('mediatype')
    mediatype.text='video'
    effect.append(mediatype)
    wipecode = Element('wipecode')
    wipecode.text='0'
    effect.append(wipecode)
    wipeaccuracy = Element('wipeaccuracy')
    wipeaccuracy.text='100'
    effect.append(wipeaccuracy)
    startratio = Element('startratio')
    startratio.text='0'
    effect.append(startratio)
    endratio = Element('endratio')
    endratio.text='1'
    effect.append(endratio)
    reverse = Element('reverse')
    reverse.text='FALSE'
    effect.append(reverse)
    return transition
def audiotransitionitem(centerframe, duration):
    transition = Element('transitionitem')
    start = Element('start')
    start.text=str(centerframe-duration)
    transition.append(start)
    end = Element('end')
    end.text=str(centerframe+duration)
    transition.append(end)
    alignment = Element('alignment')
    alignment.text='center'
    transition.append(alignment)
    rate = Element('rate')
    transition.append(rate)
    timebase = Element('timebase')
    timebase.text='60'
    rate.append(timebase)
    ntsc = Element('ntsc')
    ntsc.text='FALSE'
    rate.append(ntsc)  
    effect = Element('effect')
    transition.append(effect)
    name = Element('name')
    name.text='Cross Fade (+3dB)'
    effect.append(name)
    effectid = Element('effectid')
    effectid.text='KGAudioTransCrossFade3dB'
    effect.append(effectid)
    effecttype = Element('effecttype')
    effecttype.text='transition'
    effect.append(effecttype)
    mediatype = Element('mediatype')
    mediatype.text='audio'
    effect.append(mediatype)
    wipecode = Element('wipecode')
    wipecode.text='0'
    effect.append(wipecode)
    wipeaccuracy = Element('wipeaccuracy')
    wipeaccuracy.text='100'
    effect.append(wipeaccuracy)
    startratio = Element('startratio')
    startratio.text='0'
    effect.append(startratio)
    endratio = Element('endratio')
    endratio.text='1'
    effect.append(endratio)
    reverse = Element('reverse')
    reverse.text='FALSE'
    effect.append(reverse)
    return transition
def run_tree(
    current_path,
    video_list,
    fr,
    start_index_frame,
    end_index_frame
    ):
    for i in range(len(video_list)):
        videopy = VideoFileClip(current_path + "/inputvideo/" + video_list[i])
        total_duration = videopy.end * fr

        xmeml = Element('xmeml')
        xmeml.attrib['version']='5'

        sequence = Element('sequence')
        sequence.attrib['id']="video"
        xmeml.append(sequence)

        name = Element('name')
        name.text=video_list[i].rstrip('.mp4')
        sequence.append(name)
        duration = Element('duration')
        duration.text=str(total_duration)
        sequence.append(duration)
        rate = Element('rate')
        sequence.append(rate)
        
        timebase = Element('timebase')
        timebase.text='60'
        rate.append(timebase)
        ntsc = Element('ntsc')
        ntsc.text='false'
        rate.append(ntsc)

        media = Element('media')
        sequence.append(media)

        video = Element('video')
        media.append(video)

        format = Element('format')
        video.append(format)

        samplecharacteristics = Element('samplecharacteristics')
        format.append(samplecharacteristics)

        width = Element('width')
        width.text='1920'
        samplecharacteristics.append(width)
        height = Element('height')
        height.text='1080'
        samplecharacteristics.append(height)
        anamorphic = Element('anamorphic')
        anamorphic.text='false'
        samplecharacteristics.append(anamorphic)
        pixelaspectratio = Element('pixelaspectratio')
        pixelaspectratio.text='square'
        samplecharacteristics.append(pixelaspectratio)
        fielddominance = Element('fielddominance')
        fielddominance.text='none'
        samplecharacteristics.append(fielddominance)

        track1 = Element('track')
        video.append(track1)
        trackpng = Element('track')
        video.append(trackpng)

        audio = Element('audio')
        media.append(audio)
        inn = Element('in')
        inn.text='0'
        audio.append(inn)
        o = Element('out')
        o.text=str(total_duration)
        audio.append(o)
        channelcount = Element('channelcount')
        channelcount.text='2'
        audio.append(channelcount)
        duration = Element('duration')
        duration.text=str(total_duration)
        audio.append(duration)  
        track2 = Element('track')
        track2.attrib['MZ.TrackTargeted']="0"
        audio.append(track2)
        track3 = Element('track')
        track3.attrib['MZ.TrackTargeted']="0"
        audio.append(track3)    

        start = 0
        end = end_index_frame[i][0] - start_index_frame[i][0]
        for j in range(len(start_index_frame[i])):
            clip1 = videoclipitem(
                video_list[i], 
                str(start_index_frame[i][j]), 
                str(end_index_frame[i][j]), 
                str(start), 
                str(end), 
                str(total_duration), 
                str(j),
                current_path
                )
            track1.append(clip1)

            clip2 = audioclipitem1(
                video_list[i],
                str(start_index_frame[i][j]), 
                str(end_index_frame[i][j]), 
                str(start), 
                str(end)
            )
            track2.append(clip2)

            clip3 = audioclipitem2(
                video_list[i],
                str(start_index_frame[i][j]), 
                str(end_index_frame[i][j]), 
                str(start), 
                str(end)
            )
            track3.append(clip3)

            if j==len(start_index_frame[i]) - 1:
                break
            else:
                start = end
                end = start + end_index_frame[i][j+1] - start_index_frame[i][j+1]

        clippng = videoclipitem(
            video_list[i], 
            '0', 
            '600', 
            '0', 
            '600', 
            str(total_duration), 
            '0',
            current_path
            )
        trackpng.append(clippng)

        tree = ElementTree(xmeml)
        fileName = current_path+"/inputvideo/xmlcache/"+ video_list[i].rstrip('.mp4')+".xml"
        with open(fileName, "wb") as file:
            tree.write(file, encoding='utf-8', xml_declaration=True)
def run_dissolve_all(
    current_path,
    video_list,
    fr,
    start_index_frame,
    end_index_frame,
    video_dissolve_duration,
    audio_dissolve_duration
    ):
    for i in range(len(video_list)):
        videopy = VideoFileClip(current_path + "/inputvideo/" + video_list[i])
        total_duration = videopy.end * fr

        xmeml = Element('xmeml')
        xmeml.attrib['version']='5'

        sequence = Element('sequence')
        sequence.attrib['id']="video"
        xmeml.append(sequence)

        name = Element('name')
        name.text=video_list[i].rstrip('.mp4')
        sequence.append(name)
        duration = Element('duration')
        duration.text=str(total_duration)
        sequence.append(duration)
        rate = Element('rate')
        sequence.append(rate)
        
        timebase = Element('timebase')
        timebase.text='60'
        rate.append(timebase)
        ntsc = Element('ntsc')
        ntsc.text='false'
        rate.append(ntsc)

        media = Element('media')
        sequence.append(media)

        video = Element('video')
        media.append(video)

        format = Element('format')
        video.append(format)

        samplecharacteristics = Element('samplecharacteristics')
        format.append(samplecharacteristics)

        width = Element('width')
        width.text='1920'
        samplecharacteristics.append(width)
        height = Element('height')
        height.text='1080'
        samplecharacteristics.append(height)
        anamorphic = Element('anamorphic')
        anamorphic.text='false'
        samplecharacteristics.append(anamorphic)
        pixelaspectratio = Element('pixelaspectratio')
        pixelaspectratio.text='square'
        samplecharacteristics.append(pixelaspectratio)
        fielddominance = Element('fielddominance')
        fielddominance.text='none'
        samplecharacteristics.append(fielddominance)

        track1 = Element('track')
        video.append(track1)

        audio = Element('audio')
        media.append(audio)
        inn = Element('in')
        inn.text='0'
        audio.append(inn)
        o = Element('out')
        o.text=str(total_duration)
        audio.append(o)
        channelcount = Element('channelcount')
        channelcount.text='2'
        audio.append(channelcount)
        duration = Element('duration')
        duration.text=str(total_duration)
        audio.append(duration)  
        track2 = Element('track')
        audio.append(track2)
        track3 = Element('track')
        audio.append(track3)    

        start = []
        end =[]
        start.append(0)
        end.append(start[0] + end_index_frame[i][0] - start_index_frame[i][0])
        for j in range(len(start_index_frame[i])-1):
            start.append(end[j])
            end.append(start[j+1] + end_index_frame[i][j+1] - start_index_frame[i][j+1])

        print(start)
        print(end)

        clip1 = videoclipitem(
            video_list[i], 
            str(start_index_frame[i][0]), 
            str(end_index_frame[i][0]+video_dissolve_duration), 
            str(start[0]), 
            '-1', 
            str(total_duration), 
            str(0),
            current_path
            )
        track1.append(clip1)
        clip1 = videotransitionitem(end[0], video_dissolve_duration)
        track1.append(clip1)
        clip2 = audioclipitem1(
            video_list[i],
            str(start_index_frame[i][0]), 
            str(end_index_frame[i][0]+audio_dissolve_duration), 
            str(start[0]), 
            '-1'
        )
        track2.append(clip2)
        clip2 = audiotransitionitem(end[0], audio_dissolve_duration)
        track2.append(clip2)
        clip3 = audioclipitem2(
            video_list[i],
            str(start_index_frame[i][0]), 
            str(end_index_frame[i][0]+audio_dissolve_duration), 
            str(start[0]), 
            '-1'
        )
        track3.append(clip3)
        clip3 = audiotransitionitem(end[0], audio_dissolve_duration)
        track3.append(clip3)
        for j in range(1, len(start_index_frame[i])-1):
            clip1 = videoclipitem(
                video_list[i], 
                str(start_index_frame[i][j]-video_dissolve_duration), 
                str(end_index_frame[i][j]+video_dissolve_duration), 
                '-1', 
                '-1', 
                str(total_duration), 
                str(j),
                current_path
                )
            track1.append(clip1)

            clip1 = videotransitionitem(end[j], video_dissolve_duration)
            track1.append(clip1)

            clip1 = videoclipitem(
                video_list[i], 
                str(start_index_frame[i][j+1]-video_dissolve_duration), 
                str(end_index_frame[i][j+1]+video_dissolve_duration), 
                '-1', 
                '-1', 
                str(total_duration), 
                str(j),
                current_path
                )
            track1.append(clip1)

            clip2 = audioclipitem1(
                video_list[i],
                str(start_index_frame[i][j]-audio_dissolve_duration), 
                str(end_index_frame[i][j]+audio_dissolve_duration), 
                '-1', 
                '-1'
            )
            track2.append(clip2)

            clip2 = audiotransitionitem(end[j], audio_dissolve_duration)
            track2.append(clip2)

            clip2 = audioclipitem1(
                video_list[i],
                str(start_index_frame[i][j+1]-audio_dissolve_duration), 
                str(end_index_frame[i][j+1]+audio_dissolve_duration), 
                '-1', 
                '-1'
            )
            track2.append(clip2)

            clip3 = audioclipitem2(
                video_list[i],
                str(start_index_frame[i][j]-audio_dissolve_duration), 
                str(end_index_frame[i][j]+audio_dissolve_duration), 
                '-1', 
                '-1'
            )
            track3.append(clip3)

            clip3 = audiotransitionitem(end[j], audio_dissolve_duration)
            track3.append(clip3)

            clip3 = audioclipitem2(
                video_list[i],
                str(start_index_frame[i][j+1]-audio_dissolve_duration), 
                str(end_index_frame[i][j+1]+audio_dissolve_duration), 
                '-1', 
                '-1'
            )
            track3.append(clip3)
        clip1 = videotransitionitem(start[len(start)-1], video_dissolve_duration)
        track1.append(clip1)
        clip1 = videoclipitem(
            video_list[i], 
            str(start_index_frame[i][len(start)-1]-video_dissolve_duration), 
            str(end_index_frame[i][len(start)-1]), 
            '-1', 
            str(end[len(start)-1]), 
            str(total_duration), 
            str(0),
            current_path
            )
        track1.append(clip1)
        clip2 = audiotransitionitem(start[len(start)-1], audio_dissolve_duration)
        track2.append(clip2)
        clip2 = audioclipitem1(
            video_list[i],
            str(start_index_frame[i][len(start)-1]-audio_dissolve_duration), 
            str(end_index_frame[i][len(start)-1]), 
            '-1', 
            str(end[len(start)-1]), 
        )
        track2.append(clip2)
        clip3 = audiotransitionitem(start[len(start)-1], audio_dissolve_duration)
        track3.append(clip3)
        clip3 = audioclipitem2(
            video_list[i],
            str(start_index_frame[i][len(start)-1]-audio_dissolve_duration), 
            str(end_index_frame[i][len(start)-1]), 
            '-1', 
            str(end[len(start)-1]), 
        )
        track3.append(clip3)

        tree = ElementTree(xmeml)
        fileName = current_path+"/inputvideo/xmlcache/"+ video_list[i].rstrip('mp4')+".xml"
        with open(fileName, "wb") as file:
            tree.write(file, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    current_path = os.path.join(current_path, os.pardir)
    print(current_path)
    video_list = os.listdir(current_path + "/inputvideo/")
    video_list = [file for file in video_list if file.endswith(".mp4")]
    fr = 60
    start_index_frame = [[100, 200], [150, 300, 450]]
    end_index_frame = [[150, 250], [200, 400, 700]]
    run_tree(
        current_path,
        video_list,
        fr,
        start_index_frame,
        end_index_frame
        )