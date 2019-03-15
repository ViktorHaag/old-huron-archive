+++
title = "Traveller house rules"
description = """
Here we collect all the house rules and rule edition choices for Traveller
adventures set in my Terran Commonwealth setting. The thematic approach for
these adventures is small empire, conservative tech level, loose central
authority; this aligns well with the
[proto-Traveller](http://wiki.travellerrpg.com/Proto-traveller)
approach to rules.
"""
categories = ["rpg", "traveller"]
tags = ["house rules"]
+++

Fundamental sources
===================
For the basic reference rules, I use the 1981 editions of the Traveller "Little
Black Books" (Books 1 to Book 3) [CT]_, and the early supplements (most
specifically Supplement 4). I have also imported some select rules from the
1977 rules set and the Starter edition rules set; I've quoted them here so that
this page can act as exceptions to the '81 rules rather than having to flip
between multiple sets of rule books.

The Terran Commonwealth setting starts with the stellar data from the *Near
Space* supplement [NS]_ and then fills it out with details generated using the
rules from the World book (see `Subsector data`_ and `World data`_). The four
sub-sectors (one Traveller quadrant) described in *Near Space* represent the
extent of "known space" for all the adventures in this setting.

Subsector data
==============
When generating the subsectors and world data for this setting, I made some
small adjustments to the basic procedures established in *Worlds and
Adventures* (Book 3).

**Starport presence**. I wanted the chances of higher quality starports to
attenuate the farther out we get from Sol, so I used these die modifiers when
rolling on the Starport table:

- Within 5 parsecs (hexes) of Sol: DM -1
- Farther than 5 parsecs from Sol: DM +1

**Primary worlds**. The world(s) in each sub-sector that have the best starport
*and* are closest to Sol, I consider the *primary worlds* for that
sub-sector. Sol itself is, of course, a primary world.

.. sidebar:: Route determination table

   ===========  ==  ==  ==  ==
   Starports    Jump distances
   -----------  --------------
   (by type)    J1  J2  J3  J4
   ===========  ==  ==  ==  ==
   A - A        1   2   3   5
   A - B        1   3   4   5
   A - C        1   4   6   —
   A - D        1   5   —   —
   A - E        2   —   —   —
   B - B        1   3   4   6
   B - C        2   4   6   —
   B - D        3   6   —   —
   B - E        4   —   —   —
   C - C        3   6   —   —
   C - D        4   —   —   —
   C - E        4   —   —   —
   D - D        4   —   —   —
   D - E        5   —   —   —
   E - E        6   —   —   —
   ===========  ==  ==  ==  ==

**Jump routes**. Following the excellent analysis from Chris Kubasik's `Tales
To Astound <https://talestoastound.wordpress.com/traveller-out-of-the-box/>`_
Traveller blog series, I decided to use the jump route procedure from the 1977
edition of Book 3, and not use the travel zones or communication routes from
the 1981 edition

For each world in the sector, consider all the worlds within four hexes. For
each world pair, find the corresponding row and column in the `Route
determination table` to find the chance that a known jump route exists between
the two:

- Row corresponding to the starport types of the two worlds.

- Column corresponding to the jump distance between the two worlds (number of
  hexes).

Jump route chance is the number at the row-column intersection; if the
intersection has `—`, no known route will exist.

Throw 1D greater than the jump route chance for a known jump route to exist.

- +1 DM if one of the worlds is a subsector *primary world*.


World data
==========

**Tech level**. Sol is tech-level 15; all worlds other than Sol are capped at
TL 14, so results greater than 14 are set at 14.

**Population multiplier**.


....

.. [CE] :title:`Cepheus Engine`

.. [CT] :title:`Traveller (Classic)`, https://rpggeek.com/rpg/491/traveller-classic

.. [NS] :title:`Near Space`, https://rpggeek.com/rpgitem/211119/near-space


.. |br| raw:: html

   <br/>

.. |_| unicode:: 0xA0
   :trim:
