from xml.etree.ElementTree import *
import os
import sys
from moviepy.editor import VideoFileClip
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pysrc.user_discrimination import who
import random

def videoclipitem(video, timein, timeout, start, end, videoend, linknumber, videopath):
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
    pathurl.text= videopath
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

def questclipitem(image,video, timein, timeout, start, end,current_path):
    clipitem = Element('clipitem')
    name = Element('name')
    name.text= image
    clipitem.append(name)
    enabled = Element('enabled')
    enabled.text= 'true'
    clipitem.append(enabled)
    questduration = Element('duration')
    questduration.text='36000'
    clipitem.append(questduration)
    rate = Element('rate')
    clipitem.append(rate)
    timebase = Element('timebase')
    timebase.text= '30'
    rate.append(timebase) 
    ntsc = Element('ntsc')
    ntsc.text= 'true'
    rate.append(ntsc)
    tin = Element('in')
    tin.text= timein
    clipitem.append(tin)
    tout = Element('out')
    alphatype = Element('alphatype')
    alphatype.text= 'straight'
    clipitem.append(alphatype)
    tout.text= timeout
    clipitem.append(tout)
    st = Element('start')
    st.text= start
    clipitem.append(st)
    en = Element('end')
    en.text= end
    clipitem.append(en)
    file = Element('file')
    file.attrib['id']= image
    clipitem.append(file)

    name = Element('name')
    name.text= image
    file.append(name)
    pathurl = Element('pathurl')
    pathurl.text= current_path+"\\"+r"pysrc\image_src"+"\\"+video[:-4]+'_quest.png'
    file.append(pathurl)
    media = Element('media')
    file.append(media)
    vi = Element('video')
    media.append(vi)
    samplecharacteristics = Element('samplecharacteristics')
    vi.append(samplecharacteristics)
    width = Element('width')
    width.text= '450'
    samplecharacteristics.append(width)
    height = Element('height')
    height.text= '800'
    samplecharacteristics.append(height)    
    anamorphic = Element('anamorphic')
    anamorphic.text= 'false'
    samplecharacteristics.append(anamorphic)    
    pixelaspectratio = Element('pixelaspectratio')
    pixelaspectratio.text= 'square'
    samplecharacteristics.append(pixelaspectratio)    
    fielddominance = Element('fielddominance')
    fielddominance.text= 'none'
    samplecharacteristics.append(fielddominance)    

    filter = Element('filter')
    clipitem.append(filter)
    effect = Element('effect')
    filter.append(effect)
    filtername = Element('name')
    filtername.text= 'Basic Motion'
    effect.append(filtername)    
    effectid = Element('effectid')
    effectid.text= 'basic'
    effect.append(effectid)    
    effectcategory = Element('effectcategory')
    effectcategory.text= 'motion'
    effect.append(effectcategory)    
    effecttype = Element('effecttype')
    effecttype.text= 'motion'
    effect.append(effecttype)    
    mediatype = Element('mediatype')
    mediatype.text= 'video'
    effect.append(mediatype)    
    pproBypass = Element('pproBypass')
    pproBypass.text= 'false'
    effect.append(pproBypass)    

    parameter = Element('parameter')
    parameter.attrib['authoringApp']= "PremierePro"
    effect.append(parameter)
    parameterid = Element('parameterid')
    parameterid.text= 'center'
    parameter.append(parameterid)    
    parametername = Element('name')
    parametername.text= 'Center'
    parameter.append(parametername)    
    value = Element('value')
    parameter.append(value)    
    horiz = Element('horiz')
    horiz.text= '1.65'
    value.append(horiz)   
    vert = Element('vert')
    vert.text= '-0.07'
    value.append(vert)   
    
    parameter = Element('parameter')
    parameter.attrib['authoringApp']= "PremierePro"
    effect.append(parameter)
    parameterid = Element('parameterid')
    parameterid.text= 'rotation'
    parameter.append(parameterid)    
    valuemin = Element('valuemin')
    valuemin.text= '-8640'
    parameter.append(valuemin)        
    valuemax = Element('valuemax')
    valuemax.text= '8640'
    parameter.append(valuemax)   
    value = Element('value')
    value.text= '1'
    parameter.append(value)   

    return clipitem
