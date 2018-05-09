---
layout: post
title: "Jekyll Site Improvements"
author: "Landon"
tags:
- meta
---

I'll talk about some of the things I've done to make this site a bit more my own, or upgrade it a bit. You can also follow along in real-time by following the [source](https://github.com/lycarter/lycarter.github.com)

## Customized fonts and colors
This was one of the first things I did, and one of the reasons I moved away from Blogger - it was very difficult to customize Blogger's appearance, With Jekyll, it's much easier, and Tale has extremely nice scss support, and nice a particularly nice variables.scss file. I've never dealt with scss before, but it was super easy to figure out and change. Commit [`9faf7e0`](https://github.com/lycarter/lycarter.github.com/commit/9faf7e06ed6dae4a9065417798e4d7f97b8c018e#diff-a747c56a582f71180f6c87cc19d7bae9)

## Customized layout
Since Jekyll is a normal content site with a good templating engine, it's pretty easy to customize page layout too, just by editing the layout files. You can also add custom layouts for specific posts, which I'll cover when I talk about Mathjax. I made a few changes early on in commit [`492a6d5`](https://github.com/lycarter/lycarter.github.com/commit/492a6d59076fff15e9c9365edd0ae191bb3ee4f8) and commit [`78a49e2`](https://github.com/lycarter/lycarter.github.com/commit/78a49e226a7a9d19a45e4050c636df8759be0f61).

## Thumbnail generation
One of the things I really wanted in my new site was a seamless way to integrate photos. I still haven't gotten it where I want it (I wrote up a [draft](https://github.com/lycarter/lycarter.github.com/blob/master/_drafts/2018-03-19-content-vs-perfection.md) on that), but one thing I did add was a thumbnail generation script in commit [`46473e3`](https://github.com/lycarter/lycarter.github.com/commit/46473e3efa922c3f4e51ba9b60872bebbe16de6e). Unfortunately, it does need to be triggered manually.

## Mathjax support
This was my first foray into custom front matter, adding a `math: true` tag to my front matter enables a code block that loads mathjax. This is pretty cool - I could just enable mathjax on every page, but by only loading it when needed, I can make pages more lightweight and load faster. That was added to `_layouts/post.html` in commit [`627c82e`](https://github.com/lycarter/lycarter.github.com/commit/627c82e3132542b9395a0b8afbdf92c1014ee107#diff-663f387b6a1a407ab38de055a12bc7c8)

## Google Analytics
I wanted at least a little bit of metrics on how many people actually looked at this site, so I added Google Analytics. I should probably add a customization so that analytics is only added on the live site, because I definitely pollute my data when I'm editing the site locally. That's a task for later, though. Analytics was added in commit [`8a78a67`](https://github.com/lycarter/lycarter.github.com/commit/8a78a676fbcdab491330f85305f847d3622b4b34).

## Debugging Page
I didn't actually have anything to debug here, but again while browsing the Jekyll docs, I found some stuff I wanted to try. This is roughly equivalent to a "dumpfile" that you might have in other post-processors, but you can peek at it if you navigate to [/about-technical]({{ '/about-technical' | prepend: site.baseurl }}).

## Jekyll Plugins

I was browsing through the available Jekyll plugins and decided to add a few. They were all ridiculously easy to add, which has been awesome.

### XML Feed
I found one to generate an Atom XML feed, which would be great for anyone that wants to follow with an RSS reader (I use feedly). Turns out it was ridiculously easy to add, just two lines in commit [`19bc218`](https://github.com/lycarter/lycarter.github.com/commit/19bc218d0f675fb795fd5951df3f02852b4117df).

### Sitemap
Adding a sitemap is useful for search engines to correctly crawl your webpage. My secret goal is to push this blog way up on Google results for "Landon Carter" or "Landon Carter Blog" or similar. There are a lot of other Landon Carter's in the world - I need to surpass them all, at least on Google. Anyway, adding a sitemap was literally just another line in `_config.yml` in commit [`52e38fd`](https://github.com/lycarter/lycarter.github.com/commit/52e38fd4a583010a468f069295f93c344734ffa3).

### SEO
Search Engine Optimization adds some meta information to page headers so that search engines know what they're looking at. It also helps with sharing things on Facebook or other social media sites. This one was slightly more involved, at 3 lines of code in commit [`b3c3383`](https://github.com/lycarter/lycarter.github.com/commit/b3c338366b6b62a8ce37010c81779e1c3df219b5). I can also add custom SEO tags, like I did for my [dinner party post]({{ site.baseurl }}{% post_url 2018-05-05-dinner-party %}). I added a custom image so I could share it on Facebook with that specific image selected, you can see that change in commit [`a7ce057`](https://github.com/lycarter/lycarter.github.com/commit/a7ce057a6ac20cfcf20d2802ff2e0b276413990f).

### Tags
This isn't quite a plugin, but is a baked-in feature that you can use if you choose. I didn't start out with it, but now my posts have tags. You can browse posts by tags by navigating to [/tags]({{ '/tags' | prepend: site.baseurl }}). This was inspired by [Rebecca's site](http://rebecca.li/tags/, which has tags, and from the [source code](https://github.com/rebeccali/rliwebsite) of which I borrowed the tags page with some minor tweaks. Added in commit [`bb09075`](https://github.com/lycarter/lycarter.github.com/commit/bb09075e26637d92e123af0dd8d6939e9fd82916).

Overall, this has been a pretty fun project, with nice bite-size pieces to tackle. I've been pleased at how well I can actually keep up with it, even during the semester. Thanks for reading :)