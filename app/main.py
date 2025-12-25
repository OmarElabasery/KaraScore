import sys
import logging
from PySide6.QtWidgets import QApplication
from app.utils.logger import setup_logging
from app.ui.main_window import MainWindow

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting KaraScore...")

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    exit_code = app.exec()
    logger.info(f"KaraScore exiting with code {exit_code}")
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
