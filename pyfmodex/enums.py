"""Fmod API enumeration types."""
from enum import Enum, IntEnum

class CHANNELCONTROL_CALLBACK_TYPE(Enum):
    END = 0
    VIRTUALVOICE = 1
    SYNCPOINT = 2
    OCCLUSION = 3
    MAX = 4

class CHANNELCONTROL_DSP_INDEX(IntEnum):
    HEAD = 0
    FADER = 1
    TAIL = 3
class CHANNELCONTROL_TYPE(Enum):
    CHANNEL = 0
    CHANNELGROUP = 1
    
    
class CHANNELORDER(Enum):
    DEFAULT = 0
    WAVEFORMAT = 1
    PROTOOLS = 2
    ALLMONO = 3
    ALLSTEREO = 4
    ALSA = 5
    MAX = 6

class DEBUG_MODE(Enum):
    TTY = 0
    FILE = 1
    CALLBACK = 2

class DSPCONNECTION_TYPE(Enum):
    STANDARD = 0
    SIDECHAIN = 1
    SEND = 2
    SEND_SIDECHAIN = 3
    MAX = 4

class DSP_CHANNELMIX(Enum):
    OUTPUTGROUPING = 0
    GAIN_CH0 = 1
    GAIN_CH1 = 2
    GAIN_CH2 = 3
    GAIN_CH3 = 4
    GAIN_CH4 = 5
    GAIN_CH5 = 6
    GAIN_CH6 = 7
    GAIN_CH7 = 8
    GAIN_CH8 = 9
    GAIN_CH9 = 10
    GAIN_CH10 = 11
    GAIN_CH11 = 12
    GAIN_CH12 = 13
    GAIN_CH13 = 14
    GAIN_CH14 = 15
    GAIN_CH15 = 16
    GAIN_CH16 = 17
    GAIN_CH17 = 18
    GAIN_CH18 = 19
    GAIN_CH19 = 20
    GAIN_CH20 = 21
    GAIN_CH21 = 22
    GAIN_CH22 = 23
    GAIN_CH23 = 24
    GAIN_CH24 = 25
    GAIN_CH25 = 26
    GAIN_CH26 = 27
    GAIN_CH27 = 28
    GAIN_CH28 = 29
    GAIN_CH29 = 30
    GAIN_CH30 = 31
    GAIN_CH31 = 32
    OUTPUT_CH0 = 33
    OUTPUT_CH1 = 34
    OUTPUT_CH2 = 35
    OUTPUT_CH3 = 36
    OUTPUT_CH4 = 37
    OUTPUT_CH5 = 38
    OUTPUT_CH6 = 39
    OUTPUT_CH7 = 40
    OUTPUT_CH8 = 41
    OUTPUT_CH9 = 42
    OUTPUT_CH10 = 43
    OUTPUT_CH11 = 44
    OUTPUT_CH12 = 45
    OUTPUT_CH13 = 46
    OUTPUT_CH14 = 47
    OUTPUT_CH15 = 48
    OUTPUT_CH16 = 49
    OUTPUT_CH17 = 50
    OUTPUT_CH18 = 51
    OUTPUT_CH19 = 52
    OUTPUT_CH20 = 53
    OUTPUT_CH21 = 54
    OUTPUT_CH22 = 55
    OUTPUT_CH23 = 56
    OUTPUT_CH24 = 57
    OUTPUT_CH25 = 58
    OUTPUT_CH26 = 59
    OUTPUT_CH27 = 60
    OUTPUT_CH28 = 61
    OUTPUT_CH29 = 62
    OUTPUT_CH30 = 63
    OUTPUT_CH31 = 64


class DSP_CHANNELMIX_OUTPUT(Enum):
    DEFAULT = 0
    ALLMONO = 1
    ALLSTEREO = 2
    ALLQUAD = 3
    ALL5POINT1 = 4
    ALL7POINT1 = 5
    ALLLFE = 6

class DSP_CHORUS(IntEnum):
    MIX = 0
    RATE = 1
    DEPTH = 2

class DSP_COMPRESSOR(IntEnum):
    THRESHOLD = 0
    RATIO = 1
    ATTACK = 2
    RELEASE = 3
    GAINMAKEUP = 4
    USESIDECHAIN = 5
    LINKED = 6

