import logging
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KaraScore v0.1")
        self.resize(400, 300)

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # UI Elements
        self.status_label = QLabel("Ready")
        layout.addWidget(self.status_label)

        self.btn_record = QPushButton("Record")
        self.btn_record.clicked.connect(self.on_record)
        layout.addWidget(self.btn_record)

        self.btn_stop = QPushButton("Stop")
        self.btn_stop.clicked.connect(self.on_stop)
        layout.addWidget(self.btn_stop)

        self.btn_load_midi = QPushButton("Load MIDI")
        self.btn_load_midi.clicked.connect(self.on_load_midi)
        layout.addWidget(self.btn_load_midi)

        self.btn_compute_score = QPushButton("Compute Score")
        self.btn_compute_score.clicked.connect(self.on_compute_score)
        layout.addWidget(self.btn_compute_score)

    def on_record(self):
        logger.info("Record button clicked")
        self.status_label.setText("Recording... (Stub base)")
        # TODO: Call audio.recorder.start_recording()

    def on_stop(self):
        logger.info("Stop button clicked")
        self.status_label.setText("Stopped.")
        # TODO: Call audio.recorder.stop_recording()

    def on_load_midi(self):
        logger.info("Load MIDI button clicked")
        self.status_label.setText("Loading MIDI... (Stub base)")
        # TODO: Open file dialog and call midi.loader.load_midi()

    def on_compute_score(self):
        logger.info("Compute Score button clicked")
        self.status_label.setText("Computing Score... (Stub base)")
        # TODO: Call scoring.engine.compute_score()
