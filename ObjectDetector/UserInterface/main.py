from PyQt5.QtWidgets import (QApplication)
import sys
from ObjectDetector.UserInterface.Coordinator.MainMenuWindowCoordinator import MainMenuWindowCoordinator

# before running set path to object detection directory in interpreter
# PARENT PATH TO API/Tensorflow_Object_Detection_API/models/research
#
# PARENT PATH TO API/Tensorflow_Object_Detection_API/models/research/slim

# any issues - drop me an email at willoleary6@gmail.com

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = MainMenuWindowCoordinator()
    main_menu.go_to_main_menu_window()
    sys.exit(app.exec_())