class DSP_CONVOLUTION_REVERB(IntEnum):
    PARAM_IR = 0
    PARAM_WET = 1
    PARAM_DRY = 2
    PARAM_LINKED = 3

class DSP_DELAY(IntEnum):
    CH0 = 0
    CH1 = 1
    CH2 = 2
    CH3 = 3
    CH4 = 4
    CH5 = 5
    CH6 = 6
    CH7 = 7
    CH8 = 8
    CH9 = 9
    CH10 = 10
    CH11 = 11
    CH12 = 12
    CH13 = 13
    CH14 = 14
    CH15 = 15
    MAXDELAY = 16

class DSP_DISTORTION(IntEnum):
    LEVEL = 0
class DSP_ECHO(IntEnum):
    DELAY = 0
    FEEDBACK = 1
    DRYLEVEL = 2
    WETLEVEL = 3

class DSP_ENVELOPEFOLLOWER(IntEnum):
    ATTACK = 0
    RELEASE = 1
    ENVELOPE = 2
    USESIDECHAIN = 3

class DSP_FADER(IntEnum):
    GAIN = 0

class DSP_FFT(IntEnum):
    WINDOWSIZE = 0
    WINDOWTYPE = 1
    SPECTRUMDATA = 2
    DOMINANT_FREQ = 3
class DSP_FFT_WINDOW(IntEnum):
    RECT = 0
    TRIANGLE = 1
    HAMMING = 2
    HANNING = 3
    BLACKMAN = 4
    BLACKMANHARRIS = 5

class DSP_FLANGE(IntEnum):
    MIX = 0
    DEPTH = 1
    RATE = 2

class DSP_HIGHPASS(IntEnum):
    CUTOFF = 0
    RESONANCE = 1

class DSP_HIGHPASS_SIMPLE(IntEnum):
    CUTOFF = 0

class DSP_ITECHO(IntEnum):
    WETDRYMIX = 0
    FEEDBACK = 1
    LEFTDELAY = 2
    RIGHTDELAY = 3
    PANDELAY = 4

class DSP_ITLOWPASS(IntEnum):
    CUTOFF = 0
    RESONANCE = 1

class DSP_LIMITER(IntEnum):
    RELEASETIME = 0
    CEILING = 1
    MAXIMIZERGAIN = 2
    MODE = 3
    
class DSP_LOWPASS(IntEnum):
    CUTOFF = 0
    RESONANCE = 1

class DSP_LOWPASS_SIMPLE(IntEnum):
    CUTOFF = 0

class DSP_MULTIBAND_EQ(IntEnum):
    A_FILTER = 0
    A_FREQUENCY = 1
    A_Q = 2
    A_GAIN = 3
    B_FILTER = 4
    B_FREQUENCY = 5
    B_Q = 6
    B_GAIN = 7
    C_FILTER = 8
    C_FREQUENCY = 9
    C_Q = 10
    C_GAIN = 11
    D_FILTER = 12
    D_FREQUENCY = 13
    D_Q = 14
    D_GAIN = 15
    E_FILTER = 16
    E_FREQUENCY = 17
    E_Q = 18
    E_GAIN = 19
    
class DSP_MULTIBAND_EQ_FILTER_TYPE(IntEnum):
    DISABLED = 0
    LOWPASS_12DB = 1
    LOWPASS_24DB = 2
    LOWPASS_48DB = 3
    HIGHPASS_12DB = 4
    HIGHPASS_24DB = 5
    HIGHPASS_48DB = 6
    LOWSHELF = 7
    HIGHSHELF = 8
    PEAKING = 9
    BANDPASS = 10
    NOTCH = 11
    ALLPASS = 12
    
class DSP_NORMALIZE(IntEnum):
    FADETIME = 0
    THRESHOLD = 1
    MAXAMP = 2

class DSP_OBJECTPAN(IntEnum):
    THREED_POSITION = 0
    THREED_ROLLOFF = 1
    THREED_MIN_DISTANCE = 2
    THREED_MAX_DISTANCE = 3
    THREED_EXTENT_MODE = 4
    THREED_SOUND_SIZE = 5
    THREED_MIN_EXTENT = 6
    OVERALL_GAIN = 7
    OUTPUT_GAIN = 8

class DSP_OSCILLATOR(IntEnum):
    TYPE = 0
    RATE = 1

