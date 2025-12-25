import logging
import sounddevice as sd
import numpy as np

logger = logging.getLogger(__name__)

# Constants
SAMPLE_RATE = 22050
CHANNELS = 1
DTYPE = 'float32'

# Internal state
_stream = None
_audio_buffer = []

def start_recording():
    """
    Starts capturing audio from the default microphone.
    
    Initializes a sounddevice InputStream and appends incoming audio chunks 
    to an internal buffer. If a recording is already in progress, it logs 
    a warning and returns without starting a new one.
    """
    global _stream, _audio_buffer
    
    if _stream is not None:
        logger.warning("Recording is already in progress.")
        return

    logger.info("Starting recording...")
    _audio_buffer = [] # Reset buffer

    def callback(indata, frames, time, status):
        """Callback for sounddevice to capture audio chunks."""
        if status:
            logger.warning(f"Audio input status: {status}")
        _audio_buffer.append(indata.copy())

    try:
        _stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype=DTYPE,
            callback=callback
        )
        _stream.start()
        logger.info(f"Recording started. Sample rate: {SAMPLE_RATE}, Channels: {CHANNELS}")
    except Exception as e:
        logger.error(f"Failed to start recording: {e}")
        _stream = None

def stop_recording():
    """
    Stops the audio capture and returns the recorded data.
    
    Closes the input stream, concatenates the buffered audio chunks into 
    a single NumPy array, and returns it along with the sample rate.
    
    Returns:
        tuple: (audio_data: np.ndarray | None, sample_rate: int)
        If no audio was recorded, returns (None, SAMPLE_RATE).
    """
    global _stream, _audio_buffer
    
    if _stream is None:
        logger.warning("Stop called but no recording is in progress.")
        return None, SAMPLE_RATE

    logger.info("Stopping recording...")
    try:
        _stream.stop()
        _stream.close()
    except Exception as e:
        logger.error(f"Error stopping stream: {e}")
    finally:
        _stream = None

    if not _audio_buffer:
        logger.warning("No audio data captured.")
        return None, SAMPLE_RATE

    audio_data = np.concatenate(_audio_buffer, axis=0)
    
    # Normalize mono audio from (N, 1) to (N,) for downstream processing
    if audio_data.ndim > 1 and audio_data.shape[1] == 1:
        audio_data = audio_data.squeeze()
        
    duration = len(audio_data) / SAMPLE_RATE
    logger.info(f"Recording finished. Duration: {duration:.2f}s, Shape: {audio_data.shape}")
    
    # Clear buffer to free memory
    _audio_buffer = []
    
    return audio_data, SAMPLE_RATE
