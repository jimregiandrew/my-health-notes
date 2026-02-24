# My Health Notes (Personal Health Diaries)

## Overview

This repository demonstrates an idea:

> Individuals owning and maintaining their own long-term health notes

The core proposal is simple:

Using Git and Markdown each person (or family) creates their own ***private*** my-health-notes repository — a personal, longitudinal health diary — using plain text formats (Markdown, CSV, JSON, etc.).

These notes are owned by the individual, readable by humans, analyzable by machines, and (optionally) shareable with researchers or AI tools only if and when the owner chooses.

## Why this matters

Conditions like Long Covid, ME/CFS, IBS, POTS, and other "invisible illnesses" share a frustrating problem: medicine doesn't understand them well, and some doctors don't think they are "real" illnesses. This is in part a data problem — the kind of longitudinal, day-to-day patient data needed to understand these conditions is almost entirely absent from medical science. Short clinical appointments can't capture it. No app platform has accumulated it at the necessary scale and depth.

I have had 2 (at least) experiences where recording my personal health notes has really helped me (see below). So health notes can really help the individual. Imagine how they can help science and medicine if thousands or millions of people record such notes. I believe that they can move the dial on these otherwise intractable illnesses.

Some doctors and health care professionals are knowledable and amazing with such illnesses - typically those who had many patients with the illness. However, a significant proportion of doctors — and the general public — still don't fully accept that these are real, physical illnesses. Patients are often dismissed or sent home to cope. More and better data won't fix every attitude, but it is probably the most powerful thing that could change the picture: hard to dismiss a pattern that shows up across millions of people's lived experience.

Longitudinal patient data — daily self-observations over months and years — will help to understand these conditions, identify triggers, and accelerate research. If millions of people maintained their own health notes, and opted in to sharing them with researchers, that data would exist. AI can analyse free-form, heterogeneous data at scale. Hidden patterns — subtypes, common triggers, delayed effects, trajectories — could emerge from data that medicine currently can't even collect. AI is showing incredible progress in the programming field, if half that progress makes it to data analysis it will be a game changer for medicine *if* we have the data!

## A personal example

### Case 1

I've had Long Covid since early 2024. For almost all of 2024 I couldn't walk 50 metres to our letterbox without overexerting myself. Mercifully I am much improved since 2024.

Almost from the start, I kept a simple fatigue diary. After a couple of months into 2024 I had a nagging suspicion that overexertion was a big problem — but I couldn't detect it in the moment, and I didn't have a name for what was happening. But the data clealy showed significant events where my fatigue spiked (my health plummeted) and it took weeks or months to recover from the spike. The problem was that I was re-inventing the wheel. PEM is a known thing, at least by the doctors who have experience with ME/CFS or similar. I first heard about PEM from the charity ME Support. And they put me onto a clinician (a cardio-respiratory physiotherapist) who knew how to work with Post-Exertional Malaise (PEM). When I learned about PEM I was both happy to have my suspicion confirmed but upset that no health doctors had told me about this before. I would have been significantly better off knowing this sooner.

The knowledge that helped me most didn't come from medicine. It came from the ME/CFS patient community, who had been living this long before Covid. That community's hard-won experience reached me through informal channels — not through clinical literature or the doctors I saw in my first six months.

This is precisely the kind of knowledge that better data could surface faster, and disseminate more widely.

### Case 2

In December 2024 I had an informal referral to a holistic doctor. The doctor advised me to go on a 5-day water (and electrolyte) only fast. CAVEAT: fasting like this is demanding. It has made some people with Long Covid a lot sicker. But it has also helped many people.

I swalllowed hard and tried the fast. My heart rate rose during the fast, but dropped 2 beats a day for 7 says straight after the fast and was well below that of pre-fast. After 5 weeks my energy levels (physically) were doubled as compared to pre-fast, and I was swimming (gently) in the sea with my daughters for the first time in over a year. In 2025 I steadily improved through the fist 6 months to where I could get to work, and do ~75% of a 40hr week. I haven't fully recovered (When I get sick I get a lot sicker than usual, the mental fatigue limits are far less improved) but I am so much better.

Was it the fast ? (I've done 2 more now when I felt the fatigue coming back after the flu/bad cold). It looks and feels like it to me from my data. But that's not scientific certainty, and most doctors look at me sceptically whey I tell them. There is some scientific evidence that it helps and I've noted more acticles appearing recently. E.g. see an Internet search for 

> long term fast for Long Covid

and e.g. https://pmc.ncbi.nlm.nih.gov/articles/PMC10651743/. But so far it's exploratory only. The only way to answer this question properly is supposedly with a massive double blind random controlled trial. I'd argue that a far less controlled but massive data set (my health notes from 1000's of people) could also answer this question - or at least provide such strong evidence that it can't be ignored. And probably shed light on why it can make some people sicker.

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

Contributions welcome: improved formats, analysis scripts, tooling that lowers the barrier to entry, ethical guidelines. 

Privacy is the biggest issue. PAT's could be used to grant read-only access to trusted entities. And things like trusted execution environments (TEE) could be used. Data anonymity would be sufficient for me at least. A git archive does seem to be fundamentally incompatible with strong privacy guarantees. But this approach offers significant advantages (ownership is at the individual / parent level; incremental sync, longitudinal consistency), and maybe anonymity is sufficient.

Data first (private so no disclosure). Privacy under restricted access later.

Please do not submit real personal health data.

## Final thought

Medicine is very good at snapshots.
Chronic illness lives in timelines.

This project is about preserving those timelines — under the control of the people who live them.
