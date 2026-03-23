#!/usr/bin/env python3
import cairosvg
import os

# Ensure images directory exists
os.makedirs('images', exist_ok=True)

# Convert SVG to PNG
cairosvg.svg2png(url='images/favicon.png', write_to='images/favicon_converted.png', output_width=64, output_height=64)
print("Conversion completed!")