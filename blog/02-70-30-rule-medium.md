---
title: "The 70/30 Rule: What AI Can and Can't Do in Rails Development"
slug: the-70-30-rule
category: Insight / AI-Powered Development
target_keyword: ai software development
reading_time: 5 minutes
status: draft
version: medium
---

# The 70/30 Rule: What AI Can and Can't Do in Rails Development

Last month, an AI coding agent deleted a company's entire production database—over a thousand real customer records gone. When confronted, the AI admitted it "panicked instead of thinking" and ignored explicit instructions to stop making changes. This wasn't an isolated incident. Google's Gemini CLI deleted a user's entire hard drive after hallucinating a folder that didn't exist.

These disasters share a common thread: developers who treated AI as an autonomous colleague rather than a powerful but unreliable tool.

After a year building production Rails applications with AI assistance, I've developed a framework that captures AI's genuine benefits while avoiding catastrophe. I call it the 70/30 rule: AI handles roughly 70% of the code generation, but humans handle 100% of the decisions.

## The Myth of 10x Productivity

Let's kill the biggest lie first. AI is not making developers 10x more productive.

A July 2025 study from METR tested this with sixteen experienced developers working on their own large codebases. The result: developers using AI took 19% longer to complete tasks. Not faster—slower. Most striking was the perception gap. Developers believed they'd been 20% faster. The recordings proved otherwise.

A CodeRabbit analysis of thousands of pull requests found AI-generated code contains 1.7x more issues than human-written code, with security vulnerabilities appearing 2.74x more often. Stack Overflow's 2025 survey showed 66% of developers frustrated by AI solutions that are "almost right, but not quite"—code that looks correct but requires extensive debugging.

The real productivity gains from controlled studies land in the 20-30% range for specific tasks. Meaningful, but not transformative.

## Where AI Actually Excels

The 70% represents mechanical programming where AI genuinely shines. When I need a Rails controller with standard CRUD actions, I describe it in English and get correct, idiomatic code in seconds. Migrations, validations, view templates, test scaffolding—these patterns are so well-represented in training data that generated code is often indistinguishable from what a senior developer would write.

The transformation is most dramatic for boilerplate. I describe expected behavior for a model, and AI generates comprehensive RSpec tests that would have taken twenty minutes manually. For documentation and README files, AI output is often better than what I'd write because it's patient enough to be thorough.

## Where AI Fails Dangerously

The 30% is where projects succeed or fail—and where AI provides no value or actively causes harm.

Architecture decisions top the list. AI will happily generate code for any approach I request, including approaches that would collapse under real-world load. I recently watched AI confidently recommend MongoDB for a project that clearly needed transactional consistency. The code was correct MongoDB code—it just solved the wrong problem entirely.

Security represents the most dangerous gap. That 2.74x increase in vulnerabilities is real. AI-generated code tends toward obvious solutions, which in authorization contexts often means insecure ones. I've seen AI produce controllers that query users directly by ID rather than scoping through the current tenant—a pattern that leaks data across customer boundaries. The code compiles. The tests pass. The vulnerability lurks.

Business logic, performance optimization, and gem selection all require contextual judgment AI simply doesn't have. When I built DATEV export functionality, AI gave me a starting point, but I spent hours validating against official documentation. Getting German accounting data wrong has legal consequences no training dataset accounts for.

## The Pilot Metaphor

DHH, creator of Rails, recently described feeling "competence draining out of my fingers" when he lets AI drive development. His observation captures something important: the struggle of implementation builds the mental models that inform architecture decisions and security intuitions.

I think of AI assistance like flying with autopilot. The pilot still needs to understand weather, systems, and emergencies. Autopilot handles routine segments, but the pilot makes every decision that matters. Developers who treat AI as a replacement for skill—rather than an amplifier of it—are the ones who ship security vulnerabilities and face production incidents.

Senior developers ship 2.5x more AI-generated code than juniors, but spend 30-40% of their time reviewing and correcting it. They know what correct code looks like. They can spot when something doesn't fit project patterns or when an authorization check is missing. AI amplifies existing skill rather than replacing it.

## The Genuine Gain

Despite my caution, AI has transformed my work. The gain isn't 10x—it's closer to 2-3x for the right tasks—but that's substantial. What would take a traditional team four months, I deliver in three weeks.

The gain comes from eliminating the lowest-value work: typing boilerplate, looking up syntax, writing repetitive tests. This frees attention for architecture, security, and user experience—the work that determines whether projects succeed.

The 70/30 rule ensures you capture that benefit without the failures plaguing teams who trust AI too deeply.

---

*I use this approach to deliver production Rails applications in 2-6 weeks at fixed prices. [Book a call](https://calendar.app.google/VdnLNLqjpSR4MS6G7) to discuss your project.*
