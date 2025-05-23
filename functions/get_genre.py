music_genres = {
    "pop": ["pop"],
    "schlager (dansk top)": ["dansk top", "dansktop", "dansk-top", "dansktopmusik", "schlager"],
    "eurovision pop": ["melodi grand prix", "melodi grandprix", "melodigrandprix", "eurovision", "eurovision song contest", "eurovision musik", "mgp"],
    "rock": ["rock", "rock'n'roll", "rock and roll", "rock & roll", "rocknroll"],
    "indie rock": ["indie rock", "indie-rock", "indie/rock", "indierock", "indie"],
    "alternative rock": ["alternative rock", "alt rock", "alt-rock", "alternativ rock"],
    "heavy metal": ["heavy metal", "heavy", "hård metal", "heavy-metal", "metal"],
    "death metal": ["death metal", "dødsmetal", "deathmetal"],
    "black metal": ["black metal", "sort metal", "blackmetal"],
    "thrash metal": ["thrash metal", "thrash", "thrashmetal"],
    "doom metal": ["doom metal", "doom", "doommetal"],
    "metalcore": ["metalcore", "metal core", "metal-core"],
    "hardcore punk": ["hardcore punk", "hardcore", "hardcorepunk", "hc punk", "hc"],
    "punk": ["punk rock", " punk", "punkrock", "punk-rock", "Incontrollados"],
    "emo": [" emo ", "emotional hardcore", "emocore"],
    "grunge": ["grunge", "grungy"],
    "jazz": ["jazz", "jazzy", " lounge "],
    "blues": ["blues", "bluesy"],
    "funk": ["funk ", "funkey", "funky", " funk", "funket", "funk-", "funk/", "-funk", "/funk"],
    "soul": ["soul", "soulmusik"],
    "r&b": ["r&b", "rhythm and blues", " rnb ", "r’n’b", "R&amp;B"],
    "hip hop": ["hip hop", "hip-hop", "hiphop", " rap"],
    "trap": ["trap", "trapmusik"],
    "lo-fi": ["lo-fi", "lofi", "low fidelity", "lo fi"],
    "electronic": ["electronic", "elektronisk", "electro", "electronica, elektro"],
    "edm": ["edm", "electronic dance music", "elektronisk dansemusik", "dance-duo", "dance-gruppe", "danceduo, eurodance"],
    "house": ["housemusic", "house music", "housegruppe", "house-gruppe", "house gruppe", "houseduo"],
    "techno": ["techno", "tekno", "technomusik"],
    "trance": [" trance", "trancemusic"],
    "drum and bass": ["drum and bass", "drum & bass", "dnb", "drum n bass"],
    "dubstep": ["dubstep", "dub step"],
    "ambient": ["ambient", "ambient music", "ambience"],
    "classical": ["klassisk musik", "classical music", "klassisk gruppe", "harmoniorkester", "kammerensemble", "klassisk ensemble", "symfoniorkester"],
    "opera": ["opera"],
    "folk": ["folk-", "folkemusik", "folk music", "folkrock", "folk/"],
    "country": ["country", "countrymusik", "country music"],
    "bluegrass": ["bluegrass", "blue grass"],
    "reggae": ["reggae", "raggae"],
    "dancehall": ["dancehall"],
    "afrobeat": ["afrobeat", "afro beat"],
    "afropop": ["afropop", "afro pop"],
    "brass band": ["blæsermusik", "blæsemusik", "brass band", "brassband","blæserkvintet", "marchmusik", "wind band", "wind ensemble"],
    "world": ["world music", "verdensmusik"],
    "latin": [" latin", "latin music", "latinsk", "latino"],
    "salsa": [" salsa"],
    "bossa nova": ["bossa nova", "bossanova"],
    "flamenco": ["flamenco"],
    "k-pop": ["k-pop", "kpop", "korean pop"],
    "j-pop": ["j-pop", "jpop", "japanese pop"],
    "c-pop": ["c-pop", "cpop", "chinese pop"],
    "new age": ["new age", "new-age", "ny tids musik", "nytid"],
    "experimental": ["experimental", "eksperimentel", "eksperimenterende musik"],
    "industrial": ["industrial", "industriel"],
    "noise": [" noise", "støjmusik", "noisecore"],
    "shoegaze": ["shoegaze", "shoe gaze"],
    "post-rock": ["post-rock", "post rock", "postrock"],
    "post-punk": ["post-punk", "post punk", "postpunk"],
    "synthpop": ["synthpop", "synth pop", "synth-pop"],
    "dream pop": ["dream pop", "dreampop", "dream-pop"],
    "garage rock": ["garage rock", "garage-rock", "garagerock"],
    "progressive rock": ["progressive rock", "prog rock", "prog-rock", "progrock"],
    "progressive metal": ["progressive metal", "prog metal", "prog-metal", "progmetal"],
    "emo rap": ["emo rap", "emorap", "emo-rap"],
    "hyperpop": ["hyperpop", "hyper pop"],
    "phonk": ["phonk", "funky trap"],
    "gospel": ["gospel", "gospelmusik"],
    "choral": ["choral", "choral music", "choir music", "kormusik", "korgruppe", "kor gruppe", "kor-gruppe", "kor musik", "a cappella", "acapella", "vokalensemble", "vokalgruppe"],
    "children": ["children", "børnemusik", "children's music"],
    "theatre and entertainment": ["musical theatre", "musical theater", "teaterkoncerter","teatergruppe", "satiregruppe", "musicals", "teatermusik", "musikteater", "musikalsk teater", "underholdningsorkester", "revy musik"],
    "sound art": ["sound art", "lydkunst", "eksperimentel lyd", "audiokunst", "auditive fortolkninger af poesi"]
}

def get_genre(text):
    if not isinstance(text, str):
        return ["No text"]

    found_genres = []
    for genre, keywords in music_genres.items():
        if any(keyword in text.lower() for keyword in keywords):
            found_genres.append(genre)
    return found_genres