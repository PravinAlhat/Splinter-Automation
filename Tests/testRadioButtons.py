from Splinter_Project.Page._PracticePage import practicePage
import unittest
import pytest

class testClass(unittest.TestCase):
    _test_Obj = practicePage()

    @classmethod
    def setUpClass(cls) -> None:
        cls._test_Obj.browserClose()
        cls._test_Obj.openApplication()

    def setUp(self) -> None:
        print('<<===========Test method execution has been started========>>')

    @pytest.mark.run(order=1)
    def test_RadBtns(self):
        self._test_Obj.workingWithRadioButtons('BMW','Benz')

    @pytest.mark.run(order=2)
    def test_DropDown(self):
        self._test_Obj.workingWithDropDown('cars','honda')

    @pytest.mark.run(order=4)
    def test_mulSelect(self):
        self._test_Obj.workingWithMultiSelect('Apple','Peach')

    @pytest.mark.run(order=3)
    def test_checkBox(self):
        self._test_Obj.workingWithCheckBox('cars','benz','honda')

    @pytest.mark.run(order=5)
    def test_switchWindow(self):
        self._test_Obj.workingWithSwitchWindow()

    @pytest.mark.run(order=6)
    def test_newWindowNavigation(self):
        self._test_Obj.navigateToTab()

    def tearDown(self) -> None:
        print('<<=========Test method execution has been finished===========>>')

    @classmethod
    def tearDownClass(cls) -> None:
        cls._test_Obj.browserClose()
        print('All the tests have been successfully executed and browser is closed')




