from xml.etree.ElementTree import *
import os
import sys
from moviepy.editor import VideoFileClip
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pysrc.user_discrimination import who
import random

def in_to_start(
    videoin_frame, # start_index_frame 
    videoout_frame, # end_index_frame
    target
    ):
    start = 0
    end = int(videoout_frame[0] - videoin_frame[0])
    print('start','end', start, end)
    for x in range(1, len(videoin_frame)):
        start = end
        end = int(videoout_frame[x] - videoin_frame[x] + start)
        print('start','end', start, end)
        print(videoout_frame[x], videoin_frame[x])
        if videoin_frame[x] <= target <= videoout_frame[x]:
            target_start = target - videoin_frame[x] + start
            print('target_start:', target_start)
            break
        elif videoout_frame[x] <= target <= videoin_frame[x+1]:
            target_start = end
            print('target_start:', target_start)
            break
    return target_start

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
def scrollclipitem(image,video, timein, timeout, start, end, current_path, img_path, buddy='False'):
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
    horiz.text= '1.62'
    value.append(horiz)   
    vert = Element('vert')
    vert.text= '-0.07'
    value.append(vert)   

    if buddy == 'False':
        parameter = Element('parameter')
        parameter.attrib['authoringApp']= "PremierePro"
        effect.append(parameter)
        parameterid = Element('parameterid')
        parameterid.text= 'scale'
        parameter.append(parameterid)    
        parametername = Element('name')
        parametername.text= 'Scale'
        parameter.append(parametername)    
        valuemin = Element('valuemin')
        valuemin.text= '0'
        parameter.append(valuemin)        
        valuemax = Element('valuemax')
        valuemax.text= '1000'
        parameter.append(valuemax)   
        value = Element('value')
        value.text= '97'
        parameter.append(value)   
    else:
        parameter = Element('parameter')
        parameter.attrib['authoringApp']= "PremierePro"
        effect.append(parameter)
        parameterid = Element('parameterid')
        parameterid.text= 'scale'
        parameter.append(parameterid)    
        parametername = Element('name')
        parametername.text= 'Scale'
        parameter.append(parametername)    
        valuemin = Element('valuemin')
        valuemin.text= '0'
        parameter.append(valuemin)        
        valuemax = Element('valuemax')
        valuemax.text= '1000'
        parameter.append(valuemax)   
        value = Element('value')
        value.text= '97'
        parameter.append(value)   
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
def hpclipitem(image, timein, timeout, start, end,current_path, user, buddy):
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
    if buddy == 'False':
        print('here buddy False')
        if user == 'matsuri':
            pathurl.text= current_path+"\\"+r"pysrc\heropower\japan"+"\\"+image
        elif user == 'rimgosu' or user == 'duckdragon' or user == 'zanyang':
            pathurl.text= current_path+"\\"+r"pysrc\heropower"+"\\"+image
        else:
            pass
    elif buddy == 'anomalies':
        print('here anomalies False')
        if user == 'matsuri':
            pathurl.text= current_path+"\\"+r"pysrc\anomalies\japan"+"\\"+image
        elif user == 'rimgosu' or user == 'duckdragon' or user == 'zanyang':
            pathurl.text= current_path+"\\"+r"pysrc\anomalies"+"\\"+image
        else:
            pass
    elif buddy == 'trinket':
        print('here trinket False')
        if user == 'matsuri':
            pathurl.text= current_path+"\\"+r"pysrc\trinket\japan"+"\\"+image
        elif user == 'rimgosu' or user == 'duckdragon' or user == 'zanyang':
            pathurl.text= current_path+"\\"+r"pysrc\trinket"+"\\"+image
            print(image)
        else:
            pass
    else:
        print('here buddy True')
        if user == 'matsuri':
            pathurl.text= current_path+"\\"+r"pysrc\herobuddy\japan"+"\\"+image
        elif user == 'rimgosu' or user == 'duckdragon' or user == 'zanyang':
            pathurl.text= current_path+"\\"+r"pysrc\herobuddy"+"\\"+image
        else:
            pass
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

    if buddy == 'False':
        pass
    else:
        parameter = Element('parameter')
        parameter.attrib['authoringApp']= "PremierePro"
        effect.append(parameter)
        parameterid = Element('parameterid')
        parameterid.text= 'scale'
        parameter.append(parameterid)    
        parametername = Element('name')
        parametername.text= 'Scale'
        parameter.append(parametername)    
        valuemin = Element('valuemin')
        valuemin.text= '0'
        parameter.append(valuemin)        
        valuemax = Element('valuemax')
        valuemax.text= '1000'
        parameter.append(valuemax)   
        value = Element('value')
        value.text= '110'
        parameter.append(value)   

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
def imgclipitem(image, timein, timeout, start, end,current_path, user, imgpath):
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
    pathurl.text= imgpath
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
    parameterid.text= 'scale'
    parameter.append(parameterid)    
    parametername = Element('name')
    parametername.text= 'Scale'
    parameter.append(parametername)    
    valuemin = Element('valuemin')
    valuemin.text= '0'
    parameter.append(valuemin)        
    valuemax = Element('valuemax')
    valuemax.text= '1000'
    parameter.append(valuemax)   
    value = Element('value')
    value.text= '110'
    parameter.append(value)   

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

