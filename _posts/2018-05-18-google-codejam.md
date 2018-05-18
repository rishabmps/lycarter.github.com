---
layout: post
title: "Google Codejam 2018"
author: "Landon"
math: true
tags:
- thoughts
---

I participated in Google Code Jam for the first time last year, making it through the first two rounds to the round of 3000. I looked at the problems in the round of 3000 last year, but didn't happen to have time to actually make a good effort at solving any of them.

This year I'm competing again, and writing this post as I go along. Once again, I'm not super invested in the competition, but I'd like to at least match last year's result.

## Qualification Round (drafted 4/7/18)

I glanced at the problems Friday night shortly after the release, but then got distracted playing a game of _Werewords_ with my roommates and finishing reading _Ready Player One_. On Saturday morning, I woke up early and looked at the problems again, intending to get enough points in the morning to guarantee moving on. I opened Cubic UFO first and started drawing some things out. I pretty quickly worked out the geometry as either a rectangle or a hexagon. The rectangle covered cases for \\(A \leq \sqrt{2} \\), and the hexagon covered larger cases. I worked out the specifics of the geometry after a half hour of struggling to remember how trig works, and coded up a quick binary search numerical solver, determining that binary search would be fast enough for the input spec. Unfortunately, the server was experiencing high load, and wouldn't accept my answer before I had to head out for the day. Edit: Turns out that my solution for the hexagon case was wrong - I probably swapped a sign somewhere on accident.

I came back later in the day to find that my answer had *not* been accepted, and with very little to debug with, I decided to just do the first two problems and call it a day. Saving The Universe Again I quickly worked out a bucket system, where each shot was in a certain power bucket. The President could swap commands to move a shot down one bucket, halving its power. After that realization, the coding was a straightforward greedy simulation. When submitting that problem, I realized that my output line for Cubic UFO had been missing a colon after copying it over for the new problem, so I fixed that and resubmitted Cubic UFO. Since the server had been fixed, both solutions went through and were marked correct.

Now that the server was working again, I decided to go ahead and finish up the remaining two problems. I pretty quickly realized that Trouble Sort was flawed because it could not change the parity of any element, and coded up a solution with a dictionary of `{element value -> (count_even, count_odd)}`, which then subtracted from the same dictionary after sorting. The first time a count went negative on the second pass was the problem element. This isn't exactly what the problem was asking for, but as it turns out, the two are equivalent. I didn't even realize until reading over the problem again to write this blog post. Go figure.

For the final problem, Go, Gopher!, I decided that a clever predictive algorithm probably wasn't necessary (or if it was, I didn't care enough to code it). I started by squaring off the area into a low-aspect-ratio rectangle (in retrospect, I could have hard-coded 5x4 and 15x14). I first approached with an algorithm that would calculate the "expected value" of each interior cell of my target rectangle, then realized that I could carry this information over for each step, so I refactored to keep track of the expected value of each cell, commanding the gopher to dig at the best cell. This turned out to work just fine on pretty much the first try (modulo syntax errors and off-by-one errors), completing the contest. Final "actual time" per problem: it was about 55, 15, 15, and 30 mins for Cubic UFO, Saving The Universe Again, Trouble Sort, and Go, Gopher!, respectively. I felt pretty rusty at the beginning, but was feeling better by the end. Total score: 79/100, and an easy qualification to Round 1.

## Round 1 (completed 5/18/18)

I was busy during round 1A, traveling to NYC for a weekend trip.

During 1B, I started by coding Rounding Error, submitting a bit less than an hour into the contest. Reading the analysis, I definitely solved the full problem correctly, including the greedy approach. Unfortunately, my implementation had some sort of bug, or perhaps I missed a corner case. Anyway, didn't get it. I looked for the bug for about 10 minutes before deciding to move on.

Mysterious Road Signs looked pretty difficult for the amount of points it was worth, so I decided to skip it and look at Transmutation. I decided that I would just attempt Test set 1 with a naive approach, and coded that up in about an hour, submitting at 1:41 out of 2:30. Unfortunately, my implementation for this problem *also* had a bug.

At that point, I decided I didn't quite care enough to debug - both my solution to Rounding Error and Transmutation passed all of the test cases I gave them, so I would have to try to hunt down some corner case that I was missing, which didn't sound fun. I got 0 points, and didn't advance.

And then round 1C started at like 5am, which definitely wasn't worth waking up for.

## Conclusion

Turns out, I'm pretty rusty at coding - I've barely done any coding since the end of my internship last year, and none under any sort of time pressure (even loose time constraints like the assignment being due the next day). The problems were pretty interesting to look at though, and kept me at least a little sharp. It'll be interesting to attempt it again next year after coding full-time for 8 months. Hopefully I'll do better then? Maybe I'll even practice a bit :P

As always, thanks for reading!