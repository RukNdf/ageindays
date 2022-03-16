from behave import *
import subprocess
from a import *
from io import StringIO
import sys


@given('the person is {ageIn:d} days old')
def step_impl(context, ageIn):
    context.ageIn = ageIn

@when('we calculate the date')
def step_impl(context):
    realOut = sys.stdout
    tempOut = StringIO()
    sys.stdout = tempOut
    printF(calcD(context.ageIn))
    sys.stdout = realOut
    context.yearS, context.monthS, context.dayS = tempOut.getvalue().split('\n')[:3]

@then('the result is {years} years {months} months {days} days')
def step_impl(context, years, months, days):
    assert context.yearS == (years+' ano(s)') 
    assert context.monthS == (months +' mes(es)') 
    assert context.dayS == (days +' dia(s)')