class DSP_PAN(IntEnum):
    MODE = 0
    TWOD_STEREO_POSITION = 1
    TWOD_DIRECTION = 2
    TWOD_EXTENT = 3
    TWOD_ROTATION = 4
    TWOD_LFE_LEVEL = 5
    TWOD_STEREO_MODE = 6
    TWOD_STEREO_SEPARATION = 7
    TWOD_STEREO_AXIS = 8
    ENABLED_SPEAKERS = 9
    THREED_POSITION = 10
    THREED_ROLLOFF = 11
    THREED_MIN_DISTANCE = 12
    THREED_MAX_DISTANCE = 13
    THREED_EXTENT_MODE = 14
    THREED_SOUND_SIZE = 15
    THREED_MIN_EXTENT = 16
    THREED_PAN_BLEND = 17
    LFE_UPMIX_ENABLED = 18
    OVERALL_GAIN = 19
    SURROUND_SPEAKER_MODE = 20
    TWOD_HEIGHT_BLEND = 21

class DSP_PAN_MODE_TYPE(IntEnum):
    MONO = 0
    STEREO = 1
    SURROUND = 2

class DSP_PAN_SURROUND_FLAGS(IntEnum):
    DEFAULT = 0
    ROTATION_NOT_BIASED = 1

class DSP_PARAMEQ(IntEnum):
    CENTER = 0
    BANDWIDTH = 1
    GAIN = 2

class DSP_PARAMETER_DATA_TYPE(Enum):
    USER = 0
    OVERALLGAIN = 1
    THREED_ATTRIBUTES = 2
    SIDECHAIN = 3
    FFT = 4
    THREEDATTRIBUTES_MULTI = 5

class DSP_PARAMETER_FLOAT_MAPPING_TYPE(Enum):
    LINEAR = 0
    AUTO = 1
    PIECEWISE_LINEAR = 2
    
class DSP_PARAMETER_TYPE(Enum):
    FLOAT = 0
    INT = 1
    BOOL = 2
    DATA = 3
    MAX = 4

class DSP_PITCHSHIFT(IntEnum):
    PITCH = 0
    FFTSIZE = 1
    OVERLAP = 3
    MAXCHANNELS = 4

class DSP_PROCESS_OPERATION(Enum):
    PERFORM = 0
    QUERY = 1

class DSP_RESAMPLER(IntEnum):
    DEFAULT = 0
    NOINTERP = 1
    LINEAR = 2
    CUBIC = 3
    SPLINE = 4
    MAX = 5

class DSP_RETURN(IntEnum):
    ID = 0
    INPUT_SPEAKER_MODE = 1

class DSP_SEND(IntEnum):
    RETURNID = 0
    LEVEL = 1

class DSP_SFXREVERB(IntEnum):
    DECAYTIME = 0
    EARLYDELAY = 1
    LATEDELAY = 2
    HFREFERENCE = 3
    HFDECAYRATIO = 4
    DIFFUSION = 5
    DENSITY = 6
    LOWSHELFFREQUENCY = 7
    LOWSHELFGAIN = 8
    HIGHCUT = 9
    EARLYLATEMIX = 10
    WETLEVEL = 11
    DRYLEVEL = 12

class DSP_THREE_EQ(IntEnum):
    LOWGAIN = 0
    MIDGAIN = 1
    HIGHGAIN = 2
    LOWCROSSOVER = 3
    HIGHCROSSOVER = 4
    CROSSOVERSLOPE = 5

class DSP_THREE_EQ_CROSSOVERSLOPE_TYPE(IntEnum):
    SLOPE_12DB = 0
    SLOPE_24DB = 1
    SLOPE_48DB = 2

class DSP_TRANSCEIVER(IntEnum):
    TRANSMIT = 0
    GAIN = 1
    CHANNEL = 2
    TRANSMITSPEAKERMODE = 3
class DSP_TRANSCEIVER_SPEAKERMODE(IntEnum):
    AUTO = 0
    MONO = 1
    STEREO = 2
    SURROUND = 3

class DSP_TREMOLO(IntEnum):
    FREQUENCY = 0
    DEPTH = 1
    SHAPE = 2
    SKEW = 3
    DUTY = 4
    SQUARE = 5
    PHASE = 6
    SPREAD = 7

