import asyncio
from pythonosc import udp_client

import function_library
import config

async def main():
    print("VRC Spotify announcer by Shiina_0")
    print("Make sure that OSC is enabled ;)")

    client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

    print("OSC client setup, ready for work...")

    media_paused = False
    last_fetch_song_title = None

    while True:
        #Fetch all the media data and store it in variables
        song_info, timeline_current, timeline_end, media_state = await function_library.get_media_info()
        title = song_info['title']
        artists = song_info['artist']
        timeline_current, timeline_end = function_library.format_timestamp(timeline_current, timeline_end)
            
        #Check if media is playing 
        if function_library.is_media_playing(media_state):
            media_paused = False

            if title != last_fetch_song_title:
                
                if config.DO_NEW_MEDIA_ANNOUNCEMENT and not config.UPDATE_ONLY_ON_MEDIA_CHANGED:
                    message = f"{config.ON_NEW_MEDIA_STARTED.format(title=title, artists=artists)}"
                    message = function_library.format_string_if_too_long(message)
                    function_library.chat_box_send(client, message)
                
                if config.UPDATE_ONLY_ON_MEDIA_CHANGED:
                    message = f"{config.ON_MEDIA_PLAYING.format(title=title, artists=artists, timeline_current=timeline_current, timeline_end=timeline_end)}"
                    message = function_library.format_string_if_too_long(message)
                    function_library.chat_box_send(client, message)

            elif title == last_fetch_song_title and not config.UPDATE_ONLY_ON_MEDIA_CHANGED:
                message = f"{config.ON_MEDIA_PLAYING.format(title=title, artists=artists, timeline_current=timeline_current, timeline_end=timeline_end)}"
                message = function_library.format_string_if_too_long(message)
                function_library.chat_box_send(client, message)
        
        else:
            if not media_paused:
                message = config.ON_MEDIA_PAUSED
                message = function_library.format_string_if_too_long(message)
                function_library.chat_box_send(client, message)
            media_paused = True
            title = None

        last_fetch_song_title = title
        await asyncio.sleep(config.MEDIA_FETCH_FREQUENCY)


if __name__ == "__main__":
    asyncio.run(main())
