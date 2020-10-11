A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

I think I've got things running smoothly and fixed some major bugs, but feel free to file issues or make pull requests if you want to improve the generic template / theme.

### Note: if you are using this repo and now get a notification about a security vulnerability, delete the Gemfile.lock file. 

# Instructions

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://academicpages.github.io/

## To run locally (not on GitHub Pages, to serve on your own computer)
1. Clone the repository and made updates as detailed above

### MacOSX
2. Make sure you have 
    i. ruby via brew: https://qiita.com/is-lab/items/e0443b79da117ed48294 using gcc instead of xcode clang.
    ```
    brew install rbenv
    echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bash_profile
    echo 'if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi' >> ~/.bash_profile
    brew install ruby-build
    brew install rbenv-gemset
    brew install rbenv-gem-rehash

    rbenv --version 　　　　　 # => バージョン確認
    rbenv install --list 　　 # => インストール可能なバージョン一覧の表示
    rbenv install [バージョン] # => rubyのインストール
    rbenv rehash             # => rbenv の再読み込み
    rbenv global [バージョン]  # => defaultで使うrubyのバージョン

    export CC=/usr/bin/gcc
    ```
    ii. nodejs via nodebrew: https://qiita.com/kyosuke5_20/items/c5f68fc9d89b84c0df09
    ```
    brew install nodebrew
    nodebrew -v

    nodebrew ls-remote
    mkdir -p ~/.nodebrew/src
    nodebrew install-binary {version}/latest/stable
    nodebrew ls
    nodebrew use {version} e.g. v7.1.0

    nodebrew ls
    ```

3. Run `bundle clean` to clean up the directory (no need to run `--force`)
4. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
    i. nokogiri install has problem https://qiita.com/ywindish/items/5cb01ee974f8a7f403ba
    ```
    bundle config build.nokogiri --use-system-libraries
    ```
    or
    ```
    bundle config build.nokogiri --use-system-libraries --with-xml2-include=$(brew --prefix libxml2)/include/libxml2
    ```
5. Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change. `--port 4444` to serve on different port.

### Linux/Windows with WSL
2. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
3. Run `bundle clean` to clean up the directory (no need to run `--force`)
4. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
5. Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change. `--port 4444` to serve on different port.

For error 
```
Unable to load the EventMachine C extension; To use the pure-ruby reactor, require 'em/pure_ruby'
``` 
let install the eventmachine package by command 
```
gem uninstall eventmachine

gem install eventmachine --platform ruby
```

OR this following is worked with Windows
```

    Go to this folder C:\Ruby24-x64\lib\ruby\gems\2.4.0\gems\eventmachine-1.2.5-x64-mingw32\lib

    open this file eventmachine.rb
    write this require 'em/pure_ruby' in the first line of code in the file

```

# Changelog -- bugfixes and enhancements

There is one logistical issue with a ready-to-fork template theme like academic pages that makes it a little tricky to get bug fixes and updates to the core theme. If you fork this repository, customize it, then pull again, you'll probably get merge conflicts. If you want to save your various .yml configuration files and markdown files, you can delete the repository and fork it again. Or you can manually patch. 

To support this, all changes to the underlying code appear as a closed issue with the tag 'code change' -- get the list [here](https://github.com/academicpages/academicpages.github.io/issues?q=is%3Aclosed%20is%3Aissue%20label%3A%22code%20change%22%20). Each issue thread includes a comment linking to the single commit or a diff across multiple commits, so those with forked repositories can easily identify what they need to patch.
