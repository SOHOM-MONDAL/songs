import time
from colorama import Fore, Style
# Lyrics with corresponding delays (in seconds)
lyrics_with_timing = [
    ("     So I'ma love you every night🌌", 2.5),
    ("     Like it's the last night 🌙", 3.0),
    ("     Like it's the last night 🌙", 1.5),
    ("     If the world was ending 🔚", 4.0),
    ("     I'd wanna be next to you🫂", 4.5),
    ("     If the party was over🎊", 3.5),
    ("     And our time on Earth was through 🌎", 6.0),
    ("     I'd wanna hold you 🫂 just for a while", 5.0),
    ("     And die with a smile🙃", 4.0),
    ("     If the 😣 world was😣 ending😖", 3.0),
    ("     I'd wanna be next to you 🫶👩‍❤‍👨🗣", 5.5),
]

# Function to display lyrics with timing
def display_lyrics(lyrics_timing):
    for line, delay in lyrics_timing:
        print(Fore.RED +  line + Style.RESET_ALL)
        time.sleep(delay)  # Wait for the specified time before printing the next line

# Call the function
display_lyrics(lyrics_with_timing)

print(Fore.GREEN + "      HAPPY --- NEW --- YEAR  zzzz💀   " + Style.RESET_ALL)
