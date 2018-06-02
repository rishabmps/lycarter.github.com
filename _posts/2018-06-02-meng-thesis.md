---
layout: post
title: "MEng Thesis"
author: "Landon"
math: true
tags:
- thoughts
---

Last week, I finished up my MEng thesis and turned it in, which was my last task to accomplish before graduating, again. I've added it to my [projects]({{ '/projects' | prepend: site.baseurl }}) page.

My thesis was titled "[Multi-Path Planning for Hydraulic Fluid Routing]({{ "/assets/pdf/MIT_Thesis.pdf" }})," and focused on a path-planning algorithm I started working on during a SuperUROP, designed to route hydraulic fluid pipes within a 3D printed robot. The algorithm is far more general than that though - it solves the circuit-routing problem, which has multiple paths routed through a common space without intersecting.

# Summary

As far as I can tell, there aren't any other published exact solutions to the general circuit-routing problem, mostly because such a thing is not very useful in most scenarios - the problem is NP-Complete, so exact solutions are slow (probably, I never actually proved it, but variations are). Furthermore, exact solutions are very rarely useful - an approximate solution is usually good enough, and is much faster to compute. In the special case where \\(z = 2\\), topology-based algorithms are quite successful. This is particularly relevant for the problem's namesake-circuit routing, especially on 2-layer PCBs.

Nevertheless, it was an interesting problem to work on. The solution that I came up with was basically a series of nested graph searches - each path is planned independently using a variant of A\*, then collisions between the paths are checked, then the outer "graph search" splits - when two paths intersect, at most one of them can use the node in question in the optimal solution, so two branches are created - one where one path can use the node, and one where the other path can use the node. The paths are then replanned with the new constraints, and the procedure repeats until an optimal solution is found. That's just a rough overview - see the paper for more details.

# LPA*

One cool thing that I found was this algorithm called "Lifelong Planning A\*", aka LPA\*. This algorithm was developed by [Koenig et al in 2005](https://www.cs.cmu.edu/~maxim/files/aij04.pdf). This is a variant of A\* which remembers the intermediate values and updates them intelligently when movement costs are updated (ie, when a node is marked as unusable in the outer graph search). This allows replans to be extremely fast, a key feature in the algorithm I developed.

# Optimizations

I managed to get the algorithm working last year, during my SuperUROP, but it was still fairly slow. For my MEng, I focused on speed improvements and benchmarking.

## Code Profiling

I had a few theories about things that could be optimized in the code based on my own reasoning about the code, but the best way to figure out the actual steps to take to maximize the impact was to profile the code. I used [cProfile](https://docs.python.org/2/library/profile.html) to profile the code and [SnakeViz](https://jiffyclub.github.io/snakeviz/) to visualize it. This was amazingly easy to get working, and the visualizations were really pretty. You can (sorta) see the visualization [here]( {{ "/assets/other/meng-profiling/profiling_results.htm" }} ), but this is just a saved copy of the webpage. Without snakeviz actually running and serving things correctly, the page misbehaves slightly. If you'd like to see them for real, just install SnakeViz and grab the profiling results from my [GitHub repo](https://github.com/lycarter/mpa-star).

## Priority Queue Optimization

After profiling the code, I noticed that my priority queue implementation was very slow. I'd noted when I wrote it that the `remove` operation was just \\(O(n)\\), and that really showed. I investigated and implemented a number of other priority queue implementations, and wound up settling on wrapping [SortedSets](http://www.grantjenks.com/docs/sortedcontainers/) from the Sorted Containers Python library. [Treap](http://stromberg.dnsalias.org/~dstromberg/treap/), also from PyPI, also performed quite well, but had a bit more overhead. Turns out Python lists are *really fast*.

By optimizing the priority queue, I improved performance by about 70%.

## Caching Layer

In certain scenarios, different branches of the outer graph search can converge to contain identical inner graph searches. Without a caching layer on inner graph searches, duplicate work will be done to solve both inner graph searches, so I added a caching layer. This turned out to be a bit difficult - chasing pointers in Python isn't very intuitive, and I actually had some objects being duplicated that I didn't want duplicated. I eventually solved that and finished adding the caching layer. The added benefit was a significantly reduced memory footprint, not that the algorithm tended to have an unwieldy memory footprint anyway.

By adding the caching layer, I improved performance by an additional 50%.

# Conclusion

Frankly, I didn't have as much time to work on this research or my thesis as I would have liked. I was busy [TA'ing 2.009 and 2.744]({{ site.baseurl }}{% post_url 2018-05-18-taing-009-744 %}), which meant the amount of time I had to dedicate to research was pretty small. With some more time, I probably would have reimplemented everything in Java, or even better, learned C++ and implemented it in that. Java especially would have made debugging the caching layer addition quite a bit easier - I had a hell of a time debugging that without type-checking. Either reimplementation probably would have improved performance by a healthy margin. Anyway, feel free to shoot me a message or pull request if there's things you're interested in.

On the (very unlikely) chance that you need to reference this work, here's the appropriate BibTeX citation (to be updated later with a [DSpace](https://dspace.mit.edu/) link as well):

```
@thesis{carter_2018,
	place={Cambridge},
	title={Multi-Path Planning for Hydraulic Fluid Routing},
	url={https://www.lycarter.com/assets/pdf/MIT_Thesis.pdf},
	school={MIT},
	author={Carter, Landon Y},
	year={2018}
}
```

Thanks for reading! :)