# separation_module.py

from pydub import AudioSegment
from spleeter.separator import Separator
import yaml

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config

def separate_vocals_background(config):
    input_file = config.get("input_audio_file", '')
    output_vocal = config.get("output_vocal_file", '')
    output_background = config.get("output_background_file", '')

    # Load the input audio file
    audio = AudioSegment.from_file(input_file, format="mp4")

    # Save the audio as a WAV file
    input_wav = "inputwav/input_audio.wav"
    audio.export(input_wav, format="wav")

    # Separate vocals and background using Spleeter
    separator = Separator(config.get("spleeter_model", 'spleeter:2stems'))
    separator.separate_to_file(input_wav, 'tmp')

    # Load the separated vocal and background tracks
    vocal_track = AudioSegment.from_file("tmp/input_audio/vocals.wav", format="wav")
    background_track = AudioSegment.from_file("tmp/input_audio/accompaniment.wav", format="wav")

    # Export the separated tracks
    vocal_track.export(output_vocal, format="wav")
    background_track.export(output_background, format="wav")

if __name__ == "__main__":
    config_path = 'config.yaml' 
    config = load_config(config_path)

    # Perform separation using the loaded configuration
    separate_vocals_background(config)

    print("Separation complete.")
