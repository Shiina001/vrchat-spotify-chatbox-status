#Integers
MEDIA_FETCH_FREQUENCY = 5 #(seconds) I don't know if you can get rate limited by spamming in chat so be careful how often it posts(if I'm wrong correct me)

#Boolean
UPDATE_ONLY_ON_MEDIA_CHANGED = False #If set to False song info will update on every fetch (set to False if you want live timeline updates)
DO_NEW_MEDIA_ANNOUNCEMENT = True #When new media is detected send to chat what's in ON_NEW_MEDIA_STARTED

#Strings
ON_MEDIA_PLAYING = '{title} by {artists} {timeline_current}/{timeline_end}' #Delete timeline variables if you dont want it displayed
ON_NEW_MEDIA_STARTED = 'Coming up next --> {title} by {artists}' #Announce new media if detected
ON_MEDIA_PAUSED = 'Music paused' #When media gets paused