def add_newminion_information(video, track2f, track3f, audiotrack, user, newminion_list, start_index, end_index, current_path, newminion_patchday):
    newminion_path = os.path.join(current_path, 'pysrc')
    newminion_path = os.path.join(newminion_path, 'newminion')
    newminion_path = os.path.join(newminion_path, newminion_patchday)
    backup_path = current_path+"\\"+r"pysrc\image_src"+"\\"+'minionbackup.png'
    if user == 'matsuri':
        newminion_path = os.path.join(newminion_path, 'jp')
    elif user == 'rimgosu':
        newminion_path = os.path.join(newminion_path, 'kr')
    elif user == 'duckdragon':
        newminion_path = os.path.join(newminion_path, 'kr')
    elif user == 'zanyang':
        newminion_path = os.path.join(newminion_path, 'kr')
    elif user == 'shadybunny':
        newminion_path = os.path.join(newminion_path, 'en')
    elif user == 'sunbacon':
        newminion_path = os.path.join(newminion_path, 'en')

    for x in range(len(newminion_list)):
        if x % 4 == 0:
            display_newminion_time = in_to_start(start_index, end_index, newminion_list[x]) 
        for y in [1,2,3]:
            if x % 4 == y and newminion_list[x] != '-':
                np = os.path.join(newminion_path, newminion_list[x])
                rand1_2 =  random.randint(1,2)
                randhook = 'randhook' + str( rand1_2 ) + '.mp3'
                sound_path = current_path + r'\pysrc\wav_src' + '\\' +randhook
                clipscroll = scrollclipitem(
                    'minionbackup.png',
                    video, 
                    str(display_newminion_time+y*200 - 120), 
                    str(display_newminion_time+200+y*200 - 120), 
                    str(display_newminion_time+y*200 - 120), 
                    str(display_newminion_time+200+y*200 - 120), 
                    current_path,
                    backup_path
                    )
                track2f.append(clipscroll)
                clipheropower = imgclipitem(
                    newminion_list[x],
                    str(display_newminion_time+y*200 - 120), 
                    str(display_newminion_time+200+y*200 - 120), 
                    str(display_newminion_time+y*200 - 120), 
                    str(display_newminion_time+200+y*200 - 120), 
                    current_path,
                    user,
                    np
                    )
                track3f.append(clipheropower)
                if y == 1:
                    soundeffect = soundeffectclipitem(
                        randhook,
                        '0',
                        '60',
                        str(display_newminion_time+y*200 - 150), 
                        str(display_newminion_time+200+y*200 - 150), 
                        sound_path,
                        '60'
                    )
                    audiotrack.append(soundeffect)
    