def scrollclipitem(image,video, timein, timeout, start, end,current_path, img_path):
    clipitem = Element('clipitem')
    name = Element('name')
    name.text= image
    clipitem.append(name)
    enabled = Element('enabled')
    enabled.text= 'true'
    scrollduration = Element('duration')
    scrollduration.text='36000'
    clipitem.append(scrollduration)
    clipitem.append(enabled)
    rate = Element('rate')
    clipitem.append(rate)
    timebase = Element('timebase')
    timebase.text= '30'
    rate.append(timebase) 
    ntsc = Element('ntsc')
    ntsc.text= 'true'
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
    alphatype = Element('alphatype')
    alphatype.text= 'straight'
    clipitem.append(alphatype)
    file = Element('file')
    file.attrib['id']= image
    clipitem.append(file)

    name = Element('name')
    name.text= image
    file.append(name)
    pathurl = Element('pathurl')
    pathurl.text= img_path
    file.append(pathurl)
    media = Element('media')
    file.append(media)
    vi = Element('video')
    media.append(vi)
    samplecharacteristics = Element('samplecharacteristics')
    vi.append(samplecharacteristics)
    width = Element('width')
    width.text= '450'
    samplecharacteristics.append(width)
    height = Element('height')
    height.text= '800'
    samplecharacteristics.append(height)    
    anamorphic = Element('anamorphic')
    anamorphic.text= 'false'
    samplecharacteristics.append(anamorphic)    
    pixelaspectratio = Element('pixelaspectratio')
    pixelaspectratio.text= 'square'
    samplecharacteristics.append(pixelaspectratio)    
    fielddominance = Element('fielddominance')
    fielddominance.text= 'none'
    samplecharacteristics.append(fielddominance)    

    filter = Element('filter')
    clipitem.append(filter)
    effect = Element('effect')
    filter.append(effect)
    filtername = Element('name')
    filtername.text= 'Basic Motion'
    effect.append(filtername)    
    effectid = Element('effectid')
    effectid.text= 'basic'
    effect.append(effectid)    
    effectcategory = Element('effectcategory')
    effectcategory.text= 'motion'
    effect.append(effectcategory)    
    effecttype = Element('effecttype')
    effecttype.text= 'motion'
    effect.append(effecttype)    
    mediatype = Element('mediatype')
    mediatype.text= 'video'
    effect.append(mediatype)    
    pproBypass = Element('pproBypass')
    pproBypass.text= 'false'
    effect.append(pproBypass)    
    parameter = Element('parameter')
    parameter.attrib['authoringApp']= "PremierePro"
    effect.append(parameter)
    parameterid = Element('parameterid')
    parameterid.text= 'center'
    parameter.append(parameterid)    
    parametername = Element('name')
    parametername.text= 'Center'
    parameter.append(parametername)    
    value = Element('value')
    parameter.append(value)    
    horiz = Element('horiz')
    horiz.text= '1.65'
    value.append(horiz)   
    vert = Element('vert')
    vert.text= '-0.07'
    value.append(vert)   

    parameter = Element('parameter')
    parameter.attrib['authoringApp']= "PremierePro"
    effect.append(parameter)
    parameterid = Element('parameterid')
    parameterid.text= 'rotation'
    parameter.append(parameterid)    
    valuemin = Element('valuemin')
    valuemin.text= '-8640'
    parameter.append(valuemin)        
    valuemax = Element('valuemax')
    valuemax.text= '8640'
    parameter.append(valuemax)   
    value = Element('value')
    value.text= '1'
    parameter.append(value)   

    return clipitem
