((window, $, templates) ->
  mainContainer = $ '#main-container'
  readerFrame = null
  content = null
  placeholder = null

  onFrameLoad = () ->
    doc = readerFrame.contents()
    body = doc.find 'body'
    patched = body.html().replace placeholder, content
    body.html patched

  setup = () ->
    readerFrame = $ '#views-reader-frame'
    if not readerFrame.length
      setTimeout setup, 200
      return
    content = readerFrame.data 'content'
    placeholder = readerFrame.data 'placeholder'
    readerFrame.on 'load', () ->
      if (readerFrame.contents().prop 'readyState') is 'complete'
        onFrameLoad()

  setup()

) this, this.jQuery, this.templates
