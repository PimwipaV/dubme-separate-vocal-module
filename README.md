# Dubme-separate-vocal-module

First of all, taking into account that the task of separating vocals from background is for STT improvement, I figured out that the most disruptive background noises to STT systems could be e.g. white noises, music with lyrics, background conversations, or traffic noise.

I didn’t want to spend too much time searching for “bad sound quality” vdos on youtube as I found out most of the search results already have clear vocals and good result for STT systems. So I looked through my own vdos and found a few with conversations over background music.

I did some research on librosa and classical digital signal processing methods. There are many steps and transformations involved. It was interesting and have various tricks to play with, but only if I had enough time to understand and execute all of them.

Together with my familiarity with deep learning, therefore, I chose to use Spleeter, a pre-trained deep learning model developed by Deezer, a U-Net architecture, built on TensorFlow framework for source separation that can separate vocals and accompaniment music tracks.

My vocal separation module can be found in this repo. Here is how to use it.

1. git clone https://github.com/PimwipaV/dubme-separate-vocal-module.git
2. pip install spleeter pydub
3. in config.yaml, specify your input file path and output files paths
4. python separation_module.py

Then you will find the separated vocal and background tracks (.wav) at the paths you specified.

In evaluation.ipynb, I demonstrate the effectiveness of my solution by running a google STT on the original and cleaned audio tracks and compare transcription accuracy. We can see a slight improvement in WER from 3.08% to 2.97% and considerable improvement on F1 Score from 0.39 to 0.49.

Limitations
1. dependency on Spleeter, especially the output file structure managed by Spleeter (tmp/input_audio/vocals.wav)
2. fixed input interface (file upload only, no microphone input or live stream)
3. fixed output format (.wav only)


Potential improvements
1. Add logging
2. Add error handling (e.g. input and output format validation)
3. Add unit test

If this audio separation module is to be integrated into a larger speech-to-text pipeline, considering factors like real-time processing, scalability, and adaptability to different video sources, here are what to be discussed;

1. Real-time processing
   
Then the module should have streaming capabilities. Certainly the choices of input interface should be enhanced. Latency should be low. And perhaps we should consider some forms of paralellization or distributed processing.

2. Scalability
   
I could use Docker to containerize the module, so that the module can be orchestrated with others via Kubernetes, and can be scaled based on demands.

3. Adaptability to different vdo sources
   
There are many things I can do so that the module can adapt to different vdo sources, for example;

    • add input interfaces e.g. via microphone
    
    • add a snippet to detect file type
    
    • define default configuration and accept audio format parameters as argument 
      (def separate_vocals_background(input_file, output_vocal, output_background, audio_format='mp3'):
      
    • provide error handling or unsupported format

To be part of a larger pipeline, we should also add testing and security concerns.