def hpclipitem(image, timein, timeout, start, end,current_path, user):
    clipitem = Element('clipitem')
    name = Element('name')
    name.text= image
    clipitem.append(name)
    enabled = Element('enabled')
    enabled.text= 'true'
    clipitem.append(enabled)
    questduration = Element('duration')
    questduration.text='36000'
    clipitem.append(questduration)
    rate = Element('rate')
    clipitem.append(rate)
    timebase = Element('timebase')
    timebase.text= '30'
    rate.append(timebase) 
    ntsc = Element('ntsc')
    ntsc.text= 'true'
    rate.append(ntsc)
    tin = Element('in')
    tin.text= timein
    clipitem.append(tin)
    tout = Element('out')
    alphatype = Element('alphatype')
    alphatype.text= 'straight'
    clipitem.append(alphatype)
    tout.text= timeout
    clipitem.append(tout)
    st = Element('start')
    st.text= start
    clipitem.append(st)
    en = Element('end')
    en.text= end
    clipitem.append(en)
    file = Element('file')
    file.attrib['id']= image
    clipitem.append(file)

    name = Element('name')
    name.text= image
    file.append(name)
    pathurl = Element('pathurl')
    if user == 'matsuri':
        pathurl.text= current_path+"\\"+r"pysrc\heropower\japan"+"\\"+image
    else:
        pathurl.text= current_path+"\\"+r"pysrc\heropower"+"\\"+image
    file.append(pathurl)
    media = Element('media')
    file.append(media)
    vi = Element('video')
    media.append(vi)
    samplecharacteristics = Element('samplecharacteristics')
    vi.append(samplecharacteristics)
    width = Element('width')
    width.text= '450'
    samplecharacteristics.append(width)
    height = Element('height')
    height.text= '800'
    samplecharacteristics.append(height)    
    anamorphic = Element('anamorphic')
    anamorphic.text= 'false'
    samplecharacteristics.append(anamorphic)    
    pixelaspectratio = Element('pixelaspectratio')
    pixelaspectratio.text= 'square'
    samplecharacteristics.append(pixelaspectratio)    
    fielddominance = Element('fielddominance')
    fielddominance.text= 'none'
    samplecharacteristics.append(fielddominance)    

    filter = Element('filter')
    clipitem.append(filter)
    effect = Element('effect')
    filter.append(effect)
    filtername = Element('name')
    filtername.text= 'Basic Motion'
    effect.append(filtername)    
    effectid = Element('effectid')
    effectid.text= 'basic'
    effect.append(effectid)    
    effectcategory = Element('effectcategory')
    effectcategory.text= 'motion'
    effect.append(effectcategory)    
    effecttype = Element('effecttype')
    effecttype.text= 'motion'
    effect.append(effecttype)    
    mediatype = Element('mediatype')
    mediatype.text= 'video'
    effect.append(mediatype)    
    pproBypass = Element('pproBypass')
    pproBypass.text= 'false'
    effect.append(pproBypass)    

    parameter = Element('parameter')
    parameter.attrib['authoringApp']= "PremierePro"
    effect.append(parameter)
    parameterid = Element('parameterid')
    parameterid.text= 'center'
    parameter.append(parameterid)    
    parametername = Element('name')
    parametername.text= 'Center'
    parameter.append(parametername)    
    value = Element('value')
    parameter.append(value)    
    horiz = Element('horiz')
    horiz.text= '1.65'
    value.append(horiz)   
    vert = Element('vert')
    vert.text= '-0.07'
    value.append(vert)   
    
    parameter = Element('parameter')
    parameter.attrib['authoringApp']= "PremierePro"
    effect.append(parameter)
    parameterid = Element('parameterid')
    parameterid.text= 'rotation'
    parameter.append(parameterid)    
    valuemin = Element('valuemin')
    valuemin.text= '-8640'
    parameter.append(valuemin)        
    valuemax = Element('valuemax')
    valuemax.text= '8640'
    parameter.append(valuemax)   
    value = Element('value')
    value.text= '1'
    parameter.append(value)   

    return clipitem
