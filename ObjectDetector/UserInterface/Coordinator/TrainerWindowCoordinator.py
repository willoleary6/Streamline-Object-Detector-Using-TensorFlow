from ObjectDetector.UserInterface.Controller.TrainerWindowController import TrainerWindowController
from ObjectDetector.UserInterface.Coordinator.baseCoordinator import BaseCoordinator


class TrainerWindowCoordinator(BaseCoordinator):
    def go_to_trainer_window(self):
        trainer_controller = TrainerWindowController(self)
        self.set_view_controller(trainer_controller)
