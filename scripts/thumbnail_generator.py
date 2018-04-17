#!/usr/bin/env python

from PIL import Image
import os, sys

def resizeImage(infile, suffix="_thumb", output_dir="", size=(1024,768)):
    filename = os.path.splitext(os.path.basename(infile))[0]
    outfile = os.path.join(output_dir, filename)+suffix+".jpg"

    if infile != outfile:
        try :
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile,"JPEG")
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
            print("resizing %s" % (infile,))
            outdir = os.path.join(img_dir,output_dir_name)
            resizeImage(infile, "_thumb_200", outdir, (200,200))
            resizeImage(infile, "_thumb_800", outdir, (800,800))
