@app.route('/image', methods = ['GET'])
def get_image():
  url = request.args.get('url', '')
  if not url:
    abort(400)

  if is_image(url):
    return redirect(url)

def is_image(url):
  image_extensions = ['.jpg', '.gif', '.png', '.jpg', '.bmp', '.webp', '.webm']
  extension = url[url.rfind('.'):]
  return extension in image_extensions
