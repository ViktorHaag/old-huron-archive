+++
title = "Fleshing out a world"
date = 2019-02-25
description = """
Once you have a subsector sketched out for your Traveller players, the next
step is figuring out where in that subsector play is going to start. This will
be some world in the subsector, and it makes sense to spend a bit more
attention on that to flesh it out than just the UPP and trade code information
you have from the subsector stage of prep. Based on the various characters I
know will play, it seemed useful to pick a world in the middle of the map: not
too near the really civilized worlds; close enough to the edges of easily
travelled space to make further exploration more enticing.
"""
thumb = "https://www.futuretimeline.net/blog/images/1489-asteroid-mining-future-timeline.jpg"
thumbattr = 'asteroid mining, <a href="https://www.futuretimeline.net/blog/images/1489-asteroid-mining-future-timeline.jpg">futuretimeline</a>'
categories = ["barbican subsector", "traveller", "rpg"]
tags = ["prep"]
+++

Since our player group includes a Noble with a yacht, a Scout with access to a
scout ship, and several retired marines, it made sense for me to suggest a
starting position that would let the group decide to travel either closer to
civilization or father from it. Also, based on my decision to divide the kinds
of "standard jump routes known" into three kinds (commercial routes available
to the public, plus classified routes available only to the scout and naval
services), it made sense to pick a world where the routes on either side were
accessible for cash, or by using a scout connection.

I had already had it in my head that the world of Willesden, since it had a
"commercial route in" and "scout routes out", would likely be more strictly
controlled by the Scout service, so I decided to suggest the players start at
*Edgware*, a world two jump-ones from Willesden. Edgware seemed to have several
things going for it:

- It had a B class starport, so refined fuel would be available. I thought that
  I'd like to reserve the dangers of unrefined fuel as a matter for discovery
  by the players later on, and not necessarily force it on them out of the
  gate.

- Gas giant(s) in-system, just in case for some reason they decided that
  "getting fuel for free" was what they wanted.

- A tech-level rating of 8, so they could gear up reasonably comfortably.

- Access to nearby worlds without immediate need for jump-two trips.

- Not too close, but within a few weeks' journey of the sub-sector's
  principal worlds, if they decided what they really wanted to do was not
  *explore* but get up to hijinks in more civilized settings.

- Immediate proximity to worlds with something odd going on: the neighbouring
  world of Oval has a really high population, an exotic atmosphere, no
  surface water, and a super high law-level and theocratic central authority;
  the neighbouring world of Gant has a more livable ecology (lots of water,
  dense, tainted atmosphere), but again, a strong central authority, and a
  slightly more impoverished spaceport (no refined fuel).

  Both these neighbour worlds seemed like a good initial place to derive
  complications more than they seem like a good homebase.

So, settling on Edgware as a starting point, we need to start building it out.


What does B000355/B actually mean?
==================================
What we know about Edgware so far:

.. code::

   Edgware    B000355/B    Sb, Ni, Gg, Ab

This brief line of stats tells us some interesting stuff, just like knowing the
RPG stats for a character can lead us to form a simple picture of what the
character is like. Here's how I described the numbers for my players:

     **Features**. The system has a Scout Base, one or more Gas Giants, and an
     Asteroid Belt. Its population is a bit too low for it to be an industrial
     system, but it's on the verge of industry.

     It has a 'B' class star base, so refined fuel *is* available. The Scout
     base means Scout ships get fuelled by the Scout Service, and the base
     means that Scouts can have access to service data (i.e. navigation and
     such).

     It has no habitable world in-system; the starport is either in a station
     orbiting one of the planets or built into an astroid within/on the edge of
     its astroid belt.

     Its population is order of magnitude thousands of people.

     The law level of 5 means that personal, concealable firearms are
     prohibited. Knives of a modest size are permitted, and shotguns are
     permitted with permits and within certain areas.

     The local government is headed by a Governer, separate from the Scout
     Service personnel (who have their own bureaucracy), who runs the system
     rather like one might find on a commercial industrial platform or large
     ship -- governance is divided up into departments that are nominally in
     charge of various technical tasks, and each of those departments has their
     own reporting structure that all report up into the governor.

Where can we go from here? I decided on two approaches:

- I'd like to use the some of the extended material in *Book 6: Scouts* and the
  *Near Space* [NS]_ original stellar data on the system to bring a bit more
  physical detail to what's really there in the system -- how many gas giants
  are there? Where are they? Are there other planets there? How many stars are
  there? (And perhaps most importantly) what are the general *travel times*
  between the features in the system (i.e. distance from starport to jump
  point, distance from starport to gas giants, and so on). These facts might
  not help players choose narrative paths, but they will help bring the system
  alive and act as a backdrop of "known information" to answer simple questions
  (like "how long do we have to fly in system before we can jump?")

- I'd like to use some of the *encounter* materials from the basic books (or
  the Starter Traveller versions of them) to flesh out some rumours, patrons,
  and the like to give the world *wider playable texture*. These resources will
  help me support the pushing the first adventure forward and let the players
  make some choices about what they investigate and follow up on.

The rest of this post will deal with the first of these approaches; I'll leave
the second approach for a subsequent post.


Edgware's wider system
======================

Traveller's basic book gives you a way to generate simple data for "the main
world" in a system, whatever that main world presence might be: it could be a
planet (like Earth), a space-station, a base on a moon surrounding a gas giant,
and so forth. Traveller explicitly leaves that up to the referee to
decide. *Book 6: Scouts* gives you a system for helping to further determine
detail for a star system beyond just the main world.

The *Near Space* [NS]_ book provides more information for the system that
contains my Edgware:

