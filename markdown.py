import re

def italic(text):
  return re.sub(r'(\*|_)(.*?)\1', r'<i>\2</i>', text)

def bold(text):
  return re.sub(r'(\*\*|__)(.*?)\1', r'<b>\2</b>', text)

def block(text):
  return re.sub(r'```(.*?)\n(.*?)```', r'<div class="highlight highlight-\1"><pre><code>\2</code></pre>\n</div>', text, flags=re.DOTALL)
def code(text):
  return re.sub(r'`(.*?)`', r'<code>\1</code>', text)

def header(text):
  return re.sub(r'^([^\n]*)$.^=+$', r'<h1>\1</h1>\n', text, flags=re.DOTALL + re.MULTILINE)

def subheader(text):
  return re.sub(r'^([^\n]*)$.^-+$', r'<h2>\1</h2>\n', text, flags=re.DOTALL + re.MULTILINE)

def bullet(text):
  return re.sub(r'^\w*\*([^\n]*)$', r'<li>\1</li>', text, flags=re.DOTALL + re.MULTILINE)

def linebreak(text):
  return re.sub(r'^\s*(.*?)\n$^\s*$', r'<p>\1</p>\n', text, flags=re.DOTALL + re.MULTILINE)

def character(text):
  marked = text.replace('&', '&amp;')
  return marked

def url(text):
  marked = re.sub(r'\[!\[([^\]]+)\]\(([^\)]*)\)\]\(((http|https|ftp|git):[^\)]*)\)', r'<a href ="\3"><img src="\2" alt="\1"></a>', text, flags=re.MULTILINE)
  marked = re.sub(r'\[([^\]]+)\]\(([^\)]*)\)', r'<a href ="\2">\1</a>', marked, flags=re.MULTILINE)
  marked = re.sub(r'\(([^ \)\]]*)\)', r'<a href ="\1">\1</a>', marked, flags=re.MULTILINE)
  marked = re.sub(r'\[\[([a-zA-Z0-9_\-+]+)\]\]', r'<a href ="\1.html">\1</a>', marked, flags=re.MULTILINE)

  return marked

def formlist(text):
  return re.sub(r'<p>(<li>.*?</li>)</p>', r'<p><ul>\1</ul></p>', text, flags=re.DOTALL + re.MULTILINE)

def html(text):
  return head + text + tail

head = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>example.md - Grip</title>
  <link rel="" href="/grip-static/favicon.ico" /><link rel="stylesheet" href="github.css" />
  <link rel="stylesheet" href="github2.css" />
  <style>
    /* Page tweaks */
    .preview-page {
      margin-top: 64px;
    }
    /* Discussion tweaks */
    .discussion-timeline.wide {
      width: 920px;
    }
    .timeline-comment-wrapper > .timeline-comment:after,
    .timeline-comment-wrapper > .timeline-comment:before {
      content: none;
  }
  </style>
</head>
<body>
  <div class="page">
    <div class="preview-page">
    <div class="container">
      <div class="repository-with-sidebar repo-container with-full-navigation">
        
        
        <div class="repository-content context-loader-container">
          <div id="readme" class="boxed-group flush clearfix announce instapaper_body md">
            
            <h3>
              <span class="octicon octicon-book"></span>
                example.md
                </h3>
              
              <div class="markdown-body entry-content">
'''


tail = '''
  </div>
    </div>
      </div>
      
      
      </div>
    </div>
  </div>
  <div>&nbsp;</div>
  </div><script>
    function showCanonicalImages() {
      var images = document.getElementsByTagName('img');
      if (!images) {
        return;
      }
      for (var index = 0; index < images.length; index++) {
        var image = images[index];
        if (image.getAttribute('data-canonical-src')) {
          image.src = image.getAttribute('data-canonical-src');
      }
  }
    }
    function scrollToHash() {
      if (location.hash && !document.querySelector(":target")) {
        var elements = document.getElementsByName('user-content-' + location.hash.slice(1));
        if (elements.length > 0) {
          elements[elements.length - 1].scrollIntoView();
      }
    }
}
  window.onhashchange = function() {
    scrollToHash();
    }
    window.onload = function() {
      scrollToHash();
  }
    showCanonicalImages();
</script>
</body>
</html>
'''