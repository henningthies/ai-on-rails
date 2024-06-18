---
title: "Using OpenAI in Rails: A first usecase"
description: Learn how to integrate OpenAI into your Ruby on Rails application to generate dynamic content and enhance user experience.
teaser: Learn how to integrate OpenAI into your Ruby on Rails application to generate dynamic content and enhance user experience.
date: 2024-06-18 06:00
---

# Using OpenAI in Rails: A first usecase

OpenAI has revolutionized the way we interact with artificial intelligence with its ChatGPT product.
From generating human-like text to providing insightful recommendations, OpenAI's language models have a wide range of applications.
Integrating OpenAI into a Ruby on Rails application opens up numerous possibilities for enhancing user experience, automating tasks, and generating dynamic content.

In this blog post, we'll walk through a simple use case of using OpenAI in a Rails application: generating an outline for a blog post.

## Setting Up OpenAI in Rails

### Adding necessary gems to the Gemfile

To start using OpenAI in your Rails application, you'll need to add the [`ruby-openai`](https://github.com/alexrudall/ruby-openai){:target="_blank"} gem to your Gemfile.
This gem provides a simple interface for interacting with the OpenAI API. Open your Gemfile and add the following line:

```ruby
gem 'ruby-openai'
```

After adding the gem, run bundle install to install it:

```sh
bundle install
```

### Configuring OpenAI API credentials

Once the gem is installed, you'll need to configure it with your OpenAI API key. You can obtain an API key by signing up on the OpenAI website and creating an [API token](https://platform.openai.com/api-keys){:target="_blank"}. 

Create a new initializer file in `config/initializers/openai.rb` and add the following code to set up your API key:

```ruby
OpenAI.configure do |config|
  config.access_token = ENV.fetch("OPENAI_ACCESS_TOKEN", "")
  config.organization_id = ENV.fetch("OPENAI_ORGANIZATION_ID", "")
end
```

For security reasons, it's best to store your API key in an environment variable. You can add the key to your `.env` file (if you are using the [`dotenv-rails`](https://github.com/bkeepers/dotenv){:target="_blank"} gem) or set it directly in your environment. Here's an example of how to add it to your `.env` file:

```sh
OPENAI_ACCESS_TOKEN=your_api_key_here
OPENAI_ORGANIZATION_ID=your_organization_id_here
```

Make sure to add .env to your .gitignore file to prevent it from being committed to your version control system.

## Implementing the First Use Case

Example use case: Generate an outline for a blog post

## Scaffold a post model with title, content and outline

First, let's generate a scaffold for the Post model. This will create the necessary files for our posts, including the model, controller, and views. Run the following command:

```sh
rails generate scaffold Post title:string content:text outline:text
rails db:migrate
```

This command creates a Post model with `title`, `content`, and `outline` attributes. It also sets up the necessary database table and routes.

## Hooking up the OpenAI call in an ActiveRecord callback

Now, let's use OpenAI to generate an outline for the blog post automatically whenever a new post is created. We'll do this by adding a callback to our Post model.

Open the `app/models/post.rb` file and add the following code:

```ruby
# app/models/post.rb
class Post < ApplicationRecord
  validates :title, presence: true,
    length: {minimum: 10, maximum: 80}

  after_validation :generate_outline, on: :create

  private

  def generate_outline
    system_prompt = <<~PROMPT
Generate an outline for blog post based on a
title to help the user structure their thoughts.
    PROMPT

    self.outline = OpenAI::Client.new.chat(
      parameters: {
        model: "gpt-3.5-turbo",
        messages: [
          {role: "system", content: system_prompt},
          {role: "user", content: title}
        ],
        temperature: 0.8
      }
    ).dig("choices", 0, "message", "content")
  end
end
```

## Conclusion

This integration of OpenAI into a Ruby on Rails application is only a small glimpse of the possibilities that AI can bring to your projects. By leveraging the power of OpenAI's language models, you can automate tasks, generate dynamic content, and enhance user experience in your Rails applications. Experiment with different use cases and explore the full potential of AI in your projects.

Further ideas for enhancing this use case include:

- Generating the outline asynchronously using Active Job
- Finetuning the prompt for a better outline generation


<!-- table of contents (html disclosure + kramdown {:toc}) -->
<details class='italic' open><summary>Table of Contents</summary><aside markdown="1">
* seed list
{:toc}
</aside></details>
