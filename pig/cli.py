import click
from PIL import Image
from resizeimage import resizeimage
from utils.io import Io
import json
import os

@click.command()
@click.argument('platform', type=click.Choice(['ionic'])) # To do: 'android', 'ios'
@click.option('--file', '-f', help='file name')
@click.option('--output', '-o', default='./', help='destination folder of images')
def main(platform, file, output):
  """PIG - Python Icon Generator"""

  # load config file
  with open(os.path.dirname(os.path.abspath(__file__)) + '/dimensions/' + platform + '.dim.json') as f:
    data = json.load(f)


  if (output != './'):
    src = output + '/'
  else:
    src = './'

  logo = Image.open(file, 'r')

  for obj in data:
    for image in obj['icon']['images']:
      createImage(image, logo, src)
    for image in obj['splash']['images']:
      createImage(image, logo, src)

def createImage(image, logo, src):
  logo_w, logo_h = logo.size
  
  if logo_h > logo_w:
    height = 0.6 * image['dimensions'][1]
    width = (logo_w * height) / logo_h
  else:
    width = 0.8 * image['dimensions'][0]
    height = (logo_h * width) / logo_w
  
  if (logo_h < height) | (logo_w < width):
    brand = logo
  else:
    brand = resizeimage.resize_cover(logo, [width, height])
  
  brand_w, brand_h = brand.size

  background = Image.new('RGBA', (image['dimensions'][0], image['dimensions'][1]), (255, 255, 255, 255))
  bg_w, bg_h = background.size

  offset = ((bg_w - brand_w) // 2, (bg_h - brand_h) // 2)
  background.paste(brand, offset)

  Io.createFolders(src + image['output'])

  filename = src + image['output'] + '/' + image['name'] + '.png'
  background.save(filename, 'png')
  click.echo('file crated ===> ' + filename)
