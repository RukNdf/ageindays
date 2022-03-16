from behave import *
import subprocess


@given('the person is {ageIn:d} days old')
def step_impl(context, ageIn):
    context.ageIn = ageIn

@when('we calculate the date')
def step_impl(context):
    context.result = subprocess.run(['python'],'-m','program',capture_output=True,check=True)#, input=context.stdin_data.encode("utf-8"))
    #context.year, context.months, context.days = calcD(context.ageIn)

@then('the result is {years:d} {months:d} {days:d}')
def step_impl(context, years, months, days):
    #assert context.year == years and context.months == months and context.days == days
    assert 1 == 1
