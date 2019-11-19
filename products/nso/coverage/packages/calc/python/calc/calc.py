# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.dp import Action


class CalcAction(Action):
    """calc action."""

    @Action.action
    def cb_action(self, uinfo, name, keypath, user_input, output):
        """cb_action."""
        first = user_input.number_a
        second = user_input.number_b
        value = False
        if user_input.operation == "addition":
            message = f"{first} + {second} ="
            value = first + second
        elif user_input.operation == "subtraction":
            message = f"{first} - {second} ="
            value = first - second
        elif user_input.operation == "multiplication":
            message = f"{first} * {second} ="
            value = first * second
        elif user_input.operation == "division":
            try:
                message = f"{first} / {second} ="
                value = round(first / second, 2)
            except ZeroDivisionError:
                message = "You have to pay extra for that operation"

        output.message = message
        if value is not False:
            output.value = value


class NSOAction(ncs.application.Application):
    """Action."""

    def setup(self):
        self.log.info("Action RUNNING")
        self.register_action("calc", CalcAction)

    def teardown(self):
        self.log.info("Action FINISHED")
