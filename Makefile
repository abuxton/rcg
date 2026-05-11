build:
	bundle install
	bundle exec jekyll build

serve:
	bundle install
	bundle exec jekyll serve --livereload

clean:
	rm -rf _site .jekyll-metadata
