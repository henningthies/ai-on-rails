---
title: "The MVP Tech Stack I Recommend to Every Founder in 2025"
slug: mvp-tech-stack-2025
category: Founder Focus
target_keyword: mvp tech stack
reading_time: 7 minutes
status: draft
published_date: null
---

# The MVP Tech Stack I Recommend to Every Founder in 2025

"What technology should we use for our MVP?"

I get this question weekly. And in 2025, my answer is more definitive than ever.

**TL;DR:** Ruby on Rails 8 with PostgreSQL, Hotwire, Tailwind, and Kamal for deployment. Fixed choices, no decisions to make, proven at massive scale.

Here's why.

## The Problem with Tech Stack Decisions

Every hour spent debating technology is an hour not spent building your product. Founders—especially non-technical ones—often get trapped in analysis paralysis:

- "Should we use React or Vue?"
- "What about Next.js vs. Remix?"
- "Is Rails still relevant?"
- "Should we go serverless?"
- "What about microservices?"

These debates consumed months for companies that ultimately failed because they never shipped.

## Why Rails in 2025

Rails has a reputation problem. Many developers assume it's outdated. They're wrong.

**Who uses Rails today:**
- Shopify (billions in transactions)
- GitHub (largest code repository on Earth)
- Airbnb (though migrating pieces)
- Basecamp (obviously)
- Linear, Stripe Dashboard, Twitch, Coinbase

These aren't legacy decisions. GitHub and Shopify have actively invested in Rails because it's the most productive full-stack framework available.

**What changed with Rails 8:**

1. **Solid Queue** - Background jobs without Redis
2. **Solid Cache** - Caching without Redis
3. **Solid Cable** - WebSockets without Redis
4. **Kamal 2** - Docker deployment simplified
5. **Native authentication** - No more Devise debates

Rails 8 is self-contained. One database (PostgreSQL) handles everything. This dramatically simplifies deployment and reduces costs.

## The Complete Stack

### Database: PostgreSQL

Not MySQL. Not MongoDB. PostgreSQL.

Why:
- JSON columns when you need NoSQL flexibility
- Full-text search without Elasticsearch
- Row-level security for multi-tenancy
- Massive ecosystem and tooling
- Free on most platforms with generous limits

### Frontend: Hotwire (Turbo + Stimulus)

Not React. Not Vue. Hotwire.

"But what about interactivity?" Hotwire provides:

- Page navigation without full reloads (Turbo Drive)
- Partial page updates (Turbo Frames)
- Real-time updates (Turbo Streams)
- JavaScript sprinkles where needed (Stimulus)

For 95% of B2B SaaS features, Hotwire provides better UX than SPAs with 90% less code.

When you actually need React (complex dashboards, drag-and-drop, heavy real-time), you can add it to specific pages.

### Styling: Tailwind CSS

Not Bootstrap. Not custom CSS. Tailwind.

Why:
- AI tools generate excellent Tailwind code
- Consistent design without a designer
- Rapid iteration on UI
- Built-in responsive utilities
- Small final bundle size

### Deployment: Kamal

Not Heroku (expensive). Not Kubernetes (complex). Kamal.

Kamal deploys Docker containers to any Linux server with one command. A €5/month Hetzner VPS runs most MVPs comfortably. When you need to scale, add more servers.

### Payments: Stripe

The only choice for SaaS. The Rails integration is excellent. Don't reinvent payment processing.

### Email: Postmark or Resend

Transactional email that actually gets delivered. Both have generous free tiers.

## What This Stack Costs

**Development VPS:** €5-10/month (Hetzner)
**Domain:** €10-15/year
**Email:** Free tier or ~€10/month
**Error tracking:** Free tier (Sentry)
**Analytics:** Free (Plausible, self-hosted)

**Total:** Under €30/month to run a production SaaS.

Compare to:
- Vercel + Supabase + Redis: €50-100/month minimum
- AWS with "best practices": €200-500/month easily
- Heroku: €50-250/month for basic setup

## What About Scaling?

"But will it scale?"

Your MVP won't have scaling problems. If you're lucky enough to have scaling problems, you'll have revenue to solve them.

Rails scales to:
- Shopify: Millions of merchants
- GitHub: 100M+ developers
- Basecamp: Millions of users

The database is always the bottleneck. PostgreSQL handles this. Add read replicas when needed. Consider separation of concerns at that point.

Premature optimization is the root of all startup evil.

## The No-Decision Advantage

The most valuable aspect of this stack: zero decisions.

Every decision has cognitive cost. Technical co-founders debate frameworks instead of building. Non-technical founders hire developers who debate frameworks instead of building.

This stack removes decisions. Rails has "convention over configuration" built in. The right answer is usually the default.

When I start a new MVP project, day 1 looks identical every time:

```bash
rails new app_name --database=postgresql
bin/rails generate authentication
# Start building features
```

No setup debates. No architecture discussions. Ship.

## When to Choose Something Else

This stack isn't right for everyone:

**Choose React/Next.js if:**
- Your product IS the frontend (design tools, collaborative editors)
- You're hiring primarily frontend developers
- You have complex, highly interactive interfaces

**Choose Go/Rust if:**
- Performance is your product (infrastructure, developer tools)
- You need specific memory/latency guarantees

**Choose Django if:**
- Your team is Python-native
- Heavy data science/ML integration

For B2B SaaS, internal tools, marketplaces, and most web applications? Rails wins.

## Getting Started

If you're a founder evaluating technology:

1. Stop evaluating technology
2. Pick Rails 8
3. Build your MVP
4. Validate with customers
5. Revisit technology only if you hit actual limits

The best technology decision is the one that lets you stop making technology decisions and start making product decisions.

---

*Need help building your MVP? I deliver production Rails applications in 2-6 weeks at fixed prices. [Book a call](https://calendar.app.google/VdnLNLqjpSR4MS6G7) to discuss your project.*
