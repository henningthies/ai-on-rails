site_url = config.site_url

xml.instruct!
xml.urlset "xmlns" => "http://www.sitemaps.org/schemas/sitemap/0.9" do
  sitemap.resources.select { |page| page.destination_path =~ /\.html/ }.each do |page|
    xml.url do
      xml.loc "#{site_url}#{page.url}#{page.url.size > 1 ? '/' : ''}"
      xml.lastmod Date.today.to_time.iso8601
      xml.changefreq page.data.changefreq || "weekly"
      xml.priority page.data.priority || "0.8"
    end
  end
end
