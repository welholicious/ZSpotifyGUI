SAVED_TRACKS_URL = 'https://api.spotify.com/v1/me/tracks'

TRACKS_URL = 'https://api.spotify.com/v1/tracks'

TRACK_STATS_URL = 'https://api.spotify.com/v1/audio-features/'

TRACKNUMBER = 'tracknumber'

DISCNUMBER = 'discnumber'

TOTAL_TRACKS = 'total_tracks'

TOTAL = 'total'

YEAR = 'year'

ALBUM = 'album'

TRACKTITLE = 'tracktitle'

ARTIST = 'artist'

ARTISTS = 'artists'

ARTWORK = 'artwork'

TRACKS = 'tracks'

TRACK = 'track'

ITEMS = 'items'

NAME = 'name'

ID = 'id'

URL = 'url'

RELEASE_DATE = 'release_date'

IMAGES = 'images'

LIMIT = 'limit'

OFFSET = 'offset'

AUTHORIZATION = 'Authorization'

IS_PLAYABLE = 'is_playable'

TRACK_NUMBER = 'track_number'

DISC_NUMBER = 'disc_number'

SHOW = 'show'

ERROR = 'error'

EXPLICIT = 'explicit'

PLAYLIST = 'playlist'

PLAYLISTS = 'playlists'

OWNER = 'owner'

DISPLAY_NAME = 'display_name'

ALBUMS = 'albums'

DURATION = "duration_ms"

SPOTIFY_ID = 'comment'

DOWNLOADED = 'downloaded'

LIKED = 'liked'

TYPE = 'type'

PREMIUM = 'premium'

USER_READ_EMAIL = 'user-read-email'

PLAYLIST_READ_PRIVATE = 'playlist-read-private'

USER_LIBRARY_READ = 'user-library-read'

WINDOWS_SYSTEM = 'Windows'

CREDENTIALS_JSON = 'credentials.json'

CONFIG_FILE_PATH = '../zs_config.json'

ROOT_PATH = 'ROOT_PATH'

ROOT_PODCAST_PATH = 'ROOT_PODCAST_PATH'

SKIP_EXISTING_FILES = 'SKIP_EXISTING_FILES'

DOWNLOAD_FORMAT = 'DOWNLOAD_FORMAT'

FORCE_PREMIUM = 'FORCE_PREMIUM'

ANTI_BAN_WAIT_TIME = 'ANTI_BAN_WAIT_TIME'

OVERRIDE_AUTO_WAIT = 'OVERRIDE_AUTO_WAIT'

CHUNK_SIZE = 'CHUNK_SIZE'

COVER_DEFAULT = '../resources/cover_default.jpg'

SPLIT_ALBUM_DISCS = 'SPLIT_ALBUM_DISCS'

DOWNLOAD_REAL_TIME = 'DOWNLOAD_REAL_TIME'

BITRATE = 'BITRATE'

SEARCH_RESULTS = 'SEARCH_RESULTS'

PAUSE_ICON = '../resources/pauseIcon.png'

PLAY_ICON = '../resources/playIcon.png'

VOL_ICON = '../resources/volIcon.png'

MUTE_ICON = '../resources/mutedIcon.png'

FORMATS = ['mp3', 'ogg']


CODEC_MAP = {
    'aac': 'aac',
    'fdk_aac': 'libfdk_aac',
    'm4a': 'aac',
    'mp3': 'libmp3lame',
    'ogg': 'copy',
    'opus': 'libopus',
    'vorbis': 'copy',
}

EXT_MAP = {
    'aac': 'm4a',
    'fdk_aac': 'm4a',
    'm4a': 'm4a',
    'mp3': 'mp3',
    'ogg': 'ogg',
    'opus': 'ogg',
    'vorbis': 'ogg',
}

CONFIG_DEFAULT_SETTINGS = {
    'ROOT_PATH': '../ZSpotify Music/',
    'ROOT_PODCAST_PATH': '../ZSpotify Podcasts/',
    'SKIP_EXISTING_FILES': True,
    'DOWNLOAD_FORMAT': 'ogg',
<<<<<<< HEAD
    'SEARCH_RESULTS': 10,
=======
    'SEARCH_RESULTS':10,
>>>>>>> musicPlayer
    'FORCE_PREMIUM': False,
    'ANTI_BAN_WAIT_TIME': 1,
    'OVERRIDE_AUTO_WAIT': False,
    'CHUNK_SIZE': 50000,
    'SPLIT_ALBUM_DISCS': False,
    'DOWNLOAD_REAL_TIME': False
}
