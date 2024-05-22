# Template config
#
set :site_url, "https://ai-on-rails.com/" # for sitemap.xml.builder
set :site_title, "AI on Rails"
set :trailing_slash, false

# Extensions
#
activate :livereload                # live-reloading in dev
activate :directory_indexes         # for pretty URLs
activate :autoprefixer do |prefix|
  prefix.browsers = "last 2 versions"
end

activate :blog do |blog|
  blog.layout = "markdown_layout"    # layout from source/layouts
  blog.sources = "articles/{title}.html" # filename glob
  blog.permalink = "articles/{title}.html" # format of the URLs middleman generates
  blog.default_extension = ".md" 		 # file extension
  blog.publish_future_dated = true   # by default only builds posts with future dates
  blog.new_article_template = File.expand_path("../source/template.erb", __FILE__)
  # blog.prefix = "blog" 						  # enable this to put your URLs in a sub-path like site.com/blog/article-name
end

# Middleman doesn't support per-filetype layouts.
# The blog/ files already use the markdown layout, but we need to configure
# these top-level files separately.
#
# See 'Layouts' (https://middlemanapp.com/basics/layouts/)
#
markdown_pages = ["author", "articles", "imprint"]
markdown_pages.each do |pge|
  page "/#{pge}.html", :layout => "markdown_layout"
end

page "/*.xml", layout: false
page "/*.json", layout: false
page "/*.txt", layout: false

#-------------#

# MARKDOWN
#
activate :syntax                    # code highlighting
set :markdown_engine, :kramdown     # md parsing
set :markdown,                      # config for :kramdown
    input: "GFM",
    smartypants: true,
    toc_levels: 2..6,               # H2->H6 appear in markdown {:toc} block
    format: :html5

#-------------#

# You can enable these if you want, but some static hosts already do this for you
#
# configure :build do
#   activate :minify_css
#   activate :minify_javascript, compressor: Terser.new
# end
