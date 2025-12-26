---
title: "How I Built a SaaS MVP in 19 Days Using AI"
slug: saas-mvp-19-days
category: Tutorial / AI-Powered Development
target_keyword: ai rails development
reading_time: 8 minutes
status: draft
published_date: null
---

# How I Built a SaaS MVP in 19 Days Using AI

When I tell founders I can build their MVP in 2-4 weeks, they're skeptical. I was too, until I actually did it.

This is the story of Kunden-Cockpit, a complete multi-tenant SaaS application I built in 19 days using AI tools and Rails 8. Not a landing page. Not a prototype. A production-ready application with authentication, multi-tenancy, invoicing, document management, and DATEV integration.

## The Project Scope

A client needed a client management system for German SMEs—accountants, craftsmen, and small agencies. The requirements:

- Multi-tenant architecture (each business sees only their data)
- Client and project management
- Invoice generation with German tax compliance
- Document storage and organization
- User roles and permissions
- Dashboard with charts and KPIs
- DATEV export for accountants

Two years ago, this would have been a 3-4 month project with a team. In 2025, with the right AI tools, it's a sprint.

## My AI-Augmented Stack

Before diving into the timeline, here's what I used:

**Development Environment:**
- Cursor IDE with Claude 4 integration
- Aider for complex refactoring sessions
- Claude Projects for context management

**Rails Stack:**
- Rails 8 with Hotwire (Turbo + Stimulus)
- PostgreSQL with row-level security for multi-tenancy
- ViewComponents for UI modularity
- Tailwind CSS
- Kamal for deployment

**AI Usage Pattern:**
- 70% of code generated or assisted by AI
- 30% architecture decisions, security, and business logic by me
- 100% of code reviewed by me before committing

## The 19-Day Timeline

### Days 1-3: Foundation

**Day 1:** Project setup and architecture decisions.

I started with a fresh Rails 8 app and spent the first day on decisions AI can't make well:

```ruby
# Multi-tenancy approach: acts_as_tenant gem with row-level security
# Why: Simpler than schema-per-tenant, more secure than column-based

# Authentication: Devise with 2FA preparation
# Why: Battle-tested, AI understands it perfectly

# Authorization: Pundit
# Why: Policy objects = perfect for AI-assisted development
```

**Days 2-3:** Core models and multi-tenancy.

This is where AI shines. I described the data model in natural language:

```
Create a Tenant model that has many Users. Each tenant has Clients,
Projects, Invoices, and Documents. All models must be scoped to tenant.
Generate the migrations, models, and basic associations.
```

Cursor generated 80% of the code. I reviewed, adjusted naming conventions, and added indexes. The multi-tenancy setup that would have taken a day took 2 hours.

### Days 4-8: Core Features

**Day 4:** Client management CRUD with search and filtering.

**Day 5:** Project management with client associations.

**Day 6:** Invoice system with line items and calculations.

**Day 7:** German tax logic (VAT, reverse charge) and PDF generation.

**Day 8:** DATEV export format.

Each feature followed the same pattern:

1. Describe the feature to AI
2. Generate initial code
3. Review and adjust
4. Write edge case tests (AI-assisted)
5. Refine based on test failures

The DATEV export was interesting—Claude had trained on the format specification and generated correct export code on the first try. That would have been hours of documentation reading.

### Days 9-14: Dashboard and Polish

**Days 9-10:** Dashboard with charts using Chartkick.

**Day 11:** Document upload and organization with Active Storage.

**Day 12:** User roles and permissions with Pundit policies.

**Day 13:** Email notifications and Sidekiq background jobs.

**Day 14:** UI polish, responsive design, loading states.

### Days 15-19: Production Readiness

**Day 15:** Security audit—OWASP top 10, input validation, CSRF.

**Day 16:** Performance optimization—N+1 queries, caching, indexes.

**Day 17:** Test coverage to 85%+, CI/CD pipeline.

**Day 18:** Deployment with Kamal to Hetzner.

**Day 19:** Demo data, documentation, client walkthrough.

## What AI Did Well

**Boilerplate generation:** Controllers, views, and forms were 90% AI-generated. The patterns are well-understood, and AI produces clean, idiomatic Rails code.

**Test writing:** Describing expected behavior and having AI write RSpec tests saved enormous time. I still wrote integration tests manually for critical paths.

**Documentation lookup:** Instead of searching Stack Overflow, I asked Claude directly. "How do I configure Active Storage for S3 with Cloudflare R2?" Instant, accurate answers.

**Refactoring:** When I decided to change the invoice model structure on day 7, Aider handled the refactoring across 12 files in minutes.

## What AI Did Poorly

**Architecture decisions:** AI will happily generate any architecture you ask for, even bad ones. Choosing between multi-tenancy approaches, database structure, and gem selection required my experience.

**Security:** AI-generated code often has subtle security issues. Every controller action, authorization check, and data validation was manually reviewed.

**German business logic:** Tax rules, DATEV formats, and GoBD compliance needed careful human verification. AI provided a starting point, but I validated against official documentation.

**Performance at scale:** AI doesn't think about what happens with 10,000 records. Index placement, query optimization, and caching strategies needed human judgment.

## The Economics

**Traditional agency approach:**
- 3-4 developers for 3 months
- Cost: €60,000 - €100,000
- Timeline: 12-16 weeks

**AI-augmented solo approach:**
- 1 senior developer for 19 days
- Cost: €15,000 - €25,000 (depending on complexity)
- Timeline: 3-4 weeks

This isn't about replacing developers with AI. It's about one senior developer achieving the output of a small team by eliminating the low-value work.

## Lessons Learned

1. **AI is a multiplier, not a replacement.** The 13 years of Rails experience is what makes AI useful. Without knowing what good code looks like, I couldn't review AI output effectively.

2. **Architecture upfront, AI in sprints.** Spend day 1 making decisions. Then let AI accelerate the implementation.

3. **Review everything.** AI-generated code looks correct but often has subtle issues. Code review isn't optional.

4. **Tests are your safety net.** When AI generates code, good test coverage catches the errors humans miss.

5. **Fixed scope enables speed.** This timeline only worked because requirements were clear. Scope creep would have destroyed the schedule.

## Want This for Your Project?

I offer fixed-price MVP development with the same approach. The Kunden-Cockpit project proved the model works—now I'm applying it to client projects.

[Book a free 30-minute call](https://calendar.app.google/VdnLNLqjpSR4MS6G7) to discuss your MVP. I'll tell you honestly whether it fits the 2-6 week timeline or needs a different approach.

---

*This post is part of the "AI-Powered Rails Development" series. Follow for more deep-dives into building production software with AI assistance.*
