+++
title = "Underpinning Factions in Traveller"
date = 2020-10-14
description = """
Now that I've held up a thumb in the wind about how I might want to use
*M-Space* circles in my *Traveller* games (with some concrete examples to
support my current campaign), I'm going to follow up with some suggestions on
what the descriptive mechanics for them mean in a *Traveller* context, and some
initial rough working out of how to use them. This post is, accordingly, quite
house-rulesy.
"""
thumb = "https://upload.wikimedia.org/wikipedia/en/e/e6/HuntersCover-Murbella%2BEdrik.jpg"
thumbattr = 'guild navigator edrik meets with murbella, <a href="https://upload.wikimedia.org/wikipedia/en/e/e6/HuntersCover-Murbella%2BEdrik.jpg">Stephen Youll</a> '
categories = ["traveller", "m-space", "rpg"]
tags = ["house rules"]
+++

*M-Space* [MS]_ provides a formal way to describe "circles", or groups of people
of various sizes and reaches, organized together for one reason or another,
sharing common goals or beliefs (see MS p156). I decided to borrow this notion
and its approach for my *Classic Traveller* [CT]_ for practical use. In my
borrowing, I decided to call these things "factions" and in a previous post, I
outlined how factions might be described along with some examples for
`factions in the Hounslow system <{{<ref "factions-in-traveller.rst" >}}>`_.

In this post, I'll give a bit more detail on how I'm adapting factions for
*Traveller*.

.. sidebar:: sample faction

   A faction writeup looks like this.

   .. class:: smaller

   +------------------------------------------------------+
   | Scolari Sodality (Organization)                      |
   +======================================================+
   | Fraternal organization native to Hounslow with       |
   | significant power and influence exists primarily to  |
   | solidify the political influence for the wealthy and |
   | long-lived minor houses without sufficient resources |
   | to wield influence on their own. The Sodality        |
   | commands a handful of seats on the Hounslow council, |
   | the exact number varying slightly over time (they do |
   | not officially hold positions; rather, they act as a |
   | voting and influence bloc that contrives to support a|
   | small number of individual members). The Sodality is |
   | by nature radical but insular; their primary aims are|
   | to safeguard and grow the influence of its           |
   | membership, but they have a conservative position    |
   | with respect to engagement with the wider            |
   | Commonwealth.                                        |
   +----------------+-------------------------------------+
   |   **Ideas**    | Anti-Colonial, Power, Wealth        |
   +----------------+-------------------------------------+
   |    **UFP**     | 966                                 |
   +----------------+-------------------------------------+
   | **Attributes** | Connected-3, Legal-1, Media-2,      |
   |                | Politics-2,                         |
   +----------------+-------------------------------------+


Describing factions
-------------------
As in *M-Space* circles, factions get described with a light set of mechanics.
Here's a bit more detail on what these mechanics mean, the range of values I'm
using, and so on. Note what I'm going to write here amounts to detail about how
I'm migrating those rules in *Traveller*, not re-writing them; for full use of
these ideas, you probably want to get yourself a copy of the *M-Space* rule book.


.. sidebar:: Influence

   Measures the impact a faction can have within the wider society.

   .. class:: smaller

   .. list-table::
      :widths: 20,80
      :stub-columns: 1

      * - 0
        - No influence. Faction's ideas are unknown to most people in wider
          society.
      * - 1-4
        - Very little influence. Concepts never reach the corridors of power.
      * - 5-9
        - Moderate influence. In favourable circumstances, faction's concepts can
          shape policy in wider society.
      * - A-D
        - Significant influence. Faction's concepts regularly shape policy and
          set the agenda in wider society.
      * - E-F
        - Major influence. Faction's aims and concepts capture the policy and
          agenda of wider society.


**Type and Descriptor**. Every faction belongs to one of five types:
Organization, Ideology, Corporation, Location, Polity. When writing down the
type of a faction, you also use a *descriptor* that further characterizes it,
for example, "Corporation: Mining Conglomerate". The first four of these are in
*M-Space*; I liked the idea that a "nation" could also be modelled using
factions, and so I added a "Polity" type to the list. Otherwise, I'm treating
types and descriptors exactly as outlined in *M-Space*.


