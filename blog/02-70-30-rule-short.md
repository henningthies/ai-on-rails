---
title: "The 70/30 Rule: What AI Can and Can't Do in Rails Development"
slug: the-70-30-rule
category: Insight / AI-Powered Development
target_keyword: ai software development
reading_time: 2 minutes
status: draft
version: short
---

# The 70/30 Rule: What AI Can and Can't Do in Rails Development

An AI coding agent recently deleted a company's entire production database. Google's Gemini CLI deleted a user's hard drive after hallucinating a folder that didn't exist. These aren't edge cases—they're what happens when developers treat AI as an autonomous colleague rather than a powerful but unreliable tool.

After a year building production Rails applications with AI, I've landed on a simple framework: AI handles 70% of the code generation. Humans handle 100% of the decisions.

## The Reality Check

AI is not making developers 10x more productive. A July 2025 study found experienced developers using AI took 19% longer on tasks—not faster, slower. They believed they'd been 20% faster. The recordings proved otherwise.

CodeRabbit's analysis: AI-generated code has 1.7x more issues and 2.74x more security vulnerabilities than human code. Real productivity gains from rigorous studies: 20-30%, not 10x.

## The 70%: Where AI Shines

Controllers, migrations, view templates, test scaffolding—AI handles these brilliantly. Describe what you need in English, get correct Rails code in seconds. What took thirty minutes of typing now takes two minutes of review. For boilerplate and documentation, AI output is often better than what I'd write manually.

## The 30%: Where AI Fails

Architecture decisions, security review, business logic, performance optimization—these require contextual judgment AI doesn't have. I've seen AI recommend MongoDB for projects needing transactional consistency, generate controllers that leak data across tenants, and produce code that works for ten records but collapses at ten thousand.

Every controller action in AI-generated code needs human security review. This isn't paranoia; it's a response to that 2.74x vulnerability rate.

## The Bottom Line

Senior developers ship 2.5x more AI code than juniors—but spend 30-40% of their time fixing it. They know what correct code looks like. AI amplifies existing skill rather than replacing it.

The developers at risk are those believing the 10x marketing. They'll ship vulnerabilities, accumulate debt they don't understand, and face the production incidents that make headlines.

AI eliminates the lowest-value programming work. The 70/30 rule ensures you capture that benefit without the disasters.

---

*I deliver production Rails apps in 2-6 weeks at fixed prices. [Book a call](https://calendar.app.google/VdnLNLqjpSR4MS6G7) to discuss your project.*
