# dumarek.net — Site copy

All user-facing text on the site, in page order, exported from the components
on the `new-site` branch. Edit anything here and the changes can be applied
back to the code — each section notes its source file. Items needing real
material or confirmation are marked **[TODO]**.

---

## Page metadata

_Source: `src/layouts/Base.astro` (description, social tags),
`src/pages/index.astro` (title)_

- **Browser/tab title:** Dumarek | Music Production | Mixing & Mastering |
  Napa, CA | Pop with a Disco Soul
- **Meta description (search result snippet):** Phillip Dumarek is a music
  producer in Napa, California. He helps indie artists turn demos into
  records. Songwriting, instrumentation, vocal tracking, and mixing &
  mastering. All original, no samples, no AI. Send your demo.
- **Structured data (JSON-LD, not visible on page):** ProfessionalService
  "Dumarek" — full-service music and video production studio in Napa;
  founder Phillip Dumarek; links to Instagram, Spotify.
  **[TODO — og:image: add a 1200×630 share image at `public/og.jpg`]**

---

## Hero

_Source: `src/components/Hero.astro`_

- **Wordmark (top of page):** Dumarek
- **Headline:** Making pop songs with a disco soul. _("disco soul" in
  gradient)_
- **Lede:** I take your demo from an idea in your voice memos to a
  radio-ready record that moves people: songwriting, instrumentation, vocal
  production, mixing and mastering. All under one roof in Napa, California.
  Everything original. No samples, no AI, ever.
- **Primary button:** Send your demo
- **Secondary button:** Hear my work

---

## Recent work

_Source: `src/pages/index.astro` (uses `src/components/PlaylistSection.astro`)_

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
- **Section title:** Helping you release great music
- **Intro:** Bring a voice memo or a half-built session. I meet the song
  where it is and help you carry it the rest of the way.

### Production
Full arrangement and instrumentation, played or programmed from scratch.
Your song gets its own unique sound.

### Songwriting
Co-writing that helps you finish what you started: hooks that land, melodies
that stick, unforgettable lyrics.

### Vocal tracking
A calibrated control room, vintage pre-amps and mics, and an honest read on
your best take. We track until it feels effortless, then comp it until it
sounds effortless.

### Mixing & Mastering
Radio-ready balance with the groove kept intact. You get a mix and master
that translates from club system, to streaming, to phone speaker.

### And when the record is done — video _(full-width card; "video" in gradient)_
Getting heard today means social media, and social media means video. This is
a video production studio too: performance clips, short-form content, visuals
for the release — shot in the same room where the record was made.

---

## How it works (process)

_Source: `src/components/Process.astro`_

- **Eyebrow label:** How it works
- **Section title:** Demo to release in three steps

### 1 — Send the demo
A voice memo is enough. Tell me where you want the song to end up and I will
tell you, plainly, what I would do with it and what that will cost.

### 2 — We build the record
Arrangement, instrumentation, and vocals. In the studio or remote. We do
everything together in real time. You hear each change as it's made and
nothing moves forward without your yes.

### 3 — You release it
You walk away with a mixed, release-ready master and every stem. It is your
record, I just helped it meet its potential.

---

## The studio

_Source: `src/components/Studio.astro`_

- **Eyebrow label:** The studio
- **Section title:** A thousand square feet built for the modern artist
- **Paragraph 1:** The studio is a converted warehouse in Napa, California:
  a full music and video production space with a dedicated room for vocal
  recording.
- **Paragraph 2:** Come work in the room, or work remotely.
- **Photo:** interior shot beside the text (`src/assets/studio.jpg`)

---

## About

_Source: `src/components/About.astro`_

- **Eyebrow label:** About
- **Section title:** Hi, I'm Phillip Dumarek
- **Photo:** portrait beside the text (`src/assets/phillip.jpg`)
- **Paragraph 1:** I'm a pop music producer based in Napa, CA. I built the
  studio so artists could make a whole record in one place with one person
  who cares about it as much as they do.
- **Paragraph 2:** It's a full-service studio in the most modern sense —
  beyond the audio. Artists live on social now, and social runs on video, so
  when the record is done we can shoot the content that carries it:
  performance videos, short-form clips, the story around the song.

---

## Send your demo (form)

_Source: `src/components/DemoForm.astro`_

- **Eyebrow label:** Send your demo
- **Section title:** Let's make music. _("music." in gradient)_
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
  music@dumarek.net.

_The form posts to Formspree (`https://formspree.io/f/xaqgpgzr`) with email
subject "New inquiry from dumarek.net"._

---

## Footer

_Source: `src/components/Footer.astro`_

- **Mark:** Dumarek — Napa, California
- **Links:** Instagram (instagram.com/therealdumarek) · Spotify (artist
  1l28YhxS42qSosjk75Tzd2)
- **Fine print:** © [current year] Dumarek. All songs original, no samples.
  _(year fills in automatically)_

---

## 404 page

_Source: `src/pages/404.astro`_

- **Tab title:** Page not found — Dumarek
- **Eyebrow:** 404
- **Headline:** That track doesn't exist.
- **Body:** The page you're after isn't here — but the music is.
- **Button:** Back to the record
