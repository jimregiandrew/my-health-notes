# My Health Notes (Personal Health Diaries)

## Overview

This repository demonstrates an idea: 

```
individuals owning and maintaining their own long-term health notes using Git and Markdown.
```

The core proposal is simple:

Each person (or family) creates their own ***private*** my-health-notes repository — a personal, longitudinal health diary — using plain text formats (Markdown, CSV, JSON, etc.).

These notes are owned by the individual, readable by humans, analyzable by machines, and (optionally) shareable with researchers or AI tools only if and when the owner chooses.

This repo exists mainly to:

1. Explain the concept
2. Encourage others to create their own personal health-notes repositories.

Why? The short answer is: for illnessed like Long Covid I believe

1. Medicine undersands it very pooly
2. Personal health notes in electronic form is a great way to make progress on this understanding but this data is woefully missing.

## All the stuff that I wanted to write but is distracting

### Where did the idea come from ? 

I have long covid since Jan 2024. For almost all of 2024 I couldn't walk 50 m up a slight incline to the our letter box without over-exerting myself. I am one of the lucky ones - for now at least I can go for long walks, swim, ride a bike etc. I kept a fatigue diary almost right from the start. (I can't recall why exactly now :-) The fatigue diary clearly shows post exertional malaise (PEM) events, but I didn't know what this was at the time. I had a decent suspicion that over-exerting myself was a big problem and that over-exerting myself was difficult to detect at the time, but it took 6 months to find a doctor (actually a Physio) who knew about PEM, and confirmed my suspicions. 

This idea comes in part from the questions that I still have:

1. Why did all the doctors that I saw in the first 6 months not know about PEM?. Yes, there are some good resources on the Internet about PEM (from the ME/CFS community in particular) but you have to know where to look.
2. Why, still, do ballpark 50% of people I talk to (including doctors) think that Long Covid is "in my head" (psychosomatic or similar). Most people are very polite about it, but after a while one can tell. The answer to a redit question sums the problem with this "diagnosis":

> If i was diagnosed with a physical issue I'd be send to a doctor for treatment, support and help. If it was psychosomatic i was send home and told to deal with it

Regardless of whether it is pyschosomatic or not my experience with my Long Covid is that others have had a similar experience, or at least similar experiences - and from this there is stuff that helps. My life improved significantly after I learned these things. This knowledge came largely from the ME/CFS community who have lived this well before Covid came along. I am told that Long Covid has improved the visibility of ME/CFS perhaps because of sheer numbers and: "Long Covid has been heavily driven by patients, ...., which accelerated global studies and advocated for better care." I would argue this knowledge came largely from patients and from those doctors that had significant experience with these patients.

This has been my experience in any case. And not dissimilar to a few others I have met with Long Covid or ME/CFS. But this is a good example of how the "my-health-notes" concept could be useful. Don't take my word for it - science won't and rightly so - but if lots of people write of their experience and there are significant similarities, science and therefore eventually your average doctor will have to take note.

Conditions such as Long COVID, ME/CFS, IBS, POTS, autoimmune disorders, and other “invisible illnesses” — are:

- Poorly understood
- Difficult to capture in short clinical appointments

And there are other properties that make them difficult to analyse (Highly individual, some are episodic and non-linear).

What does work well is longitudinal self-observation:

- Daily or near-daily notes
- Simple numeric scales (fatigue, mood, pain, anxiety, etc.)
- Context (sleep, food, activity, stress)
- Free-text descriptions of what actually happened

Over time, this kind of diary can reveal:

- Triggers
- Delayed effects (e.g. PEM)
- Personal baselines
- Early warning signs of relapse or improvement

Historically, this data has been hard to analyze at scale. AI changes that. But AI needs data, and data for these invisible illnesses is woeful. 

Why Git (and GitHub)? It doesn't have to be Git (or GitHub) but these tools exist now and are - I think - a surprisingly good fit.

Using Git (for example via GitHub) provides several important properties by default:

1. Ownership and control
    - You own your repository
    - You decide whether it is private or public
    - You decide who (if anyone) can access it
    - You can revoke access at any time
    - There is no central platform that owns or monetizes your data.
2. Authenticity without central identity

Maintaining a Git repo requires real human effort over time

Longitudinal consistency is hard to fake

This naturally filters out low-effort or automated noise

This is not perfect identity verification — but neither are most clinical datasets.

3. Efficient long-term data storage

Git stores changes efficiently (diffs, compression)

Researchers or tools can:

Clone once

Pull updates incrementally

Years of daily notes can be synced with minimal bandwidth

This makes long-term participation feasible.

4. Free-form and structured data

You are not locked into a rigid schema.

A single repo might contain:

Markdown daily logs

CSV numeric scales

JSON/YAML metadata

Wearable exports

Lab results (PDFs)

Notes about medications or supplements

Structure can emerge organically instead of being imposed upfront.

What’s in this repository?

This repo is not meant to store personal health data.

Instead, it provides:

Example directory structures

Example CSV formats for numeric scales (e.g. fatigue, mood)

Simple Python scripts to plot or analyze that data

Illustrative sample data (fictional or anonymized)

Think of it as a starter kit and proof of concept.

How to use this idea yourself

Create a private repository called something like:

my-health-notes

Use simple, boring formats:

Markdown (.md) for notes

CSV for numeric scales

One file per day, week, or month — whatever works for you

Keep it sustainable:

Short entries are fine

Consistency matters more than detail

This should help you, not burden you

Use AI locally (or with tools you trust) to:

Summarize trends

Identify correlations

Detect delayed effects

Generate questions for clinicians

Even your data alone can be valuable to you.

The bigger idea: collective insight (opt-in only)

If thousands — or millions — of people maintain their own my-health-notes repositories, something powerful becomes possible:

AI could analyze patterns across individuals

Subtypes of poorly understood illnesses might emerge

Common triggers or trajectories could be identified

Research could be guided by real lived experience

Crucially:

Participation in any collective analysis would be entirely opt-in.

Your data remains yours.

Privacy and risks (important!)

This approach involves real risks. You should understand them before participating.

Key concerns

Accidental oversharing

Revealing identifiable information

Long-term permanence of Git history

Public repos being indexed and archived

Mitigations

Default to private repositories

Use pseudonyms and avoid identifiable details

Separate private vs shareable files

Be deliberate before making anything public

Consider sharing derived data (summaries, aggregates) rather than raw notes

This project does not recommend uploading sensitive data publicly.

What this is not

Not a medical device

Not a diagnostic tool

Not a replacement for clinicians

Not a centralized data platform

Not a startup (at least not by default)

It is a patient-first, open, low-tech idea that leverages existing tools in a new way.

Who is this for?

People managing chronic or poorly understood conditions

Parents keeping long-term notes for children

Researchers interested in patient-generated data

Developers exploring AI + health + ethics

Anyone who believes lived experience matters

Contributing

Contributions are welcome:

Improved example formats

Analysis scripts

Documentation

Ethical guidelines

Tooling ideas that lower the barrier to entry

Please do not submit real personal health data.

Final thought

Medicine is very good at snapshots.
Chronic illness lives in timelines.

This project is about preserving those timelines — under the control of the people who live them.
