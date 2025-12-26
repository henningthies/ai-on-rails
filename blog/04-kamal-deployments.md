---
title: "Why I Moved All My Clients to Kamal for Deployments"
slug: kamal-deployments
category: Rails Excellence
target_keyword: kamal deployment rails
reading_time: 5 minutes
status: draft
published_date: null
---

# Why I Moved All My Clients to Kamal for Deployments

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

*I deploy all client projects with Kamal on affordable infrastructure. Need help migrating from Heroku or setting up a new deployment? [Book a call](https://calendar.app.google/VdnLNLqjpSR4MS6G7).*
