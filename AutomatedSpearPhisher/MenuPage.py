from CommonFrame import CommonFrame
from helpers import *
#-------------------------------------------Selection--------------------------------------------------
class MenuPage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        #Set center subheading
        setSubHeading(self, 'Main Menu')
        #selection label
        createLeftSubHeading(self, 'Please make a selection')
        #buttons/frame to select which application to Scrape
        self.createButtonFrame()
        button_frame = self.getButtonFrame()
        button_manager = ButtonManager(button_frame, controller)
        
        #spear fish symbol
        createPictureInFrame(button_frame, 'images/fish.png')

        # create selection button to go to pages
        button_manager.autoCreateChangePageButton('FacebookPage', 'Scrape Facebook')
        button_manager.autoCreateChangePageButton('TwitterPage', 'Scrape Twitter')
        button_manager.autoCreateChangePageButton('LoginPage', 'Exit')