import os
from pydub import AudioSegment

# Target settings
TARGET_SAMPLE_RATE = 8000  # Hz
TARGET_CHANNELS = 1        # mono
TARGET_SAMPLE_WIDTH = 2    # 16-bit = 2 bytes

# Folder with audio files (same folder as this script)
folder_path = "."

# Process all .mp3 and .wav files
for filename in os.listdir(folder_path):
    if filename.lower().endswith((".mp3", ".wav")) and not filename.endswith("_converted.wav"):
        filepath = os.path.join(folder_path, filename)
        print(f"Processing: {filename}")

        try:
            # Load audio file
            audio = AudioSegment.from_file(filepath)

            # Convert to mono, 8000 Hz, 16-bit
            audio = audio.set_channels(TARGET_CHANNELS)
            audio = audio.set_frame_rate(TARGET_SAMPLE_RATE)
            audio = audio.set_sample_width(TARGET_SAMPLE_WIDTH)

            # Export to new WAV file (PCM 16-bit)
            out_filename = "new_" + os.path.splitext(filename)[0] + ".wav"
            out_path = os.path.join(folder_path, out_filename)
            audio.export(out_path, format="wav", codec="pcm_s16le")

            print(f"✅ Saved: {out_filename}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
