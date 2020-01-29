from Splinter_Project.Base._baseClass import baseClass
from Splinter_Project.loggingPackage.custom_logger import customlogger as cl
from selenium.webdriver.common.action_chains import ActionChains as AC



class DragAndDrop():

    dd = baseClass()
    


    def test_draganddrop(self):

        self.dd._BG_broswerLanunch(broswerType='chrome',url='https://www.w3schools.com/html/html5_draganddrop.asp')
        s = self.dd._BG_getElement(locator="//div[@id='div1']//img[@id='drag1']", locatorType='xpath')
        target = self.dd._BG_getElement(locator="//div[@id='div2']",locatorType='xpath')
        action = AC(self.dd.browser)
        action.drag_and_drop_by_offset(source=s, xoffset=202, yoffset=427)


tt = DragAndDrop()
tt.test_draganddrop()