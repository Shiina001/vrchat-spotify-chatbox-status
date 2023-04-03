from pythonosc import udp_client

from winsdk.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager

from winsdk.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionPlaybackStatus

#Post Chatbox message to OSC server
def chat_box_send(client, message):
    client.send_message("/chatbox/input", [message, True, False])

#Get media info from windows (ty Stack <3)
async def get_media_info():
    sessions = await MediaManager.request_async()

    current_session = sessions.get_current_session()
    if current_session:  # there needs to be a media session running

        info = await current_session.try_get_media_properties_async()
        timeline = current_session.get_timeline_properties()

        playback = current_session.get_playback_info()

        media_state = playback.playback_status

        info_dict = {song_attr: info.__getattribute__(song_attr) for song_attr in dir(info) if song_attr[0] != '_'}

        info_dict['genres'] = list(info_dict['genres'])
        return info_dict, timeline.position, timeline.end_time, media_state

    raise Exception('TARGET_PROGRAM is not the current media session')


def is_media_playing(media_state):
    if media_state == GlobalSystemMediaTransportControlsSessionPlaybackStatus.PLAYING:
        return True
    elif media_state == GlobalSystemMediaTransportControlsSessionPlaybackStatus.PAUSED:
        return False
    else:
        raise Exception('Invalid media_state was given')
    

#Can be done better for sure, I need to look into it later... although it supports hours nicely XD
def format_timestamp(timeline_current, timeline_end):
    timeline_current = str(timeline_current)
    timeline_end = str(timeline_end)
    
    if timeline_end[0] == '0':
        timeline_end = timeline_end[2:]
        timeline_current = timeline_current[2:]

    if timeline_end[0] == '0':
        timeline_end = timeline_end[1:]        
        timeline_current = timeline_current[1:]

    timeline_end = timeline_end[0:-7]        
    timeline_current = timeline_current[0:-7]  

    return (timeline_current, timeline_end)