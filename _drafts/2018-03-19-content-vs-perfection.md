---
layout: post
title: "Content vs Perfection: Photo Galleries"
author: "Landon"
tags:
- thoughts
---

I started the draft on that [photography post]({{ site.baseurl }}{% post_url 2018-03-14-photography %}) on 3/8 or so. As of 3/19, I still haven't posted it. The reason, of course, was seeking perfection. I started that draft when I still used Blogger, on which I wrote only a single post before switching to Jekyll because it's more customizable. I wanted to include a mini-gallery in the photography post, and was unhappy with Blogger's options.

After making the switch to Jekyll, I was really happy with the templating and customizability. I feel like I have a much better method to customize this site than if I'd stuck with Blogger, and I can include lots more custom scripts, custom js, etc. Unfortunately, I still haven't found and installed a gallery that I like, and haven't come up with a workflow for posting pictures that I like. Some considerations in no particular order: I want the process of adding a photo to the site to be relatively painless. I want the option to resize thumbnails later if I adjust the formatting of the site. I want the process of referring to a photo from the post source to be relatively small/compact (eg, give it a filename, some script automatically fills in the different size thumbnail options). I want the aesthetics to look good, and to have a similar backend for single photos and for galleries. I want the option to host galleries, which can be relatively large.

### Adding a photo should be easy.

I also started thinking about how Github would automatically build my site, and in particular how Github Pages doesn't support third-party Jekyll Plugins, which is kind of annoying. I usually edit the blog posts on my Ubuntu VM, since I've got the full Ruby+Jekyll stack built really nicely, and have no desire to make it work on Windows. The problem with that is that all of my photos aren't readily available from the VM, so the transfer process is slow and manual.

### Resizing Thumbnails should be automated.
I started with a [thumbnail generator](https://github.com/lycarter/lycarter.github.com/blob/master/scripts/thumbnail_generator.py), which is a Python variant of the [Jekyll Gallery Generator](https://github.com/ggreer/jekyll-gallery-generator) that [Rebecca](https://rebecca.li) uses. Rebecca mentioned being unhappy with the plugin, and I didn't love it either. I did like the automatic thumbnail generation, because manually exporting lots of different sizes from Lightroom is annoying, and if I ever wanted to change what size my thumnbails were, I'd have to re-export everything from Lightroom again. I don't even have any images actively on the website yet, and I'm already worrying about this...

### Referring to a photo should be compact.

Right now, I refer to photos something like this:

<p><figure class="highlight"><pre><code class="language-markdown" data-lang="markdown"><span class="p">![</span><span class="nv">Image name</span><span class="p">](</span><span class="sx">{% raw %}{{{% endraw %}</span> <span class="nn">"/assets/img/thumbnail/image_800.jpg"</span> <span class="sx">{% raw %}}}{% endraw %}</span> "alt text")_caption_</code></pre></figure><em>good lord getting that to format correctly was difficult</em></p>


### Aesthetics should look good.

I actually really like the aesthetics of Wordpress's mini-galleries, but I also like [Lightbox](http://lokeshdhakar.com/projects/lightbox2/) pretty well. [This post](https://christianspecht.de/2014/03/08/generating-an-image-gallery-with-jekyll-and-lightbox2/) has some pretty good information on how to accomplish a nice combination of Lightbox and Jekyll. [Photoswipe](http://photoswipe.com/) also looks like a really nice alternative that I probably will look into more. So far I've done none of the above. Whoops.

### Hosting should accommodate galleries.

My full-res photos are large, and since this site is currently being served on Github Pages as a Github repo, there's a 1GB size limit. So then I started going down the rabbit hole of looking into hosting options...I eventually concluded that should I make the switch away from Github Pages, [GCP](https://cloud.google.com/free/) is probably the best way for me to go. For now, I'll stick with Github Pages, and cross that bridge when I need to (when I hit the 1GB size limit).

# Content vs Perfection

But the real point of this post is in the title: **Content vs Perfection**. I wrote the [Hello World]({{ site.baseurl }}{% post_url 2018-03-07-hello-world %}) post in Blogger, with minimal customization and tweaking. As I mentioned in that post, I had started like 3 different blogs in the past, and always got caught up trying to achieve "perfection". I'm a bit of a perfectionist, I think most MIT students are. I've learned for schoolwork or actual work when to allow "good enough" to get that pset or project or code turned in on time, but for personal projects with no deadline, it's hard to let go of the idea of perfect. For this blog in particular though, I don't want to fall into the category of "least interesting man in the world" (see [xkcd 621](https://xkcd.com/621/), panel 3).

Maybe I'll get around to making a better gallery/better image includes, but for now, I'll live with my thumbnail script and annoying file transfers.

While finding that xkcd article above, I also stumbled upon _[Stop Saying "Sorry" And Say "Thank You" Instead](https://www.boredpanda.com/stop-saying-sorry-say-thank-you-comic-yao-xiao/)_, a cool comic that you should read, and then I'll finish this article by saying ~~sorry I didn't get that photography post out earlier~~ thanks for reading!