class DSP_TYPE(IntEnum):
    UNKNOWN = 0
    MIXER = 1
    OSCILLATOR = 2
    LOWPASS = 3
    ITLOWPASS = 4
    HIGHPASS = 5
    ECHO = 6
    FADER = 7
    FLANGE = 8
    DISTORTION = 9
    NORMALIZE = 10
    LIMITER = 11
    PARAMEQ = 12
    PITCHSHIFT = 13
    CHORUS = 14
    VSTPLUGIN = 15
    WINAMPPLUGIN = 16
    ITECHO = 17
    COMPRESSOR = 18
    SFXREVERB = 19
    LOWPASS_SIMPLE = 20
    DELAY = 21
    TREMOLO = 22
    LADSPAPLUGIN = 23
    SEND = 24
    RETURN = 25
    HIGHPASS_SIMPLE = 26
    PAN = 27
    THREE_EQ = 28
    FFT = 29
    LOUDNESS_METER = 30
    ENVELOPEFOLLOWER = 31
    CONVOLUTIONREVERB = 32
    CHANNELMIX = 33
    TRANSCEIVER = 34
    OBJECTPAN = 35
    MULTIBAND_EQ = 36
    MAX = 37

class ERRORCALLBACK_INSTANCETYPE(Enum):
    NONE = 0
    SYSTEM = 1
    CHANNEL = 2
    CHANNELGROUP = 2
    CHANNELCONTROL = 3
    SOUND = 4
    SOUNDGROUP = 5
    DSP = 6
    DSPCONNECTION = 7
    GEOMETRY = 8
    REVERB3D = 9
    STUDIO_SYSTEM = 10
    STUDIO_EVENTDESCRIPTION = 11
    STUDIO_EVENTINSTANCE = 12
    STUDIO_PARAMETERINSTANCE = 13
    STUDIO_BUS = 14
    STUDIO_VCA = 15
    STUDIO_BANK = 16
    STUDIO_COMMANDREPLAY = 17

class OPENSTATE(Enum):
    READY = 0
    LOADING = 1
    ERROR = 2
    CONNECTING = 3
    BUFFERING = 4
    SEEKING = 5
    PLAYING = 6
    SETPOSITION = 7
    MAX = 8

class OUTPUTTYPE(Enum):
    AUTODETECT = 0
    UNKNOWN = 1
    NOSOUND = 2
    WAVWRITER = 3
    NOSOUND_NRT = 4
    WAVWRITER_NRT = 5
    WASAPI = 6
    ASIO = 7
    PULSEAUDIO = 8
    ALSA = 9
    COREAUDIO = 10
    AUDIOTRACK = 11
    OPENSL = 12
    AUDIOOUT = 13
    AUDIO3D = 14
    WEBAUDIO = 15
    NAUDIO = 16
    WINSONIC = 17
    AAUDIO = 18
    MAX = 19

class PLUGINTYPE(Enum):
    OUTPUT = 0
    CODEC = 1
    DSP = 2
    MAX = 3