.. sidebar:: Size

   Measures the number of individuals the faction comprises.

   .. class:: smaller

   .. list-table::
      :widths: 20,80
      :stub-columns: 1

      * - 0
        - No members
      * - 1
        - Tens of members
      * - 2
        - Hundreds of members
      * - 3
        - Thousands of members
      * - 4
        - Tens of thousands
      * - 5
        - Hundreds of thousands
      * - 6
        - Millions of members
      * - 7
        - Tens of millions
      * - 8
        - Hundreds of millions
      * - 9
        - Billions of members
      * - A
        - Tens of billions


**Ideas**. I'm using the "ideas" as outlined in *M-Space* (see MS p156-7,166).
I'm not treating their provided list as exhaustive as I don't interpret their
rules to suggest that its list should be. Accordingly, in my examples, I've
added a few ideas that seem at the same general level of scope as the ones on
their list, that more directly tie to my background:

- *Innovation* -- A notion of progress, especially technical progress is
  important to the faction.

- *Anti-Colonialist* -- The faction is explicitly not in favour of central
  Commonwealth authority and pits itself in opposition to same.

- *Research* -- Gaining more knowledge, especially through science, is a goal in
  itself for the faction.

- *Resistance* -- The faction is in active opposition to some other faction.

- *Pro-Commonwealth* -- The faction is explicitly in favour of central
  Commonwealth authority.


.. sidebar:: Resources

   Measures the wealth and property a faction can bring to bear.

   .. class:: smaller

   .. list-table::
      :widths: 20,80
      :stub-columns: 1

      * - 0
        - Destitute.
      * - 1-4
        - Poor.
      * - 5-9
        - Average.
      * - A-D
        - Affluent.
      * - E-F
        - Wealthy.


**Characteristics**. Every faction has three characteristics given numeric
ratings just as with the properties of characters and worlds in *Traveller*:
INFluence, SIZe, and RESources (collected together into a *Universal Faction
Profile* or UFP).

The general meanings for these characteristics is the same as in *M-Space*;
however, the value scales are adapted and specific to *Traveller*; two of the
characteristics range across five groupings (INF and RES) as in *M-Space*,
whereas SIZ is more granular and borrows directly from the population table
familiar to the *Worlds* section of *Traveller* (the UWP population digit).


**Attributes**. Every faction has a variable number of attributes that work
roughly like *Traveller* skills; they describe how a faction implements its
ideas and how it reaches its goals. As with *Traveller* skills, we use that same
rough rating system. A rating of `0` indicates only a very basic level of
capability (rather than no capability at all), with a swiftly widening scale of
capability as attribute levels increase.

I'm using the list of likely attributes from *M-Space* (on pages 160-1) as the
basic list, but as with *Ideas*, I view the list as somewhat open-ended and so
specific factions may have attributes not found on the *M-Space* list (for
example, the `Research` attribute).


**Rank**. Every faction, as with *Traveller* careers, comes with a concept of
rank, with values ranging from `0` to `6` (where the rank and file members of a
faction all have a rank of `0` and those with some higher prestigious rank
ranging from `1` up to `6`). It's up to the referee to determine when, and how,
a character might raise in rank within a faction; as a matter of guidance, it's
quite rare for anyone with only a casual relationship with a faction to have a
rank above `0`.


**More**. *M-Space* also includes a number of other factors that can describe
factions: *benefits* that a faction can offer its members; *trait* keywords that
are neither precisely ideas nor attributes but similar in spirit; and a host of
narrative *details* that comprise historical information about the faction,
policies and requirements to join and leave, and so forth; *structure* to
generally describe how the faction organizes itself.


Using factions
--------------

The use of factions in play is quite straight-forward and can follow the suggestions
found in *M-Space* adapted in a *Traveller* spirit. This basically means if you
need to make tests with respect to factions, use a standard dice throw (roll
2D6) and use attribute ratings in a fashion that seems appropriate to the
circumstances; for example, you can add an attribute rating to the throw and use
the result to help interpret the outcome of the test at hand.

For the most part, the idea of factions here is  merely a way to formally
describe a portion of the campaign setting, as one might do worlds, star ships,
animals, patrons, and so on.


....

.. [CT] :title:`Traveller (Classic)`, https://rpggeek.com/rpg/491/traveller-classic

.. [MS] :title:`M-Space`, https://rpggeek.com/rpgitem/210934/m-space

.. |br| raw:: html

   <br/>

.. |sp| raw:: html

   &nbsp;

.. |_| unicode:: 0xA0
   :trim:

.. |__| unicode:: 0xA0 0xA0
   :trim:
