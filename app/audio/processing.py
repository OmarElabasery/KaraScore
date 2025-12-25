import logging
import numpy as np
import librosa

logger = logging.getLogger(__name__)

def extract_pitch(audio_buffer, sr=22050):
    """
    Extracts pitch from audio buffer using librosa.pyin.
    
    Args:
        audio_buffer (np.ndarray): 1D array of audio samples (mono).
        sr (int): Sample rate of the audio (default 22050).
        
    Returns:
        tuple: (times, pitches) where:
            times (np.ndarray): Array of timestamps in seconds.
            pitches (np.ndarray): Array of fundamental frequencies in Hz.
                                  Unvoiced frames are marked as NaN.
    """
    if audio_buffer is None or len(audio_buffer) == 0:
        logger.warning("extract_pitch called with empty or None buffer.")
        return np.array([]), np.array([])
    
    logger.info(f"Starting pitch extraction for {len(audio_buffer)} samples at {sr}Hz.")
    
    # Parameters for human singing voice range
    fmin = 80.0
    fmax = 1000.0
    hop_length = 512
    
    try:
        # librosa.pyin returns (f0, voiced_flag, voiced_probs)
        # f0 contains the estimated fundamental frequency (NaN for unvoiced)
        f0, voiced_flag, voiced_probs = librosa.pyin(
            audio_buffer,
            fmin=fmin,
            fmax=fmax,
            sr=sr,
            hop_length=hop_length
        )
        
        # Calculate timestamps for each frame
        times = librosa.times_like(f0, sr=sr, hop_length=hop_length)
        
        # Ensure equal length (sometimes times can be slightly off by 1 frame depending on centering)
        min_len = min(len(times), len(f0))
        times = times[:min_len]
        pitches = f0[:min_len]
        
        voiced_count = np.sum(voiced_flag)
        total_frames = len(f0)
        voiced_pct = (voiced_count / total_frames) * 100 if total_frames > 0 else 0
        
        logger.info(f"Pitch extraction finished. Frames: {total_frames}, Voiced: {voiced_count} ({voiced_pct:.1f}%)")
        
        return times, pitches
        
    except Exception as e:
        logger.error(f"Pitch extraction failed: {e}")
        return np.array([]), np.array([])
