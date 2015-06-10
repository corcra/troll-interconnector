#!/bin/python
# One script to rule them and in the darkness troll them.

import madbot

selector = '#hashtag'

# --- option one: find target, then find match --- #
# identify target to neutralise
target = madbot.get_target(selector)
# find a partner for them
match = madbot.get_match(target, selector)

# --- option two: find many targets, pair them off --- #
# find many potential targets
targets = madbot.find_trolls(selector)
# pair them off
target, match = madbot.pair_trolls(targets)

# --- now manage the mischief --- #
tweet = madbot.form_connection(match, target, selector)
# ... and then you send the tweet, somehow (API-implementation specific)