* The real-world star system for Edgware is Eggen 372, a single-star system
  with a real-world spectral type of `WD` (*Near Space* uses the code `WD` to
  cover all the white dwarf sub-classifications; in reality, I believe that
  Eggen 372's currently understood
  `real-world spectral class <http://www.stellar-database.com/scripts/search_star.exe?ID=124100>`_ is `DXP9`.)

* The system has one asteroid belt, and one gas giant.

* The main world's temperature range is "Cold", which isn't at all surprising
  given its star.
  
**Star type**. The *Scouts* book does not provide good info for how to use
`DXP9` spectral types (partly because it seems to me that the `DX` designation
means "we can't really tell what the spectral type classification for this star
should be"), however, if we look at the ISDB indication for its visual
luminosity and its apparent diameter, the closest match seems to peg its
spectral class at `DG` as most similar on that basis.

**Orbital features**. A `DG` type star is too feeble to have a habitable zone,
according to the *Scouts* book. According to the table of zones, a `DG` type
star has five orbital zones available, all "outer". First we place the gas giant
and belt in the available zones, and determine that none of the other available
orbits are empty. Then we generate basic planet attributes for the additional
planets in the system, including how many satellites they may have.

One interesting thing to fall out of this process is to note that the Eggen
372/II (the second planet in the system) has two moons, and also has a
population of `2` (or, order hundreds). It may be that there's an outpost
further in-system from the asteroid belt that has the main "world" (dubbed
"Edgware station") -- why it's there is for further thought.

Grabbing some names from around Edgware tube station using Google Maps gives us
some names to slap on planets in the Edgware system.

===== ================================ ========== ===========
Edgware (Eggen 372)                               B000355/B
------------------------------------------------- -----------
Orbit Feature                          Satellites Feature UPP
===== ================================ ========== ===========
0     Stonegrove (Eggen 372/I)                    xS000
1     Rectory (Eggen 372/II)           2          x2002
--    -- i
--    -- ii     
2     Edgware station (asteroid belt)             B000355/B
3     Hale (Eggen 372/III)             8          L gas giant
--    -- i
--    -- ii
--    -- Hale station                             x0001
--    -- iv
--    -- v
--    -- vi
--    -- vii 
--    -- viii
4     Whitchurch (Eggen 372/IV)        3          x2000
--    -- i
--    -- ii
--    -- iii
===== ================================ ========== ===========

We can dive down another level of detail and figure out if there's anything on
any of those moons that's meaningful by generating UPP stats for them, too. I
won't bother at this point except to arbitrarily put a "station" of some sort
on the third moon of Hale (the gas giant), with population of `1` (order tens).

.. sidebar:: calculating travel time

   Because using a web-browser calculator to do math when you could use Python
   instead is silly:

   .. class:: smaller

   .. code:: python

      import math
      def traveltime(km,g):
       da = (km * 1000) / (g * 9.80665)
       secs = 2 * (math.sqrt(da))
       return 'Hrs: {}  Days: {}'.format(
             secs/3600,
             secs/86400)

**Travel times**. One aspect of this system detail is knowing how long it takes
to travel from one place in-system to another. The planetary orbits have radius
lengths, so roughly speaking, the travel time between two orbits would range
from that value, up to twice the value, depending on where in-orbit the start
and end point of a trip are actually relative to one another (in actual fact,
because orbits aren't always circular or arranged on a flat plane, it's
probably more complicated than that, but I only want to know in rough terms
what the travel times are between features). For Edgeware's system then:

* Travel from Edgware Station to either Hale, the gas giant, or the outpost on
  Rectory is a trip of about 70 million km on average; at 1G that's "about two
  days", and at 2G that's "about a day and a half".

* Travel between Rectory and Hale is a trip of about 135 million km on average;
  at 1G that's "about two and three-quarter days", and at 2G that's "about two
  days".

* Travel from Edgware Station to a jump point is likely pretty fast since the
  gravity disturbance from the asteroid field is minimal; let's say the safe
  jump distance from Edgware is about 80,000 km (about half the distance that's
  a safe jump distance from a size 1 world); at 1G that's "about an hour and a
  half", and at 2G that's "about an hour".

  Travel from Rectory to a jump point is about 320,000 km; at 1G that's "just
  over three hours", and at 2G that's "about two and a quarter hours".

  Travel from Hale to a jump point is *long*. We can estimate that Hale (as a
  large gas giant) has a diameter that's about 230,000 km [GG]_, and a safe jump
  distance is 100 diameters, or 23 million km; at 1G that's a trip of "just
  over a day", and at 2G that's "about three-quarters of a day".

**Scout base**. The question of where to put the Scout base is interesting; is
it co-located with the main world at Edgware, in the belt? Or is it elsewhere
in-system. I like the idea that it's co-located, providing for cooperation but
also cheek-by-jowl tension with the local authority. Thus, the population on
Rectory and Hale station are for some reason other than the scout base:
listening posts, small scientific research stations, and so forth.

At this point, I think we have all the physical detail for the system that we
need. Now we have a better idea of what the system looks like, and how the
local lay of the land might look, and we can use that information to help seed
some tables for encounters (rumours and patrons, and so on).


....

.. [NS] :title:`Near Space`, https://rpggeek.com/rpgitem/211119/near-space

.. [GG] :title:`Gas Giants in Traveller`, http://wiki.travellerrpg.com/Gas_Giant


    
.. |br| raw:: html

   <br/>

.. |_| unicode:: 0xA0
   :trim:

.. |__| unicode:: 0xA0 0xA0
   :trim:
