# Example Blog Posts for AI on Rails

This document contains 5 example blog posts ready for publication on ai-on-rails.com. Each post aligns with the content strategy and targets specific keywords.

---

# Blog Post 1: How I Built a SaaS MVP in 19 Days Using AI

**Category:** Tutorial / AI-Powered Development
**Target Keyword:** ai rails development
**Word Count:** ~1,800
**Reading Time:** 8 minutes

---

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

[Book a free 30-minute call](https://calendly.com) to discuss your MVP. I'll tell you honestly whether it fits the 2-6 week timeline or needs a different approach.

---

*This post is part of the "AI-Powered Rails Development" series. Follow for more deep-dives into building production software with AI assistance.*

---

# Blog Post 2: The 70/30 Rule: What AI Can and Can't Do in Rails Development

**Category:** Insight / AI-Powered Development
**Target Keyword:** ai software development
**Word Count:** ~1,400
**Reading Time:** 6 minutes

---

After 6 months of building production Rails applications with AI assistance, I've landed on what I call the 70/30 rule:

**AI handles 70% of the code. Humans handle 100% of the decisions.**

This isn't about AI doing 70% of the work. It's about understanding which parts of software development can be safely delegated to AI and which absolutely cannot.

## The 70%: What AI Does Excellently

### CRUD Operations

Creating controllers, models, views, and forms for standard data operations is AI's sweet spot. Describe what you need:

"Create a RESTful controller for Projects with index, show, new, create, edit, update, and destroy actions. Projects belong to a Client and have a name, description, status enum, and due_date."

AI generates correct, idiomatic Rails code instantly. Before AI, this was 30 minutes of typing. Now it's 2 minutes of review.

### Database Migrations

"Add a status column to projects as an integer with a default of 0. Add an index on client_id and status for common queries."

```ruby
# AI-generated migration
class AddStatusToProjects < ActiveRecord::Migration[8.0]
  def change
    add_column :projects, :status, :integer, default: 0, null: false
    add_index :projects, [:client_id, :status]
  end
end
```

Perfect. Every time.

### Test Writing

Describing expected behavior and having AI write tests is incredibly efficient:

"Write RSpec tests for the Project model. Test validations for presence of name and client. Test the status enum. Test the scope for active projects."

AI generates comprehensive tests that would take 20 minutes to write manually.

### View Templates

ERB, Haml, or Slim templates with proper conditionals, loops, and partial usage. AI understands view layer patterns extremely well.

### CSS/Tailwind Classes

"Style this form with Tailwind. Use a card layout with proper spacing, responsive grid for form fields, and a prominent submit button."

AI's CSS output is often better than what I'd write manually because it's seen millions of examples.

### Documentation

README files, inline comments, API documentation. AI excels at explaining code in clear language.

## The 30%: What Humans Must Own

### Architecture Decisions

Should you use:
- Schema-per-tenant or row-level security for multi-tenancy?
- REST or GraphQL?
- Sidekiq or Solid Queue?
- PostgreSQL or MySQL?

AI will give you pros and cons, but it won't make the decision based on your specific context: team experience, scale requirements, existing infrastructure, and business constraints.

I've seen AI confidently recommend patterns that would fail at scale or create maintenance nightmares. Architecture requires understanding the full context of a project—something AI doesn't have.

### Security Review

AI-generated code often has security issues:

```ruby
# AI might generate this
def show
  @user = User.find(params[:id])
end

# But it should be this
def show
  @user = current_tenant.users.find(params[:id])
end
```

The first version leaks data across tenants. AI doesn't understand your authorization model unless you explicitly tell it every time.

Every controller action, every query, every user input handling needs human security review.

### Business Logic Validation

AI doesn't know your business. It doesn't know that:

- German invoices require specific VAT calculations
- Your client's workflow has an unusual approval step
- Certain data combinations should be impossible

When I built the DATEV export for Kunden-Cockpit, AI gave me a starting point. I then spent hours validating against official DATEV documentation because getting German accounting data wrong isn't acceptable.

### Performance at Scale

AI optimizes for correctness, not performance. It doesn't think about:

- What happens when this table has 1 million rows?
- Should this query be eager-loaded?
- Does this need a database index?
- Should this run in a background job?

I review every database query in AI-generated code. N+1 queries slip through constantly.

### User Experience Flows

AI can implement features but doesn't design experiences. The flow from user registration to first value delivered, error messaging that helps instead of frustrates, and progressive disclosure of complexity—these require human empathy and design thinking.

### Gem Selection

"Which gem should I use for PDF generation?"

AI lists options: Prawn, WickedPDF, Grover. It explains pros and cons. But it doesn't know:

- Your deployment environment constraints
- Which gems have good maintenance track records
- What your team already knows

Gem selection requires research beyond AI's training data, including checking GitHub activity, issues, and Rails version compatibility.

## How I Apply the 70/30 Rule

**Morning:** Architecture and planning (100% human). I decide what to build and how.

**Core work hours:** Feature implementation (70/30 blend). AI generates, I review and guide.

**Before committing:** Security and performance review (100% human). Every line of AI code gets scrutinized.

**Before shipping:** Integration testing and UX review (100% human). Does it actually work? Is it good?

## The Productivity Multiplier

The 70/30 rule isn't about AI doing 70% of the "work." It's about AI eliminating 70% of the typing, searching, and syntax remembering—the low-value parts of programming.

What remains is the high-value work: deciding what to build, ensuring it's secure, making it fast, and delivering good experiences.

A senior developer with AI assistance isn't 70% faster. They're 3-5x more productive because they can focus entirely on the work that matters.

## The Danger Zone

Where developers get into trouble:

1. **Trusting AI output without review.** AI code looks correct. It often isn't.

2. **Asking AI for architecture decisions.** It will answer confidently. It will often be wrong.

3. **Skipping security review.** AI doesn't understand your authorization model.

4. **Assuming AI-generated tests are sufficient.** AI tests what you describe, not edge cases you didn't think of.

AI is a powerful tool. Like all powerful tools, it requires skill and judgment to use safely.

---

*Building an MVP? I use this exact approach to deliver production applications in 2-6 weeks. [Book a call](https://calendly.com) to discuss your project.*

---

# Blog Post 3: The MVP Tech Stack I Recommend to Every Founder in 2025

**Category:** Founder Focus
**Target Keyword:** mvp tech stack
**Word Count:** ~1,500
**Reading Time:** 7 minutes

---

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

*Need help building your MVP? I deliver production Rails applications in 2-6 weeks at fixed prices. [Book a call](https://calendly.com) to discuss your project.*

---

# Blog Post 4: Why I Moved All My Clients to Kamal for Deployments

**Category:** Rails Excellence
**Target Keyword:** kamal deployment rails
**Word Count:** ~1,200
**Reading Time:** 5 minutes

---

For years, I deployed Rails apps to Heroku. It was expensive but simple. Then I tried Kubernetes. It was cheap but complex.

Kamal changed everything.

In 2024, I moved every client project to Kamal deployments on cheap Linux VPS servers. Here's why, and how the economics work.

## The Heroku Problem

Heroku was the default choice for Rails deployment for over a decade. And for good reason—`git push heroku main` and you're deployed.

But Heroku pricing became absurd:

- Basic dyno: $25/month (sleeps after 30 minutes of inactivity)
- Standard dyno: $50/month minimum
- PostgreSQL: $50/month for anything beyond hobby tier
- Redis: $25/month for Sidekiq
- SSL: Used to cost extra

A simple Rails app with background jobs easily costs $150-200/month on Heroku. A production app with proper redundancy? $400-600/month.

For an MVP validating a market, that's painful.

## The Kubernetes Problem

"Just use Kubernetes" is advice I've received repeatedly. So I tried it.

Setting up a Rails app on Kubernetes requires:
- Understanding pods, services, deployments, ingresses
- ConfigMaps and secrets management
- Helm charts or Kustomize
- kubectl fluency
- Load balancer configuration
- Certificate management
- Persistent volume claims

For a 3-person startup, Kubernetes is massive overhead. You're not Google. You don't need Google's infrastructure.

## Enter Kamal

Kamal (formerly MRSK) is Basecamp's answer to deployment complexity. DHH built it because even Basecamp—the company that created Rails—found existing deployment options unsatisfying.

The premise: Deploy Docker containers to any Linux server with SSH access. No orchestration platform. No complex networking. Just SSH and Docker.

## How Kamal Works

Your deployment configuration lives in `config/deploy.yml`:

```yaml
service: myapp
image: myregistry/myapp

servers:
  web:
    hosts:
      - 192.168.1.1
  job:
    hosts:
      - 192.168.1.2
    cmd: bundle exec sidekiq

registry:
  server: ghcr.io
  username: myusername
  password:
    - KAMAL_REGISTRY_PASSWORD

env:
  clear:
    DB_HOST: 192.168.1.3
  secret:
    - RAILS_MASTER_KEY
    - DATABASE_URL
```

Deploy with:

```bash
kamal deploy
```

That's it. Kamal:
1. Builds your Docker image
2. Pushes to your registry
3. SSHs into your servers
4. Pulls and starts the new container
5. Performs zero-downtime container replacement
6. Cleans up old containers

## The Economics

Here's what a production Rails deployment costs with Kamal:

**Hetzner Cloud (Germany):**
- Web server (CX21): €5.09/month (2 vCPU, 4GB RAM)
- Background jobs (CX11): €3.85/month (1 vCPU, 2GB RAM)
- PostgreSQL (managed): €12/month

**Total: ~€21/month**

Compare to Heroku: €150-200/month for equivalent resources.

For most MVPs, a single €5 VPS handles everything—web, background jobs, and database. Add dedicated database when you need it.

## What About Reliability?

"But Heroku handles everything!"

Yes, and you pay for that. With Kamal:

- Hetzner has 99.95% uptime SLA
- Docker containers restart automatically on failure
- Rolling deploys mean zero downtime
- Health checks route traffic only to healthy containers

For additional reliability:
- Add a second web server (€5/month) behind a load balancer
- Use managed PostgreSQL (automated backups, failover)
- Set up uptime monitoring (free with UptimeRobot)

Total cost for highly-available production setup: €40-60/month.

## The Migration Process

Moving a Heroku app to Kamal takes about 4 hours:

**Hour 1:** Set up server
- Provision Hetzner VPS
- Basic server hardening
- Install Docker

**Hour 2:** Configure Kamal
- Create deploy.yml
- Set up environment variables
- Configure SSL with Let's Encrypt

**Hour 3:** Database migration
- Spin up managed PostgreSQL
- Migrate data from Heroku Postgres
- Update DATABASE_URL

**Hour 4:** DNS and testing
- Update DNS records
- Verify deployment
- Set up monitoring

For existing clients, I've done this migration without any downtime.

## When to Stay on Heroku

Heroku still makes sense when:
- You have zero DevOps capacity and can't afford any learning curve
- Your company has budget but no time (enterprise contracts)
- You need specific Heroku add-ons without alternatives

For most startups and MVPs, these conditions don't apply.

## My Current Setup

For client projects, I use:

**Provider:** Hetzner Cloud (Germany) or DigitalOcean (US)
**Container Registry:** GitHub Container Registry (free for public, cheap for private)
**Database:** Managed PostgreSQL from the same provider
**SSL:** Let's Encrypt via Kamal's built-in traefik proxy
**Monitoring:** UptimeRobot (free) + Sentry (free tier)
**Backups:** Provider's automated snapshots + daily database dumps

Total cost for typical MVP: €15-30/month.

## Getting Started with Kamal

1. Add kamal to your Gemfile: `gem 'kamal'`
2. Run `kamal init` to generate configuration
3. Set up a Linux server with SSH access and Docker
4. Configure your deploy.yml
5. Run `kamal setup` then `kamal deploy`

The [Kamal documentation](https://kamal-deploy.org) is excellent. Most Rails developers can have their first deployment running in an afternoon.

---

*I deploy all client projects with Kamal on affordable infrastructure. Need help migrating from Heroku or setting up a new deployment? [Book a call](https://calendly.com).*

---

# Blog Post 5: Build vs. Buy: When Should Founders Choose Custom Development?

**Category:** Founder Focus
**Target Keyword:** build vs buy software
**Word Count:** ~1,300
**Reading Time:** 6 minutes

---

The build vs. buy decision costs founders more sleep than any technical choice. Build something custom, and you might waste months on solved problems. Buy an existing solution, and you might outgrow it in six months.

Here's my framework for making this decision after helping dozens of founders navigate it.

## The Real Question

"Should we build or buy?" is the wrong question. The right question is:

**"Is this software core to our competitive advantage?"**

If software is your product, build it. If software supports your product, buy it until you have a specific reason not to.

## When to Buy (Use Existing Tools)

### Problem: CRM and Sales Pipeline

**Buy:** Pipedrive, HubSpot, Close.io

Unless you're building a CRM company, don't build CRM functionality. The problem is completely solved. Integration APIs exist for everything.

### Problem: Email Marketing

**Buy:** ConvertKit, Mailchimp, Customer.io

Email infrastructure is complex—deliverability, bounce handling, unsubscribe management, spam filtering. Let specialists handle it.

### Problem: Customer Support

**Buy:** Intercom, Zendesk, Help Scout

Support ticket management and live chat are not your business. Focus elsewhere.

### Problem: Internal Team Communication

**Buy:** Slack, Discord, or just email

Building a chat system is tempting. Don't.

### Problem: Basic E-commerce

**Buy:** Shopify

If you're selling physical products, Shopify handles 95% of use cases better than any custom solution.

## When to Build Custom Software

### Your Core Product IS Software

If customers pay you for software functionality, you must own that software. SaaS companies, B2B platforms, and digital products need custom development.

**Example:** A project management tool for construction companies. The project management IS the product. Build it.

### Existing Tools Can't Handle Your Workflow

When your business process doesn't fit any existing tool, and you've actually tried multiple tools—build.

**Example:** A logistics company with unique routing algorithms and compliance requirements. Standard logistics software doesn't fit. Build a custom solution.

### You've Outgrown Generic Solutions

When you started with Airtable and now have 50,000 records with complex relationships and it's constantly breaking—time to build.

**Warning:** Make sure you've actually outgrown it. Many "outgrown" situations are actually configuration problems.

### Integration Requirements Are Extreme

When you need deep integrations between 5+ systems that don't have APIs or have incompatible APIs—custom middleware or a unified platform makes sense.

### You Need Specific German/EU Compliance

DATEV integration, German invoicing requirements (GoBD), EU data residency—sometimes compliance requirements make off-the-shelf solutions impractical.

## The Hybrid Approach

Most startups benefit from a hybrid approach:

**Build:** Your core product, the thing customers pay for
**Buy:** Everything else—CRM, email, support, analytics, payments

**Example:** A SaaS for restaurant inventory management.

*Build:* Inventory tracking, ordering system, analytics dashboard
*Buy:* Stripe (payments), Postmark (email), Intercom (support), QuickBooks API (accounting)

Focus development resources on what makes you unique. Everything else is a distraction.

## The MVP Build Decision

For founders building an MVP, the framework simplifies:

**If your startup succeeds, will you need to own this software?**

- Yes → Build it now, even if a simpler version
- No → Use existing tools, possibly forever

Many founders build custom admin panels, dashboards, and internal tools when Retool, Airtable, or even Notion would work fine for years.

## Cost Comparison Framework

When evaluating build vs. buy:

**Monthly SaaS costs for the next 24 months** vs. **Custom development cost + maintenance**

Example calculation:

*Scenario:* Client management system

**Buy option (Salesforce/HubSpot):**
- €150/user/month × 5 users = €750/month
- 24 months = €18,000
- Plus implementation, training, customization: €5,000
- **Total: €23,000 over 2 years**

**Build option (Custom Rails):**
- Development: €15,000-25,000
- Hosting: €30/month × 24 = €720
- Maintenance: €500/month × 24 = €12,000
- **Total: €28,000-38,000 over 2 years**

In this case, buying is cheaper initially. But consider:
- Does the SaaS do exactly what you need?
- Will you need features it doesn't support?
- Are there vendor lock-in risks?

If you'll need significant customization, build wins long-term.

## Red Flags: When to Stop and Reconsider

**Stop building if:**
- You've spent 3+ months building something you could buy for €100/month
- Your custom solution replicates a market-leading product with fewer features
- Engineers are maintaining internal tools instead of your actual product

**Stop buying if:**
- You're paying €1,000+/month for tools you use 10% of
- You need an integration that doesn't exist
- You're hacking around limitations constantly
- The vendor is sunsetting the product or raising prices aggressively

## My Recommendation for Most Founders

1. Start with off-the-shelf tools. Validate your business model first.
2. Build your core product custom. This is what makes you unique.
3. Only build supporting tools when you have clear evidence existing tools fail you.
4. Review every 6 months. What made sense at €10k ARR might not at €100k ARR.

The goal isn't to build everything or buy everything. The goal is to spend engineering resources only on problems that create competitive advantage.

---

*Need help deciding what to build vs. buy? I offer free 30-minute strategy calls for founders evaluating custom development. [Book a call](https://calendly.com) to discuss your situation.*

---

## Summary of Blog Posts

| # | Title | Category | Keywords | Length |
|---|-------|----------|----------|--------|
| 1 | How I Built a SaaS MVP in 19 Days Using AI | Tutorial | ai rails development | 1,800 words |
| 2 | The 70/30 Rule: What AI Can and Can't Do | Insight | ai software development | 1,400 words |
| 3 | The MVP Tech Stack I Recommend in 2025 | Founder | mvp tech stack | 1,500 words |
| 4 | Why I Moved All Clients to Kamal | Rails | kamal deployment rails | 1,200 words |
| 5 | Build vs. Buy: When to Choose Custom | Founder | build vs buy software | 1,300 words |

All posts include:
- Clear value proposition in the first paragraph
- Actionable advice backed by experience
- Code examples where relevant
- CTA linking to Calendly booking
- Appropriate length for SEO (1,000-2,000 words)
