# dumarek.net — Site copy

All user-facing text on the site, in page order. Edit anything here and the
changes can be applied back to the components — each section notes its source
file. Placeholder content that needs real material is marked **[TODO]**.

---

## Page metadata

_Source: `src/layouts/Base.astro`, `src/pages/index.astro`_

- **Browser/tab title:** Dumarek · Music Producer in Napa | Pop with a Disco Soul
- **Meta description (search result snippet):** Dumarek is a music producer
  in Napa, California making pop songs with a disco soul. Songwriting,
  instrumentation, vocal tracking, and mixing — all original, no samples.
  Send your demo.

---

## Hero

_Source: `src/components/Hero.astro`_

- **Wordmark (top of page):** Dumarek
- **Headline:** Pop songs with a disco soul.
- **Lede:** I take your demo from an idea in your voice memos to a record
  that moves people — songwriting, instrumentation, vocals, and mix, all
  under one roof in Napa, California. Everything original. No samples, ever.
- **Primary button:** Send your demo
- **Secondary button:** Hear the work

---

## Recent work (track sheet)

_Source: `src/components/Work.astro`_

- **Eyebrow label:** Track sheet
- **Section title:** Recent work

_Embeds Disco.ac playlist 28423054 (dark theme, tangerine accent)._

---

## Recent instrumentals

_Source: `src/pages/index.astro` (uses `src/components/PlaylistSection.astro`)_

- **Eyebrow label:** Instrumentals
- **Section title:** Recent instrumentals

_Embeds Disco.ac playlist 29054005 (dark theme, tangerine accent)._

---

## What I do (services)

_Source: `src/components/Services.astro`_

- **Eyebrow label:** What I do
- **Section title:** One roof, whole record
- **Intro:** Bring a voice memo or a half-built session — I meet the song
  where it is and carry it the rest of the way.

### Production
Full arrangement and instrumentation, played and programmed from scratch.
Your song gets a sound that belongs to it alone — no loops, no sample packs.

### Songwriting
Co-writing that finishes what you started: the hook that will not land, the
bridge that is missing, the lyric that says it plainly.

### Vocal tracking
A dedicated control room and a comfortable read on your best take. We track
until it feels effortless, then comp it honest.

### Mixing
Radio-ready balance with the groove kept intact. You get a mix that
translates from club system to phone speaker.

---

## How it works (process)

_Source: `src/components/Process.astro`_

- **Eyebrow label:** How it works
- **Section title:** Demo to release in three moves

### 1 — Send the demo
A voice memo is enough. Tell me where you want the song to end up and I will
tell you, plainly, what I would do with it and what it costs.

### 2 — We build the record
Arrangement, instrumentation, and vocals — in the studio or remote. You hear
versions as we go and nothing moves forward without your yes.

### 3 — You release it
You walk away with a mixed, release-ready master and every stem. It is your
record — I just helped it sound like one.

---

## The studio

_Source: `src/components/Studio.astro`_

- **Eyebrow label:** The room
- **Section title:** A thousand square feet built for records
- **Paragraph 1:** The studio is a converted warehouse in Napa, California —
  a full music and video production space with a dedicated control room for
  vocals and instruments. Big enough to track a band, quiet enough to hear
  the difference.
- **Paragraph 2:** Come work in the room, or send sessions remotely — most
  projects end up being a mix of both.
- **Photo placeholder text:** Studio photo coming soon **[TODO — real photo]**

---

## About

_Source: `src/components/About.astro`_

- **Eyebrow label:** About
- **Section title:** Hi, I'm Dumarek
- **Paragraph 1:** I'm Phillip — a producer in Napa making the kind of pop
  that owes its pulse to disco: real grooves, real players, hooks that earn
  their repetition. I built the studio so artists could make a whole record
  in one place with one person who cares about it as much as they do.
- **Paragraph 2:** Every note on every production here is original. No sample
  packs, no borrowed loops — if you hear it, we made it.

---

## Send your demo (form)

_Source: `src/components/DemoForm.astro`_

- **Eyebrow label:** Send your demo
- **Section title:** Let's make music.
- **Intro:** Submit your inquiry and I'll be in touch within 24 hours.

**Form fields** _(all required)_

- Your full name
- Your email
- Where are you located?
- What best describes you? _(options **[TODO — confirm]**: Artist / band ·
  Songwriter · Manager or label · Other)_
- Where can I hear your music? _(placeholder: `https://…`)_
- What are you hoping to accomplish with your song/project?
- What can I help you with? _(options: Full production / Songwriting /
  Vocal tracking / Mixing / Not sure yet)_
- What funds have you allocated to this project? _(options **[TODO —
  confirm]**: Under $1,000 · $1,000 – $3,000 · $3,000 – $5,000 · $5,000+ ·
  Prefer to discuss)_
- Describe your project in detail
- How did you hear about my work?
- **Submit button:** Send it over

- **Fallback line:** Forms not your thing? Email me directly at
  hello@dumarek.net. **[TODO — confirm email address]**

_The form posts to Formspree (`https://formspree.io/f/xaqgpgzr`)._

---

## Footer

_Source: `src/components/Footer.astro`_

- **Mark:** Dumarek — Napa, California
- **Links:** lnk.bio **[TODO — add Instagram / Spotify / YouTube]**
- **Fine print:** © 2026 Dumarek. All songs original, no samples.

---

## 404 page

_Source: `src/pages/404.astro`_

- **Tab title:** Page not found — Dumarek
- **Eyebrow:** 404
- **Headline:** That track doesn't exist.
- **Body:** The page you're after isn't here — but the music is.
- **Button:** Back to the record
