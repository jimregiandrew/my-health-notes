# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`my-health-notes` is a personal health diary and analysis tool built around Long Covid / CFS symptom tracking. The core idea: individuals log free-form daily health notes (food, fatigue, mood, anxiety, heart rate, sleep, bowel movements, activities) using personal subjective rating scales (typically 0–10), and AI is used to extract insights from that data — identifying patterns, PEM (Post-Exertional Malaise) triggers, correlations, and trends that might not be obvious to the individual.

The vision extends beyond personal use: if many people log similar health data, aggregated AI analysis could surface insights valuable to medical research on poorly-understood "invisible illnesses."

## Current State

This repository has no code yet. The `initial-prompt.md` file contains the founding concept/vision document. Development is starting from scratch.

## Key Domain Concepts

- **PEM (Post-Exertional Malaise)**: A hallmark of Long Covid/CFS where overexertion causes a delayed crash in energy/function, sometimes 24–48 hours later. Identifying PEM triggers from diary data is a primary use case.
- **Subjective rating scales**: User-defined numeric scales (e.g., fatigue 0–10, mood 0–10). Scales are personal and may evolve.
- **Free-form diary entries**: Natural language notes alongside structured ratings. AI is well-suited to parse and analyze this mixed format.
- **Longitudinal data**: The value comes from trends over time (weeks, months, years), not single entries.

## Communication Style

Always give honest, candid feedback. Don't soften criticism or hedge excessively. If something is a bad idea, say so directly.

## Design Considerations (from vision document)

- Input data is personal, sensitive health information — privacy is paramount.
- The diary format is intentionally flexible/free-form; parsers should be tolerant of variation.
- Fatigue tracking history predates the detailed diary (2+ years of simple fatigue scale vs. ~3 months of detailed logs) — the system should accommodate data of varying completeness.
- The project may eventually support aggregation across multiple users for research purposes, which has significant privacy/anonymization implications.
