#!/usr/bin/env python3
"""
Generate visual audit sheet for EVE_Ships SVG collection.
Converts SVGs to PNG thumbnails and creates a contact sheet.
"""

import os
import sys
from pathlib import Path

try:
    import cairosvg
    from PIL import Image, ImageDraw, ImageFont
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install cairosvg Pillow")
    sys.exit(1)

def get_font(size=12):
    """Get a font with fallback."""
    font_paths = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/TTF/DejaVuSans.ttf',
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except:
                pass
    return ImageFont.load_default()

def svg_to_png(svg_path: Path, size: int = 128) -> Image.Image:
    """Convert SVG to PNG thumbnail."""
    try:
        png_data = cairosvg.svg2png(
            url=str(svg_path),
            output_width=size,
            output_height=size,
        )
        from io import BytesIO
        img = Image.open(BytesIO(png_data)).convert('RGBA')

        # Center on transparent background
        result = Image.new('RGBA', (size, size), (0, 0, 0, 0))

        # Fit and center
        img.thumbnail((size - 8, size - 8), Image.Resampling.LANCZOS)
        x = (size - img.width) // 2
        y = (size - img.height) // 2
        result.paste(img, (x, y), img if img.mode == 'RGBA' else None)

        return result
    except Exception as e:
        # Return error placeholder
        result = Image.new('RGBA', (size, size), (50, 0, 0, 255))
        return result

def main():
    ships_dir = Path(__file__).parent / 'ships'
    output_dir = Path(__file__).parent / 'audit_sheets'
    output_dir.mkdir(exist_ok=True)

    # Find all SVGs
    svgs = sorted(ships_dir.glob('*.svg'))
    print(f"Found {len(svgs)} SVG files")

    if not svgs:
        print("No SVGs found!")
        return 1

    # Settings
    thumb_size = 100
    label_height = 16
    cols = 12
    rows = (len(svgs) + cols - 1) // cols

    cell_width = thumb_size
    cell_height = thumb_size + label_height

    header_height = 40
    img_width = cols * cell_width + 20
    img_height = header_height + rows * cell_height + 20

    # Create image
    img = Image.new('RGBA', (img_width, img_height), (30, 30, 35, 255))
    draw = ImageDraw.Draw(img)

    title_font = get_font(18)
    label_font = get_font(9)

    # Header
    draw.rectangle([0, 0, img_width, header_height], fill=(40, 40, 45))
    draw.text((10, 10), f"EVE_Ships SVG Audit ({len(svgs)} ships)",
              fill=(200, 200, 200), font=title_font)

    # Process SVGs
    print("Converting SVGs to thumbnails...")
    for idx, svg_path in enumerate(svgs):
        if idx % 50 == 0:
            print(f"  Progress: {idx}/{len(svgs)}")

        row = idx // cols
        col = idx % cols

        x = 10 + col * cell_width
        y = header_height + 10 + row * cell_height

        # Convert SVG to thumbnail
        thumb = svg_to_png(svg_path, thumb_size)
        img.paste(thumb, (x, y), thumb)

        # Label
        label = svg_path.stem
        if len(label) > 12:
            label = label[:10] + '..'
        draw.text((x + 2, y + thumb_size), label, fill=(150, 150, 150), font=label_font)

    # Save
    output_path = output_dir / 'svg_audit.png'
    img.save(output_path, 'PNG')
    print(f"\nCreated: {output_path}")

    return 0

if __name__ == '__main__':
    sys.exit(main())
