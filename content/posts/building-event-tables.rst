+++
title = "Building event tables"
date = 2018-12-31
description = """
Eventually, one key to old-style sandbox play in any game genre is letting your
dice choice drive the game and that means _event tables_. Later versions of the
original _Traveller_ game actually give more useful support for the referee in
this regard than the original three books; I am going to borrow some of these
techniques from the later editions and add them to the toolkit for my game.
"""
categories = ["traveller", "rpg"]
tags = ["prep", "tools"]
+++

The *Starter* and *Book* editions of the original *Traveller* introduce tables
for random generation of patrons and rumours that the referee can use as
templates, in addition to the random animal encounter table that one can also
find in the original little black books. While this is useful in and of itself,
it's even more useful because of the new table design introduced, leading to
two kinds of table templates which I'll investigate a bit here.

For use in the "`Tufte-inspired <https://edwardtufte.github.io/tufte-css/>`_"
layout I'm using in this blog, these two kinds of table templates that
*Traveller* uses for random events are ideally suited.

It's obvious that the *Traveller* rules explicitly intend you as the referee to
use these different event table types as *tools* or templates to fiddle with,
building specific instances of them for use in your own set of adventures. As
my adventures expand and my players continue to investigate the setting, these
tables (animal encounters, patron encounters, random encounters, rumours) are
going to form the backbone for each setting and situation the players find
themselves in. The tables will exist both "in space" (that is, the sub-settings
and terrain types for each world can have appropriate tables), but also "in
time" (that is, as adventures and campaign time rolls forward, the *contents*
of these tables can adjust over time to account for things discovered, already
done, implications of choices, and so on).


2D wide table type
==================
The *Typical Animal Encounter Table* (Book 3, p35) is a prototypical example of
the 2D wide table; here's a slightly abbreviated excerpt of it. These kinds of
tables typically have 12 rows, one for every result possible on a 2D
throw. When these kinds of tables need to also account for DMs to the throw,
the number of rows expands to account for all the possible throw results.

=== ===================== ======= ===== ======= =========================
CLEAR Terrain                           Regina (A788899-A)
--------------------------------------- ---------------------------------
Die Animal                Weight  Hits  Armour  Wounds & Weapons
=== ===================== ======= ===== ======= =========================
2   1 Hijacker            200kg   18/11 jack    11 |__| teeth A5 F7 S2
3   2 Hunters             12kg    3/7   none    4  |__| claws A5 F4 S1
... ...                   ...     ...   ...     ...
9   1 Chaser              50kg    11/9  none    6  |__| claws+1 A0 F7 S2
10  Event — Howling carnivores. Out of sight, chasers (below) are heard
    howling continuously, if the party spends the night nearby, they may
    attack (throw 7+)
--- ---------------------------------------------------------------------
... ...                   ...     ...   ...     ...
12  1 Killer              200kg   21/12 none    17 |__| as pike A1 F9 S1
=== ===================== ======= ===== ======= =========================

These tables are ideal for accommodating detailed columnar information, along
with the throw value, in a compact way.

However, one side-effect of this table style is that it obscures the fact that
*the chance of rolling each row* varies; this is especially the case if DMs get
involved in the throw. Book 3 includes construction templates for both 2D
(belled throw result chance) and 1D (linear throw result chance) versions of
the animal encounter table to help you determine what spread of animal types
you might want to use when building the table.

D66 narrow table type
=====================

.. sidebar:: D66 matrix table
   :class: titleless

   .. csv-table:: Rumours for DOWNBELOW STATION
      :class: smaller fullwidth
      :widths: auto
      :header-rows: 1
      :stub-columns: 1

      |_|, 1, 2, 3, 4, 5, 6
      1, A, B, C, D, E, F
      2, G, U, U, W, W, H
      3, I, U, Y, Y, W, J
      4, K, X, Z, Z, V, L
      5, M, X, X, V, V, N
      6, O, P, Q, R, S, T

   .. csv-table:: Specific rumours
      :class: smaller fullwidth
      :widths: auto
      :stub-columns: 1

      A, Background information
      B, Minor fact
      C, Major fact
      D, Partial (potentially misleading) fact
      E, Veiled clue
      F, Information leading to trap
      G, Location data
      ..., ...
      Q, Background information
      R, Minor fact
      S, Veiled clue
      T, Misleading clue

   .. csv-table:: General rumours
      :class: smaller fullwidth
      :widths: auto
      :stub-columns: 1

      U, Broad background information
      V, Misleading background information
      W, Reference to library data
      X, General location data
      Y, Specific background data
      Z, Misleading background data

   .. class:: smaller

      Consult this matrix weekly on a throw of 7+; also consult this matrix if
      `Rumour` is a patron encounter result.

The *Starter* and *Book* editions' patron, random event, and rumour tables
introduce the D66 "matrix" type table (a tweaked excerpt of the rumours matrix
table from the rule-book you can see in the nearby sidebar). This kind of table
helps spray a large number (up to 36) of results across a range of
linear-chance throw results, and uses a letter-keying method in the table to
let you more easily manage the occurrence chance for individual results. This
table style also has the advantage that it's narrow, and thus ideal for
presentation in a thin column or sidebar.

To use this table, throw two dice of different colours; one coloured die gets
used to choose the row and one to choose the column (a D66 throw can also
generate a linear range of results from `11` through to `66` — this style of
table just spreads that out into a matrix).

Notice that you can fiddle with the chance of occurrences in two ways,
demonstrated in the example *Rumours Matrix* shown in the rule-book:

- Some entries in the matrix can occur more than once. In this case: all the
  `Specific rumours` results use keys `A` through `T`, and occur only once in
  the matrix; all the `General rumours` results use keys `X` through `Z`, and
  occur more than once — `U` through `X` three times, `Y` and `Z`, twice.

- This duplication can also carry through into the *list of specific rumours*:
  in the rule-book's template, you can see that a "Minor fact" result occurs
  twice, as does "Background information".




.. |br| raw:: html

   <br/>

.. |_| unicode:: 0xA0
   :trim:

.. |__| unicode:: 0xA0 0xA0
   :trim:
