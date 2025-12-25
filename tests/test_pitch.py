import time
import numpy as np

from app.audio.recorder import start_recording, stop_recording
from app.audio.processing import extract_pitch

print("Recording 5 seconds of audio...")
start_recording()
time.sleep(5)
audio, sr = stop_recording()

print(f"Audio length: {len(audio)} samples at {sr} Hz")

print("Extracting pitch...")
times, pitches = extract_pitch(audio, sr)

print(f"Total frames: {len(pitches)}")
print(f"Voiced frames: {np.sum(~np.isnan(pitches))}")
print(f"Unvoiced frames: {np.sum(np.isnan(pitches))}")

print("\nFirst 20 pitch values (Hz):")
print(pitches[:20])

# Basic sanity checks
assert len(times) == len(pitches), "Times and pitches length mismatch"
assert len(pitches) > 0, "No pitch frames extracted"

print("\nPitch extraction test PASSED.")