class RESULT(Enum):
    OK = 0
    BADCOMMAND = 1
    CHANNEL_ALLOC = 2
    CHANNEL_STOLEN = 3
    DMA = 4
    DSP_CONNECTION = 5
    DSP_DONTPROCESS = 6
    DSP_FORMAT = 7
    DSP_INUSE = 8
    DSP_NOTFOUND = 9
    DSP_RESERVED = 10
    DSP_SILENCE = 11
    DSP_TYPE = 12
    FILE_BAD = 13
    FILE_COULDNOTSEEK = 14
    FILE_DISKEJECTED = 15
    FILE_EOF = 16
    FILE_ENDOFDATA = 17
    FILE_NOTFOUND = 18
    FORMAT = 19
    HEADER_MISMATCH = 20
    HTTP = 21
    HTTP_ACCESS = 22
    HTTP_PROXY_AUTH = 23
    HTTP_SERVER_ERROR = 24
    HTTP_TIMEOUT = 25
    INITIALIZATION = 26
    INITIALIZED = 27
    INTERNAL = 28
    INVALID_FLOAT = 29
    INVALID_HANDLE = 30
    INVALID_PARAM = 31
    INVALID_POSITION = 32
    INVALID_SPEAKER = 33
    INVALID_SYNCPOINT = 34
    INVALID_THREAD = 35
    INVALID_VECTOR = 36
    MAXAUDIBLE = 37
    MEMORY = 38
    MEMORY_CANTPOINT = 39
    NEEDS3D = 40
    NEEDSHARDWARE = 41
    NET_CONNECT = 42
    NET_SOCKET_ERROR = 43
    NET_URL = 44
    NET_WOULD_BLOCK = 45
    NOTREADY = 46
    OUTPUT_ALLOCATED = 47
    OUTPUT_CREATEBUFFER = 48
    OUTPUT_DRIVERCALL = 49
    OUTPUT_FORMAT = 50
    OUTPUT_INIT = 51
    OUTPUT_NODRIVERS = 52
    PLUGIN = 53
    PLUGIN_MISSING = 54
    PLUGIN_RESOURCE = 55
    PLUGIN_VERSION = 56
    RECORD = 57
    REVERB_CHANNELGROUP = 58
    REVERB_INSTANCE = 59
    SUBSOUNDS = 60
    SUBSOUND_ALLOCATED = 61
    SUBSOUND_CANTMOVE = 62
    TAGNOTFOUND = 63
    TOOMANYCHANNELS = 64
    TRUNCATED = 65
    UNIMPLEMENTED = 66
    UNINITIALIZED = 67
    UNSUPPORTED = 68
    VERSION = 69
    EVENT_ALREADY_LOADED = 70
    EVENT_LIVEUPDATE_BUSY = 71
    EVENT_LIVEUPDATE_MISMATCH = 72
    EVENT_LIVEUPDATE_TIMEOUT = 73
    EVENT_NOTFOUND = 74
    STUDIO_UNINITIALIZED = 75
    STUDIO_NOT_LOADED = 76
    INVALID_STRING = 77
    ALREADY_LOCKED = 78
    NOT_LOCKED = 79
    RECORD_DISCONNECTED = 80
    TOOMANYSAMPLES = 81

class SOUNDGROUP_BEHAVIOR(Enum):
    FAIL = 0
    MUTE = 1
    STEALLOWEST = 2
    MAX = 3

class SOUND_FORMAT(Enum):
    NONE = 0
    PCM8 = 1
    PCM16 = 2
    PCM24 = 3
    PCM32 = 4
    PCMFLOAT = 5
    BITSTREAM = 6
    MAX = 7

class SOUND_TYPE(Enum):
    UNKNOWN = 0
    AIFF = 1
    ASF = 2
    DLS = 3
    FLAC = 4
    FSB = 5
    IT = 6
    MIDI = 7
    MOD = 8
    MPEG = 9
    OGGVORBIS = 10
    PLAYLIST = 11
    RAW = 12
    S3M = 13
    USER = 14
    WAV = 15
    XM = 16
    XMA = 17
    AUDIOQUEUE = 18
    AT9 = 19
    VORBIS = 20
    MEDIA_FOUNDATION = 21
    MEDIACODEC = 22
    FADPCM = 23
    MAX = 24

class SPEAKER(Enum):
    FRONT_LEFT = 0
    FRONT_RIGHT = 1
    FRONT_CENTER = 2
    LOW_FREQUENCY = 3
    SURROUND_LEFT = 4
    SURROUND_RIGHT = 5
    BACK_LEFT = 6
    BACK_RIGHT = 7
    MAX = 8

class SPEAKERMODE(Enum):
    DEFAULT = 0
    RAW = 1
    MONO = 2
    STEREO = 3
    QUAD = 4
    SURROUND = 5
    FIVEPOINTONE = 6
    SEVENPOINTONE = 7
    SEVENPOINTONEPOINTFOUR = 8
    MAX = 9

class TAGDATATYPE(Enum):
    BINARY = 0
    INT = 1
    FLOAT = 2
    STRING = 3
    STRING_UTF16 = 4
    STRING_UTF16BE = 5
    STRING_UTF8 = 6
    CDTOC = 7
    MAX = 8

class TAGTYPE(Enum):
    UNKNOWN = 0
    ID3V1 = 1
    ID3V2 = 2
    VORBISCOMMENT = 3
    SHOUTCAST = 4
    ICECAST = 5
    ASF = 6
    MIDI = 7
    PLAYLIST = 8
    FMOD = 9
    USER = 10
    MAX = 11