def soundeffectclipitem(efsoundfile, timein, timeout, start, end, efsoundfile_path, length):
    clipitem = Element('clipitem')
    name = Element('name')
    name.text= efsoundfile
    clipitem.append(name)
    enabled = Element('enabled')
    enabled.text= 'true'
    clipitem.append(enabled)
    duration = Element('duration')
    duration.text= length
    clipitem.append(duration)
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
    file.attrib['id']= efsoundfile
    clipitem.append(file)
    name = Element('name')
    name.text= efsoundfile
    file.append(name)
    pathurl = Element('pathurl')
    pathurl.text= efsoundfile_path
    file.append(pathurl)
    rate2 = Element('rate')
    file.append(rate2)
    timebase = Element('timebase')
    timebase.text= '30'
    rate2.append(timebase)
    ntsc = Element('ntsc')
    ntsc.text= 'true'
    rate2.append(ntsc)
    duration2 = Element('duration')
    duration2.text= '29'
    file.append(duration2)
    timecode = Element('timecode')
    file.append(timecode)
    rate3 = Element('rate')
    timecode.append(rate3)
    timebase = Element('timebase')
    timebase.text= '30'
    rate3.append(timebase)
    ntsc = Element('ntsc')
    ntsc.text= 'true'
    rate3.append(ntsc)
    string = Element('string')
    string.text= '00;00;00;00'
    timecode.append(string)
    frame = Element('frame')
    frame.text= '0'
    timecode.append(frame)
    displayformat = Element('displayformat')
    displayformat.text= 'DF'
    timecode.append(displayformat)
    media = Element('media')
    file.append(media)
    audio = Element('audio')
    media.append(audio)
    samplecharacteristics = Element('samplecharacteristics')
    audio.append(samplecharacteristics)
    depth = Element('depth')
    depth.text= '16'
    samplecharacteristics.append(depth)
    samplerate = Element('samplerate')
    samplerate.text= '44100'
    samplecharacteristics.append(samplerate)
    channelcount = Element('channelcount')
    channelcount.text= '2'
    audio.append(channelcount)
    sourcetrack = Element('sourcetrack')
    clipitem.append(sourcetrack)
    mediatype = Element('mediatype')
    mediatype.text= 'audio'
    sourcetrack.append(mediatype)
    trackindex = Element('trackindex')
    trackindex.text= '1'
    sourcetrack.append(trackindex)

    return clipitem

def bgmclipitem(bgmsoundfile, timein, timeout, start, end, bgmsoundfile_path, length, tracknumber):
    clipitem = Element('clipitem')
    name = Element('name')
    name.text= bgmsoundfile
    clipitem.append(name)
    enabled = Element('enabled')
    enabled.text= 'true'
    clipitem.append(enabled)
    duration = Element('duration')
    duration.text= length
    clipitem.append(duration)
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
    file.attrib['id']= bgmsoundfile
    clipitem.append(file)
    name = Element('name')
    name.text= bgmsoundfile
    file.append(name)
    pathurl = Element('pathurl')
    pathurl.text= bgmsoundfile_path
    file.append(pathurl)
    rate2 = Element('rate')
    file.append(rate2)
    timebase = Element('timebase')
    timebase.text= '30'
    rate2.append(timebase)
    ntsc = Element('ntsc')
    ntsc.text= 'true'
    rate2.append(ntsc)
    duration2 = Element('duration')
    duration2.text= '29'
    file.append(duration2)
    timecode = Element('timecode')
    file.append(timecode)
    rate3 = Element('rate')
    timecode.append(rate3)
    timebase = Element('timebase')
    timebase.text= '30'
    rate3.append(timebase)
    ntsc = Element('ntsc')
    ntsc.text= 'true'
    rate3.append(ntsc)
    string = Element('string')
    string.text= '00;00;00;00'
    timecode.append(string)
    frame = Element('frame')
    frame.text= '0'
    timecode.append(frame)
    displayformat = Element('displayformat')
    displayformat.text= 'DF'
    timecode.append(displayformat)
    media = Element('media')
    file.append(media)
    audio = Element('audio')
    media.append(audio)
    samplecharacteristics = Element('samplecharacteristics')
    audio.append(samplecharacteristics)
    depth = Element('depth')
    depth.text= '16'
    samplecharacteristics.append(depth)
    samplerate = Element('samplerate')
    samplerate.text= '44100'
    samplecharacteristics.append(samplerate)
    channelcount = Element('channelcount')
    channelcount.text= '2'
    audio.append(channelcount)
    sourcetrack = Element('sourcetrack')
    clipitem.append(sourcetrack)
    mediatype = Element('mediatype')
    mediatype.text= 'audio'
    sourcetrack.append(mediatype)
    trackindex = Element('trackindex')
    trackindex.text= tracknumber
    sourcetrack.append(trackindex)

    return clipitem

