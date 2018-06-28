#!/usr/bin/env python

from PIL import Image
import os, sys
import json

converter = {".gif": ".gif", ".jpg": ".jpg", ".jpeg": ".jpg", ".png": ".png"}
sizes = {}


def addSize(filename, im):
    width, height = im.size
    post = '-'.join(filename.split('-')[:-1])
    if post not in sizes:
        sizes[post] = {}
    sizes[post][filename] = "%sx%s" % (width, height)

def resizeImage(infile, suffix, output_dir, size):
    filename = os.path.splitext(os.path.basename(infile))[0]
    extension = os.path.splitext(infile)[1].lower()
    if extension == '':
        return
    try:
        outfile = os.path.join(output_dir, filename) + suffix + converter[extension]
    except Exception as e:
        print filename
        raise e

    if infile != outfile:
        try :
            print("looking at %s" % (infile,))
            im = Image.open(infile)
            addSize(filename, im)
            if not os.path.isfile(outfile):
                im.thumbnail(size, Image.ANTIALIAS)
                im.save(outfile)
        except IOError:
            print("cannot reduce image for %s" % infile)


if __name__=="__main__":
    print("generating thumbnails")
    output_dir_name = "thumbnail"
    img_dir = os.path.join(os.getcwd(), "../assets/img")

    if not os.path.exists(os.path.join(img_dir,output_dir_name)):
        os.mkdir(os.path.join(img_dir,output_dir))

    for file in os.listdir(img_dir):
        if os.path.isfile(os.path.join(img_dir, file)):
            infile = os.path.join(img_dir,file)
            outdir = os.path.join(img_dir,output_dir_name)
            resizeImage(infile, "_thumb_200", outdir, (200,200))
            resizeImage(infile, "_thumb_800", outdir, (800,800))

    for post in sizes:
        with open('../assets/img/sizes/%s.js' % (post,), 'w') as outfile:
            json_data = json.dumps(sizes[post])
            prefix = "if (typeof SIZES == 'undefined') {var SIZES = {}}; SIZES['%s'] =" % (post)
            suffix = ";"
            outfile.write(prefix + json_data + suffix)
