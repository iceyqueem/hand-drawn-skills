---
name: hand-drawn-illustration
description: Generate or restyle illustrations in a natural, freehand ink style with one accent colour, in two modes. Quiet: a pared-down designer's sketch, few strokes, no shading, one accent of light, for portfolio covers, dark-mode pages and anywhere the drawing must support rather than lead. Lively: an expressive editorial illustration with gesture, wit and a small story, for team announcements, visual stories, guides and bot imagery. Use as the preferred style for illustrative images unless another style is explicitly requested. Does not override requirements for photography, technical diagrams or existing brand assets.
---

# Hand-Drawn Illustration

One hand, two moods. Both modes are black ink on white with one restrained accent, drawn by someone with confidence and a point of view. They differ in how much they say.

| | Quiet | Lively |
|---|---|---|
| Job | Support the real work beside it | Tell a small story on its own |
| Strokes | Under ~30–40, open, overshooting | As many as the gesture needs, variable pressure |
| Shading | None: no hatching, fills or washes | Small areas of hatching or solid ink allowed |
| Faces | Blank or nearly blank | Economical features, expressive gaze |
| Accent | One soft wash, always a light | Emphasises the action or punchline |
| Best on | Dark or minimal pages, next to products | Light pages, standalone images |

**Choosing:** if the image sits next to a product, a screenshot or a big headline, or will be shown on a dark background, use **Quiet**. If the image is the content (an announcement, a story, a guide), use **Lively**. If unsure, start Quiet: it is easier to add life than to take weight away.

## Shared visual language

- **Line:** Freehand black ink. Decisive and relaxed, never traced, vector-uniform or artificially distressed.
- **People:** Personality through posture, gesture and interaction. Natural adult proportions. Never oversized eyes, baby proportions or exaggerated cartoon expressions.
- **Composition:** One clear action or idea. Asymmetry and off-centre placement are welcome. Generous white space. A small scene, not a collage of symbols.
- **Colour:** Black ink on white or warm off-white, one accent. Default accents: warm yellow `#eaa900` for Quiet (it reads as light), cobalt blue for Lively. Follow explicit palette requests.
- **Mood:** Warm, observant, grown-up. Humour comes from a relatable situation, not decoration.
- **Text:** Only when it serves the image; concise English unless asked otherwise; casual handwritten lettering; preserve supplied copy exactly.

## Mode: Quiet

A designer's quick sketch that catches people and one idea, then stops.

- Fast fineliner lines that overshoot corners and stay open; a few construction lines may remain.
- Suggest, do not describe. No hatching, no fills, no grey washes, no texture, no ground or background scenery.
- Exactly one accent, and it is a light: a lit doorway, a glowing screen, a small point everyone turns toward. A soft wash, never an outline colour. The light is where the meaning is.
- In a series that shows growth (two people, a team, a crowd), let the number of people carry the story; keep line, economy and the single light constant.

Prompt foundation:

> A very minimal ink sketch by a confident designer, drawn fast with a black fineliner in under [30–40] strokes. Loose, elegant, open lines that do not close, a few lines overshooting at corners. No shading, no hatching, no fills, no texture, no background details, no ground. Subject: [people doing one simple thing], [faces left blank / suggested with a few gestural lines]. Lots of empty white space. The only colour: one soft wash of [accent] on [the light]. Pure white background, no text, no signature.

## Mode: Lively

An accomplished editorial illustrator's sketchbook: natural, spontaneous, loose, expressive and alive. The reference spirit is a colleague onboarding a small DIY bot at a desk: a badge handed over, an open setup booklet, a bot already carrying a checkmark. Keep the warmth, movement and storytelling, not those objects.

- Variable pressure, slight wobble, tapered ends, occasional broken contours, a few searching strokes.
- Only the details needed to tell the story: an expressive hand, a tilted posture or a well-chosen prop beats decoration. Simplicity keeps character; do not reduce scenes to generic outline icons.
- Small areas of loose hatching, solid ink or subtle paper texture are welcome when they add character. No heavy shading, grunge, gradients or rendered volume.
- Bots, when relevant: small, simply constructed, expressive body language; charming without being a glossy toy or kawaii mascot. No bot when the subject does not call for one.

Prompt foundation:

> Create a lively, understated hand-drawn editorial illustration of [subject doing a specific action], communicating [message]. Confident, spontaneous black ink on warm white; varied line pressure, relaxed imperfect contours, expressive gestures, economical detail, and generous negative space. Use [accent] sparingly to emphasize [key element]. A warm, witty, human moment, like a skilled illustrator's observational sketch. Keep the composition simple but alive. Avoid generic corporate clip art, glossy 3D, oversized cartoon eyes, rigid vector geometry, and decorative clutter. [Format and exact text requirements, if any.]

## Working approach

1. Name the message and the one action or visual idea. Pick the mode.
2. Generate with the available image-generation or editing tool, following its workflow. This skill is art direction, not a renderer: do not substitute SVG or code-drawn approximations unless asked.
3. When a reference image is supplied, use it as a style reference; keep requested content and edit constraints rather than copying unrelated objects.
4. Inspect and revise the single most important issue with a targeted edit:
   - Quiet: anything shaded, filled, cute or crowded? More than one light? Could one more line go?
   - Lively: generic, stiff, overly cute or cluttered? Does gesture carry the life, not facial cuteness?
5. For a dark page, convert with `scripts/ink_to_dark.py`: ink becomes light cream lines, the accent stays, the paper becomes transparent. Pass `--glow X,Y,RADIUS` to turn a small hard accent dot into a soft light. Use Quiet mode for anything that will be converted: shading and fills turn into a photo-negative look on dark.

## Final quality check

- Does the scene communicate its message without leaning on a caption?
- Is there one clear focal point and enough room to breathe?
- Do the lines feel spontaneous and purposeful, not mechanically neat or randomly messy?
- Quiet: does it stay quiet next to what it supports? Lively: is it alive because of gesture and interaction?
- Are text, content and format faithful to the request?

Prefer a few memorable, expressive choices over polished complexity. Explicit user instructions take precedence over these defaults.
