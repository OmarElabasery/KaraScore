import time
from app.audio.recorder import start_recording, stop_recording

print("Starting recording for 5 seconds...")
start_recording()

time.sleep(5)

audio, sr = stop_recording()

print("Recording stopped.")
print(f"Sample rate: {sr}")
print(f"Audio shape: {audio.shape}")
print(f"Duration (seconds): {len(audio) / sr:.2f}")

# Basic sanity checks
assert audio.ndim == 1, "Audio should be mono"
assert len(audio) > 0, "Audio buffer is empty"

print("Mic recording test PASSED.")
