# EVE Ships

**267 vector ship silhouettes from the EVE Online universe.**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Ships](https://img.shields.io/badge/Ships-267-blue.svg)]()
[![Format](https://img.shields.io/badge/Format-SVG-orange.svg)]()
[![Size](https://img.shields.io/badge/Size-2.3MB-purple.svg)]()

---

![Ship Silhouettes Preview](docs/preview.png)

> **Preview Instructions:** Create a grid montage showing:
> 1. A selection of iconic ships: Rifter, Apocalypse, Nyx, Avatar
> 2. Ships from each faction represented
> 3. Various sizes from frigates to titans
>
> Generate with ImageMagick:
> ```bash
> montage ships/rifter.svg ships/apocalypse.svg ships/nyx.svg ships/avatar.svg \
>   -geometry 200x200+10+10 -tile 4x1 docs/preview.png
> ```

---

## Overview

A curated collection of 267 SVG vector silhouettes covering EVE Online's iconic spacecraft. From the humble Rifter to the mighty Avatar titan, this library provides scalable assets for:

- Game development (2D shooters, strategy games)
- Fan projects and visualizations
- Fleet composition tools
- Educational materials
- UI/UX design elements

All ships are vector graphics—scale to any size without quality loss.

---

## Quick Start

### Clone Everything

```bash
git clone https://github.com/AreteDriver/EVE_Ships.git
```

### Sparse Checkout (Recommended)

Pull only the ships you need:

```bash
# Clone without files
git clone --depth 1 --filter=blob:none --sparse \
    https://github.com/AreteDriver/EVE_Ships.git

cd EVE_Ships

# Pull specific ships
git sparse-checkout set ships/rifter.svg ships/wolf.svg ships/apocalypse.svg

# Or pull by pattern
git sparse-checkout set 'ships/[a-m]*'  # Ships A-M
```

### Direct Download

```bash
# Single ship
curl -O https://raw.githubusercontent.com/AreteDriver/EVE_Ships/main/ships/rifter.svg

# Multiple ships
for ship in rifter wolf apocalypse abaddon; do
  curl -O "https://raw.githubusercontent.com/AreteDriver/EVE_Ships/main/ships/${ship}.svg"
done
```

---

## Ship Collection

### By Faction

| Faction | Notable Ships |
|---------|---------------|
| **Amarr** | Apocalypse, Abaddon, Avatar, Archon, Revelation, Aeon |
| **Caldari** | Raven, Rokh, Leviathan, Chimera, Phoenix, Wyvern |
| **Gallente** | Megathron, Hyperion, Erebus, Thanatos, Moros, Nyx |
| **Minmatar** | Rifter, Tempest, Ragnarok, Nidhoggur, Naglfar, Hel |
| **Pirate** | Machariel, Nightmare, Barghest, Dramiel, Cynabal |
| **Sisters of EVE** | Astero, Stratios, Nestor |
| **Triglavian** | Kikimora, Damavik, Vedmak, Leshak, Zirnitra |

### By Class

| Class | Count | Examples |
|-------|-------|----------|
| Frigates | 40+ | Rifter, Punisher, Merlin, Atron, Executioner |
| Destroyers | 15+ | Thrasher, Coercer, Catalyst, Cormorant |
| Cruisers | 35+ | Stabber, Omen, Moa, Thorax, Caracal |
| Battlecruisers | 15+ | Hurricane, Harbinger, Drake, Brutix |
| Battleships | 25+ | Tempest, Apocalypse, Raven, Megathron |
| Capitals | 20+ | Archon, Chimera, Thanatos, Nidhoggur |
| Supercapitals | 10+ | Aeon, Wyvern, Nyx, Hel |
| Titans | 4 | Avatar, Leviathan, Erebus, Ragnarok |
| Industrials | 15+ | Bestower, Badger, Iteron, Mammoth |
| Specialty | 20+ | Venture, Procurer, Orca, Rorqual |

### Complete Ship List

<details>
<summary>Click to expand full list (267 ships)</summary>

```
abaddon        absolution     aeon           algos          anathema
apocalypse     apostle        apotheosis     arbitrator     archon
ares           armageddon     ashimmu        astero         atron
augoror        avatar         badger         bantam         barghest
basilisk       bellicose      bestower       bifrost        blackbird
bowhead        breacher       broadsword     brutix         burst
bustard        buzzard        caracal        catalyst       celestis
cerberus       charon         cheetah        chimera        claw
cockroach      coercer        comet          condor         confessor
corax          cormorant      covenant       covetor        crane
crow           crucifier      cruor          crusader       curse
cyclone        cyclops        cynabal        damavik        damnation
daredevil      deacon         deimos         devoter        dominix
dragonfly      dragoon        drake          dramiel        draugur
drekavac       eagle          echelon        einherji       endurance
enforcer       enyo           eos            epithal        erebus
eris           etana          executioner    exequror       falcon
fenrir         ferox          firbolg        firetail       flycatcher
garmur         gnosis         golem          griffin        guardian
harbringer     harpy          hawk           hecate         hel
helios         heretic        heron          hoarder        hookbill
hound          huginn         hulk           hurricane      hyena
hyperion       ibis           ikitursa       imicus         impairor
incursus       inquisitor     ishkur         ishtar         iteron mark v
jackdaw        jaguar         keres          kestrel        kikimora
kirin          kitsune        kronos         kryos          legion
leshak         leviathan      lif            loki           machariel
mackinaw       maelstorm      magnate        magus          malediction
maller         malleus        mammoth        manticore      mantis
marshal        maulus         megathron      merlin         miasmos
minokawa       moa            moracha        moros          muninn
myrmidon       naga           naglfar        navitas        nemesis
nergal         nerus          nestor         nidhoggur      nighthawk
nightmare      ninazu         nyx            obelisk        omen
onyx           oracle         orca           orthrus        osprey
pacifier       paladin        panther        phantasm       phobos
phoenix        pilgrim        polaris        pontifex       porpoise
praxis         probe          procurer       prophecy       prospect
proteus        providence     punisher       purifier       ragnarok
rapier         raptor         raven          reaper         redeemer
retribution    retriever      revelation     revenant       rifter
rodiva         rokh           rook           rorqual        rupture
sabre          sacrilege      scalpel        scorpion       scythe
shuttle_amarr  shuttle_caldari shuttle_gallente shuttle_minmatar
sigil          sin            skiff          skybreaker     slasher
sleipnir       slicer         stabber        stiletto       stork
stormbringer   stratios       succubus       sunesis        svipul
talos          talwar         taranis        tayra          tempest
templar        tengu          thalia         thanatos       thorax
thrasher       thunderchild   tormentor      tornado        tristan
typhoon        tyrfing        vagabond       vargur         vedmak
velator        vengeance      venture        vexor          vigil
widow          wolf           wreathe        wyvern         zarmazd
zealot         zephyr         zirnitra
```

</details>

---

## File Format

All ships are **SVG (Scalable Vector Graphics)**:

```xml
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
 "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg version="1.0" xmlns="http://www.w3.org/2000/svg"
 width="3000" height="900" viewBox="0 0 3000 900">
  <path d="M..." fill="#000000"/>
</svg>
```

### Specifications

| Property | Value |
|----------|-------|
| Format | SVG 1.0 |
| Colors | Black silhouettes (#000000) |
| Viewports | 2000x600 to 5000x900 |
| File sizes | 2KB - 18KB each |
| Total size | 2.3 MB |
| Generator | potrace 1.16 |

### Converting to Other Formats

```bash
# SVG to PNG (requires Inkscape or ImageMagick)
inkscape ships/rifter.svg -o rifter.png -w 256 -h 256

# SVG to PNG with ImageMagick
convert -background none ships/rifter.svg -resize 256x256 rifter.png

# Batch convert all ships
for svg in ships/*.svg; do
  convert -background none "$svg" -resize 128x128 "png/$(basename "$svg" .svg).png"
done
```

---

## Usage Examples

### Python (Pygame + CairoSVG)

```python
import pygame
import cairosvg
from io import BytesIO

def load_ship_svg(path, scale=1.0):
    """Load SVG ship and convert to Pygame surface."""
    # Convert SVG to PNG in memory
    png_data = cairosvg.svg2png(url=path, scale=scale)

    # Load into Pygame
    image = pygame.image.load(BytesIO(png_data))
    return image.convert_alpha()

# Usage
rifter = load_ship_svg("ships/rifter.svg", scale=0.1)
screen.blit(rifter, (100, 100))
```

### JavaScript (Browser)

```html
<img src="ships/rifter.svg" alt="Rifter" width="128" height="128">

<!-- Or inline -->
<object data="ships/rifter.svg" type="image/svg+xml" width="128"></object>
```

### CSS Background

```css
.ship-rifter {
  background-image: url('ships/rifter.svg');
  background-size: contain;
  width: 128px;
  height: 128px;
}
```

### React Component

```jsx
import { ReactComponent as Rifter } from './ships/rifter.svg';

function ShipDisplay() {
  return <Rifter className="ship" style={{ width: 128, fill: '#ff6600' }} />;
}
```

---

## Integration with EVE_Rebellion

This repository serves as the asset library for [Minmatar Rebellion](https://github.com/AreteDriver/EVE_Rebellion).

### Build Integration

```bash
# In EVE_Rebellion build script
SHIPS_NEEDED="rifter wolf apocalypse abaddon executioner punisher"

git clone --depth 1 --filter=blob:none --sparse \
    https://github.com/AreteDriver/EVE_Ships.git temp_ships

cd temp_ships
for ship in $SHIPS_NEEDED; do
  git sparse-checkout add "ships/${ship}.svg"
done

cp ships/*.svg ../assets/ships/
cd .. && rm -rf temp_ships
```

### Why Separate Repository?

| Approach | Game Repo Size | Pros | Cons |
|----------|----------------|------|------|
| Embedded assets | 50+ MB | Simple | Bloated, slow clones |
| **Separate repo** | <5 MB | Fast clones, selective pulls | Extra build step |
| Git LFS | Variable | Good for binaries | Bandwidth limits |

Keeping assets separate allows:
- Fast game repo clones for contributors
- Selective asset pulling per build target
- Independent asset versioning
- Easier asset updates without game commits

---

## Project Structure

```
EVE_Ships/
├── ships/                  # 267 SVG ship files
│   ├── rifter.svg
│   ├── apocalypse.svg
│   ├── avatar.svg
│   └── ... (264 more)
├── README.md              # This file
└── LICENSE                # MIT License
```

### Planned Structure

```
EVE_Ships/
├── ships/
│   ├── amarr/
│   │   ├── frigates/
│   │   ├── cruisers/
│   │   └── capitals/
│   ├── caldari/
│   ├── gallente/
│   ├── minmatar/
│   └── pirate/
├── tools/
│   └── validate_ships.py
├── ship_manifest.json
└── README.md
```

---

## Contributing

### Adding Ships

1. Create SVG silhouette (black on transparent)
2. Name file lowercase: `shipname.svg`
3. Ensure clean paths (no embedded rasters)
4. Submit PR with ship name and class

### Quality Guidelines

- **Clean vectors**: No embedded bitmaps
- **Consistent style**: Black silhouettes
- **Proper naming**: Lowercase, underscores for spaces
- **Reasonable size**: 2-20KB per file

---

## Roadmap

- [ ] Organize by faction/class subdirectories
- [ ] Add `ship_manifest.json` with metadata
- [ ] Create validation script
- [ ] Add colored variants (faction colors)
- [ ] Generate PNG sprite sheets
- [ ] Add ship thumbnails for preview

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Disclaimer

**This project is not affiliated with or endorsed by CCP Games.**

EVE Online and all associated ship names and designs are registered trademarks of CCP hf. These silhouettes are fan-created interpretations for educational and non-commercial use. The vector graphics in this repository are original tracings, not extracted game assets.

For commercial use, please create original designs or obtain licensing from CCP Games.

---

## Support the Project

If you enjoy this project, consider supporting development:

- **In-Game**: Send ISK donations to **AreteDriver** in EVE Online
- **Buy Me a Coffee**: [buymeacoffee.com/aretedriver](https://buymeacoffee.com/aretedriver)

Your support helps keep these projects maintained and improving. o7

---

## Acknowledgments

- **CCP Games** - For creating the EVE Online universe and its iconic ships
- **potrace** - Vector tracing tool used for silhouette generation
- **EVE Community** - For decades of ship appreciation

---

<p align="center">
  <em>From frigates to titans, every hull tells a story.</em>
  <br><br>
  <strong>o7</strong>
</p>