def run_tree(
    current_path,
    video,
    fr,
    start_index_frame,
    end_index_frame,
    quest_start,
    quest_end,
    quest_bool,
    heropower
    ):
    videopy = VideoFileClip(current_path + "/inputvideo/" + video)
    total_duration = videopy.end * fr
    scroll_path = current_path+"\\"+r"pysrc\image_src"+"\\"+'scroll.png'
    hpbackup_path = current_path+"\\"+r"pysrc\image_src"+"\\"+'hpbackup.png'
    xmeml = Element('xmeml')
    xmeml.attrib['version']='5'

    sequence = Element('sequence')
    sequence.attrib['id']="video"
    xmeml.append(sequence)

    name = Element('name')
    name.text=video[:-4]
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

    videoe = Element('video')
    media.append(videoe)

    format = Element('format')
    videoe.append(format)

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
    videoe.append(track1)
    trackscroll = Element('track')
    videoe.append(trackscroll)
    trackquest = Element('track')
    videoe.append(trackquest)
    trackfrontscroll = Element('track')
    videoe.append(trackfrontscroll)

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
    trackefsound = Element('track')
    audio.append(trackefsound)

    start = 0
    end = end_index_frame[0] - start_index_frame[0]
    for j in range(len(start_index_frame)):
        clip1 = videoclipitem(
            video, 
            str(start_index_frame[j]), 
            str(end_index_frame[j]), 
            str(start), 
            str(end), 
            str(total_duration), 
            str(j),
            current_path+"\\"+"inputvideo"+"\\"+video
            )
        track1.append(clip1)

        clip2 = audioclipitem1(
            video,
            str(start_index_frame[j]), 
            str(end_index_frame[j]), 
            str(start), 
            str(end)
        )
        track2.append(clip2)

        clip3 = audioclipitem2(
            video,
            str(start_index_frame[j]), 
            str(end_index_frame[j]), 
            str(start), 
            str(end)
        )
        track3.append(clip3)

        if j==len(start_index_frame) - 1:
            break
        else:
            start = end
            end = start + end_index_frame[j+1] - start_index_frame[j+1]

    if quest_bool:
        clipscroll = scrollclipitem(
            'scroll.png',
            video, 
            str(quest_start), 
            str(quest_end), 
            str(quest_start), 
            str(quest_end), 
            current_path,
            scroll_path
            )
        trackscroll.append(clipscroll)
        clipquest = questclipitem(
            video[:-4]+'_quest_bgremoved.png',
            video, 
            str(quest_start), 
            str(quest_end), 
            str(quest_start), 
            str(quest_end), 
            current_path
            )
        trackquest.append(clipquest)
        soundeffect = soundeffectclipitem(
            'Hole_punch.mp3',
            '0',
            '60',
            str(quest_start),
            str(quest_start + 60),
            current_path + r'\pysrc\wav_src\Hole_punch.mp3',
            '60'
        )
        trackefsound.append(soundeffect)

    user = who(video)
    print('user: ' + user)
    if heropower:
        clipscroll = scrollclipitem(
            'hpbackup.png',
            video, 
            str(end_index_frame[0] - start_index_frame[0]+ 120), 
            str(end_index_frame[0] - start_index_frame[0] + end_index_frame[1] - start_index_frame[1]+ 120), 
            str(end_index_frame[0] - start_index_frame[0]+ 120), 
            str(end_index_frame[0] - start_index_frame[0] + end_index_frame[1] - start_index_frame[1]+ 120), 
            current_path,
            hpbackup_path
            )
        trackscroll.append(clipscroll)
        clipheropower = hpclipitem(
            heropower,
            str(end_index_frame[0] - start_index_frame[0]+ 120), 
            str(end_index_frame[0] - start_index_frame[0] + end_index_frame[1] - start_index_frame[1]+ 120), 
            str(end_index_frame[0] - start_index_frame[0]+ 120), 
            str(end_index_frame[0] - start_index_frame[0] + end_index_frame[1] - start_index_frame[1]+ 120), 
            current_path,
            user
            )
        trackquest.append(clipheropower)
        soundeffect = soundeffectclipitem(
            'huk.mp3',
            '0',
            '60',
            str(end_index_frame[0] - start_index_frame[0] + 115),
            str(end_index_frame[0] - start_index_frame[0] + 165),
            current_path + r'\pysrc\wav_src\huk.mp3',
            '60'
        )
        trackefsound.append(soundeffect)
    
    if user == 'matsuri':
        rand1_3 =  random.randint(1,3)
        print(rand1_3)
        outro_duration = 900
        outro_end = end + outro_duration
        outrovideo = 'matsuri_outro0'+ str(rand1_3) +'.mp4'
        print(outrovideo)
        outrovideo_path = os.path.join(current_path, 'pysrc')
        outrovideo_path = os.path.join(outrovideo_path, 'video_src')
        outrovideo_path = os.path.join(outrovideo_path, user)
        
        clip1 = videoclipitem(
            outrovideo, 
            str(0), 
            str(outro_duration), 
            str(end), 
            str(outro_end), 
            str(outro_end), 
            str(len(start_index_frame)),
            outrovideo_path + '\\' + outrovideo
            )
        track1.append(clip1)

        clip2 = audioclipitem1(
            outrovideo,
            str(0), 
            str(outro_duration), 
            str(end), 
            str(outro_end), 
        )
        track2.append(clip2)

        clip3 = audioclipitem2(
            outrovideo,
            str(0), 
            str(outro_duration), 
            str(end), 
            str(outro_end), 
        )
        track3.append(clip3)


    if user == 'beterbabbit':
        beterbabbit_bgm1 = bgmclipitem(
            'BETERBABBIT_BGM.mp3',
            str(0),
            str(end),
            str(0),
            str(end),
            current_path + r'\pysrc\wav_src\BETERBABBIT_BGM.mp3',
            str(106992),
            str(1)
        )
        beterbabbit_bgm2 = bgmclipitem(
            'BETERBABBIT_BGM.mp3',
            str(0),
            str(end),
            str(0),
            str(end),
            current_path + r'\pysrc\wav_src\BETERBABBIT_BGM.mp3',
            str(106992),
            str(2)
        )
        trackbgm1 = Element('track')
        audio.append(trackbgm1)
        trackbgm2 = Element('track')
        audio.append(trackbgm2)
        trackbgm1.append(beterbabbit_bgm1)
        trackbgm2.append(beterbabbit_bgm2)

    tree = ElementTree(xmeml)
    fileName = current_path+"/inputvideo/xmlcache/"+ video[:-4]+".xml"
    with open(fileName, "wb") as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)
