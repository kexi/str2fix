from behave import *
from hamcrest import *
from str2fix import *


@given('I initialize a values with "{val}",{blen}.')
def step_impl(context, val, blen):
    context.val = val
    context.blen = int(blen)


@then('It returns "{expect}".')
def step_impl(context, expect):
    assert_that(convert_with_x(context.val, context.blen), equal_to(expect))
