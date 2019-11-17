# -*- mode: python; python-indent: 4 -*-
import datetime

import ncs
from ncs.dp import Action


def time_of_day(hour):
    """Return pleasant time of day."""

    if hour < 5:
        return "night"
    elif hour >= 5 and hour < 12:
        return "morning"
    elif hour == 12:
        return "noon"
    elif hour > 12 and hour < 18:
        return "afternoon"
    elif hour >= 18 and hour < 19:
        return "dinner time"
    elif hour >= 19:
        return "evening"


class GreetAction(Action):
    """Greet action."""

    @Action.action
    def cb_action(self, uinfo, name, keypath, user_input, output):
        """cb_action."""

        hour = datetime.datetime.now().hour
        period = time_of_day(hour)
        if period == "dinner time" or period == "noon":
            output.message = "You must be getting hungry!"
        else:
            output.message = f"Good {period}!"


class NSOAction(ncs.application.Application):
    """Action."""

    def setup(self):
        self.log.info("Action RUNNING")
        self.register_action("greet", GreetAction)

    def teardown(self):
        self.log.info("Action FINISHED")
