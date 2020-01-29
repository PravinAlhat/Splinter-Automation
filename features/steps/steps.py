from Splinter_Project.Tests.testRadioButtons import testClass as TC
from behave import *

@given('User is on practice page')
def step_impl(context):
    context.driver = TC()
    context.driver._test_Obj.openApplication()

@when('User clicks radio buttons')
def step_impl(context):
    context.driver.test_RadBtns()

@then('Radio buttons should be selected')
def step_impl(context):
    print("Radio buttons are successfully selected")
    context.driver._test_Obj.browserClose()

