# My Health Notes (Personal Health Diaries)

## Overview

This repository demonstrates an idea:

> Individuals owning and maintaining their own long-term health notes

The core proposal is simple:

Using Git and Markdown each person (or family) creates their own ***private*** my-health-notes repository — a personal, longitudinal health diary — using plain text formats (Markdown, CSV, JSON, etc.).

These notes are owned by the individual, readable by humans, analyzable by machines, and (optionally) shareable with researchers or AI tools only if and when the owner chooses.

## Why this matters

Conditions like Long Covid, ME/CFS, IBS, POTS, and other "invisible illnesses" share a frustrating problem: medicine doesn't understand them well. At the root, this is a data problem — the kind of longitudinal, day-to-day patient data needed to understand these conditions is almost entirely absent from medical science. Short clinical appointments can't capture it. No app platform has accumulated it at the necessary scale and depth.

Compounding this, many doctors — and much of the general public — still don't fully accept that these are real, physical illnesses. Patients are often dismissed or sent home to cope. More and better data won't fix every attitude, but it is probably the most powerful thing that could change the picture: hard to dismiss a pattern that shows up across millions of people's lived experience.

Longitudinal patient data — daily self-observations over months and years — is exactly what's needed to understand these conditions, identify triggers, and accelerate research. If millions of people maintained their own health notes, and opted in to sharing them, that data would exist. AI can analyse free-form, heterogeneous data at scale. Hidden patterns — subtypes, common triggers, delayed effects, trajectories — could emerge from data that medicine currently can't even collect.

## A personal example

I've had Long Covid since early 2024. For much of that year I couldn't walk 50 metres to our letterbox without overexerting myself.

Almost from the start, I kept a simple fatigue diary. After a couple of months I had a nagging suspicion that overexertion was a big problem — but I couldn't detect it in the moment, and I didn't have a name for what was happening. It took six months to find a clinician (a physiotherapist, not a doctor) who knew about Post-Exertional Malaise (PEM). When I learned about PEM, a light went on. Looking back at my diary, the PEM events were obvious. I would have been significantly better off knowing this sooner.

The knowledge that helped me most didn't come from medicine. It came from the ME/CFS patient community, who had been living this long before Covid. That community's hard-won experience reached me through informal channels — not through clinical literature or the doctors I saw in my first six months.

This is precisely the kind of knowledge that better data could surface faster, and disseminate more widely.

## The idea

Each person (or family) creates a private Git repository — their own `my-health-notes` — and logs whatever is useful to them:

- Simple numeric scales (fatigue, mood, pain, sleep quality, etc.)
- Free-text daily notes (food, activity, symptoms, context)
- Wearable or device exports, lab results, medication notes

The format is flexible. Short entries are fine. Consistency over time matters more than detail.

Over time, this diary can reveal things that are invisible day-to-day:

- PEM triggers and delayed effects
- Personal baselines and early warning signs
- Correlations between food, sleep, activity, and symptoms

And at scale — if thousands or millions of people do this and choose to share — the collective data becomes a research resource that doesn't currently exist.

## Why Git?

Git (via GitHub, GitLab, or self-hosted) is a surprisingly good fit:

- **You own the data.** No platform monetises it. You decide what's private, what's shared, and you can revoke access at any time.
- **Plain text is durable.** Markdown and CSV files will be readable in 20 years. No proprietary formats, no app lock-in.
- **Longitudinal consistency is hard to fake.** A genuine Git history built up over years is a form of authenticity that's difficult to manufacture.
- **Incremental sync is efficient.** Researchers or AI tools can clone once and pull updates — years of daily notes with minimal bandwidth.

## Privacy (important)

Keeping health notes in a Git repository involves real risks. The defaults here matter:

- **Use a private repository** unless you have a specific reason to make it public.
- **Avoid identifiable details** — use a pseudonym, don't include full names, addresses, or other identifying information.
- **Be deliberate before sharing.** Consider sharing derived summaries rather than raw notes.

This project does not recommend uploading sensitive health data to public repositories.

## What's in this repository

This repo is a starter kit and proof of concept. It contains:

- Example directory structures and file formats
- Sample CSV formats for numeric scales (fatigue, mood, etc.)
- Simple Python scripts to plot and analyse data
- Illustrative sample data (fictional or anonymised)

It is not intended to store anyone's real personal health data.

## Who is this for?

- People managing chronic or poorly understood conditions
- Families keeping long-term notes for children with health issues
- Researchers interested in patient-generated longitudinal data
- Developers exploring AI, health data, and ethics

## Contributing

Contributions welcome: improved formats, analysis scripts, tooling that lowers the barrier to entry, ethical guidelines. Please do not submit real personal health data.

## Final thought

Medicine is very good at snapshots.
Chronic illness lives in timelines.

This project is about preserving those timelines — under the control of the people who live them.