def run_tree(
    current_path,
    input_path,
    exf_path,
    video,
    fr,
    start_index_frame,
    end_index_frame,
    heropower,
    newminion_forxml,
    newminion_patchday,
    anomalies='',
    trinket=[],
    trinketframe=[]
    ):
    videopy = VideoFileClip(input_path + "/" + video)
    total_duration = videopy.end * fr
    scroll_path = current_path+"\\"+r"pysrc\image_src"+"\\"+'scroll.png'
    hpbackup_path = current_path+"\\"+r"pysrc\image_src"+"\\"+'hpbackup.png'
    buddybackup_path = current_path+"\\"+r"pysrc\image_src"+"\\"+'buddybackup.png'
    xmeml = Element('xmeml')
    xmeml.attrib['version']='5'

    print('here')
    print(heropower)

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

    print('inputvideopath', input_path)

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
            input_path+"\\"+video
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

    user = who(video)
    print('user: ' + user)
    if user == 'shadybunny' or user == 'sunbacon':
        pass
    else:
        if heropower:
            heropower_display_start = str(end_index_frame[0] - start_index_frame[0]+ 120)
            heropower_display_end = str(end_index_frame[0] - start_index_frame[0] + end_index_frame[1] - start_index_frame[1]+ 120)
            clipscroll = scrollclipitem(
                'hpbackup.png',
                video, 
                heropower_display_start, 
                heropower_display_end, 
                heropower_display_start, 
                heropower_display_end, 
                current_path,
                hpbackup_path
                )
            trackscroll.append(clipscroll)
            clipheropower = hpclipitem(
                heropower,
                heropower_display_start, 
                heropower_display_end, 
                heropower_display_start, 
                heropower_display_end, 
                current_path,
                user,
                'False'
                )
            trackquest.append(clipheropower)
        if anomalies:
            # for anomalies
            print(anomalies)
            anomalies_display_start = heropower_display_end
            anomalies_display_end = str(end_index_frame[0] - start_index_frame[0] + end_index_frame[1] - start_index_frame[1]+ 120 + 300)
            clipscroll = scrollclipitem(
                'hpbackup.png',
                video, 
                anomalies_display_start, 
                anomalies_display_end, 
                anomalies_display_start, 
                anomalies_display_end, 
                current_path,
                buddybackup_path,
                buddy='anomalies'
                )
            trackscroll.append(clipscroll)

            clipheropower = hpclipitem(
                anomalies,
                anomalies_display_start, 
                anomalies_display_end, 
                anomalies_display_start, 
                anomalies_display_end,  
                current_path,
                user,
                'anomalies'
                )
            trackquest.append(clipheropower)
    
        # for trinket
        if trinket:
            for j in trinket:
                trinketindex = trinket.index(j)
                print(trinket)
                print(trinketframe[trinketindex])
                trinket_display_start = str(in_to_start(start_index_frame, end_index_frame, trinketframe[trinketindex]))
                trinket_display_end = str(in_to_start(start_index_frame, end_index_frame, trinketframe[trinketindex]) + 300)
                clipscroll = scrollclipitem(
                    'hpbackup.png',
                    video, 
                    trinket_display_start, 
                    trinket_display_end, 
                    trinket_display_start, 
                    trinket_display_end, 
                    current_path,
                    buddybackup_path,
                    buddy='trinket'
                    )
                trackscroll.append(clipscroll)

                clipheropower = hpclipitem(
                    j,
                    trinket_display_start, 
                    trinket_display_end, 
                    trinket_display_start, 
                    trinket_display_end,  
                    current_path,
                    user,
                    'trinket'
                    )
                print('cliperopower')
                trackquest.append(clipheropower)

            
            # #for buddy
            # herobuddy = heropower[:-4] + '_buddy.png'
            # buddy_display_start = heropower_display_end
            # buddy_display_end = str(end_index_frame[0] - start_index_frame[0] + end_index_frame[1] - start_index_frame[1]+ 120 + 300)
            
            # clipscroll = scrollclipitem(
            #     'buddybackup.png',
            #     video, 
            #     buddy_display_start, 
            #     buddy_display_end, 
            #     buddy_display_start, 
            #     buddy_display_end, 
            #     current_path,
            #     buddybackup_path,
            #     buddy='False'
            #     )
            # trackscroll.append(clipscroll)
            # clipheropower = hpclipitem(
            #     herobuddy,
            #     buddy_display_start, 
            #     buddy_display_end, 
            #     buddy_display_start, 
            #     buddy_display_end, 
            #     current_path,
            #     user,
            #     'True'
            #     )
            # trackquest.append(clipheropower)
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
    elif user == 'x-later':
        intro_duration = 300
        introvideo = 'zanyang_intro1.mp4'
        introvideo_path = os.path.join(current_path, 'pysrc')
        introvideo_path = os.path.join(introvideo_path, 'video_src')
        introvideo_path = os.path.join(introvideo_path, user)
        
        clip1 = videoclipitem(
            introvideo, 
            str(0), 
            str(intro_duration), 
            str(0), 
            str(intro_duration), 
            str(intro_duration), 
            str(0),
            introvideo_path + '\\' + introvideo
            )
        trackscroll.append(clip1)
        soundeffect = soundeffectclipitem(
            'Hole_punch.mp3',
            str(0), 
            str(60), 
            str(0), 
            str(60), 
            current_path + r'\pysrc\wav_src\Hole_punch.mp3',
            '60'
        )
        trackefsound.append(soundeffect)

    add_newminion_information(
        video, 
        trackscroll, 
        trackquest, 
        trackefsound, 
        user, 
        newminion_forxml, 
        start_index_frame, 
        end_index_frame, 
        current_path, 
        newminion_patchday)

    if user == 'sunbacon':
        sunbacon_bgm1 = bgmclipitem(
            'sunba_bgm.mp3',
            str(0),
            str(end),
            str(0),
            str(end),
            current_path + r'\pysrc\wav_src\sunba_bgm.mp3',
            str(106992),
            str(1)
        )
        trackbgm1 = Element('track')
        audio.append(trackbgm1)
        trackbgm1.append(sunbacon_bgm1)

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