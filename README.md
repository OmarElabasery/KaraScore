# 🎤 KaraScore

KaraScore is a desktop-based karaoke scoring system built in Python that evaluates a singer’s performance by analyzing vocal pitch and timing against a reference melody.

The project is designed for **physical karaoke venues**, where a controlled environment (fixed microphones, rooms, and hardware) enables fair, consistent, and enjoyable scoring. KaraScore focuses on building a transparent and extensible **scoring engine**, rather than a mobile or web karaoke application.

---

## 🎯 Project Objectives

- Capture live microphone input in real time
- Extract vocal pitch over time
- Compare the performance against a reference melody (MIDI-based)
- Compute a fair and intuitive karaoke score
- Visualize user pitch versus reference pitch
- Support fullscreen, kiosk-style desktop setups

---

## 🧠 Design Philosophy

- **Accuracy over hype** — scoring should feel fair, not perfect
- **Transparency** — visual feedback builds trust in the score
- **Modularity** — audio, scoring, and UI layers are cleanly separated
- **Offline-first** — no external services or cloud dependencies
- **Solo-developer friendly** — optimized for long-term iteration

---

## 🖥️ Target Platform

- Desktop only (Windows-first, cross-platform capable)
- Intended for use in physical karaoke rooms
- Not designed for mobile or browser deployment

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **PySide6 (Qt)** for desktop UI
- **sounddevice** for microphone input
- **librosa**, **NumPy**, **SciPy** for audio and signal processing
- **MIDI reference files** for melody alignment
- Fully offline operation

---

## 📁 Project Structure (v0.1)

```text
kara-score/
│
├── app/
│   ├── main.py              # Application entry point
│   ├── ui/                  # Qt UI components
│   ├── audio/               # Mic input & preprocessing
│   ├── midi/                # MIDI loading & parsing
│   ├── scoring/             # Alignment & scoring logic
│   ├── utils/               # Shared helpers
│   └── data/
│       └── songs/           # MIDI & metadata files
│
├── experiments/             # Prototypes & testing scripts
├── tests/                   # Unit tests
├── requirements.txt
└── README.md
