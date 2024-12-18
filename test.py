# import pyaudio

# p = pyaudio.PyAudio()

# for i in range(p.get_device_count()):
#     info = p.get_device_info_by_index(i)
#     print(f"Device {i}: {info['name']}, max input channels: {info['maxInputChannels']}, max output channels: {info['maxOutputChannels']}, default sample rate: {info['defaultSampleRate']}")

# p.terminate()
















import pyaudio

p = pyaudio.PyAudio()

print("Available audio output devices:")
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    if info['maxOutputChannels'] > 0:  # Only list output devices
        print(f"Device {i}: {info['name']}, Max Output Channels: {info['maxOutputChannels']}, Default Sample Rate: {info['defaultSampleRate']}")

p.terminate()













# import numpy as np
# import pyaudio
# import sys

# # Use a supported sample rate
# rate = 48000  # Change this to 44100 if you encounter issues
# duration = 1.0  # seconds
# frequency = 440.0  # A4 note

# # Generate a sine wave
# t = np.linspace(0, duration, int(rate * duration), endpoint=False)
# samples = 0.5 * np.sin(2 * np.pi * frequency * t)
# samples = (samples * 32767).astype(np.int16)  # Convert to 16-bit PCM format

# # p = pyaudio.PyAudio()


# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     info = p.get_device_info_by_index(i)
#     print(f"Device {i}: {info['name']}, Input Channels: {info['maxInputChannels']}, Output Channels: {info['maxOutputChannels']}")



# # Set output_device_index based on your previous device listing
# output_device_index = 0  # Change this if you want to try a different device

# try:
#     # Open the stream
#     stream = p.open(format=pyaudio.paInt16,
#                     channels=1,
#                     rate=rate,
#                     output=True,
#                     output_device_index=output_device_index)

#     # Write samples to the stream
#     stream.write(samples.tobytes())
#     print("Audio played successfully!")

# except Exception as e:
#     print(f"An error occurred: {e}", file=sys.stderr)

# finally:
#     # Stop and close the stream
#     stream.stop_stream()
#     stream.close()
#     p.terminate()




