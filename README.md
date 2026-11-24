# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/trijavani-eng/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/trijavani-eng/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A program that draws one clean, dense newspaper front page summing
up the world's news of Tuesday, 24 November 2026: 18 stories across
6 regions, with a key-numbers strip, a region bar, a timeline, a
schematic world map with pins, and a DATE CHECK box naming what was
left out. Modelled on the previous day's prize-winning entries, but
built to beat them: the date is the biggest thing on the page, the
three lead illustrations are larger, body text is bigger, badges sit
top-right of each card so they never cover a summary, and the map
uses numbered pins only for the three leads.

Built for the make.fun bounty "Sum up 24 November's world news in
one image" (https://make.fun/bounty/news-image-20261124).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library + Pillow only) draws a
1024x1024 front page with Pillow and writes it to `entry.png`. It
uses no network, no clock and no randomness, so two runs write
byte-identical files. All illustrations are drawn, not photographs.

## The stories

Lead stories:

1. **COP31 collapses — no deal** (Antalya) — UN climate talks end
   with no deal after 50+ hours overtime, the first collapse since
   2009; the final text never mentioned fossil fuels.
2. **Ukraine sinks Russian warship off Libya** — seven sea drones
   sink the corvette Merkury at Benghazi, Kyiv says; the cargo
   ship Angara is struck too.
3. **Gulf standoff deepens** — Trump warns Iran of a "very
   traumatic" outcome if no nuclear deal; the US tightens its
   blockade and adds sanctions; Iran demands $290bn.

Plus 9 grid stories (NATO airspace, Nvidia, the Rohingya ruling,
the Nepal quake, 96 drones over Ukraine, Gaza winter aid, the
Grok lawsuits, the Hanoi blast, Hasina's planned return) and 6
more in "Also on Tuesday". Every story carries a status badge
(CONFIRMED = 2+ outlets, REPORTED = carried by the wires) and its
sources. The DATE CHECK box states that every story was reported
on Tuesday, 24 November 2026, and lists what was deliberately
left out (El Chapo Isidro's capture on 20 Nov, the Jul 2025
US–Japan / US–Indonesia trade deals, SoftBank's Aug 2025 Intel
stake, the ICJ ruling itself on 19 Nov).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
