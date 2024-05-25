---
title: Setting Up a Local AI-Powered Ruby on Rails Environment
description: Discover how to integrate AI into your Ruby on Rails application without the need for expensive API calls.
teaser: Discover how to integrate AI into your Ruby on Rails application without the need for expensive API calls. This guide walks you through setting up a local environment using Foreman and llamafile.
date: 2024-05-26 00:24
---

# Setting Up a Local AI-Powered Ruby on Rails Environment

<details class='italic'><summary>Table of Contents</summary><aside markdown="1">
* seed list
{:toc}
</aside></details>

## Overview


Integrating AI into your Ruby on Rails application can enhance its capabilities, but relying on external APIs can be costly. This guide will show you how to set up a local AI environment using [llamafile](https://llamafile.ai/){:target="_blank"} and Foreman to run your AI models alongside your Rails application.

## Step 1. Download llamafile

First, download the `Phi-3-mini-4k-instruct.Q4_0.llamafile` or a model of your choice from [huggingface.co](https://huggingface.co/Mozilla/Phi-3-mini-4k-instruct-llamafile/tree/main){:target="_blank"} and save it in the `storage` directory within your Rails application.

```sh
cd storage
wget https://huggingface.co/Mozilla/Phi-3-mini-4k-instruct-llamafile/blob/main/Phi-3-mini-4k-instruct.Q4_0.llamafile
```

Make sure the downloaded llamafile is executable:

```sh
chmod +x storage/Phi-3-mini-4k-instruct.Q4_0.llamafile
```

## Step 2. Set Up Foreman

Install Foreman, a tool to manage multiple processes for your Rails application:

```sh
gem install foreman
```

Create or update the `Procfile.dev` in your Rails application to include the web server and AI model:

```sh
# Procfile.dev
web: bin/rails server
ai: storage/Phi-3-mini-4k-instruct.Q4_0.llamafile
```

## Step 3. Start Your Rails Application

Run your Rails application along with the AI model using Foreman:

```sh
foreman start -f Procfile.dev
```

**Note:** The llamafile readme provides addional gotchas and tips for running the server locally.

## Step 4. Happy Coding and AI Integrating!

Your AI model will be available at `http://localhost:8080`, providing an API similar to OpenAI's. You can use the [OpenAI Gem](https://github.com/alexrudall/ruby-openai){:target="_blank"} by configuring it to point to your local llamafile API, or develop your own API client.
For more details on the API endpoints, refer to the [llamafile repository](https://github.com/Mozilla-Ocho/llamafile/blob/main/llama.cpp/server/README.md#api-endpoints){:target="_blank"}.