def run_dissolve_all(
    current_path,
    video,
    fr,
    start_index_frame,
    end_index_frame,
    video_dissolve_duration,
    audio_dissolve_duration
    ):
    videopy = VideoFileClip(current_path + "/inputvideo/" + video)
    total_duration = videopy.end * fr

    xmeml = Element('xmeml')
    xmeml.attrib['version']='5'

    sequence = Element('sequence')
    sequence.attrib['id']="video"
    xmeml.append(sequence)

    name = Element('name')
    name.text=video[:-4]
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
    end.append(start[0] + end_index_frame[0] - start_index_frame[0])
    for j in range(len(start_index_frame)-1):
        start.append(end[j])
        end.append(start[j+1] + end_index_frame[j+1] - start_index_frame[j+1])

    print(start)
    print(end)

    clip1 = videoclipitem(
        video, 
        str(start_index_frame[0]), 
        str(end_index_frame[0]+video_dissolve_duration), 
        str(start[0]), 
        '-1', 
        str(total_duration), 
        str(0),
        current_path+"\\"+"inputvideo"+"\\"+video
        )
    track1.append(clip1)
    clip1 = videotransitionitem(end[0], video_dissolve_duration)
    track1.append(clip1)
    clip2 = audioclipitem1(
        video,
        str(start_index_frame[0]), 
        str(end_index_frame[0]+audio_dissolve_duration), 
        str(start[0]), 
        '-1'
    )
    track2.append(clip2)
    clip2 = audiotransitionitem(end[0], audio_dissolve_duration)
    track2.append(clip2)
    clip3 = audioclipitem2(
        video,
        str(start_index_frame[0]), 
        str(end_index_frame[0]+audio_dissolve_duration), 
        str(start[0]), 
        '-1'
    )
    track3.append(clip3)
    clip3 = audiotransitionitem(end[0], audio_dissolve_duration)
    track3.append(clip3)
    for j in range(1, len(start_index_frame)-1):
        clip1 = videoclipitem(
            video, 
            str(start_index_frame[j]-video_dissolve_duration), 
            str(end_index_frame[j]+video_dissolve_duration), 
            '-1', 
            '-1', 
            str(total_duration), 
            str(j),
            current_path+"\\"+"inputvideo"+"\\"+video
            )
        track1.append(clip1)

        clip1 = videotransitionitem(end[j], video_dissolve_duration)
        track1.append(clip1)

        clip1 = videoclipitem(
            video, 
            str(start_index_frame[j+1]-video_dissolve_duration), 
            str(end_index_frame[j+1]+video_dissolve_duration), 
            '-1', 
            '-1', 
            str(total_duration), 
            str(j),
            current_path+"\\"+"inputvideo"+"\\"+video
            )
        track1.append(clip1)

        clip2 = audioclipitem1(
            video,
            str(start_index_frame[j]-audio_dissolve_duration), 
            str(end_index_frame[j]+audio_dissolve_duration), 
            '-1', 
            '-1'
        )
        track2.append(clip2)

        clip2 = audiotransitionitem(end[j], audio_dissolve_duration)
        track2.append(clip2)

        clip2 = audioclipitem1(
            video,
            str(start_index_frame[j+1]-audio_dissolve_duration), 
            str(end_index_frame[j+1]+audio_dissolve_duration), 
            '-1', 
            '-1'
        )
        track2.append(clip2)

        clip3 = audioclipitem2(
            video,
            str(start_index_frame[j]-audio_dissolve_duration), 
            str(end_index_frame[j]+audio_dissolve_duration), 
            '-1', 
            '-1'
        )
        track3.append(clip3)

        clip3 = audiotransitionitem(end[j], audio_dissolve_duration)
        track3.append(clip3)

        clip3 = audioclipitem2(
            video,
            str(start_index_frame[j+1]-audio_dissolve_duration), 
            str(end_index_frame[j+1]+audio_dissolve_duration), 
            '-1', 
            '-1'
        )
        track3.append(clip3)
    clip1 = videotransitionitem(start[len(start)-1], video_dissolve_duration)
    track1.append(clip1)
    clip1 = videoclipitem(
        video, 
        str(start_index_frame[len(start)-1]-video_dissolve_duration), 
        str(end_index_frame[len(start)-1]), 
        '-1', 
        str(end[len(start)-1]), 
        str(total_duration), 
        str(0),
        current_path+"\\"+"inputvideo"+"\\"+video
        )
    track1.append(clip1)
    clip2 = audiotransitionitem(start[len(start)-1], audio_dissolve_duration)
    track2.append(clip2)
    clip2 = audioclipitem1(
        video,
        str(start_index_frame[len(start)-1]-audio_dissolve_duration), 
        str(end_index_frame[len(start)-1]), 
        '-1', 
        str(end[len(start)-1]), 
    )
    track2.append(clip2)
    clip3 = audiotransitionitem(start[len(start)-1], audio_dissolve_duration)
    track3.append(clip3)
    clip3 = audioclipitem2(
        video,
        str(start_index_frame[len(start)-1]-audio_dissolve_duration), 
        str(end_index_frame[len(start)-1]), 
        '-1', 
        str(end[len(start)-1]), 
    )
    track3.append(clip3)

    tree = ElementTree(xmeml)
    fileName = current_path+"/inputvideo/xmlcache/"+ video[:-4]+".xml"
    with open(fileName, "wb") as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    current_path = os.path.join(current_path, os.pardir)
    video_list = os.listdir(current_path + "/inputvideo/")
    video_list = [file for file in video_list if file.endswith(".mp4")]
    print(video_list)
    print(video_list[0])
    fr = 60
    start_index_frame = [100, 200]
    end_index_frame = [150, 250]
    quest_start = 150
    quest_end = 200
    run_tree(
        current_path,
        video_list[0],
        fr,
        start_index_frame,
        end_index_frame,
        quest_start,
        quest_end
        )