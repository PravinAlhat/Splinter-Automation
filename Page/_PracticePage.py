from Splinter_Project.Base._baseClass import baseClass
import time
from Splinter_Project.loggingPackage.custom_logger import customlogger as cln

class practicePage():

    _tpObj = baseClass()
    #_url = 'https://learn.letskodeit.com/p/practice'
    _url = 'https://learn.letskodeit.info/t/hello'
    _ApplicationName = 'Lets code it application'
    _t_log = cln(loglevel='DEBUG')

    def openApplication(self):
        self._tpObj._BG_broswerLanunch('chrome', self._url)
        if self._tpObj.browser.title == "Practice | Let's Kode It":
            print('Practice page is successfully launched')
            self._t_log.info('Application is successfully launched')
            self._tpObj._B_screenShot("HomePage")
        else:
            print('Page is not successfully launched')
            self._t_log.error('Application is not launched')
            self._tpObj.browser.quit()

    def workingWithRadioButtons(self, *args):
        #self._tpObj._BG_broswerLanunch(browserType, url)
        radioBtns = self._tpObj._BG_getElement('id','radio-btn-example')
        #print(radioBtns.value)
        for arg in args:
            if arg in radioBtns.value:
                if arg == 'BMW':
                    self._tpObj._BG_getElement('xpath',"//input[@id='bmwradio']").click()
                    time.sleep(2)
                    print('Radio button "{}" is successfully clicked'.format(arg))
                if arg == 'Benz':
                    self._tpObj._BG_getElement('xpath', "//input[@id='benzradio']").click()
                    time.sleep(2)
                    print('Radio button "{}" is successfully clicked'.format(arg))
                if arg == 'Honda':
                    self._tpObj._BG_getElement('xpath', "//input[@id='hondaradio']").click()
                    time.sleep(2)
                    print('Radio button "{}" is successfully clicked'.format(arg))
                self._tpObj._B_screenShot("Radio button{}".format(arg))

    def workingWithDropDown(self, locator, *args):
        '''# Approach # 1
        eleDropDown = self._tpObj._BG_getElement('xpath',"//select[@id='carselect']")
        #eleDropDown.select('benz')
        for option in eleDropDown.find_by_tag('option'):
            for arg in args:
                if option.text.strip() == arg:
                    option.click()'''

        # Approach # 2
        self._tpObj._BG_dropDownElementSection(locator, *args)
        for arg in args:
            print('Item "{}" is successfully selected from the drop down'.format(arg))



    def workingWithMultiSelect(self, *args):
        mulSelect = self._tpObj._BG_getElement('xpath',"//select[@id='multiple-select-example']")
        for option in mulSelect.find_by_tag('option'):
            for arg in args:
                    if option.text == arg:
                        option.click()
                        print('Option "{}" is successfully selected from the drop down'.format(arg))
                    else:
                        print('Option "{}" is not present in the drop down'.format(arg))

    def workingWithCheckBox(self, locator, *args):
        self._tpObj._BG_checkBoxSelect(locator, *args)


    def workingWithSwitchWindow(self):
        all_windows = self._tpObj._BG_switchWindowExample('id','openwindow')
        window = all_windows[1]
        window.is_current = True
        print('New window "{}" is active'.format(window))
        self._tpObj.browser.driver.maximize_window()
        self._tpObj.browser.fill('query','python')
        window.close()
        window = all_windows[0]
        window.is_current = True
        print('Parent window "{}" is activated now'.format(window))

    def navigateToTab(self):
        self._tpObj.browser.click_link_by_href('http://letskodeit.teachable.com/courses')
        all_windows = self._tpObj._BG_navigateToNewTab()
        window = all_windows[1]
        window.is_current = True
        pageTitle = self._tpObj.browser.title
        isElpresent = self._tpObj.browser.is_element_present_by_id('search-courses')
        if isElpresent == True:
            print('New tab with title {} is opened'.format(pageTitle))
            self._tpObj.browser.fill('query','Java')
            search_Btn = self._tpObj._BG_getElement('id','search-course-button')
            search_Btn.click()
        else:
            print('New tab is not opened')

    def browserClose(self):
        self._tpObj._BG_closeBrowser()
