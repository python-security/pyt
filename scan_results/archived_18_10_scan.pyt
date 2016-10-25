pallets/flask
https://github.com/pallets/flask
Entry file: flask/setup.py
Scanned: 2016-10-11 18:14:36.283896
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

gigq/flasktodo
https://github.com/gigq/flasktodo
Entry file: flasktodo/application.py
Scanned: 2016-10-11 18:14:38.118531
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flosch/simpleapi
https://github.com/flosch/simpleapi
Entry file: simpleapi/example_project/server/flask1/app.py
Scanned: 2016-10-11 18:14:39.802222
No vulnerabilities found.


codebykat/robotkitten
https://github.com/codebykat/robotkitten
Entry file: None
Scanned: 2016-10-11 18:15:01.560131
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/codebykat/robotkitten.

mitsuhiko/flask-oauth
https://github.com/mitsuhiko/flask-oauth
Entry file: flask-oauth/example/facebook.py
Scanned: 2016-10-11 18:15:31.945990
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-openid
https://github.com/mitsuhiko/flask-openid
Entry file: flask-openid/flask_openid.py
Scanned: 2016-10-11 18:15:34.648207
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

artisonian/flaskengine
https://github.com/artisonian/flaskengine
Entry file: flaskengine/flaskengine/__init__.py
Scanned: 2016-10-11 18:15:40.015333
No vulnerabilities found.


toomoresuch/template-gae-with-flask
https://github.com/toomoresuch/template-gae-with-flask
Entry file: template-gae-with-flask/application.py
Scanned: 2016-10-11 18:15:40.525272
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: template-gae-with-flask/flask.py

aljoscha/shot-o-matic
https://github.com/aljoscha/shot-o-matic
Entry file: shot-o-matic/shotomatic.py
Scanned: 2016-10-11 18:16:33.925018
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-sqlalchemy
https://github.com/mitsuhiko/flask-sqlalchemy
Entry file: flask-sqlalchemy/flask_sqlalchemy/__init__.py
Scanned: 2016-10-11 18:16:36.461562
No vulnerabilities found.


mitsuhiko/flask-fungiform
https://github.com/mitsuhiko/flask-fungiform
Entry file: flask-fungiform/examples/example.py
Scanned: 2016-10-11 18:16:38.804206
No vulnerabilities found.


fsouza/talks
https://github.com/fsouza/talks
Entry file: talks/flask/app.py
Scanned: 2016-10-11 18:16:41.854468
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

unbracketed/flapp
https://github.com/unbracketed/flapp
Entry file: flapp/flapp/project_template/application.py
Scanned: 2016-10-11 18:16:44.056582
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dcolish/flask-markdown
https://github.com/dcolish/flask-markdown
Entry file: flask-markdown/tests/test_markdown.py
Scanned: 2016-10-11 18:17:33.470098
No vulnerabilities found.


blossom/flask-gae-skeleton
https://github.com/blossom/flask-gae-skeleton
Entry file: flask-gae-skeleton/gae/main.py
Scanned: 2016-10-11 18:17:36.276229
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kijun/flask-methodhack
https://github.com/kijun/flask-methodhack
Entry file: flask-methodhack/flaskext/methodhack.py
Scanned: 2016-10-11 18:17:38.585148
No vulnerabilities found.


viniciusfs/pasted-flask
https://github.com/viniciusfs/pasted-flask
Entry file: pasted-flask/pasted.py
Scanned: 2016-10-11 18:17:39.891936
Vulnerability 1:
File: pasted-flask/pasted.py
 > User input at line 219, trigger word "form[": 
	hexdigest = calc_md5(request.form['code'])
Reassigned in: 
	File: pasted-flask/pasted.py
	 > Line 221: paste = query_db('select * from pasted where md5 = ?', [hexdigest],one=True)
	File: pasted-flask/pasted.py
	 > Line 225: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 231: paste_id = cur.lastrowid
	File: pasted-flask/pasted.py
	 > Line 232: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 234: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 203: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 207: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 209: ret_MAYBE_FUNCTION_NAME = render_template('form.html',original=paste)
	File: pasted-flask/pasted.py
	 > Line 213: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 217: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
File: pasted-flask/pasted.py
 > reaches line 229, trigger word "execute(": 
	cur = g.db.execute('insert into pasted (code, md5, viewed_at, parent) values (?, ?, ?, ?)', [request.form['code'], hexdigest, viewed_at, request.form['parent']])



Cornu/Brain
https://github.com/Cornu/Brain
Entry file: Brain/brain/__init__.py
Scanned: 2016-10-11 18:17:44.604381
Vulnerability 1:
File: Brain/brain/controllers/text.py
 > User input at line 43, trigger word "get(": 
	key = request.form.get('search')
File: Brain/brain/controllers/text.py
 > reaches line 44, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('/' + key)



jbochi/scrum-you
https://github.com/jbochi/scrum-you
Entry file: scrum-you/application.py
Scanned: 2016-10-11 18:18:05.563985
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

miracle2k/flask-assets
https://github.com/miracle2k/flask-assets
Entry file: flask-assets/tests/test_config.py
Scanned: 2016-10-11 18:18:36.975871
No vulnerabilities found.


jgumbley/flask-payment
https://github.com/jgumbley/flask-payment
Entry file: flask-payment/tests.py
Scanned: 2016-10-11 18:18:38.464376
No vulnerabilities found.


eugenkiss/Simblin
https://github.com/eugenkiss/Simblin
Entry file: Simblin/simblin/__init__.py
Scanned: 2016-10-11 18:18:40.181802
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jugyo/flask-gae-template
https://github.com/jugyo/flask-gae-template
Entry file: flask-gae-template/app.py
Scanned: 2016-10-11 18:18:41.982922
No vulnerabilities found.


swanson/flask-embedly
https://github.com/swanson/flask-embedly
Entry file: flask-embedly/example/app.py
Scanned: 2016-10-11 18:18:43.378892
No vulnerabilities found.


LightStyle/Python-Board
https://github.com/LightStyle/Python-Board
Entry file: Python-Board/src/index.py
Scanned: 2016-10-11 18:18:44.759847
No vulnerabilities found.


miku/flask-gae-stub
https://github.com/miku/flask-gae-stub
Entry file: flask-gae-stub/flask/app.py
Scanned: 2016-10-11 18:18:46.603485
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

derwiki/wordisms_flask
https://github.com/derwiki/wordisms_flask
Entry file: wordisms_flask/www/main.py
Scanned: 2016-10-11 18:19:05.919632
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flebel/cisco79xx_phone_directory
https://github.com/flebel/cisco79xx_phone_directory
Entry file: cisco79xx_phone_directory/cisco79xx_phone_directory.py
Scanned: 2016-10-11 18:19:34.640362
No vulnerabilities found.


jkossen/imposter
https://github.com/jkossen/imposter
Entry file: None
Scanned: 2016-10-11 18:19:38.116710
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/jkossen/imposter.

sublee/subleekr
https://github.com/sublee/subleekr
Entry file: subleekr/subleekr/app.py
Scanned: 2016-10-11 18:19:40.474051
No vulnerabilities found.


akhodakivskiy/flask
https://github.com/akhodakivskiy/flask
Entry file: flask/skeleton/skeleton/__init__.py
Scanned: 2016-10-11 18:19:42.842073
No vulnerabilities found.


thadeusb/flask-cache
https://github.com/thadeusb/flask-cache
Entry file: flask-cache/examples/hello.py
Scanned: 2016-10-11 18:19:44.664503
No vulnerabilities found.


kamalgill/flask-appengine-template
https://github.com/kamalgill/flask-appengine-template
Entry file: flask-appengine-template/src/lib/flask/sessions.py
Scanned: 2016-10-11 18:19:47.693675
No vulnerabilities found.


sublee/flask-autoindex
https://github.com/sublee/flask-autoindex
Entry file: flask-autoindex/flask_autoindex/__init__.py
Scanned: 2016-10-11 18:20:07.212612
No vulnerabilities found.


ericmoritz/flaskcma
https://github.com/ericmoritz/flaskcma
Entry file: flaskcma/flaskcma/app.py
Scanned: 2016-10-11 18:20:34.666352
No vulnerabilities found.


indexofire/flasky
https://github.com/indexofire/flasky
Entry file: flasky/flasky/flask/app.py
Scanned: 2016-10-11 18:20:37.571363
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ericmoritz/flask-auth
https://github.com/ericmoritz/flask-auth
Entry file: flask-auth/flaskext/auth/tests/workflow.py
Scanned: 2016-10-11 18:20:39.976691
No vulnerabilities found.


sublee/flask-silk
https://github.com/sublee/flask-silk
Entry file: flask-silk/test.py
Scanned: 2016-10-11 18:20:44.079990
No vulnerabilities found.


proudlygeek/proudlygeek-blog
https://github.com/proudlygeek/proudlygeek-blog
Entry file: proudlygeek-blog/flask/app.py
Scanned: 2016-10-11 18:20:46.200057
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

JunKikuchi/flask-gae
https://github.com/JunKikuchi/flask-gae
Entry file: flask-gae/app/main.py
Scanned: 2016-10-11 18:20:47.420114
No vulnerabilities found.


glenbot/flask-tweetfeed
https://github.com/glenbot/flask-tweetfeed
Entry file: flask-tweetfeed/tweetfeedapp.py
Scanned: 2016-10-11 18:20:48.703898
No vulnerabilities found.


fsouza/palestra-flask-2010-giran
https://github.com/fsouza/palestra-flask-2010-giran
Entry file: palestra-flask-2010-giran/projetos/projetos.py
Scanned: 2016-10-11 18:20:50.083954
No vulnerabilities found.


shiloa/flask-clean
https://github.com/shiloa/flask-clean
Entry file: flask-clean/app.py
Scanned: 2016-10-11 18:21:07.497903
No vulnerabilities found.


dag/flask-genshi
https://github.com/dag/flask-genshi
Entry file: flask-genshi/examples/flaskr/flaskr.py
Scanned: 2016-10-11 18:21:41.351971
No vulnerabilities found.


raliste/Flaskito
https://github.com/raliste/Flaskito
Entry file: Flaskito/flaskito/__init__.py
Scanned: 2016-10-11 18:21:43.098312
No vulnerabilities found.


mikewest/flask-pyplaceholder
https://github.com/mikewest/flask-pyplaceholder
Entry file: flask-pyplaceholder/generator.py
Scanned: 2016-10-11 18:21:49.312440
No vulnerabilities found.


whalesalad/arbesko-files
https://github.com/whalesalad/arbesko-files
Entry file: arbesko-files/files/__init__.py
Scanned: 2016-10-11 18:21:50.924319
No vulnerabilities found.


danjac/Flask-Script
https://github.com/danjac/Flask-Script
Entry file: Flask-Script/tests.py
Scanned: 2016-10-11 18:22:35.066156
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

danjac/Flask-WTF
https://github.com/danjac/Flask-WTF
Entry file: Flask-WTF/examples/recaptcha/app.py
Scanned: 2016-10-11 18:22:37.987421
No vulnerabilities found.


danjac/Flask-Mail
https://github.com/danjac/Flask-Mail
Entry file: Flask-Mail/tests.py
Scanned: 2016-10-11 18:22:42.941041
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cropd/crashkurs-flask
https://github.com/cropd/crashkurs-flask
Entry file: crashkurs-flask/flask/app.py
Scanned: 2016-10-11 18:22:47.423300
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hasgeek/github-hook
https://github.com/hasgeek/github-hook
Entry file: github-hook/github-hook.py
Scanned: 2016-10-11 18:22:48.702782
No vulnerabilities found.


pygloo/bewype-flask-controllers
https://github.com/pygloo/bewype-flask-controllers
Entry file: bewype-flask-controllers/bewype/flask/_app.py
Scanned: 2016-10-11 18:22:50.112654
No vulnerabilities found.


sontek-archive/redditor-stats
https://github.com/sontek-archive/redditor-stats
Entry file: redditor-stats/web.py
Scanned: 2016-10-11 18:22:51.349585
No vulnerabilities found.


pallets/flask
https://github.com/pallets/flask
Entry file: flask/setup.py
Scanned: 2016-10-11 20:18:02.901113
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

gigq/flasktodo
https://github.com/gigq/flasktodo
Entry file: flasktodo/application.py
Scanned: 2016-10-11 20:18:04.733731
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flosch/simpleapi
https://github.com/flosch/simpleapi
Entry file: simpleapi/example_project/server/flask1/app.py
Scanned: 2016-10-11 20:18:06.463184
No vulnerabilities found.


codebykat/robotkitten
https://github.com/codebykat/robotkitten
Entry file: None
Scanned: 2016-10-11 20:18:28.134558
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/codebykat/robotkitten.

mitsuhiko/flask-oauth
https://github.com/mitsuhiko/flask-oauth
Entry file: flask-oauth/example/facebook.py
Scanned: 2016-10-11 20:18:58.811346
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-openid
https://github.com/mitsuhiko/flask-openid
Entry file: flask-openid/flask_openid.py
Scanned: 2016-10-11 20:19:01.387226
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

artisonian/flaskengine
https://github.com/artisonian/flaskengine
Entry file: flaskengine/flaskengine/__init__.py
Scanned: 2016-10-11 20:19:06.731978
No vulnerabilities found.


toomoresuch/template-gae-with-flask
https://github.com/toomoresuch/template-gae-with-flask
Entry file: template-gae-with-flask/application.py
Scanned: 2016-10-11 20:19:08.554292
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: template-gae-with-flask/flask.py

aljoscha/shot-o-matic
https://github.com/aljoscha/shot-o-matic
Entry file: shot-o-matic/shotomatic.py
Scanned: 2016-10-11 20:19:59.910739
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-sqlalchemy
https://github.com/mitsuhiko/flask-sqlalchemy
Entry file: flask-sqlalchemy/flask_sqlalchemy/__init__.py
Scanned: 2016-10-11 20:20:02.376825
No vulnerabilities found.


mitsuhiko/flask-fungiform
https://github.com/mitsuhiko/flask-fungiform
Entry file: flask-fungiform/examples/example.py
Scanned: 2016-10-11 20:20:04.670993
No vulnerabilities found.


fsouza/talks
https://github.com/fsouza/talks
Entry file: talks/flask/app.py
Scanned: 2016-10-11 20:20:08.751428
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

unbracketed/flapp
https://github.com/unbracketed/flapp
Entry file: flapp/flapp/project_template/application.py
Scanned: 2016-10-11 20:20:10.514371
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dcolish/flask-markdown
https://github.com/dcolish/flask-markdown
Entry file: flask-markdown/tests/test_markdown.py
Scanned: 2016-10-11 20:20:58.792617
No vulnerabilities found.


blossom/flask-gae-skeleton
https://github.com/blossom/flask-gae-skeleton
Entry file: flask-gae-skeleton/gae/main.py
Scanned: 2016-10-11 20:21:02.665251
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kijun/flask-methodhack
https://github.com/kijun/flask-methodhack
Entry file: flask-methodhack/flaskext/methodhack.py
Scanned: 2016-10-11 20:21:04.984108
No vulnerabilities found.


viniciusfs/pasted-flask
https://github.com/viniciusfs/pasted-flask
Entry file: pasted-flask/pasted.py
Scanned: 2016-10-11 20:21:06.288957
Vulnerability 1:
File: pasted-flask/pasted.py
 > User input at line 219, trigger word "form[": 
	hexdigest = calc_md5(request.form['code'])
Reassigned in: 
	File: pasted-flask/pasted.py
	 > Line 221: paste = query_db('select * from pasted where md5 = ?', [hexdigest],one=True)
	File: pasted-flask/pasted.py
	 > Line 225: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 231: paste_id = cur.lastrowid
	File: pasted-flask/pasted.py
	 > Line 232: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 234: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 203: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 207: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 209: ret_MAYBE_FUNCTION_NAME = render_template('form.html',original=paste)
	File: pasted-flask/pasted.py
	 > Line 213: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 217: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
File: pasted-flask/pasted.py
 > reaches line 229, trigger word "execute(": 
	cur = g.db.execute('insert into pasted (code, md5, viewed_at, parent) values (?, ?, ?, ?)', [request.form['code'], hexdigest, viewed_at, request.form['parent']])



Cornu/Brain
https://github.com/Cornu/Brain
Entry file: Brain/brain/__init__.py
Scanned: 2016-10-11 20:21:10.958518
Vulnerability 1:
File: Brain/brain/controllers/text.py
 > User input at line 43, trigger word "get(": 
	key = request.form.get('search')
File: Brain/brain/controllers/text.py
 > reaches line 44, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('/' + key)



jbochi/scrum-you
https://github.com/jbochi/scrum-you
Entry file: scrum-you/application.py
Scanned: 2016-10-11 20:21:31.831404
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

miracle2k/flask-assets
https://github.com/miracle2k/flask-assets
Entry file: flask-assets/tests/test_config.py
Scanned: 2016-10-11 20:22:03.188112
No vulnerabilities found.


jgumbley/flask-payment
https://github.com/jgumbley/flask-payment
Entry file: flask-payment/tests.py
Scanned: 2016-10-11 20:22:04.658253
No vulnerabilities found.


eugenkiss/Simblin
https://github.com/eugenkiss/Simblin
Entry file: Simblin/simblin/__init__.py
Scanned: 2016-10-11 20:22:06.362786
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jugyo/flask-gae-template
https://github.com/jugyo/flask-gae-template
Entry file: flask-gae-template/app.py
Scanned: 2016-10-11 20:22:08.117388
No vulnerabilities found.


swanson/flask-embedly
https://github.com/swanson/flask-embedly
Entry file: flask-embedly/example/app.py
Scanned: 2016-10-11 20:22:09.381476
No vulnerabilities found.


LightStyle/Python-Board
https://github.com/LightStyle/Python-Board
Entry file: Python-Board/src/index.py
Scanned: 2016-10-11 20:22:10.656376
No vulnerabilities found.


miku/flask-gae-stub
https://github.com/miku/flask-gae-stub
Entry file: flask-gae-stub/flask/app.py
Scanned: 2016-10-11 20:22:13.020246
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

derwiki/wordisms_flask
https://github.com/derwiki/wordisms_flask
Entry file: wordisms_flask/www/main.py
Scanned: 2016-10-11 20:22:31.391063
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flebel/cisco79xx_phone_directory
https://github.com/flebel/cisco79xx_phone_directory
Entry file: cisco79xx_phone_directory/cisco79xx_phone_directory.py
Scanned: 2016-10-11 20:22:59.763295
No vulnerabilities found.


jkossen/imposter
https://github.com/jkossen/imposter
Entry file: None
Scanned: 2016-10-11 20:23:04.057223
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/jkossen/imposter.

sublee/subleekr
https://github.com/sublee/subleekr
Entry file: subleekr/subleekr/app.py
Scanned: 2016-10-11 20:23:06.645265
No vulnerabilities found.


akhodakivskiy/flask
https://github.com/akhodakivskiy/flask
Entry file: flask/skeleton/skeleton/__init__.py
Scanned: 2016-10-11 20:23:08.943721
No vulnerabilities found.


thadeusb/flask-cache
https://github.com/thadeusb/flask-cache
Entry file: flask-cache/examples/hello.py
Scanned: 2016-10-11 20:23:11.425157
No vulnerabilities found.


kamalgill/flask-appengine-template
https://github.com/kamalgill/flask-appengine-template
Entry file: flask-appengine-template/src/lib/flask/sessions.py
Scanned: 2016-10-11 20:23:14.777997
No vulnerabilities found.


sublee/flask-autoindex
https://github.com/sublee/flask-autoindex
Entry file: flask-autoindex/flask_autoindex/__init__.py
Scanned: 2016-10-11 20:23:32.562510
No vulnerabilities found.


ericmoritz/flaskcma
https://github.com/ericmoritz/flaskcma
Entry file: flaskcma/flaskcma/app.py
Scanned: 2016-10-11 20:23:59.907993
No vulnerabilities found.


indexofire/flasky
https://github.com/indexofire/flasky
Entry file: flasky/flasky/flask/app.py
Scanned: 2016-10-11 20:24:03.771246
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ericmoritz/flask-auth
https://github.com/ericmoritz/flask-auth
Entry file: flask-auth/flaskext/auth/tests/workflow.py
Scanned: 2016-10-11 20:24:06.197794
No vulnerabilities found.


sublee/flask-silk
https://github.com/sublee/flask-silk
Entry file: flask-silk/test.py
Scanned: 2016-10-11 20:24:09.673244
No vulnerabilities found.


proudlygeek/proudlygeek-blog
https://github.com/proudlygeek/proudlygeek-blog
Entry file: proudlygeek-blog/flask/app.py
Scanned: 2016-10-11 20:24:11.860935
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

JunKikuchi/flask-gae
https://github.com/JunKikuchi/flask-gae
Entry file: flask-gae/app/main.py
Scanned: 2016-10-11 20:24:13.103872
No vulnerabilities found.


glenbot/flask-tweetfeed
https://github.com/glenbot/flask-tweetfeed
Entry file: flask-tweetfeed/tweetfeedapp.py
Scanned: 2016-10-11 20:24:14.388275
No vulnerabilities found.


fsouza/palestra-flask-2010-giran
https://github.com/fsouza/palestra-flask-2010-giran
Entry file: palestra-flask-2010-giran/projetos/projetos.py
Scanned: 2016-10-11 20:24:16.742093
No vulnerabilities found.


shiloa/flask-clean
https://github.com/shiloa/flask-clean
Entry file: flask-clean/app.py
Scanned: 2016-10-11 20:24:32.193765
No vulnerabilities found.


dag/flask-genshi
https://github.com/dag/flask-genshi
Entry file: flask-genshi/examples/flaskr/flaskr.py
Scanned: 2016-10-11 20:25:07.064759
No vulnerabilities found.


raliste/Flaskito
https://github.com/raliste/Flaskito
Entry file: Flaskito/flaskito/__init__.py
Scanned: 2016-10-11 20:25:09.813807
No vulnerabilities found.


mikewest/flask-pyplaceholder
https://github.com/mikewest/flask-pyplaceholder
Entry file: flask-pyplaceholder/generator.py
Scanned: 2016-10-11 20:25:15.112722
No vulnerabilities found.


whalesalad/arbesko-files
https://github.com/whalesalad/arbesko-files
Entry file: arbesko-files/files/__init__.py
Scanned: 2016-10-11 20:25:17.793755
No vulnerabilities found.


danjac/Flask-Script
https://github.com/danjac/Flask-Script
Entry file: Flask-Script/tests.py
Scanned: 2016-10-11 20:26:00.804157
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

danjac/Flask-WTF
https://github.com/danjac/Flask-WTF
Entry file: Flask-WTF/examples/recaptcha/app.py
Scanned: 2016-10-11 20:26:04.598207
No vulnerabilities found.


danjac/Flask-Mail
https://github.com/danjac/Flask-Mail
Entry file: Flask-Mail/tests.py
Scanned: 2016-10-11 20:26:10.503276
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cropd/crashkurs-flask
https://github.com/cropd/crashkurs-flask
Entry file: crashkurs-flask/flask/app.py
Scanned: 2016-10-11 20:26:12.854565
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hasgeek/github-hook
https://github.com/hasgeek/github-hook
Entry file: github-hook/github-hook.py
Scanned: 2016-10-11 20:26:14.077631
No vulnerabilities found.


pygloo/bewype-flask-controllers
https://github.com/pygloo/bewype-flask-controllers
Entry file: bewype-flask-controllers/bewype/flask/_app.py
Scanned: 2016-10-11 20:26:15.411397
No vulnerabilities found.


sontek-archive/redditor-stats
https://github.com/sontek-archive/redditor-stats
Entry file: redditor-stats/web.py
Scanned: 2016-10-11 20:26:17.688867
No vulnerabilities found.


Frozen-Flask/Frozen-Flask
https://github.com/Frozen-Flask/Frozen-Flask
Entry file: Frozen-Flask/flask_frozen/__init__.py
Scanned: 2016-10-11 20:27:00.983942
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

cobrateam/flask-mongoalchemy
https://github.com/cobrateam/flask-mongoalchemy
Entry file: flask-mongoalchemy/flask_mongoalchemy/__init__.py
Scanned: 2016-10-11 20:27:04.753702
No vulnerabilities found.


Flask-FlatPages/Flask-FlatPages
https://github.com/Flask-FlatPages/Flask-FlatPages
Entry file: Flask-FlatPages/tests/test_flask_flatpages.py
Scanned: 2016-10-11 20:27:07.331298
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

fsouza/flask-rest-example
https://github.com/fsouza/flask-rest-example
Entry file: flask-rest-example/library.py
Scanned: 2016-10-11 20:27:10.570125
Vulnerability 1:
File: flask-rest-example/library.py
 > User input at line 63, trigger word "form[": 
	name = request.form['name']
Reassigned in: 
	File: flask-rest-example/library.py
	 > Line 64: book = Book(id=2, name=name)
File: flask-rest-example/library.py
 > reaches line 65, trigger word "flash(": 
	flash('Book %s sucessful saved!' % book.name)



pilt/flask-versioned
https://github.com/pilt/flask-versioned
Entry file: flask-versioned/test_versioned.py
Scanned: 2016-10-11 20:27:11.905794
No vulnerabilities found.


tokibito/flask-hgwebcommit
https://github.com/tokibito/flask-hgwebcommit
Entry file: flask-hgwebcommit/hgwebcommit/__init__.py
Scanned: 2016-10-11 20:27:16.453420
Vulnerability 1:
File: flask-hgwebcommit/hgwebcommit/views.py
 > User input at line 97, trigger word ".data": 
	message = operation_repo(repo, form.data['operation'], form.data['files'], form.data['commit_message'])
File: flask-hgwebcommit/hgwebcommit/views.py
 > reaches line 98, trigger word "flash(": 
	flash(message)



Nassty/flask-gae
https://github.com/Nassty/flask-gae
Entry file: flask-gae/lib/flask/app.py
Scanned: 2016-10-11 20:27:18.261312
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sgk/BulkDM
https://github.com/sgk/BulkDM
Entry file: BulkDM/application.py
Scanned: 2016-10-11 20:27:34.357683
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sontek-archive/redditor-stats
https://github.com/sontek-archive/redditor-stats
Entry file: redditor-stats/web.py
Scanned: 2016-10-11 20:28:05.200904
No vulnerabilities found.


zzzsochi/Flask-Gravatar
https://github.com/zzzsochi/Flask-Gravatar
Entry file: Flask-Gravatar/tests/test_core.py
Scanned: 2016-10-11 20:28:11.286584
No vulnerabilities found.


dag/flask-zodb
https://github.com/dag/flask-zodb
Entry file: flask-zodb/flask_zodb.py
Scanned: 2016-10-11 20:28:13.024724
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

zen4ever/route53manager
https://github.com/zen4ever/route53manager
Entry file: route53manager/route53/__init__.py
Scanned: 2016-10-11 20:28:14.506566
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-kitchensink
https://github.com/mitsuhiko/flask-kitchensink
Entry file: flask-kitchensink/example-code/hello.py
Scanned: 2016-10-11 20:28:15.827475
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

eyeseast/flask-docviewer
https://github.com/eyeseast/flask-docviewer
Entry file: flask-docviewer/docviewer/app.py
Scanned: 2016-10-11 20:28:17.076736
No vulnerabilities found.


dag/flask-attest
https://github.com/dag/flask-attest
Entry file: flask-attest/tests.py
Scanned: 2016-10-11 20:28:18.609829
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

ekalinin/flask-noextref
https://github.com/ekalinin/flask-noextref
Entry file: flask-noextref/test_noextref.py
Scanned: 2016-10-11 20:28:34.557573
No vulnerabilities found.


teohm/flitter
https://github.com/teohm/flitter
Entry file: flitter/flitter/__init__.py
Scanned: 2016-10-11 20:29:08.108805
Vulnerability 1:
File: flitter/flitter/controllers/user.py
 > User input at line 19, trigger word "form[": 
	username = request.form['username']
Reassigned in: 
	File: flitter/flitter/controllers/user.py
	 > Line 24: session['user'] = username
	File: flitter/flitter/controllers/user.py
	 > Line 26: ret_MAYBE_FUNCTION_NAME = redirect(url_for('entry.entries',username=username))
	File: flitter/flitter/controllers/user.py
	 > Line 30: ret_MAYBE_FUNCTION_NAME = render_template('signup.html',error=error)
	File: flitter/flitter/controllers/user.py
	 > Line 15: ret_MAYBE_FUNCTION_NAME = redirect_to_user_page()
File: flitter/flitter/controllers/user.py
 > reaches line 25, trigger word "flash(": 
	flash('Welcome, {0}.'.format(username))



aaront/calcmymarks2
https://github.com/aaront/calcmymarks2
Entry file: calcmymarks2/main.py
Scanned: 2016-10-11 20:29:12.154045
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-feedback
https://github.com/mitsuhiko/flask-feedback
Entry file: flask-feedback/feedback.py
Scanned: 2016-10-11 20:29:15.244469
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

wilsaj/flask-admin-old
https://github.com/wilsaj/flask-admin-old
Entry file: flask-admin-old/test_admin.py
Scanned: 2016-10-11 20:29:23.129953
No vulnerabilities found.


leandrosilva/flaskito
https://github.com/leandrosilva/flaskito
Entry file: flaskito/src/flaskito.py
Scanned: 2016-10-11 20:29:26.674720
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/Flask-API-Server
https://github.com/marchon/Flask-API-Server
Entry file: Flask-API-Server/apiserver/tests/app.py
Scanned: 2016-10-11 20:29:28.074325
No vulnerabilities found.


kapilreddy/Shabda-Sangraha
https://github.com/kapilreddy/Shabda-Sangraha
Entry file: Shabda-Sangraha/dict.py
Scanned: 2016-10-11 20:30:06.776461
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tooxie/flask-syrinx
https://github.com/tooxie/flask-syrinx
Entry file: flask-syrinx/syrinx/__init__.py
Scanned: 2016-10-11 20:30:08.433792
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joshourisman/flask-shortly
https://github.com/joshourisman/flask-shortly
Entry file: flask-shortly/shortly/__init__.py
Scanned: 2016-10-11 20:30:12.254774
No vulnerabilities found.


jamiltron/fitgen
https://github.com/jamiltron/fitgen
Entry file: fitgen/fitgen.py
Scanned: 2016-10-11 20:30:17.552958
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tomviner/Flask-Name-that-actor-or-movie
https://github.com/tomviner/Flask-Name-that-actor-or-movie
Entry file: Flask-Name-that-actor-or-movie/namer.py
Scanned: 2016-10-11 20:30:28.240315
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/flylons
https://github.com/marchon/flylons
Entry file: flylons/application/__init__.py
Scanned: 2016-10-11 20:30:34.784109
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/checkinmapper
https://github.com/marchon/checkinmapper
Entry file: checkinmapper/checkinmapper.py
Scanned: 2016-10-11 20:31:03.158769
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

comfuture/simplesite
https://github.com/comfuture/simplesite
Entry file: simplesite/simplesite/core.py
Scanned: 2016-10-11 20:31:08.583387
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

zachwill/flask-engine
https://github.com/zachwill/flask-engine
Entry file: flask-engine/libs/flask/sessions.py
Scanned: 2016-10-11 20:31:15.171914
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

spantaleev/flask-sijax
https://github.com/spantaleev/flask-sijax
Entry file: flask-sijax/examples/comet.py
Scanned: 2016-10-11 20:31:16.640469
No vulnerabilities found.


utahta/Flask-MVC-Pattern
https://github.com/utahta/Flask-MVC-Pattern
Entry file: Flask-MVC-Pattern/main.py
Scanned: 2016-10-11 20:31:18.025292
No vulnerabilities found.


jzempel/flask-exceptional
https://github.com/jzempel/flask-exceptional
Entry file: flask-exceptional/flask_exceptional.py
Scanned: 2016-10-11 20:31:25.571791
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

qsnake/flask
https://github.com/qsnake/flask
Entry file: flask/setup.py
Scanned: 2016-10-11 20:31:35.805946
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joeyespo/flask-scaffold
https://github.com/joeyespo/flask-scaffold
Entry file: flask-scaffold/[appname].py
Scanned: 2016-10-11 20:32:03.340606
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

iwebhosting/collectd-flask
https://github.com/iwebhosting/collectd-flask
Entry file: collectd-flask/collectdflask.py
Scanned: 2016-10-11 20:32:08.773220
No vulnerabilities found.


yxm0513/flask-ims
https://github.com/yxm0513/flask-ims
Entry file: flask-ims/flask/sessions.py
Scanned: 2016-10-11 20:32:11.645504
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fay/flask-skeleton
https://github.com/fay/flask-skeleton
Entry file: flask-skeleton/app/__init__.py
Scanned: 2016-10-11 20:32:14.639639
No vulnerabilities found.


joshourisman/flask-beans
https://github.com/joshourisman/flask-beans
Entry file: flask-beans/beans.py
Scanned: 2016-10-11 20:32:16.918063
No vulnerabilities found.


jjinux/pyteladventure
https://github.com/jjinux/pyteladventure
Entry file: pyteladventure/pyteladventure/__init__.py
Scanned: 2016-10-11 20:32:18.436538
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.List'>)

mchambliss/flask
https://github.com/mchambliss/flask
Entry file: flask/webapp/webapp/__init__.py
Scanned: 2016-10-11 20:32:35.963912
No vulnerabilities found.


robi42/backbone-flask
https://github.com/robi42/backbone-flask
Entry file: backbone-flask/app.py
Scanned: 2016-10-11 20:33:16.298780
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

suzanshakya/flask-clevercss
https://github.com/suzanshakya/flask-clevercss
Entry file: flask-clevercss/example/runserver.py
Scanned: 2016-10-11 20:33:17.767123
No vulnerabilities found.


joshfinnie/Flask-shrtn
https://github.com/joshfinnie/Flask-shrtn
Entry file: Flask-shrtn/Flask-shrtn.py
Scanned: 2016-10-11 20:33:19.211552
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tomatohater/goonhilly
https://github.com/tomatohater/goonhilly
Entry file: goonhilly/goonhilly.py
Scanned: 2016-10-11 20:33:29.962796
No vulnerabilities found.


jmoiron/jmoiron.net
https://github.com/jmoiron/jmoiron.net
Entry file: None
Scanned: 2016-10-11 20:33:36.934717
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/jmoiron/jmoiron.net.

pallets/flask
https://github.com/pallets/flask
Entry file: flask/setup.py
Scanned: 2016-10-11 20:35:45.968871
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

gigq/flasktodo
https://github.com/gigq/flasktodo
Entry file: flasktodo/application.py
Scanned: 2016-10-11 20:35:47.816039
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flosch/simpleapi
https://github.com/flosch/simpleapi
Entry file: simpleapi/example_project/server/flask1/app.py
Scanned: 2016-10-11 20:35:49.520772
No vulnerabilities found.


codebykat/robotkitten
https://github.com/codebykat/robotkitten
Entry file: None
Scanned: 2016-10-11 20:36:12.624403
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/codebykat/robotkitten.

mitsuhiko/flask-oauth
https://github.com/mitsuhiko/flask-oauth
Entry file: flask-oauth/example/facebook.py
Scanned: 2016-10-11 20:36:41.917490
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-openid
https://github.com/mitsuhiko/flask-openid
Entry file: flask-openid/flask_openid.py
Scanned: 2016-10-11 20:36:44.277824
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

artisonian/flaskengine
https://github.com/artisonian/flaskengine
Entry file: flaskengine/flaskengine/__init__.py
Scanned: 2016-10-11 20:36:49.538608
No vulnerabilities found.


toomoresuch/template-gae-with-flask
https://github.com/toomoresuch/template-gae-with-flask
Entry file: template-gae-with-flask/application.py
Scanned: 2016-10-11 20:36:51.268231
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: template-gae-with-flask/flask.py

aljoscha/shot-o-matic
https://github.com/aljoscha/shot-o-matic
Entry file: shot-o-matic/shotomatic.py
Scanned: 2016-10-11 20:37:43.676399
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-sqlalchemy
https://github.com/mitsuhiko/flask-sqlalchemy
Entry file: flask-sqlalchemy/flask_sqlalchemy/__init__.py
Scanned: 2016-10-11 20:37:46.094982
No vulnerabilities found.


mitsuhiko/flask-fungiform
https://github.com/mitsuhiko/flask-fungiform
Entry file: flask-fungiform/examples/example.py
Scanned: 2016-10-11 20:37:48.392978
No vulnerabilities found.


fsouza/talks
https://github.com/fsouza/talks
Entry file: talks/flask/app.py
Scanned: 2016-10-11 20:37:51.477595
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

unbracketed/flapp
https://github.com/unbracketed/flapp
Entry file: flapp/flapp/project_template/application.py
Scanned: 2016-10-11 20:37:53.332393
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dcolish/flask-markdown
https://github.com/dcolish/flask-markdown
Entry file: flask-markdown/tests/test_markdown.py
Scanned: 2016-10-11 20:38:42.882299
No vulnerabilities found.


blossom/flask-gae-skeleton
https://github.com/blossom/flask-gae-skeleton
Entry file: flask-gae-skeleton/gae/main.py
Scanned: 2016-10-11 20:38:45.768680
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kijun/flask-methodhack
https://github.com/kijun/flask-methodhack
Entry file: flask-methodhack/flaskext/methodhack.py
Scanned: 2016-10-11 20:38:48.090057
No vulnerabilities found.


viniciusfs/pasted-flask
https://github.com/viniciusfs/pasted-flask
Entry file: pasted-flask/pasted.py
Scanned: 2016-10-11 20:38:49.376864
Vulnerability 1:
File: pasted-flask/pasted.py
 > User input at line 219, trigger word "form[": 
	hexdigest = calc_md5(request.form['code'])
Reassigned in: 
	File: pasted-flask/pasted.py
	 > Line 221: paste = query_db('select * from pasted where md5 = ?', [hexdigest],one=True)
	File: pasted-flask/pasted.py
	 > Line 225: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 231: paste_id = cur.lastrowid
	File: pasted-flask/pasted.py
	 > Line 232: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 234: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 203: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 207: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 209: ret_MAYBE_FUNCTION_NAME = render_template('form.html',original=paste)
	File: pasted-flask/pasted.py
	 > Line 213: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 217: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
File: pasted-flask/pasted.py
 > reaches line 229, trigger word "execute(": 
	cur = g.db.execute('insert into pasted (code, md5, viewed_at, parent) values (?, ?, ?, ?)', [request.form['code'], hexdigest, viewed_at, request.form['parent']])



Cornu/Brain
https://github.com/Cornu/Brain
Entry file: Brain/brain/__init__.py
Scanned: 2016-10-11 20:38:54.057496
Vulnerability 1:
File: Brain/brain/controllers/text.py
 > User input at line 43, trigger word "get(": 
	key = request.form.get('search')
File: Brain/brain/controllers/text.py
 > reaches line 44, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('/' + key)



jbochi/scrum-you
https://github.com/jbochi/scrum-you
Entry file: scrum-you/application.py
Scanned: 2016-10-11 20:39:15.931396
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

miracle2k/flask-assets
https://github.com/miracle2k/flask-assets
Entry file: flask-assets/tests/test_config.py
Scanned: 2016-10-11 20:39:46.429910
No vulnerabilities found.


jgumbley/flask-payment
https://github.com/jgumbley/flask-payment
Entry file: flask-payment/tests.py
Scanned: 2016-10-11 20:39:47.898204
No vulnerabilities found.


eugenkiss/Simblin
https://github.com/eugenkiss/Simblin
Entry file: Simblin/simblin/__init__.py
Scanned: 2016-10-11 20:39:49.565852
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jugyo/flask-gae-template
https://github.com/jugyo/flask-gae-template
Entry file: flask-gae-template/app.py
Scanned: 2016-10-11 20:39:51.370459
No vulnerabilities found.


swanson/flask-embedly
https://github.com/swanson/flask-embedly
Entry file: flask-embedly/example/app.py
Scanned: 2016-10-11 20:39:52.702048
No vulnerabilities found.


LightStyle/Python-Board
https://github.com/LightStyle/Python-Board
Entry file: Python-Board/src/index.py
Scanned: 2016-10-11 20:39:54.012555
No vulnerabilities found.


miku/flask-gae-stub
https://github.com/miku/flask-gae-stub
Entry file: flask-gae-stub/flask/app.py
Scanned: 2016-10-11 20:39:55.827702
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

derwiki/wordisms_flask
https://github.com/derwiki/wordisms_flask
Entry file: wordisms_flask/www/main.py
Scanned: 2016-10-11 20:40:16.217215
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

pallets/flask
https://github.com/pallets/flask
Entry file: flask/setup.py
Scanned: 2016-10-11 20:42:36.743612
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

gigq/flasktodo
https://github.com/gigq/flasktodo
Entry file: flasktodo/application.py
Scanned: 2016-10-11 20:42:38.552705
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flosch/simpleapi
https://github.com/flosch/simpleapi
Entry file: simpleapi/example_project/server/flask1/app.py
Scanned: 2016-10-11 20:42:40.260848
No vulnerabilities found.


codebykat/robotkitten
https://github.com/codebykat/robotkitten
Entry file: None
Scanned: 2016-10-11 20:43:06.046684
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/codebykat/robotkitten.

mitsuhiko/flask-oauth
https://github.com/mitsuhiko/flask-oauth
Entry file: flask-oauth/example/facebook.py
Scanned: 2016-10-11 20:43:32.250289
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-openid
https://github.com/mitsuhiko/flask-openid
Entry file: flask-openid/flask_openid.py
Scanned: 2016-10-11 20:43:35.133269
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

artisonian/flaskengine
https://github.com/artisonian/flaskengine
Entry file: flaskengine/flaskengine/__init__.py
Scanned: 2016-10-11 20:43:40.425365
No vulnerabilities found.


toomoresuch/template-gae-with-flask
https://github.com/toomoresuch/template-gae-with-flask
Entry file: template-gae-with-flask/application.py
Scanned: 2016-10-11 20:43:42.261659
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: template-gae-with-flask/flask.py

aljoscha/shot-o-matic
https://github.com/aljoscha/shot-o-matic
Entry file: shot-o-matic/shotomatic.py
Scanned: 2016-10-11 20:44:34.525610
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-sqlalchemy
https://github.com/mitsuhiko/flask-sqlalchemy
Entry file: flask-sqlalchemy/flask_sqlalchemy/__init__.py
Scanned: 2016-10-11 20:44:36.903381
No vulnerabilities found.


mitsuhiko/flask-fungiform
https://github.com/mitsuhiko/flask-fungiform
Entry file: flask-fungiform/examples/example.py
Scanned: 2016-10-11 20:44:39.291022
No vulnerabilities found.


fsouza/talks
https://github.com/fsouza/talks
Entry file: talks/flask/app.py
Scanned: 2016-10-11 20:44:42.340859
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

unbracketed/flapp
https://github.com/unbracketed/flapp
Entry file: flapp/flapp/project_template/application.py
Scanned: 2016-10-11 20:44:44.200542
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dcolish/flask-markdown
https://github.com/dcolish/flask-markdown
Entry file: flask-markdown/tests/test_markdown.py
Scanned: 2016-10-11 20:45:32.504830
No vulnerabilities found.


blossom/flask-gae-skeleton
https://github.com/blossom/flask-gae-skeleton
Entry file: flask-gae-skeleton/gae/main.py
Scanned: 2016-10-11 20:45:37.378271
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kijun/flask-methodhack
https://github.com/kijun/flask-methodhack
Entry file: flask-methodhack/flaskext/methodhack.py
Scanned: 2016-10-11 20:45:39.645429
No vulnerabilities found.


viniciusfs/pasted-flask
https://github.com/viniciusfs/pasted-flask
Entry file: pasted-flask/pasted.py
Scanned: 2016-10-11 20:45:41.034402
Vulnerability 1:
File: pasted-flask/pasted.py
 > User input at line 219, trigger word "form[": 
	hexdigest = calc_md5(request.form['code'])
Reassigned in: 
	File: pasted-flask/pasted.py
	 > Line 221: paste = query_db('select * from pasted where md5 = ?', [hexdigest],one=True)
	File: pasted-flask/pasted.py
	 > Line 225: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 231: paste_id = cur.lastrowid
	File: pasted-flask/pasted.py
	 > Line 232: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 234: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 203: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 207: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 209: ret_MAYBE_FUNCTION_NAME = render_template('form.html',original=paste)
	File: pasted-flask/pasted.py
	 > Line 213: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 217: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
File: pasted-flask/pasted.py
 > reaches line 229, trigger word "execute(": 
	cur = g.db.execute('insert into pasted (code, md5, viewed_at, parent) values (?, ?, ?, ?)', [request.form['code'], hexdigest, viewed_at, request.form['parent']])



Cornu/Brain
https://github.com/Cornu/Brain
Entry file: Brain/brain/__init__.py
Scanned: 2016-10-11 20:45:44.770003
Vulnerability 1:
File: Brain/brain/controllers/text.py
 > User input at line 43, trigger word "get(": 
	key = request.form.get('search')
File: Brain/brain/controllers/text.py
 > reaches line 44, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('/' + key)



jbochi/scrum-you
https://github.com/jbochi/scrum-you
Entry file: scrum-you/application.py
Scanned: 2016-10-11 20:46:09.650635
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

miracle2k/flask-assets
https://github.com/miracle2k/flask-assets
Entry file: flask-assets/tests/test_config.py
Scanned: 2016-10-11 20:46:38.025988
No vulnerabilities found.


jgumbley/flask-payment
https://github.com/jgumbley/flask-payment
Entry file: flask-payment/tests.py
Scanned: 2016-10-11 20:46:39.600106
No vulnerabilities found.


eugenkiss/Simblin
https://github.com/eugenkiss/Simblin
Entry file: Simblin/simblin/__init__.py
Scanned: 2016-10-11 20:46:41.327422
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jugyo/flask-gae-template
https://github.com/jugyo/flask-gae-template
Entry file: flask-gae-template/app.py
Scanned: 2016-10-11 20:46:43.161709
No vulnerabilities found.


swanson/flask-embedly
https://github.com/swanson/flask-embedly
Entry file: flask-embedly/example/app.py
Scanned: 2016-10-11 20:46:44.513177
No vulnerabilities found.


LightStyle/Python-Board
https://github.com/LightStyle/Python-Board
Entry file: Python-Board/src/index.py
Scanned: 2016-10-11 20:46:45.797387
No vulnerabilities found.


miku/flask-gae-stub
https://github.com/miku/flask-gae-stub
Entry file: flask-gae-stub/flask/app.py
Scanned: 2016-10-11 20:46:47.654996
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

derwiki/wordisms_flask
https://github.com/derwiki/wordisms_flask
Entry file: wordisms_flask/www/main.py
Scanned: 2016-10-11 20:47:10.000649
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flebel/cisco79xx_phone_directory
https://github.com/flebel/cisco79xx_phone_directory
Entry file: cisco79xx_phone_directory/cisco79xx_phone_directory.py
Scanned: 2016-10-11 20:47:33.570445
No vulnerabilities found.


jkossen/imposter
https://github.com/jkossen/imposter
Entry file: None
Scanned: 2016-10-11 20:47:38.833148
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/jkossen/imposter.

sublee/subleekr
https://github.com/sublee/subleekr
Entry file: subleekr/subleekr/app.py
Scanned: 2016-10-11 20:47:41.220398
No vulnerabilities found.


akhodakivskiy/flask
https://github.com/akhodakivskiy/flask
Entry file: flask/setup.py
Scanned: 2016-10-11 20:47:43.329781
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

thadeusb/flask-cache
https://github.com/thadeusb/flask-cache
Entry file: flask-cache/examples/hello.py
Scanned: 2016-10-11 20:47:45.213880
No vulnerabilities found.


kamalgill/flask-appengine-template
https://github.com/kamalgill/flask-appengine-template
Entry file: flask-appengine-template/src/lib/flask/sessions.py
Scanned: 2016-10-11 20:47:48.655874
No vulnerabilities found.


sublee/flask-autoindex
https://github.com/sublee/flask-autoindex
Entry file: flask-autoindex/flask_autoindex/__init__.py
Scanned: 2016-10-11 20:48:11.280976
No vulnerabilities found.


ericmoritz/flaskcma
https://github.com/ericmoritz/flaskcma
Entry file: flaskcma/flaskcma/app.py
Scanned: 2016-10-11 20:48:34.261254
No vulnerabilities found.


indexofire/flasky
https://github.com/indexofire/flasky
Entry file: flasky/flasky/flask/app.py
Scanned: 2016-10-11 20:48:39.138526
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ericmoritz/flask-auth
https://github.com/ericmoritz/flask-auth
Entry file: flask-auth/flaskext/auth/tests/workflow.py
Scanned: 2016-10-11 20:48:40.610743
No vulnerabilities found.


sublee/flask-silk
https://github.com/sublee/flask-silk
Entry file: flask-silk/test.py
Scanned: 2016-10-11 20:48:44.078267
No vulnerabilities found.


proudlygeek/proudlygeek-blog
https://github.com/proudlygeek/proudlygeek-blog
Entry file: proudlygeek-blog/flask/app.py
Scanned: 2016-10-11 20:48:46.279412
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

JunKikuchi/flask-gae
https://github.com/JunKikuchi/flask-gae
Entry file: flask-gae/app/main.py
Scanned: 2016-10-11 20:48:47.552567
No vulnerabilities found.


glenbot/flask-tweetfeed
https://github.com/glenbot/flask-tweetfeed
Entry file: flask-tweetfeed/tweetfeedapp.py
Scanned: 2016-10-11 20:48:48.854078
No vulnerabilities found.


fsouza/palestra-flask-2010-giran
https://github.com/fsouza/palestra-flask-2010-giran
Entry file: palestra-flask-2010-giran/projetos/projetos.py
Scanned: 2016-10-11 20:48:50.216954
No vulnerabilities found.


shiloa/flask-clean
https://github.com/shiloa/flask-clean
Entry file: flask-clean/app.py
Scanned: 2016-10-11 20:49:10.634653
No vulnerabilities found.


dag/flask-genshi
https://github.com/dag/flask-genshi
Entry file: flask-genshi/examples/flaskr/flaskr.py
Scanned: 2016-10-11 20:49:41.657426
No vulnerabilities found.


raliste/Flaskito
https://github.com/raliste/Flaskito
Entry file: Flaskito/flaskito/__init__.py
Scanned: 2016-10-11 20:49:43.520256
No vulnerabilities found.


mikewest/flask-pyplaceholder
https://github.com/mikewest/flask-pyplaceholder
Entry file: flask-pyplaceholder/generator.py
Scanned: 2016-10-11 20:49:49.936798
No vulnerabilities found.


whalesalad/arbesko-files
https://github.com/whalesalad/arbesko-files
Entry file: arbesko-files/files/__init__.py
Scanned: 2016-10-11 20:49:51.646827
No vulnerabilities found.


danjac/Flask-Script
https://github.com/danjac/Flask-Script
Entry file: Flask-Script/tests.py
Scanned: 2016-10-11 20:50:34.942610
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

danjac/Flask-WTF
https://github.com/danjac/Flask-WTF
Entry file: Flask-WTF/examples/recaptcha/app.py
Scanned: 2016-10-11 20:50:41.483224
No vulnerabilities found.


danjac/Flask-Mail
https://github.com/danjac/Flask-Mail
Entry file: Flask-Mail/tests.py
Scanned: 2016-10-11 20:50:43.492102
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cropd/crashkurs-flask
https://github.com/cropd/crashkurs-flask
Entry file: crashkurs-flask/flask/app.py
Scanned: 2016-10-11 20:50:46.907168
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hasgeek/github-hook
https://github.com/hasgeek/github-hook
Entry file: github-hook/github-hook.py
Scanned: 2016-10-11 20:50:49.198148
No vulnerabilities found.


pygloo/bewype-flask-controllers
https://github.com/pygloo/bewype-flask-controllers
Entry file: bewype-flask-controllers/bewype/flask/_app.py
Scanned: 2016-10-11 20:50:50.551784
No vulnerabilities found.


sontek-archive/redditor-stats
https://github.com/sontek-archive/redditor-stats
Entry file: redditor-stats/web.py
Scanned: 2016-10-11 20:50:51.946271
No vulnerabilities found.


Frozen-Flask/Frozen-Flask
https://github.com/Frozen-Flask/Frozen-Flask
Entry file: Frozen-Flask/flask_frozen/__init__.py
Scanned: 2016-10-11 20:51:35.848176
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

cobrateam/flask-mongoalchemy
https://github.com/cobrateam/flask-mongoalchemy
Entry file: flask-mongoalchemy/flask_mongoalchemy/__init__.py
Scanned: 2016-10-11 20:51:41.527399
No vulnerabilities found.


Flask-FlatPages/Flask-FlatPages
https://github.com/Flask-FlatPages/Flask-FlatPages
Entry file: Flask-FlatPages/tests/test_flask_flatpages.py
Scanned: 2016-10-11 20:51:43.164416
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

fsouza/flask-rest-example
https://github.com/fsouza/flask-rest-example
Entry file: flask-rest-example/library.py
Scanned: 2016-10-11 20:51:44.405603
Vulnerability 1:
File: flask-rest-example/library.py
 > User input at line 63, trigger word "form[": 
	name = request.form['name']
Reassigned in: 
	File: flask-rest-example/library.py
	 > Line 64: book = Book(id=2, name=name)
File: flask-rest-example/library.py
 > reaches line 65, trigger word "flash(": 
	flash('Book %s sucessful saved!' % book.name)



pilt/flask-versioned
https://github.com/pilt/flask-versioned
Entry file: flask-versioned/test_versioned.py
Scanned: 2016-10-11 20:51:45.831106
No vulnerabilities found.


tokibito/flask-hgwebcommit
https://github.com/tokibito/flask-hgwebcommit
Entry file: flask-hgwebcommit/hgwebcommit/__init__.py
Scanned: 2016-10-11 20:51:51.459423
Vulnerability 1:
File: flask-hgwebcommit/hgwebcommit/views.py
 > User input at line 97, trigger word ".data": 
	message = operation_repo(repo, form.data['operation'], form.data['files'], form.data['commit_message'])
File: flask-hgwebcommit/hgwebcommit/views.py
 > reaches line 98, trigger word "flash(": 
	flash(message)



Nassty/flask-gae
https://github.com/Nassty/flask-gae
Entry file: flask-gae/lib/flask/app.py
Scanned: 2016-10-11 20:51:53.291116
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sgk/BulkDM
https://github.com/sgk/BulkDM
Entry file: BulkDM/application.py
Scanned: 2016-10-11 20:52:12.227586
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sontek-archive/redditor-stats
https://github.com/sontek-archive/redditor-stats
Entry file: redditor-stats/web.py
Scanned: 2016-10-11 20:52:42.115718
No vulnerabilities found.


zzzsochi/Flask-Gravatar
https://github.com/zzzsochi/Flask-Gravatar
Entry file: Flask-Gravatar/tests/test_core.py
Scanned: 2016-10-11 20:52:45.255653
No vulnerabilities found.


dag/flask-zodb
https://github.com/dag/flask-zodb
Entry file: flask-zodb/flask_zodb.py
Scanned: 2016-10-11 20:52:46.958417
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

zen4ever/route53manager
https://github.com/zen4ever/route53manager
Entry file: route53manager/route53/__init__.py
Scanned: 2016-10-11 20:52:48.473707
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-kitchensink
https://github.com/mitsuhiko/flask-kitchensink
Entry file: flask-kitchensink/example-code/hello.py
Scanned: 2016-10-11 20:52:49.863513
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

eyeseast/flask-docviewer
https://github.com/eyeseast/flask-docviewer
Entry file: flask-docviewer/docviewer/app.py
Scanned: 2016-10-11 20:52:51.127515
No vulnerabilities found.


dag/flask-attest
https://github.com/dag/flask-attest
Entry file: flask-attest/tests.py
Scanned: 2016-10-11 20:52:53.661894
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

ekalinin/flask-noextref
https://github.com/ekalinin/flask-noextref
Entry file: flask-noextref/test_noextref.py
Scanned: 2016-10-11 20:53:12.131982
No vulnerabilities found.


teohm/flitter
https://github.com/teohm/flitter
Entry file: flitter/flitter/__init__.py
Scanned: 2016-10-11 20:53:43.743938
Vulnerability 1:
File: flitter/flitter/controllers/user.py
 > User input at line 19, trigger word "form[": 
	username = request.form['username']
Reassigned in: 
	File: flitter/flitter/controllers/user.py
	 > Line 24: session['user'] = username
	File: flitter/flitter/controllers/user.py
	 > Line 26: ret_MAYBE_FUNCTION_NAME = redirect(url_for('entry.entries',username=username))
	File: flitter/flitter/controllers/user.py
	 > Line 30: ret_MAYBE_FUNCTION_NAME = render_template('signup.html',error=error)
	File: flitter/flitter/controllers/user.py
	 > Line 15: ret_MAYBE_FUNCTION_NAME = redirect_to_user_page()
File: flitter/flitter/controllers/user.py
 > reaches line 25, trigger word "flash(": 
	flash('Welcome, {0}.'.format(username))



aaront/calcmymarks2
https://github.com/aaront/calcmymarks2
Entry file: calcmymarks2/main.py
Scanned: 2016-10-11 20:53:45.755115
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-feedback
https://github.com/mitsuhiko/flask-feedback
Entry file: flask-feedback/feedback.py
Scanned: 2016-10-11 20:53:48.841976
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

wilsaj/flask-admin-old
https://github.com/wilsaj/flask-admin-old
Entry file: flask-admin-old/test_admin.py
Scanned: 2016-10-11 20:53:56.830004
No vulnerabilities found.


leandrosilva/flaskito
https://github.com/leandrosilva/flaskito
Entry file: flaskito/src/flaskito.py
Scanned: 2016-10-11 20:54:00.399699
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/Flask-API-Server
https://github.com/marchon/Flask-API-Server
Entry file: Flask-API-Server/apiserver/tests/app.py
Scanned: 2016-10-11 20:54:01.769239
No vulnerabilities found.


kapilreddy/Shabda-Sangraha
https://github.com/kapilreddy/Shabda-Sangraha
Entry file: Shabda-Sangraha/dict.py
Scanned: 2016-10-11 20:54:43.029733
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tooxie/flask-syrinx
https://github.com/tooxie/flask-syrinx
Entry file: flask-syrinx/syrinx/__init__.py
Scanned: 2016-10-11 20:54:44.610366
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joshourisman/flask-shortly
https://github.com/joshourisman/flask-shortly
Entry file: flask-shortly/shortly/__init__.py
Scanned: 2016-10-11 20:54:46.511023
No vulnerabilities found.


jamiltron/fitgen
https://github.com/jamiltron/fitgen
Entry file: fitgen/fitgen.py
Scanned: 2016-10-11 20:54:50.924599
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tomviner/Flask-Name-that-actor-or-movie
https://github.com/tomviner/Flask-Name-that-actor-or-movie
Entry file: Flask-Name-that-actor-or-movie/namer.py
Scanned: 2016-10-11 20:55:01.705222
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/flylons
https://github.com/marchon/flylons
Entry file: flylons/application/__init__.py
Scanned: 2016-10-11 20:55:13.114927
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/checkinmapper
https://github.com/marchon/checkinmapper
Entry file: checkinmapper/checkinmapper.py
Scanned: 2016-10-11 20:55:38.726118
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

comfuture/simplesite
https://github.com/comfuture/simplesite
Entry file: simplesite/simplesite/core.py
Scanned: 2016-10-11 20:55:45.095413
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

zachwill/flask-engine
https://github.com/zachwill/flask-engine
Entry file: flask-engine/libs/flask/sessions.py
Scanned: 2016-10-11 20:55:49.588402
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

spantaleev/flask-sijax
https://github.com/spantaleev/flask-sijax
Entry file: flask-sijax/examples/comet.py
Scanned: 2016-10-11 20:55:51.028357
No vulnerabilities found.


utahta/Flask-MVC-Pattern
https://github.com/utahta/Flask-MVC-Pattern
Entry file: Flask-MVC-Pattern/main.py
Scanned: 2016-10-11 20:55:52.251325
No vulnerabilities found.


jzempel/flask-exceptional
https://github.com/jzempel/flask-exceptional
Entry file: flask-exceptional/flask_exceptional.py
Scanned: 2016-10-11 20:55:58.752232
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

qsnake/flask
https://github.com/qsnake/flask
Entry file: flask/setup.py
Scanned: 2016-10-11 20:56:13.333311
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

joeyespo/flask-scaffold
https://github.com/joeyespo/flask-scaffold
Entry file: flask-scaffold/[appname].py
Scanned: 2016-10-11 20:56:37.838407
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

iwebhosting/collectd-flask
https://github.com/iwebhosting/collectd-flask
Entry file: collectd-flask/collectdflask.py
Scanned: 2016-10-11 20:56:45.283478
No vulnerabilities found.


yxm0513/flask-ims
https://github.com/yxm0513/flask-ims
Entry file: flask-ims/flask/sessions.py
Scanned: 2016-10-11 20:56:48.246922
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fay/flask-skeleton
https://github.com/fay/flask-skeleton
Entry file: flask-skeleton/app/__init__.py
Scanned: 2016-10-11 20:56:50.268491
No vulnerabilities found.


joshourisman/flask-beans
https://github.com/joshourisman/flask-beans
Entry file: flask-beans/beans.py
Scanned: 2016-10-11 20:56:51.585840
No vulnerabilities found.


jjinux/pyteladventure
https://github.com/jjinux/pyteladventure
Entry file: pyteladventure/pyteladventure/__init__.py
Scanned: 2016-10-11 20:56:53.134963
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.List'>)

mchambliss/flask
https://github.com/mchambliss/flask
Entry file: flask/setup.py
Scanned: 2016-10-11 20:57:13.393638
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

robi42/backbone-flask
https://github.com/robi42/backbone-flask
Entry file: backbone-flask/app.py
Scanned: 2016-10-11 20:57:51.343535
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

suzanshakya/flask-clevercss
https://github.com/suzanshakya/flask-clevercss
Entry file: flask-clevercss/example/runserver.py
Scanned: 2016-10-11 20:57:52.824851
No vulnerabilities found.


joshfinnie/Flask-shrtn
https://github.com/joshfinnie/Flask-shrtn
Entry file: Flask-shrtn/Flask-shrtn.py
Scanned: 2016-10-11 20:57:54.323434
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tomatohater/goonhilly
https://github.com/tomatohater/goonhilly
Entry file: goonhilly/goonhilly.py
Scanned: 2016-10-11 20:58:03.090592
No vulnerabilities found.


pallets/flask
https://github.com/pallets/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 10:51:13.668182
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

gigq/flasktodo
https://github.com/gigq/flasktodo
Entry file: flasktodo/application.py
Scanned: 2016-10-12 10:51:14.636615
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flosch/simpleapi
https://github.com/flosch/simpleapi
Entry file: simpleapi/example_project/server/flask1/app.py
Scanned: 2016-10-12 10:51:17.230215
No vulnerabilities found.


codebykat/robotkitten
https://github.com/codebykat/robotkitten
Entry file: None
Scanned: 2016-10-12 10:51:39.714840
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/codebykat/robotkitten.

mitsuhiko/flask-oauth
https://github.com/mitsuhiko/flask-oauth
Entry file: flask-oauth/example/facebook.py
Scanned: 2016-10-12 10:52:10.879643
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-openid
https://github.com/mitsuhiko/flask-openid
Entry file: flask-openid/flask_openid.py
Scanned: 2016-10-12 10:52:11.928089
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

artisonian/flaskengine
https://github.com/artisonian/flaskengine
Entry file: flaskengine/flaskengine/__init__.py
Scanned: 2016-10-12 10:52:16.263660
No vulnerabilities found.


toomoresuch/template-gae-with-flask
https://github.com/toomoresuch/template-gae-with-flask
Entry file: template-gae-with-flask/application.py
Scanned: 2016-10-12 10:52:17.787351
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: template-gae-with-flask/flask.py

aljoscha/shot-o-matic
https://github.com/aljoscha/shot-o-matic
Entry file: shot-o-matic/shotomatic.py
Scanned: 2016-10-12 10:53:11.874384
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-sqlalchemy
https://github.com/mitsuhiko/flask-sqlalchemy
Entry file: flask-sqlalchemy/flask_sqlalchemy/__init__.py
Scanned: 2016-10-12 10:53:15.325422
No vulnerabilities found.


mitsuhiko/flask-fungiform
https://github.com/mitsuhiko/flask-fungiform
Entry file: flask-fungiform/examples/example.py
Scanned: 2016-10-12 10:53:17.663919
No vulnerabilities found.


fsouza/talks
https://github.com/fsouza/talks
Entry file: talks/flask/app.py
Scanned: 2016-10-12 10:53:18.635388
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

unbracketed/flapp
https://github.com/unbracketed/flapp
Entry file: flapp/flapp/project_template/application.py
Scanned: 2016-10-12 10:53:19.139297
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dcolish/flask-markdown
https://github.com/dcolish/flask-markdown
Entry file: flask-markdown/tests/test_markdown.py
Scanned: 2016-10-12 10:54:13.724573
No vulnerabilities found.


blossom/flask-gae-skeleton
https://github.com/blossom/flask-gae-skeleton
Entry file: flask-gae-skeleton/gae/main.py
Scanned: 2016-10-12 10:54:14.209633
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kijun/flask-methodhack
https://github.com/kijun/flask-methodhack
Entry file: flask-methodhack/flaskext/methodhack.py
Scanned: 2016-10-12 10:54:17.425839
No vulnerabilities found.


viniciusfs/pasted-flask
https://github.com/viniciusfs/pasted-flask
Entry file: pasted-flask/pasted.py
Scanned: 2016-10-12 10:54:18.788238
Vulnerability 1:
File: pasted-flask/pasted.py
 > User input at line 219, trigger word "form[": 
	hexdigest = calc_md5(request.form['code'])
Reassigned in: 
	File: pasted-flask/pasted.py
	 > Line 221: paste = query_db('select * from pasted where md5 = ?', [hexdigest],one=True)
	File: pasted-flask/pasted.py
	 > Line 225: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 231: paste_id = cur.lastrowid
	File: pasted-flask/pasted.py
	 > Line 232: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 234: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 203: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 207: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 209: ret_MAYBE_FUNCTION_NAME = render_template('form.html',original=paste)
	File: pasted-flask/pasted.py
	 > Line 213: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 217: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
File: pasted-flask/pasted.py
 > reaches line 229, trigger word "execute(": 
	cur = g.db.execute('insert into pasted (code, md5, viewed_at, parent) values (?, ?, ?, ?)', [request.form['code'], hexdigest, viewed_at, request.form['parent']])



Cornu/Brain
https://github.com/Cornu/Brain
Entry file: Brain/brain/__init__.py
Scanned: 2016-10-12 10:54:22.158419
Vulnerability 1:
File: Brain/brain/controllers/text.py
 > User input at line 43, trigger word "get(": 
	key = request.form.get('search')
File: Brain/brain/controllers/text.py
 > reaches line 44, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('/' + key)



jbochi/scrum-you
https://github.com/jbochi/scrum-you
Entry file: scrum-you/application.py
Scanned: 2016-10-12 10:54:40.686327
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

miracle2k/flask-assets
https://github.com/miracle2k/flask-assets
Entry file: flask-assets/tests/test_config.py
Scanned: 2016-10-12 10:55:16.578803
No vulnerabilities found.


jgumbley/flask-payment
https://github.com/jgumbley/flask-payment
Entry file: flask-payment/tests.py
Scanned: 2016-10-12 10:55:18.073059
No vulnerabilities found.


eugenkiss/Simblin
https://github.com/eugenkiss/Simblin
Entry file: Simblin/simblin/__init__.py
Scanned: 2016-10-12 10:55:18.621464
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jugyo/flask-gae-template
https://github.com/jugyo/flask-gae-template
Entry file: flask-gae-template/app.py
Scanned: 2016-10-12 10:55:20.339051
No vulnerabilities found.


swanson/flask-embedly
https://github.com/swanson/flask-embedly
Entry file: flask-embedly/example/app.py
Scanned: 2016-10-12 10:55:21.666413
No vulnerabilities found.


LightStyle/Python-Board
https://github.com/LightStyle/Python-Board
Entry file: Python-Board/src/index.py
Scanned: 2016-10-12 10:55:22.944759
No vulnerabilities found.


miku/flask-gae-stub
https://github.com/miku/flask-gae-stub
Entry file: flask-gae-stub/flask/app.py
Scanned: 2016-10-12 10:55:23.442279
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

derwiki/wordisms_flask
https://github.com/derwiki/wordisms_flask
Entry file: wordisms_flask/www/main.py
Scanned: 2016-10-12 10:55:40.958702
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flebel/cisco79xx_phone_directory
https://github.com/flebel/cisco79xx_phone_directory
Entry file: cisco79xx_phone_directory/cisco79xx_phone_directory.py
Scanned: 2016-10-12 10:56:14.354096
No vulnerabilities found.


jkossen/imposter
https://github.com/jkossen/imposter
Entry file: None
Scanned: 2016-10-12 10:56:18.942385
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/jkossen/imposter.

sublee/subleekr
https://github.com/sublee/subleekr
Entry file: subleekr/subleekr/app.py
Scanned: 2016-10-12 10:56:23.823614
No vulnerabilities found.


akhodakivskiy/flask
https://github.com/akhodakivskiy/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 10:56:25.847724
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

thadeusb/flask-cache
https://github.com/thadeusb/flask-cache
Entry file: flask-cache/examples/hello.py
Scanned: 2016-10-12 10:56:28.630445
No vulnerabilities found.


kamalgill/flask-appengine-template
https://github.com/kamalgill/flask-appengine-template
Entry file: flask-appengine-template/src/lib/flask/sessions.py
Scanned: 2016-10-12 10:56:34.301242
No vulnerabilities found.


sublee/flask-autoindex
https://github.com/sublee/flask-autoindex
Entry file: flask-autoindex/flask_autoindex/__init__.py
Scanned: 2016-10-12 10:56:44.282652
No vulnerabilities found.


ericmoritz/flaskcma
https://github.com/ericmoritz/flaskcma
Entry file: flaskcma/flaskcma/app.py
Scanned: 2016-10-12 10:57:14.620813
No vulnerabilities found.


indexofire/flasky
https://github.com/indexofire/flasky
Entry file: flasky/flasky/flask/app.py
Scanned: 2016-10-12 10:57:15.112022
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ericmoritz/flask-auth
https://github.com/ericmoritz/flask-auth
Entry file: flask-auth/flaskext/auth/tests/workflow.py
Scanned: 2016-10-12 10:57:20.435850
No vulnerabilities found.


sublee/flask-silk
https://github.com/sublee/flask-silk
Entry file: flask-silk/test.py
Scanned: 2016-10-12 10:57:28.191712
No vulnerabilities found.


proudlygeek/proudlygeek-blog
https://github.com/proudlygeek/proudlygeek-blog
Entry file: proudlygeek-blog/flask/app.py
Scanned: 2016-10-12 10:57:28.731593
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

JunKikuchi/flask-gae
https://github.com/JunKikuchi/flask-gae
Entry file: flask-gae/lib/flask/app.py
Scanned: 2016-10-12 10:57:29.215738
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

glenbot/flask-tweetfeed
https://github.com/glenbot/flask-tweetfeed
Entry file: flask-tweetfeed/tweetfeedapp.py
Scanned: 2016-10-12 10:57:30.433573
No vulnerabilities found.


fsouza/palestra-flask-2010-giran
https://github.com/fsouza/palestra-flask-2010-giran
Entry file: palestra-flask-2010-giran/projetos/projetos.py
Scanned: 2016-10-12 10:57:35.778860
No vulnerabilities found.


shiloa/flask-clean
https://github.com/shiloa/flask-clean
Entry file: flask-clean/app.py
Scanned: 2016-10-12 10:57:43.186206
No vulnerabilities found.


dag/flask-genshi
https://github.com/dag/flask-genshi
Entry file: flask-genshi/examples/flaskr/flaskr.py
Scanned: 2016-10-12 10:58:21.624757
No vulnerabilities found.


raliste/Flaskito
https://github.com/raliste/Flaskito
Entry file: Flaskito/flaskito/__init__.py
Scanned: 2016-10-12 10:58:26.355806
No vulnerabilities found.


mikewest/flask-pyplaceholder
https://github.com/mikewest/flask-pyplaceholder
Entry file: flask-pyplaceholder/generator.py
Scanned: 2016-10-12 10:58:30.705084
No vulnerabilities found.


whalesalad/arbesko-files
https://github.com/whalesalad/arbesko-files
Entry file: arbesko-files/files/__init__.py
Scanned: 2016-10-12 10:58:37.406081
No vulnerabilities found.


danjac/Flask-Script
https://github.com/danjac/Flask-Script
Entry file: Flask-Script/tests.py
Scanned: 2016-10-12 10:59:15.552737
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

danjac/Flask-WTF
https://github.com/danjac/Flask-WTF
Entry file: Flask-WTF/examples/recaptcha/app.py
Scanned: 2016-10-12 10:59:18.793431
No vulnerabilities found.


danjac/Flask-Mail
https://github.com/danjac/Flask-Mail
Entry file: Flask-Mail/tests.py
Scanned: 2016-10-12 10:59:25.788838
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cropd/crashkurs-flask
https://github.com/cropd/crashkurs-flask
Entry file: crashkurs-flask/flask/app.py
Scanned: 2016-10-12 10:59:30.212830
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hasgeek/github-hook
https://github.com/hasgeek/github-hook
Entry file: github-hook/github-hook.py
Scanned: 2016-10-12 10:59:31.937115
No vulnerabilities found.


pygloo/bewype-flask-controllers
https://github.com/pygloo/bewype-flask-controllers
Entry file: bewype-flask-controllers/bewype/flask/_app.py
Scanned: 2016-10-12 10:59:34.028492
No vulnerabilities found.


sontek-archive/redditor-stats
https://github.com/sontek-archive/redditor-stats
Entry file: redditor-stats/web.py
Scanned: 2016-10-12 10:59:36.312836
No vulnerabilities found.


Frozen-Flask/Frozen-Flask
https://github.com/Frozen-Flask/Frozen-Flask
Entry file: Frozen-Flask/flask_frozen/__init__.py
Scanned: 2016-10-12 11:00:16.494760
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

cobrateam/flask-mongoalchemy
https://github.com/cobrateam/flask-mongoalchemy
Entry file: flask-mongoalchemy/flask_mongoalchemy/__init__.py
Scanned: 2016-10-12 11:00:18.638953
No vulnerabilities found.


Flask-FlatPages/Flask-FlatPages
https://github.com/Flask-FlatPages/Flask-FlatPages
Entry file: Flask-FlatPages/tests/test_flask_flatpages.py
Scanned: 2016-10-12 11:00:21.185543
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

fsouza/flask-rest-example
https://github.com/fsouza/flask-rest-example
Entry file: flask-rest-example/library.py
Scanned: 2016-10-12 11:00:27.472412
Vulnerability 1:
File: flask-rest-example/library.py
 > User input at line 63, trigger word "form[": 
	name = request.form['name']
Reassigned in: 
	File: flask-rest-example/library.py
	 > Line 64: book = Book(id=2, name=name)
File: flask-rest-example/library.py
 > reaches line 65, trigger word "flash(": 
	flash('Book %s sucessful saved!' % book.name)



pilt/flask-versioned
https://github.com/pilt/flask-versioned
Entry file: flask-versioned/test_versioned.py
Scanned: 2016-10-12 11:00:28.887407
No vulnerabilities found.


tokibito/flask-hgwebcommit
https://github.com/tokibito/flask-hgwebcommit
Entry file: flask-hgwebcommit/hgwebcommit/__init__.py
Scanned: 2016-10-12 11:00:35.099928
Vulnerability 1:
File: flask-hgwebcommit/hgwebcommit/views.py
 > User input at line 97, trigger word ".data": 
	message = operation_repo(repo, form.data['operation'], form.data['files'], form.data['commit_message'])
File: flask-hgwebcommit/hgwebcommit/views.py
 > reaches line 98, trigger word "flash(": 
	flash(message)



Nassty/flask-gae
https://github.com/Nassty/flask-gae
Entry file: flask-gae/lib/flask/app.py
Scanned: 2016-10-12 11:00:35.602345
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sgk/BulkDM
https://github.com/sgk/BulkDM
Entry file: BulkDM/application.py
Scanned: 2016-10-12 11:00:44.121941
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sontek-archive/redditor-stats
https://github.com/sontek-archive/redditor-stats
Entry file: redditor-stats/web.py
Scanned: 2016-10-12 11:01:18.017175
No vulnerabilities found.


zzzsochi/Flask-Gravatar
https://github.com/zzzsochi/Flask-Gravatar
Entry file: Flask-Gravatar/tests/test_core.py
Scanned: 2016-10-12 11:01:28.054158
No vulnerabilities found.


dag/flask-zodb
https://github.com/dag/flask-zodb
Entry file: flask-zodb/flask_zodb.py
Scanned: 2016-10-12 11:01:28.589605
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

zen4ever/route53manager
https://github.com/zen4ever/route53manager
Entry file: route53manager/route53/__init__.py
Scanned: 2016-10-12 11:01:31.074035
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-kitchensink
https://github.com/mitsuhiko/flask-kitchensink
Entry file: flask-kitchensink/example-code/hello.py
Scanned: 2016-10-12 11:01:31.574720
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

eyeseast/flask-docviewer
https://github.com/eyeseast/flask-docviewer
Entry file: flask-docviewer/docviewer/app.py
Scanned: 2016-10-12 11:01:34.915753
No vulnerabilities found.


dag/flask-attest
https://github.com/dag/flask-attest
Entry file: flask-attest/tests.py
Scanned: 2016-10-12 11:01:36.447853
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

ekalinin/flask-noextref
https://github.com/ekalinin/flask-noextref
Entry file: flask-noextref/test_noextref.py
Scanned: 2016-10-12 11:01:45.880468
No vulnerabilities found.


teohm/flitter
https://github.com/teohm/flitter
Entry file: flitter/flitter/__init__.py
Scanned: 2016-10-12 11:02:23.447235
Vulnerability 1:
File: flitter/flitter/controllers/user.py
 > User input at line 19, trigger word "form[": 
	username = request.form['username']
Reassigned in: 
	File: flitter/flitter/controllers/user.py
	 > Line 24: session['user'] = username
	File: flitter/flitter/controllers/user.py
	 > Line 26: ret_MAYBE_FUNCTION_NAME = redirect(url_for('entry.entries',username=username))
	File: flitter/flitter/controllers/user.py
	 > Line 30: ret_MAYBE_FUNCTION_NAME = render_template('signup.html',error=error)
	File: flitter/flitter/controllers/user.py
	 > Line 15: ret_MAYBE_FUNCTION_NAME = redirect_to_user_page()
File: flitter/flitter/controllers/user.py
 > reaches line 25, trigger word "flash(": 
	flash('Welcome, {0}.'.format(username))



aaront/calcmymarks2
https://github.com/aaront/calcmymarks2
Entry file: calcmymarks2/main.py
Scanned: 2016-10-12 11:02:27.978172
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-feedback
https://github.com/mitsuhiko/flask-feedback
Entry file: flask-feedback/feedback.py
Scanned: 2016-10-12 11:02:31.118557
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

wilsaj/flask-admin-old
https://github.com/wilsaj/flask-admin-old
Entry file: flask-admin-old/test_admin.py
Scanned: 2016-10-12 11:02:40.262705
No vulnerabilities found.


leandrosilva/flaskito
https://github.com/leandrosilva/flaskito
Entry file: flaskito/src/flaskito.py
Scanned: 2016-10-12 11:02:40.808059
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/Flask-API-Server
https://github.com/marchon/Flask-API-Server
Entry file: Flask-API-Server/apiserver/tests/app.py
Scanned: 2016-10-12 11:02:42.212158
No vulnerabilities found.


kapilreddy/Shabda-Sangraha
https://github.com/kapilreddy/Shabda-Sangraha
Entry file: Shabda-Sangraha/dict.py
Scanned: 2016-10-12 11:03:18.228825
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tooxie/flask-syrinx
https://github.com/tooxie/flask-syrinx
Entry file: flask-syrinx/syrinx/__init__.py
Scanned: 2016-10-12 11:03:18.749245
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joshourisman/flask-shortly
https://github.com/joshourisman/flask-shortly
Entry file: flask-shortly/shortly/__init__.py
Scanned: 2016-10-12 11:03:29.579930
No vulnerabilities found.


jamiltron/fitgen
https://github.com/jamiltron/fitgen
Entry file: fitgen/fitgen.py
Scanned: 2016-10-12 11:03:32.048841
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tomviner/Flask-Name-that-actor-or-movie
https://github.com/tomviner/Flask-Name-that-actor-or-movie
Entry file: Flask-Name-that-actor-or-movie/namer.py
Scanned: 2016-10-12 11:03:42.021253
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/flylons
https://github.com/marchon/flylons
Entry file: flylons/application/__init__.py
Scanned: 2016-10-12 11:03:46.522199
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/checkinmapper
https://github.com/marchon/checkinmapper
Entry file: checkinmapper/checkinmapper.py
Scanned: 2016-10-12 11:04:19.155118
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

comfuture/simplesite
https://github.com/comfuture/simplesite
Entry file: simplesite/simplesite/core.py
Scanned: 2016-10-12 11:04:19.650495
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

zachwill/flask-engine
https://github.com/zachwill/flask-engine
Entry file: flask-engine/libs/flask/sessions.py
Scanned: 2016-10-12 11:04:30.222180
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

spantaleev/flask-sijax
https://github.com/spantaleev/flask-sijax
Entry file: flask-sijax/examples/comet.py
Scanned: 2016-10-12 11:04:32.981106
No vulnerabilities found.


utahta/Flask-MVC-Pattern
https://github.com/utahta/Flask-MVC-Pattern
Entry file: Flask-MVC-Pattern/main.py
Scanned: 2016-10-12 11:04:34.330586
No vulnerabilities found.


jzempel/flask-exceptional
https://github.com/jzempel/flask-exceptional
Entry file: flask-exceptional/flask_exceptional.py
Scanned: 2016-10-12 11:04:41.827599
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

qsnake/flask
https://github.com/qsnake/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 11:04:47.533167
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

joeyespo/flask-scaffold
https://github.com/joeyespo/flask-scaffold
Entry file: flask-scaffold/[appname].py
Scanned: 2016-10-12 11:05:20.071201
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

iwebhosting/collectd-flask
https://github.com/iwebhosting/collectd-flask
Entry file: collectd-flask/collectdflask.py
Scanned: 2016-10-12 11:05:21.385958
No vulnerabilities found.


yxm0513/flask-ims
https://github.com/yxm0513/flask-ims
Entry file: flask-ims/flask/sessions.py
Scanned: 2016-10-12 11:05:24.911632
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fay/flask-skeleton
https://github.com/fay/flask-skeleton
Entry file: flask-skeleton/app/__init__.py
Scanned: 2016-10-12 11:05:31.992316
No vulnerabilities found.


joshourisman/flask-beans
https://github.com/joshourisman/flask-beans
Entry file: flask-beans/beans.py
Scanned: 2016-10-12 11:05:33.402271
No vulnerabilities found.


jjinux/pyteladventure
https://github.com/jjinux/pyteladventure
Entry file: pyteladventure/pyteladventure/__init__.py
Scanned: 2016-10-12 11:05:33.943424
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.List'>)

mchambliss/flask
https://github.com/mchambliss/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 11:05:47.985021
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

robi42/backbone-flask
https://github.com/robi42/backbone-flask
Entry file: backbone-flask/app.py
Scanned: 2016-10-12 11:06:31.417371
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

suzanshakya/flask-clevercss
https://github.com/suzanshakya/flask-clevercss
Entry file: flask-clevercss/example/runserver.py
Scanned: 2016-10-12 11:06:34.148915
No vulnerabilities found.


joshfinnie/Flask-shrtn
https://github.com/joshfinnie/Flask-shrtn
Entry file: Flask-shrtn/Flask-shrtn.py
Scanned: 2016-10-12 11:06:34.659245
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tomatohater/goonhilly
https://github.com/tomatohater/goonhilly
Entry file: goonhilly/goonhilly.py
Scanned: 2016-10-12 11:06:44.407577
No vulnerabilities found.


jmoiron/jmoiron.net
https://github.com/jmoiron/jmoiron.net
Entry file: None
Scanned: 2016-10-12 11:06:47.920224
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

fzuslide/video_new
https://github.com/fzuslide/video_new
Entry file: video_new/application.py
Scanned: 2016-10-12 11:07:22.185506
No vulnerabilities found.


tomatohater/lydon
https://github.com/tomatohater/lydon
Entry file: lydon/lydon/__init__.py
Scanned: 2016-10-12 11:07:23.584083
No vulnerabilities found.


williamratcliff/django-feedback
https://github.com/williamratcliff/django-feedback
Entry file: django-feedback/feedback.py
Scanned: 2016-10-12 11:07:35.524462
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joelbm24/blog
https://github.com/joelbm24/blog
Entry file: blog/flaskr.py
Scanned: 2016-10-12 11:07:37.359068
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hoprocker/mylons
https://github.com/hoprocker/mylons
Entry file: mylons/lib/python2.5/site-packages/Flask-0.6.1-py2.5.egg/flask/app.py
Scanned: 2016-10-12 11:07:50.214469
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

crisisking/bsg-raffle
https://github.com/crisisking/bsg-raffle
Entry file: bsg-raffle/raffle.py
Scanned: 2016-10-12 11:07:51.527350
Vulnerability 1:
File: bsg-raffle/raffle.py
 > User input at line 39, trigger word "form[": 
	user_id = int(request.form['user_id'])
File: bsg-raffle/raffle.py
 > reaches line 42, trigger word "execute(": 
	g.db.execute('INSERT INTO winners(participant_id, prize_name)
            VALUES (?, ?)', (user_id, prize))

Vulnerability 2:
File: bsg-raffle/raffle.py
 > User input at line 40, trigger word "form[": 
	prize = request.form['prize']
Reassigned in: 
	File: bsg-raffle/raffle.py
	 > Line 49: ret_MAYBE_FUNCTION_NAME = render_template('winner_added.html',name=username[0], prize=prize)
File: bsg-raffle/raffle.py
 > reaches line 42, trigger word "execute(": 
	g.db.execute('INSERT INTO winners(participant_id, prize_name)
            VALUES (?, ?)', (user_id, prize))

Vulnerability 3:
File: bsg-raffle/raffle.py
 > User input at line 66, trigger word "form[": 
	username = request.form['username']
File: bsg-raffle/raffle.py
 > reaches line 68, trigger word "execute(": 
	g.db.execute('INSERT INTO participants(name)
                VALUES (?)', (username))

Vulnerability 4:
File: bsg-raffle/raffle.py
 > User input at line 66, trigger word "form[": 
	username = request.form['username']
File: bsg-raffle/raffle.py
 > reaches line 70, trigger word "flash(": 
	flash('%s added successfully!' % username)



adamgreig/pyautopull
https://github.com/adamgreig/pyautopull
Entry file: pyautopull/pyautopull.py
Scanned: 2016-10-12 11:07:52.799237
No vulnerabilities found.


sean-/flask-skeleton
https://github.com/sean-/flask-skeleton
Entry file: None
Scanned: 2016-10-12 11:08:24.461484
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/sean-/flask-skeleton.

Runscope/httpbin
https://github.com/Runscope/httpbin
Entry file: httpbin/httpbin/filters.py
Scanned: 2016-10-12 11:08:29.242038
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.FunctionDef'>)

hasgeek/flask-lastuser
https://github.com/hasgeek/flask-lastuser
Entry file: flask-lastuser/tests/test_mergeuser.py
Scanned: 2016-10-12 11:08:33.373966
No vulnerabilities found.


BooBSD/flask-odesk
https://github.com/BooBSD/flask-odesk
Entry file: flask-odesk/tests.py
Scanned: 2016-10-12 11:08:35.310785
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cool-shark/redimon
https://github.com/cool-shark/redimon
Entry file: redimon/src/redimon/app.py
Scanned: 2016-10-12 11:08:38.289505
No vulnerabilities found.


pcsanwald/flask_site
https://github.com/pcsanwald/flask_site
Entry file: flask_site/mysite.py
Scanned: 2016-10-12 11:08:56.683660
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

suzanshakya/flask-clevercss
https://github.com/suzanshakya/flask-clevercss
Entry file: flask-clevercss/example/runserver.py
Scanned: 2016-10-12 11:08:58.171678
No vulnerabilities found.


dag/flask-sassy
https://github.com/dag/flask-sassy
Entry file: flask-sassy/tests/__init__.py
Scanned: 2016-10-12 11:09:23.482712
No vulnerabilities found.


charlieevett/jiffy-portal
https://github.com/charlieevett/jiffy-portal
Entry file: jiffy-portal/portal/app.py
Scanned: 2016-10-12 11:09:24.843851
No vulnerabilities found.


tomekwojcik/Flask-Module-Static-Files
https://github.com/tomekwojcik/Flask-Module-Static-Files
Entry file: Flask-Module-Static-Files/stest/__init__.py
Scanned: 2016-10-12 11:09:28.204510
No vulnerabilities found.


justjkk/dotpath
https://github.com/justjkk/dotpath
Entry file: dotpath/run.py
Scanned: 2016-10-12 11:09:35.945826
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

almet/semantic-bookclub
https://github.com/almet/semantic-bookclub
Entry file: semantic-bookclub/app/web.py
Scanned: 2016-10-12 11:09:37.782215
Vulnerability 1:
File: semantic-bookclub/app/web.py
 > User input at line 81, trigger word ".data": 
	book_title = dict(self.book.choices)[self.book.data]
File: semantic-bookclub/app/web.py
 > reaches line 82, trigger word "flash(": 
	flash('%s have successfully borrowed %s' % (self.borrower.data, book_title))

Vulnerability 2:
File: semantic-bookclub/app/web.py
 > User input at line 101, trigger word ".data": 
	member = Member.get_by(foaf_givenName=self.member.data).one()
File: semantic-bookclub/app/web.py
 > reaches line 105, trigger word "flash(": 
	flash('%s now owns %s' % (member.foaf_givenName.first, book.dcterms_title.first))

Vulnerability 3:
File: semantic-bookclub/app/web.py
 > User input at line 102, trigger word ".data": 
	book = Book.get_by(dcterms_identifier=self.book.data).one()
File: semantic-bookclub/app/web.py
 > reaches line 105, trigger word "flash(": 
	flash('%s now owns %s' % (member.foaf_givenName.first, book.dcterms_title.first))



t9md/snippy
https://github.com/t9md/snippy
Entry file: snippy/snippy.py
Scanned: 2016-10-12 11:09:40.655158
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

stehem/Tywna
https://github.com/stehem/Tywna
Entry file: Tywna/application/__init__.py
Scanned: 2016-10-12 11:09:49.655978
No vulnerabilities found.


hoprocker/mylons
https://github.com/hoprocker/mylons
Entry file: mylons/lib/python2.5/site-packages/Flask-0.6.1-py2.5.egg/flask/app.py
Scanned: 2016-10-12 11:09:53.880523
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

pallets/flask
https://github.com/pallets/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 11:15:54.516424
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

gigq/flasktodo
https://github.com/gigq/flasktodo
Entry file: flasktodo/application.py
Scanned: 2016-10-12 11:15:55.848453
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flosch/simpleapi
https://github.com/flosch/simpleapi
Entry file: simpleapi/example_project/server/flask1/app.py
Scanned: 2016-10-12 11:15:58.448862
No vulnerabilities found.


codebykat/robotkitten
https://github.com/codebykat/robotkitten
Entry file: None
Scanned: 2016-10-12 11:16:17.877380
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/codebykat/robotkitten.

mitsuhiko/flask-oauth
https://github.com/mitsuhiko/flask-oauth
Entry file: flask-oauth/example/facebook.py
Scanned: 2016-10-12 11:16:52.031000
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-openid
https://github.com/mitsuhiko/flask-openid
Entry file: flask-openid/flask_openid.py
Scanned: 2016-10-12 11:16:53.053320
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

artisonian/flaskengine
https://github.com/artisonian/flaskengine
Entry file: flaskengine/flaskengine/__init__.py
Scanned: 2016-10-12 11:16:57.372208
No vulnerabilities found.


toomoresuch/template-gae-with-flask
https://github.com/toomoresuch/template-gae-with-flask
Entry file: template-gae-with-flask/application.py
Scanned: 2016-10-12 11:16:59.890526
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: template-gae-with-flask/flask.py

aljoscha/shot-o-matic
https://github.com/aljoscha/shot-o-matic
Entry file: shot-o-matic/shotomatic.py
Scanned: 2016-10-12 11:17:52.896335
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-sqlalchemy
https://github.com/mitsuhiko/flask-sqlalchemy
Entry file: flask-sqlalchemy/flask_sqlalchemy/__init__.py
Scanned: 2016-10-12 11:17:56.227788
No vulnerabilities found.


mitsuhiko/flask-fungiform
https://github.com/mitsuhiko/flask-fungiform
Entry file: flask-fungiform/examples/example.py
Scanned: 2016-10-12 11:17:58.556232
No vulnerabilities found.


fsouza/talks
https://github.com/fsouza/talks
Entry file: talks/flask/app.py
Scanned: 2016-10-12 11:17:59.535710
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

unbracketed/flapp
https://github.com/unbracketed/flapp
Entry file: flapp/flapp/project_template/application.py
Scanned: 2016-10-12 11:18:00.050654
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dcolish/flask-markdown
https://github.com/dcolish/flask-markdown
Entry file: flask-markdown/tests/test_markdown.py
Scanned: 2016-10-12 11:18:54.597942
No vulnerabilities found.


blossom/flask-gae-skeleton
https://github.com/blossom/flask-gae-skeleton
Entry file: flask-gae-skeleton/gae/main.py
Scanned: 2016-10-12 11:18:55.096452
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kijun/flask-methodhack
https://github.com/kijun/flask-methodhack
Entry file: flask-methodhack/flaskext/methodhack.py
Scanned: 2016-10-12 11:18:58.332176
No vulnerabilities found.


viniciusfs/pasted-flask
https://github.com/viniciusfs/pasted-flask
Entry file: pasted-flask/pasted.py
Scanned: 2016-10-12 11:18:59.684683
Vulnerability 1:
File: pasted-flask/pasted.py
 > User input at line 219, trigger word "form[": 
	hexdigest = calc_md5(request.form['code'])
Reassigned in: 
	File: pasted-flask/pasted.py
	 > Line 221: paste = query_db('select * from pasted where md5 = ?', [hexdigest],one=True)
	File: pasted-flask/pasted.py
	 > Line 225: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 231: paste_id = cur.lastrowid
	File: pasted-flask/pasted.py
	 > Line 232: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 234: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 203: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 207: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 209: ret_MAYBE_FUNCTION_NAME = render_template('form.html',original=paste)
	File: pasted-flask/pasted.py
	 > Line 213: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 217: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
File: pasted-flask/pasted.py
 > reaches line 229, trigger word "execute(": 
	cur = g.db.execute('insert into pasted (code, md5, viewed_at, parent) values (?, ?, ?, ?)', [request.form['code'], hexdigest, viewed_at, request.form['parent']])



Cornu/Brain
https://github.com/Cornu/Brain
Entry file: Brain/brain/__init__.py
Scanned: 2016-10-12 11:19:03.117748
Vulnerability 1:
File: Brain/brain/controllers/text.py
 > User input at line 43, trigger word "get(": 
	key = request.form.get('search')
File: Brain/brain/controllers/text.py
 > reaches line 44, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('/' + key)



jbochi/scrum-you
https://github.com/jbochi/scrum-you
Entry file: scrum-you/application.py
Scanned: 2016-10-12 11:19:19.669833
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

miracle2k/flask-assets
https://github.com/miracle2k/flask-assets
Entry file: flask-assets/tests/test_config.py
Scanned: 2016-10-12 11:19:57.507869
No vulnerabilities found.


jgumbley/flask-payment
https://github.com/jgumbley/flask-payment
Entry file: flask-payment/tests.py
Scanned: 2016-10-12 11:19:59.004026
No vulnerabilities found.


eugenkiss/Simblin
https://github.com/eugenkiss/Simblin
Entry file: Simblin/simblin/__init__.py
Scanned: 2016-10-12 11:19:59.513265
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jugyo/flask-gae-template
https://github.com/jugyo/flask-gae-template
Entry file: flask-gae-template/app.py
Scanned: 2016-10-12 11:20:01.269898
No vulnerabilities found.


swanson/flask-embedly
https://github.com/swanson/flask-embedly
Entry file: flask-embedly/example/app.py
Scanned: 2016-10-12 11:20:02.606417
No vulnerabilities found.


LightStyle/Python-Board
https://github.com/LightStyle/Python-Board
Entry file: Python-Board/src/index.py
Scanned: 2016-10-12 11:20:03.815211
No vulnerabilities found.


miku/flask-gae-stub
https://github.com/miku/flask-gae-stub
Entry file: flask-gae-stub/flask/app.py
Scanned: 2016-10-12 11:20:04.316454
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

derwiki/wordisms_flask
https://github.com/derwiki/wordisms_flask
Entry file: wordisms_flask/www/main.py
Scanned: 2016-10-12 11:20:19.840101
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flebel/cisco79xx_phone_directory
https://github.com/flebel/cisco79xx_phone_directory
Entry file: cisco79xx_phone_directory/cisco79xx_phone_directory.py
Scanned: 2016-10-12 11:20:54.115519
No vulnerabilities found.


jkossen/imposter
https://github.com/jkossen/imposter
Entry file: None
Scanned: 2016-10-12 11:21:00.676557
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/jkossen/imposter.

sublee/subleekr
https://github.com/sublee/subleekr
Entry file: subleekr/subleekr/app.py
Scanned: 2016-10-12 11:21:05.552772
No vulnerabilities found.


akhodakivskiy/flask
https://github.com/akhodakivskiy/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 11:21:07.951989
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

thadeusb/flask-cache
https://github.com/thadeusb/flask-cache
Entry file: flask-cache/examples/hello.py
Scanned: 2016-10-12 11:21:10.809470
No vulnerabilities found.


kamalgill/flask-appengine-template
https://github.com/kamalgill/flask-appengine-template
Entry file: flask-appengine-template/src/lib/flask/sessions.py
Scanned: 2016-10-12 11:21:16.373100
No vulnerabilities found.


sublee/flask-autoindex
https://github.com/sublee/flask-autoindex
Entry file: flask-autoindex/flask_autoindex/__init__.py
Scanned: 2016-10-12 11:21:23.321705
No vulnerabilities found.


ericmoritz/flaskcma
https://github.com/ericmoritz/flaskcma
Entry file: flaskcma/flaskcma/app.py
Scanned: 2016-10-12 11:21:54.620864
No vulnerabilities found.


indexofire/flasky
https://github.com/indexofire/flasky
Entry file: flasky/flasky/flask/app.py
Scanned: 2016-10-12 11:21:57.116735
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ericmoritz/flask-auth
https://github.com/ericmoritz/flask-auth
Entry file: flask-auth/flaskext/auth/tests/workflow.py
Scanned: 2016-10-12 11:22:02.510494
No vulnerabilities found.


sublee/flask-silk
https://github.com/sublee/flask-silk
Entry file: flask-silk/test.py
Scanned: 2016-10-12 11:22:10.209914
No vulnerabilities found.


proudlygeek/proudlygeek-blog
https://github.com/proudlygeek/proudlygeek-blog
Entry file: proudlygeek-blog/flask/app.py
Scanned: 2016-10-12 11:22:10.773206
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

JunKikuchi/flask-gae
https://github.com/JunKikuchi/flask-gae
Entry file: flask-gae/lib/flask/app.py
Scanned: 2016-10-12 11:22:11.254909
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

glenbot/flask-tweetfeed
https://github.com/glenbot/flask-tweetfeed
Entry file: flask-tweetfeed/tweetfeedapp.py
Scanned: 2016-10-12 11:22:12.601083
No vulnerabilities found.


fsouza/palestra-flask-2010-giran
https://github.com/fsouza/palestra-flask-2010-giran
Entry file: palestra-flask-2010-giran/projetos/projetos.py
Scanned: 2016-10-12 11:22:17.959594
No vulnerabilities found.


shiloa/flask-clean
https://github.com/shiloa/flask-clean
Entry file: flask-clean/app.py
Scanned: 2016-10-12 11:22:21.325209
No vulnerabilities found.


dag/flask-genshi
https://github.com/dag/flask-genshi
Entry file: flask-genshi/examples/flaskr/flaskr.py
Scanned: 2016-10-12 11:23:03.703426
No vulnerabilities found.


raliste/Flaskito
https://github.com/raliste/Flaskito
Entry file: Flaskito/flaskito/__init__.py
Scanned: 2016-10-12 11:23:08.490724
No vulnerabilities found.


mikewest/flask-pyplaceholder
https://github.com/mikewest/flask-pyplaceholder
Entry file: flask-pyplaceholder/generator.py
Scanned: 2016-10-12 11:23:12.875082
No vulnerabilities found.


whalesalad/arbesko-files
https://github.com/whalesalad/arbesko-files
Entry file: arbesko-files/files/__init__.py
Scanned: 2016-10-12 11:23:18.908785
No vulnerabilities found.


danjac/Flask-Script
https://github.com/danjac/Flask-Script
Entry file: Flask-Script/tests.py
Scanned: 2016-10-12 11:23:55.064886
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

danjac/Flask-WTF
https://github.com/danjac/Flask-WTF
Entry file: Flask-WTF/examples/recaptcha/app.py
Scanned: 2016-10-12 11:24:00.131390
No vulnerabilities found.


danjac/Flask-Mail
https://github.com/danjac/Flask-Mail
Entry file: Flask-Mail/tests.py
Scanned: 2016-10-12 11:24:08.125750
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cropd/crashkurs-flask
https://github.com/cropd/crashkurs-flask
Entry file: crashkurs-flask/flask/app.py
Scanned: 2016-10-12 11:24:11.116450
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hasgeek/github-hook
https://github.com/hasgeek/github-hook
Entry file: github-hook/github-hook.py
Scanned: 2016-10-12 11:24:12.362494
No vulnerabilities found.


pygloo/bewype-flask-controllers
https://github.com/pygloo/bewype-flask-controllers
Entry file: bewype-flask-controllers/bewype/flask/_app.py
Scanned: 2016-10-12 11:24:13.710153
No vulnerabilities found.


sontek-archive/redditor-stats
https://github.com/sontek-archive/redditor-stats
Entry file: redditor-stats/web.py
Scanned: 2016-10-12 11:24:19.058712
No vulnerabilities found.


Frozen-Flask/Frozen-Flask
https://github.com/Frozen-Flask/Frozen-Flask
Entry file: Frozen-Flask/flask_frozen/__init__.py
Scanned: 2016-10-12 11:24:55.217969
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

cobrateam/flask-mongoalchemy
https://github.com/cobrateam/flask-mongoalchemy
Entry file: flask-mongoalchemy/flask_mongoalchemy/__init__.py
Scanned: 2016-10-12 11:24:59.216084
No vulnerabilities found.


Flask-FlatPages/Flask-FlatPages
https://github.com/Flask-FlatPages/Flask-FlatPages
Entry file: Flask-FlatPages/tests/test_flask_flatpages.py
Scanned: 2016-10-12 11:25:02.770636
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

fsouza/flask-rest-example
https://github.com/fsouza/flask-rest-example
Entry file: flask-rest-example/library.py
Scanned: 2016-10-12 11:25:09.013884
Vulnerability 1:
File: flask-rest-example/library.py
 > User input at line 63, trigger word "form[": 
	name = request.form['name']
Reassigned in: 
	File: flask-rest-example/library.py
	 > Line 64: book = Book(id=2, name=name)
File: flask-rest-example/library.py
 > reaches line 65, trigger word "flash(": 
	flash('Book %s sucessful saved!' % book.name)



pilt/flask-versioned
https://github.com/pilt/flask-versioned
Entry file: flask-versioned/test_versioned.py
Scanned: 2016-10-12 11:25:10.387781
No vulnerabilities found.


tokibito/flask-hgwebcommit
https://github.com/tokibito/flask-hgwebcommit
Entry file: flask-hgwebcommit/hgwebcommit/__init__.py
Scanned: 2016-10-12 11:25:15.243710
Vulnerability 1:
File: flask-hgwebcommit/hgwebcommit/views.py
 > User input at line 97, trigger word ".data": 
	message = operation_repo(repo, form.data['operation'], form.data['files'], form.data['commit_message'])
File: flask-hgwebcommit/hgwebcommit/views.py
 > reaches line 98, trigger word "flash(": 
	flash(message)



Nassty/flask-gae
https://github.com/Nassty/flask-gae
Entry file: flask-gae/lib/flask/app.py
Scanned: 2016-10-12 11:25:18.735218
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sgk/BulkDM
https://github.com/sgk/BulkDM
Entry file: BulkDM/application.py
Scanned: 2016-10-12 11:25:22.246866
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sontek-archive/redditor-stats
https://github.com/sontek-archive/redditor-stats
Entry file: redditor-stats/web.py
Scanned: 2016-10-12 11:25:59.173671
No vulnerabilities found.


zzzsochi/Flask-Gravatar
https://github.com/zzzsochi/Flask-Gravatar
Entry file: Flask-Gravatar/tests/test_core.py
Scanned: 2016-10-12 11:26:10.258894
No vulnerabilities found.


dag/flask-zodb
https://github.com/dag/flask-zodb
Entry file: flask-zodb/flask_zodb.py
Scanned: 2016-10-12 11:26:10.790190
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

zen4ever/route53manager
https://github.com/zen4ever/route53manager
Entry file: route53manager/route53/__init__.py
Scanned: 2016-10-12 11:26:12.284978
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-kitchensink
https://github.com/mitsuhiko/flask-kitchensink
Entry file: flask-kitchensink/example-code/hello.py
Scanned: 2016-10-12 11:26:12.789352
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

eyeseast/flask-docviewer
https://github.com/eyeseast/flask-docviewer
Entry file: flask-docviewer/docviewer/app.py
Scanned: 2016-10-12 11:26:15.176493
No vulnerabilities found.


dag/flask-attest
https://github.com/dag/flask-attest
Entry file: flask-attest/tests.py
Scanned: 2016-10-12 11:26:19.717352
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

ekalinin/flask-noextref
https://github.com/ekalinin/flask-noextref
Entry file: flask-noextref/test_noextref.py
Scanned: 2016-10-12 11:26:24.099729
No vulnerabilities found.


teohm/flitter
https://github.com/teohm/flitter
Entry file: flitter/flitter/__init__.py
Scanned: 2016-10-12 11:27:05.621605
Vulnerability 1:
File: flitter/flitter/controllers/user.py
 > User input at line 19, trigger word "form[": 
	username = request.form['username']
Reassigned in: 
	File: flitter/flitter/controllers/user.py
	 > Line 24: session['user'] = username
	File: flitter/flitter/controllers/user.py
	 > Line 26: ret_MAYBE_FUNCTION_NAME = redirect(url_for('entry.entries',username=username))
	File: flitter/flitter/controllers/user.py
	 > Line 30: ret_MAYBE_FUNCTION_NAME = render_template('signup.html',error=error)
	File: flitter/flitter/controllers/user.py
	 > Line 15: ret_MAYBE_FUNCTION_NAME = redirect_to_user_page()
File: flitter/flitter/controllers/user.py
 > reaches line 25, trigger word "flash(": 
	flash('Welcome, {0}.'.format(username))



aaront/calcmymarks2
https://github.com/aaront/calcmymarks2
Entry file: calcmymarks2/main.py
Scanned: 2016-10-12 11:27:10.147448
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-feedback
https://github.com/mitsuhiko/flask-feedback
Entry file: flask-feedback/feedback.py
Scanned: 2016-10-12 11:27:13.252191
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

wilsaj/flask-admin-old
https://github.com/wilsaj/flask-admin-old
Entry file: flask-admin-old/test_admin.py
Scanned: 2016-10-12 11:27:22.460832
No vulnerabilities found.


leandrosilva/flaskito
https://github.com/leandrosilva/flaskito
Entry file: flaskito/src/flaskito.py
Scanned: 2016-10-12 11:27:22.980595
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/Flask-API-Server
https://github.com/marchon/Flask-API-Server
Entry file: Flask-API-Server/apiserver/tests/app.py
Scanned: 2016-10-12 11:27:24.361399
No vulnerabilities found.


kapilreddy/Shabda-Sangraha
https://github.com/kapilreddy/Shabda-Sangraha
Entry file: Shabda-Sangraha/dict.py
Scanned: 2016-10-12 11:27:57.431839
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tooxie/flask-syrinx
https://github.com/tooxie/flask-syrinx
Entry file: flask-syrinx/syrinx/__init__.py
Scanned: 2016-10-12 11:27:59.946753
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joshourisman/flask-shortly
https://github.com/joshourisman/flask-shortly
Entry file: flask-shortly/shortly/__init__.py
Scanned: 2016-10-12 11:28:11.718036
No vulnerabilities found.


jamiltron/fitgen
https://github.com/jamiltron/fitgen
Entry file: fitgen/fitgen.py
Scanned: 2016-10-12 11:28:14.172837
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tomviner/Flask-Name-that-actor-or-movie
https://github.com/tomviner/Flask-Name-that-actor-or-movie
Entry file: Flask-Name-that-actor-or-movie/namer.py
Scanned: 2016-10-12 11:28:24.143336
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/flylons
https://github.com/marchon/flylons
Entry file: flylons/application/__init__.py
Scanned: 2016-10-12 11:28:25.639273
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/checkinmapper
https://github.com/marchon/checkinmapper
Entry file: checkinmapper/checkinmapper.py
Scanned: 2016-10-12 11:28:58.248105
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

comfuture/simplesite
https://github.com/comfuture/simplesite
Entry file: simplesite/simplesite/core.py
Scanned: 2016-10-12 11:29:00.750205
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

zachwill/flask-engine
https://github.com/zachwill/flask-engine
Entry file: flask-engine/libs/flask/sessions.py
Scanned: 2016-10-12 11:29:12.363933
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

spantaleev/flask-sijax
https://github.com/spantaleev/flask-sijax
Entry file: flask-sijax/examples/comet.py
Scanned: 2016-10-12 11:29:14.880983
No vulnerabilities found.


utahta/Flask-MVC-Pattern
https://github.com/utahta/Flask-MVC-Pattern
Entry file: Flask-MVC-Pattern/main.py
Scanned: 2016-10-12 11:29:16.154647
No vulnerabilities found.


jzempel/flask-exceptional
https://github.com/jzempel/flask-exceptional
Entry file: flask-exceptional/flask_exceptional.py
Scanned: 2016-10-12 11:29:24.663794
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

qsnake/flask
https://github.com/qsnake/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 11:29:27.181156
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

joeyespo/flask-scaffold
https://github.com/joeyespo/flask-scaffold
Entry file: flask-scaffold/[appname].py
Scanned: 2016-10-12 11:29:58.710538
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

iwebhosting/collectd-flask
https://github.com/iwebhosting/collectd-flask
Entry file: collectd-flask/collectdflask.py
Scanned: 2016-10-12 11:30:02.109127
No vulnerabilities found.


yxm0513/flask-ims
https://github.com/yxm0513/flask-ims
Entry file: flask-ims/flask/sessions.py
Scanned: 2016-10-12 11:30:06.652162
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fay/flask-skeleton
https://github.com/fay/flask-skeleton
Entry file: flask-skeleton/app/__init__.py
Scanned: 2016-10-12 11:30:13.706687
No vulnerabilities found.


joshourisman/flask-beans
https://github.com/joshourisman/flask-beans
Entry file: flask-beans/beans.py
Scanned: 2016-10-12 11:30:14.971086
No vulnerabilities found.


jjinux/pyteladventure
https://github.com/jjinux/pyteladventure
Entry file: pyteladventure/pyteladventure/__init__.py
Scanned: 2016-10-12 11:30:15.493923
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.List'>)

mchambliss/flask
https://github.com/mchambliss/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 11:30:27.720142
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

robi42/backbone-flask
https://github.com/robi42/backbone-flask
Entry file: backbone-flask/app.py
Scanned: 2016-10-12 11:31:13.159092
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

suzanshakya/flask-clevercss
https://github.com/suzanshakya/flask-clevercss
Entry file: flask-clevercss/example/runserver.py
Scanned: 2016-10-12 11:31:15.598321
No vulnerabilities found.


joshfinnie/Flask-shrtn
https://github.com/joshfinnie/Flask-shrtn
Entry file: Flask-shrtn/Flask-shrtn.py
Scanned: 2016-10-12 11:31:16.117102
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tomatohater/goonhilly
https://github.com/tomatohater/goonhilly
Entry file: goonhilly/goonhilly.py
Scanned: 2016-10-12 11:31:26.880532
No vulnerabilities found.


jmoiron/jmoiron.net
https://github.com/jmoiron/jmoiron.net
Entry file: None
Scanned: 2016-10-12 11:31:27.382591
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

fzuslide/video_new
https://github.com/fzuslide/video_new
Entry file: video_new/application.py
Scanned: 2016-10-12 11:32:00.749636
No vulnerabilities found.


tomatohater/lydon
https://github.com/tomatohater/lydon
Entry file: lydon/lydon/__init__.py
Scanned: 2016-10-12 11:32:03.136169
No vulnerabilities found.


williamratcliff/django-feedback
https://github.com/williamratcliff/django-feedback
Entry file: django-feedback/feedback.py
Scanned: 2016-10-12 11:32:13.604654
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joelbm24/blog
https://github.com/joelbm24/blog
Entry file: blog/flaskr.py
Scanned: 2016-10-12 11:32:16.560850
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hoprocker/mylons
https://github.com/hoprocker/mylons
Entry file: mylons/lib/python2.5/site-packages/Flask-0.6.1-py2.5.egg/flask/app.py
Scanned: 2016-10-12 11:32:26.138507
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

crisisking/bsg-raffle
https://github.com/crisisking/bsg-raffle
Entry file: bsg-raffle/raffle.py
Scanned: 2016-10-12 11:32:27.462969
Vulnerability 1:
File: bsg-raffle/raffle.py
 > User input at line 39, trigger word "form[": 
	user_id = int(request.form['user_id'])
File: bsg-raffle/raffle.py
 > reaches line 42, trigger word "execute(": 
	g.db.execute('INSERT INTO winners(participant_id, prize_name)
            VALUES (?, ?)', (user_id, prize))

Vulnerability 2:
File: bsg-raffle/raffle.py
 > User input at line 40, trigger word "form[": 
	prize = request.form['prize']
Reassigned in: 
	File: bsg-raffle/raffle.py
	 > Line 49: ret_MAYBE_FUNCTION_NAME = render_template('winner_added.html',name=username[0], prize=prize)
File: bsg-raffle/raffle.py
 > reaches line 42, trigger word "execute(": 
	g.db.execute('INSERT INTO winners(participant_id, prize_name)
            VALUES (?, ?)', (user_id, prize))

Vulnerability 3:
File: bsg-raffle/raffle.py
 > User input at line 66, trigger word "form[": 
	username = request.form['username']
File: bsg-raffle/raffle.py
 > reaches line 68, trigger word "execute(": 
	g.db.execute('INSERT INTO participants(name)
                VALUES (?)', (username))

Vulnerability 4:
File: bsg-raffle/raffle.py
 > User input at line 66, trigger word "form[": 
	username = request.form['username']
File: bsg-raffle/raffle.py
 > reaches line 70, trigger word "flash(": 
	flash('%s added successfully!' % username)



adamgreig/pyautopull
https://github.com/adamgreig/pyautopull
Entry file: pyautopull/pyautopull.py
Scanned: 2016-10-12 11:32:28.704165
No vulnerabilities found.


sean-/flask-skeleton
https://github.com/sean-/flask-skeleton
Entry file: None
Scanned: 2016-10-12 11:33:04.339922
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/sean-/flask-skeleton.

Runscope/httpbin
https://github.com/Runscope/httpbin
Entry file: httpbin/httpbin/filters.py
Scanned: 2016-10-12 11:33:07.877518
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.FunctionDef'>)

hasgeek/flask-lastuser
https://github.com/hasgeek/flask-lastuser
Entry file: flask-lastuser/tests/test_mergeuser.py
Scanned: 2016-10-12 11:33:14.976242
No vulnerabilities found.


BooBSD/flask-odesk
https://github.com/BooBSD/flask-odesk
Entry file: flask-odesk/tests.py
Scanned: 2016-10-12 11:33:15.463472
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cool-shark/redimon
https://github.com/cool-shark/redimon
Entry file: redimon/src/redimon/app.py
Scanned: 2016-10-12 11:33:16.851933
No vulnerabilities found.


pcsanwald/flask_site
https://github.com/pcsanwald/flask_site
Entry file: flask_site/mysite.py
Scanned: 2016-10-12 11:33:27.317945
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

suzanshakya/flask-clevercss
https://github.com/suzanshakya/flask-clevercss
Entry file: flask-clevercss/example/runserver.py
Scanned: 2016-10-12 11:33:29.828356
No vulnerabilities found.


dag/flask-sassy
https://github.com/dag/flask-sassy
Entry file: flask-sassy/tests/__init__.py
Scanned: 2016-10-12 11:34:01.262757
No vulnerabilities found.


charlieevett/jiffy-portal
https://github.com/charlieevett/jiffy-portal
Entry file: jiffy-portal/portal/app.py
Scanned: 2016-10-12 11:34:04.699312
No vulnerabilities found.


tomekwojcik/Flask-Module-Static-Files
https://github.com/tomekwojcik/Flask-Module-Static-Files
Entry file: Flask-Module-Static-Files/stest/__init__.py
Scanned: 2016-10-12 11:34:08.969320
No vulnerabilities found.


justjkk/dotpath
https://github.com/justjkk/dotpath
Entry file: dotpath/run.py
Scanned: 2016-10-12 11:34:13.499245
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

almet/semantic-bookclub
https://github.com/almet/semantic-bookclub
Entry file: semantic-bookclub/app/web.py
Scanned: 2016-10-12 11:34:17.337277
Vulnerability 1:
File: semantic-bookclub/app/web.py
 > User input at line 81, trigger word ".data": 
	book_title = dict(self.book.choices)[self.book.data]
File: semantic-bookclub/app/web.py
 > reaches line 82, trigger word "flash(": 
	flash('%s have successfully borrowed %s' % (self.borrower.data, book_title))

Vulnerability 2:
File: semantic-bookclub/app/web.py
 > User input at line 101, trigger word ".data": 
	member = Member.get_by(foaf_givenName=self.member.data).one()
File: semantic-bookclub/app/web.py
 > reaches line 105, trigger word "flash(": 
	flash('%s now owns %s' % (member.foaf_givenName.first, book.dcterms_title.first))

Vulnerability 3:
File: semantic-bookclub/app/web.py
 > User input at line 102, trigger word ".data": 
	book = Book.get_by(dcterms_identifier=self.book.data).one()
File: semantic-bookclub/app/web.py
 > reaches line 105, trigger word "flash(": 
	flash('%s now owns %s' % (member.foaf_givenName.first, book.dcterms_title.first))



t9md/snippy
https://github.com/t9md/snippy
Entry file: snippy/snippy.py
Scanned: 2016-10-12 11:34:18.309468
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

stehem/Tywna
https://github.com/stehem/Tywna
Entry file: Tywna/application/__init__.py
Scanned: 2016-10-12 11:34:32.328849
No vulnerabilities found.


hoprocker/mylons
https://github.com/hoprocker/mylons
Entry file: mylons/lib/python2.5/site-packages/Flask-0.6.1-py2.5.egg/flask/app.py
Scanned: 2016-10-12 11:34:32.952468
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

maxcountryman/bitpit-https-bridge
https://github.com/maxcountryman/bitpit-https-bridge
Entry file: bitpit-https-bridge/httpstobitpit/__init__.py
Scanned: 2016-10-12 11:34:34.431404
No vulnerabilities found.


maxcountryman/flask-bcrypt
https://github.com/maxcountryman/flask-bcrypt
Entry file: flask-bcrypt/flask_bcrypt.py
Scanned: 2016-10-12 11:35:06.138757
No vulnerabilities found.


kennethreitz-archive/flask-rest
https://github.com/kennethreitz-archive/flask-rest
Entry file: flask-rest/haystack/core.py
Scanned: 2016-10-12 11:35:14.904026
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tdryer/flask-forum
https://github.com/tdryer/flask-forum
Entry file: flask-forum/app.py
Scanned: 2016-10-12 11:35:17.200403
Vulnerability 1:
File: flask-forum/app.py
 > User input at line 124, trigger word ".data": 
	new_topic_id = post_topic(form.subject.data, form.content.data)
Reassigned in: 
	File: flask-forum/app.py
	 > Line 127: ret_MAYBE_FUNCTION_NAME = render_template('newtopic.html',form=form)
File: flask-forum/app.py
 > reaches line 126, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('/topic/' + new_topic_id)

Vulnerability 2:
File: flask-forum/app.py
 > User input at line 196, trigger word ".data": 
	username = form.username.data
File: flask-forum/app.py
 > reaches line 199, trigger word "execute(": 
	g.db.execute('INSERT INTO users (username, password_hash)                 values (?, ?)', [username, pw_hash])

Vulnerability 3:
File: flask-forum/app.py
 > User input at line 197, trigger word ".data": 
	password = form.password1.data
Reassigned in: 
	File: flask-forum/app.py
	 > Line 198: pw_hash = hashpw(password, gensalt())
File: flask-forum/app.py
 > reaches line 199, trigger word "execute(": 
	g.db.execute('INSERT INTO users (username, password_hash)                 values (?, ?)', [username, pw_hash])



dqminh/flask-mongoobject
https://github.com/dqminh/flask-mongoobject
Entry file: flask-mongoobject/examples_hello.py
Scanned: 2016-10-12 11:35:19.541113
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

gmonnerat/flask-sandbox
https://github.com/gmonnerat/flask-sandbox
Entry file: flask-sandbox/hello/hello.py
Scanned: 2016-10-12 11:35:20.719564
No vulnerabilities found.


DarkSector/wombat
https://github.com/DarkSector/wombat
Entry file: wombat/wombatdb.py
Scanned: 2016-10-12 11:35:31.666327
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lOlIl/Flask---Local-election
https://github.com/lOlIl/Flask---Local-election
Entry file: Flask---Local-election/app.py
Scanned: 2016-10-12 11:35:34.523187
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

paulftw/appengine-flask-template
https://github.com/paulftw/appengine-flask-template
Entry file: appengine-flask-template/app/app.py
Scanned: 2016-10-12 11:35:36.050201
No vulnerabilities found.


flores/aquadoc
https://github.com/flores/aquadoc
Entry file: aquadoc/aquadoc.py
Scanned: 2016-10-12 11:36:05.806672
No vulnerabilities found.


jorgeatorres/cotufa
https://github.com/jorgeatorres/cotufa
Entry file: cotufa/cotufa.py
Scanned: 2016-10-12 11:36:10.108515
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mbr/flask-kvsession
https://github.com/mbr/flask-kvsession
Entry file: flask-kvsession/tests/conftest.py
Scanned: 2016-10-12 11:36:21.042654
No vulnerabilities found.


radekstepan/Flask-Skeleton-App
https://github.com/radekstepan/Flask-Skeleton-App
Entry file: Flask-Skeleton-App/flask_app.py
Scanned: 2016-10-12 11:36:29.837232
No vulnerabilities found.


utahta/flask-on-fluxflex
https://github.com/utahta/flask-on-fluxflex
Entry file: flask-on-fluxflex/app/__init__.py
Scanned: 2016-10-12 11:36:36.580340
No vulnerabilities found.


femmerling/brunch-flask-gae-skeleton
https://github.com/femmerling/brunch-flask-gae-skeleton
Entry file: brunch-flask-gae-skeleton/gae/main.py
Scanned: 2016-10-12 11:37:05.783703
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

amcameron/gchartsdemo
https://github.com/amcameron/gchartsdemo
Entry file: gchartsdemo/charts.py
Scanned: 2016-10-12 11:37:07.081166
No vulnerabilities found.


bagyr/flaskPage
https://github.com/bagyr/flaskPage
Entry file: flaskPage/__init__.py
Scanned: 2016-10-12 11:37:10.324337
No vulnerabilities found.


sbook/flask-script
https://github.com/sbook/flask-script
Entry file: flask-script/tests.py
Scanned: 2016-10-12 11:37:21.901765
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joemarct/flask-gae-app
https://github.com/joemarct/flask-gae-app
Entry file: flask-gae-app/flask/app.py
Scanned: 2016-10-12 11:37:26.330492
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

Bhagyashree-Mandora/The-Python-Task
https://github.com/Bhagyashree-Mandora/The-Python-Task
Entry file: The-Python-Task/main.py
Scanned: 2016-10-12 11:37:30.594048
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

piratesolutions/ps-website
https://github.com/piratesolutions/ps-website
Entry file: ps-website/app.py
Scanned: 2016-10-12 11:37:36.250528
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

samrat/blogengine
https://github.com/samrat/blogengine
Entry file: blogengine/blogengine.py
Scanned: 2016-10-12 11:37:37.579346
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

TimFletcher/cmprss
https://github.com/TimFletcher/cmprss
Entry file: cmprss/cmprss.py
Scanned: 2016-10-12 11:38:03.839833
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

andyvanee/mappy
https://github.com/andyvanee/mappy
Entry file: mappy/mappy.py
Scanned: 2016-10-12 11:38:09.611105
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

barnslig/foreveralonebook
https://github.com/barnslig/foreveralonebook
Entry file: foreveralonebook/foreveralonebook.py
Scanned: 2016-10-12 11:38:16.511996
Vulnerability 1:
File: foreveralonebook/foreveralonebook.py
 > User input at line 47, trigger word "form[": 
	entry = escape(request.form['entry'])
File: foreveralonebook/foreveralonebook.py
 > reaches line 57, trigger word "execute(": 
	g.db.cur.execute('INSERT INTO feabook_posts (u_id, content) VALUES ({0}, '{1}');'.format(session['u_id'], entry))

Vulnerability 2:
File: foreveralonebook/foreveralonebook.py
 > User input at line 113, trigger word "form[": 
	password = hashlib.sha1(request.form['new_pw']).hexdigest()
File: foreveralonebook/foreveralonebook.py
 > reaches line 115, trigger word "execute(": 
	g.db.cur.execute('UPDATE feabook_user SET password = '{0}' WHERE id = '{1}';'.format(password, session['u_id']))

Vulnerability 3:
File: foreveralonebook/foreveralonebook.py
 > User input at line 151, trigger word "form[": 
	username = escape(request.form['username'])
Reassigned in: 
	File: foreveralonebook/foreveralonebook.py
	 > Line 171: session['username'] = username
	File: foreveralonebook/foreveralonebook.py
	 > Line 172: session['u_id'] = rows[0][0]
File: foreveralonebook/foreveralonebook.py
 > reaches line 157, trigger word "execute(": 
	g.db.cur.execute('SELECT username FROM feabook_user WHERE username = '{0}';'.format(username))

Vulnerability 4:
File: foreveralonebook/foreveralonebook.py
 > User input at line 151, trigger word "form[": 
	username = escape(request.form['username'])
Reassigned in: 
	File: foreveralonebook/foreveralonebook.py
	 > Line 171: session['username'] = username
	File: foreveralonebook/foreveralonebook.py
	 > Line 172: session['u_id'] = rows[0][0]
File: foreveralonebook/foreveralonebook.py
 > reaches line 164, trigger word "execute(": 
	g.db.cur.execute('INSERT INTO feabook_user (username, password) VALUES ('{0}', '{1}');'.format(username, password))

Vulnerability 5:
File: foreveralonebook/foreveralonebook.py
 > User input at line 152, trigger word "form[": 
	password = hashlib.sha1(request.form['password']).hexdigest()
File: foreveralonebook/foreveralonebook.py
 > reaches line 164, trigger word "execute(": 
	g.db.cur.execute('INSERT INTO feabook_user (username, password) VALUES ('{0}', '{1}');'.format(username, password))

Vulnerability 6:
File: foreveralonebook/foreveralonebook.py
 > User input at line 151, trigger word "form[": 
	username = escape(request.form['username'])
Reassigned in: 
	File: foreveralonebook/foreveralonebook.py
	 > Line 171: session['username'] = username
	File: foreveralonebook/foreveralonebook.py
	 > Line 172: session['u_id'] = rows[0][0]
File: foreveralonebook/foreveralonebook.py
 > reaches line 169, trigger word "execute(": 
	g.db.cur.execute('SELECT id, username FROM feabook_user WHERE username = '{0}';'.format(username))

Vulnerability 7:
File: foreveralonebook/foreveralonebook.py
 > User input at line 193, trigger word "form[": 
	username = escape(request.form['username'])
Reassigned in: 
	File: foreveralonebook/foreveralonebook.py
	 > Line 222: session['username'] = username
	File: foreveralonebook/foreveralonebook.py
	 > Line 223: session['u_id'] = rows[0][0]
File: foreveralonebook/foreveralonebook.py
 > reaches line 197, trigger word "execute(": 
	g.db.cur.execute('SELECT id, username, password FROM feabook_user WHERE username = '{0}' AND password = '{1}';'.format(username, password))

Vulnerability 8:
File: foreveralonebook/foreveralonebook.py
 > User input at line 194, trigger word "form[": 
	password = hashlib.sha1(request.form['password']).hexdigest()
File: foreveralonebook/foreveralonebook.py
 > reaches line 197, trigger word "execute(": 
	g.db.cur.execute('SELECT id, username, password FROM feabook_user WHERE username = '{0}' AND password = '{1}';'.format(username, password))



geek22com/referral_dashboard_engine
https://github.com/geek22com/referral_dashboard_engine
Entry file: referral_dashboard_engine/heymoose/__init__.py
Scanned: 2016-10-12 11:38:38.059056
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dqminh/flask-lettuce
https://github.com/dqminh/flask-lettuce
Entry file: flask-lettuce/test.py
Scanned: 2016-10-12 11:38:40.538882
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

radekstepan/FlaskBudget
https://github.com/radekstepan/FlaskBudget
Entry file: FlaskBudget/budget.py
Scanned: 2016-10-12 11:38:43.380604
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

UfSoft/Flask-MenuBuilder
https://github.com/UfSoft/Flask-MenuBuilder
Entry file: Flask-MenuBuilder/tests/test_menuitem.py
Scanned: 2016-10-12 11:39:04.781805
No vulnerabilities found.


gregglind/flask-tool
https://github.com/gregglind/flask-tool
Entry file: flask-tool/flasktool/console.py
Scanned: 2016-10-12 11:39:09.106773
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kblin/flask-downloader
https://github.com/kblin/flask-downloader
Entry file: flask-downloader/tests.py
Scanned: 2016-10-12 11:39:11.397014
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

maxcountryman/flog
https://github.com/maxcountryman/flog
Entry file: flog/flog/__init__.py
Scanned: 2016-10-12 11:39:16.971065
No vulnerabilities found.


sublee/Flask-Handler
https://github.com/sublee/Flask-Handler
Entry file: None
Scanned: 2016-10-12 11:39:19.172297
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/sublee/Flask-Handler.

Ramblurr/pyqdb
https://github.com/Ramblurr/pyqdb
Entry file: pyqdb/src/pyqdb.py
Scanned: 2016-10-12 11:39:41.706633
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

zackster/DijScrape--flask-rewrite-
https://github.com/zackster/DijScrape--flask-rewrite-
Entry file: DijScrape--flask-rewrite-/dijscrape.py
Scanned: 2016-10-12 11:39:43.007832
No vulnerabilities found.


asenchi/pomp
https://github.com/asenchi/pomp
Entry file: pomp/pomp/pomp.py
Scanned: 2016-10-12 11:39:44.222280
No vulnerabilities found.


tshirtman/snakenest
https://github.com/tshirtman/snakenest
Entry file: snakenest/main.py
Scanned: 2016-10-12 11:40:05.507537
No vulnerabilities found.


jvreeland/Python-Web-Service-for-Android-GMaps-AsyncTask-Demo
https://github.com/jvreeland/Python-Web-Service-for-Android-GMaps-AsyncTask-Demo
Entry file: Python-Web-Service-for-Android-GMaps-AsyncTask-Demo/gmaps.py
Scanned: 2016-10-12 11:40:08.822876
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: Python-Web-Service-for-Android-GMaps-AsyncTask-Demo/env/lib/python2.7/genericpath.py

triposo/geocodecache
https://github.com/triposo/geocodecache
Entry file: geocodecache/geocodecache.py
Scanned: 2016-10-12 11:40:12.037405
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

toastwaffle/ToDoQuick
https://github.com/toastwaffle/ToDoQuick
Entry file: ToDoQuick/todoquick.py
Scanned: 2016-10-12 11:40:17.521473
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

coleifer/flask-peewee
https://github.com/coleifer/flask-peewee
Entry file: flask-peewee/example/app.py
Scanned: 2016-10-12 11:40:43.406112
Vulnerability 1:
File: flask-peewee/example/admin.py
 > User input at line 27, trigger word "get(": 
	next = request.form.get('next') or self.dashboard_url()
File: flask-peewee/example/admin.py
 > reaches line 28, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect(next)



jeanphix/Flask-Dashed
https://github.com/jeanphix/Flask-Dashed
Entry file: Flask-Dashed/examples/sqlalchemy_backend.py
Scanned: 2016-10-12 11:40:46.914641
No vulnerabilities found.


jarus/flask-mongokit
https://github.com/jarus/flask-mongokit
Entry file: flask-mongokit/tests/test_base.py
Scanned: 2016-10-12 11:40:48.633588
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

namlook/flask-apibee
https://github.com/namlook/flask-apibee
Entry file: flask-apibee/example/app.py
Scanned: 2016-10-12 11:40:50.397922
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

voluntas/heroku-template-flask
https://github.com/voluntas/heroku-template-flask
Entry file: heroku-template-flask/snowflake/__init__.py
Scanned: 2016-10-12 11:41:05.638508
No vulnerabilities found.


Deepwalker/Flask-Bundle
https://github.com/Deepwalker/Flask-Bundle
Entry file: Flask-Bundle/samples/simple.py
Scanned: 2016-10-12 11:41:17.925434
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sunlightlabs/flask-districtoffices
https://github.com/sunlightlabs/flask-districtoffices
Entry file: flask-districtoffices/districtoffices.py
Scanned: 2016-10-12 11:41:20.762993
No vulnerabilities found.


quanticle/flask_blog
https://github.com/quanticle/flask_blog
Entry file: flask_blog/blog.py
Scanned: 2016-10-12 11:41:49.091710
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

garrettr/haps
https://github.com/garrettr/haps
Entry file: haps/quickstart.py
Scanned: 2016-10-12 11:41:50.427669
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dsully/sitter
https://github.com/dsully/sitter
Entry file: sitter/sitter/__init__.py
Scanned: 2016-10-12 11:42:08.404544
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ahri/nodeblog
https://github.com/ahri/nodeblog
Entry file: nodeblog/blog.py
Scanned: 2016-10-12 11:42:09.603762
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

maxcountryman/celeb
https://github.com/maxcountryman/celeb
Entry file: celeb/celeb/__init__.py
Scanned: 2016-10-12 11:42:13.168036
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/PO
https://github.com/marchon/PO
Entry file: PO/main.py
Scanned: 2016-10-12 11:42:18.422899
No vulnerabilities found.


slok/xlarrakoetxeaorg
https://github.com/slok/xlarrakoetxeaorg
Entry file: xlarrakoetxeaorg/mysite/blog/__init__.py
Scanned: 2016-10-12 11:42:21.811173
No vulnerabilities found.


boboppie/pyLiftOver
https://github.com/boboppie/pyLiftOver
Entry file: pyLiftOver/flask/lift-over-app.py
Scanned: 2016-10-12 11:42:41.223391
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

no0p/homepage
https://github.com/no0p/homepage
Entry file: homepage/site.py
Scanned: 2016-10-12 11:42:50.007821
No vulnerabilities found.


tjosten/python-push
https://github.com/tjosten/python-push
Entry file: python-push/push.py
Scanned: 2016-10-12 11:42:51.333854
No vulnerabilities found.


Joshkunz/PyChannel
https://github.com/Joshkunz/PyChannel
Entry file: PyChannel/PyChannel/__init__.py
Scanned: 2016-10-12 11:42:55.674942
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cbess/ytlinker
https://github.com/cbess/ytlinker
Entry file: ytlinker/flask/app.py
Scanned: 2016-10-12 11:42:58.676915
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

openshift/flask-example
https://github.com/openshift/flask-example
Entry file: flask-example/wsgi/myflaskapp.py
Scanned: 2016-10-12 11:43:10.877484
No vulnerabilities found.


wasabi0522/flaskr
https://github.com/wasabi0522/flaskr
Entry file: flaskr/flaskr/__init__.py
Scanned: 2016-10-12 11:43:42.596557
No vulnerabilities found.


amehta/Flaskly
https://github.com/amehta/Flaskly
Entry file: Flaskly/flaskly.py
Scanned: 2016-10-12 11:43:51.351508
Vulnerability 1:
File: Flaskly/flaskly.py
 > User input at line 73, trigger word "form[": 
	url = request.form['long_url']
Reassigned in: 
	File: Flaskly/flaskly.py
	 > Line 74: short = pickShortUrl(url)
File: Flaskly/flaskly.py
 > reaches line 75, trigger word "flash(": 
	flash('Short Url http:/localhost/' + short)



fyears/flaskr-redis
https://github.com/fyears/flaskr-redis
Entry file: flaskr-redis/app.py
Scanned: 2016-10-12 11:43:57.110854
No vulnerabilities found.


Jc2k/flask-example
https://github.com/Jc2k/flask-example
Entry file: flask-example/web.py
Scanned: 2016-10-12 11:44:07.392733
No vulnerabilities found.


brainTrain/flasktest
https://github.com/brainTrain/flasktest
Entry file: flasktest/hello.py
Scanned: 2016-10-12 11:44:12.273099
No vulnerabilities found.


proles/flaskr
https://github.com/proles/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 11:44:13.548165
No vulnerabilities found.


joeyespo/hello-redis-tasks
https://github.com/joeyespo/hello-redis-tasks
Entry file: hello-redis-tasks/hello_redis_tasks.py
Scanned: 2016-10-12 11:44:18.936738
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cemk/flask-expander
https://github.com/cemk/flask-expander
Entry file: flask-expander/expand.py
Scanned: 2016-10-12 11:44:21.140556
No vulnerabilities found.


pygraz/old-flask-website
https://github.com/pygraz/old-flask-website
Entry file: old-flask-website/pygraz_website/__init__.py
Scanned: 2016-10-12 11:44:43.216139
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

thomasballinger/Utok
https://github.com/thomasballinger/Utok
Entry file: Utok/webapp.py
Scanned: 2016-10-12 11:44:55.393617
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lcruz/Igualitos-appengine
https://github.com/lcruz/Igualitos-appengine
Entry file: Igualitos-appengine/config.py
Scanned: 2016-10-12 11:44:59.608222
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hettan/MyPortfolio
https://github.com/hettan/MyPortfolio
Entry file: MyPortfolio/web/myFlaskProject.py
Scanned: 2016-10-12 11:45:10.546097
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lcruz/igualitos
https://github.com/lcruz/igualitos
Entry file: igualitos/config.py
Scanned: 2016-10-12 11:45:11.924631
No vulnerabilities found.


agonzalezro/gplus-blog
https://github.com/agonzalezro/gplus-blog
Entry file: gplus-blog/gplusblog/__init__.py
Scanned: 2016-10-12 11:45:14.326097
No vulnerabilities found.


fwenzel/strassendeutsch
https://github.com/fwenzel/strassendeutsch
Entry file: strassendeutsch/woerterbuch/__init__.py
Scanned: 2016-10-12 11:45:22.858964
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lzyy/chat
https://github.com/lzyy/chat
Entry file: chat/src/app.py
Scanned: 2016-10-12 11:45:52.518876
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ferhensil/flask-example
https://github.com/ferhensil/flask-example
Entry file: flask-example/main.py
Scanned: 2016-10-12 11:45:54.005297
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jeanphix/flask-dashed-demo
https://github.com/jeanphix/flask-dashed-demo
Entry file: flask-dashed-demo/app.py
Scanned: 2016-10-12 11:46:08.774736
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kenkam/msgbrd
https://github.com/kenkam/msgbrd
Entry file: msgbrd/app.py
Scanned: 2016-10-12 11:46:12.143973
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

grigouze/flask-jenkins-radiator
https://github.com/grigouze/flask-jenkins-radiator
Entry file: flask-jenkins-radiator/radiator/radiator.py
Scanned: 2016-10-12 11:46:15.385954
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rduplain/flask-jquery-autosave-example
https://github.com/rduplain/flask-jquery-autosave-example
Entry file: flask-jquery-autosave-example/app.py
Scanned: 2016-10-12 11:46:19.951095
No vulnerabilities found.


kracekumar/Gummi
https://github.com/kracekumar/Gummi
Entry file: Gummi/gummi/tests/test.py
Scanned: 2016-10-12 11:46:27.518422
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ivoscc/qchaes
https://github.com/ivoscc/qchaes
Entry file: qchaes/runserver.py
Scanned: 2016-10-12 11:46:48.356326
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fdemmer/flask-principal
https://github.com/fdemmer/flask-principal
Entry file: flask-principal/tests/test_principal.py
Scanned: 2016-10-12 11:46:53.049136
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dasevilla/evernote-oauth-example
https://github.com/dasevilla/evernote-oauth-example
Entry file: evernote-oauth-example/webapp.py
Scanned: 2016-10-12 11:46:54.328780
No vulnerabilities found.


zeninthehome/flaskr
https://github.com/zeninthehome/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 11:47:09.149316
No vulnerabilities found.


joshfinnie/Flacker-News
https://github.com/joshfinnie/Flacker-News
Entry file: Flacker-News/flacker-news/app.py
Scanned: 2016-10-12 11:47:12.375265
No vulnerabilities found.
An Error occurred while scanning the repo: 'NoneType' object has no attribute 'label'

moneill/uber-flask
https://github.com/moneill/uber-flask
Entry file: uber-flask/uber.py
Scanned: 2016-10-12 11:47:18.150655
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: uber-flask/env/lib/python2.7/genericpath.py

nubela/radar-backend
https://github.com/nubela/radar-backend
Entry file: radar-backend/src/radar.py
Scanned: 2016-10-12 11:47:20.802894
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

TxSSC/the-questionator
https://github.com/TxSSC/the-questionator
Entry file: the-questionator/questionator/__init__.py
Scanned: 2016-10-12 11:47:23.926894
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

satonaoya/flask-epio-skelton
https://github.com/satonaoya/flask-epio-skelton
Entry file: flask-epio-skelton/app.py
Scanned: 2016-10-12 11:47:44.213852
No vulnerabilities found.


marksteve/bookmarks
https://github.com/marksteve/bookmarks
Entry file: bookmarks/bookmarks.py
Scanned: 2016-10-12 11:47:48.576422
No vulnerabilities found.


paradoxxxzero/polldance
https://github.com/paradoxxxzero/polldance
Entry file: polldance/dance.py
Scanned: 2016-10-12 11:47:52.839796
No vulnerabilities found.


flebel/Egami
https://github.com/flebel/Egami
Entry file: Egami/egami.py
Scanned: 2016-10-12 11:47:55.262516
No vulnerabilities found.


mitsuhiko/flask-pastebin
https://github.com/mitsuhiko/flask-pastebin
Entry file: flask-pastebin/pastebin.py
Scanned: 2016-10-12 11:48:09.636700
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

maxcountryman/flask-seasurf
https://github.com/maxcountryman/flask-seasurf
Entry file: flask-seasurf/test_seasurf.py
Scanned: 2016-10-12 11:48:15.408984
No vulnerabilities found.


maxcountryman/logmon
https://github.com/maxcountryman/logmon
Entry file: logmon/logmon/__init__.py
Scanned: 2016-10-12 11:48:21.403409
No vulnerabilities found.


hasgeek/coaster
https://github.com/hasgeek/coaster
Entry file: coaster/tests/test_render_with.py
Scanned: 2016-10-12 11:48:25.435980
No vulnerabilities found.


craigkerstiens/flask-helloworld
https://github.com/craigkerstiens/flask-helloworld
Entry file: flask-helloworld/app.py
Scanned: 2016-10-12 11:48:44.722068
No vulnerabilities found.


jarodl/flask-github
https://github.com/jarodl/flask-github
Entry file: flask-github/example/example.py
Scanned: 2016-10-12 11:48:49.907936
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

ahri/flask-mustache
https://github.com/ahri/flask-mustache
Entry file: flask-mustache/tests/test_mustache.py
Scanned: 2016-10-12 11:48:53.265139
No vulnerabilities found.


gears/flask-gears
https://github.com/gears/flask-gears
Entry file: flask-gears/example/app.py
Scanned: 2016-10-12 11:48:55.680087
No vulnerabilities found.


mitsuhiko/tugraz-flask-demo
https://github.com/mitsuhiko/tugraz-flask-demo
Entry file: tugraz-flask-demo/pastebin.py
Scanned: 2016-10-12 11:49:09.470460
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

mattoufoutu/flask-project-templates
https://github.com/mattoufoutu/flask-project-templates
Entry file: None
Scanned: 2016-10-12 11:49:13.793814
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/mattoufoutu/flask-project-templates.

svieira/Budget-Manager
https://github.com/svieira/Budget-Manager
Entry file: None
Scanned: 2016-10-12 11:49:24.361296
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/svieira/Budget-Manager.

solarmist/Flaskr
https://github.com/solarmist/Flaskr
Entry file: Flaskr/flaskr.py
Scanned: 2016-10-12 11:49:45.692776
No vulnerabilities found.


cybertoast/flask-router
https://github.com/cybertoast/flask-router
Entry file: flask-router/test_router.py
Scanned: 2016-10-12 11:49:53.521304
No vulnerabilities found.


srusskih/Flask-application-template
https://github.com/srusskih/Flask-application-template
Entry file: Flask-application-template/myapp/myapp.py
Scanned: 2016-10-12 11:50:00.408036
No vulnerabilities found.


Rootbuzz/heroku-basic-flask-app
https://github.com/Rootbuzz/heroku-basic-flask-app
Entry file: heroku-basic-flask-app/sso.py
Scanned: 2016-10-12 11:50:09.716698
No vulnerabilities found.


adgaudio/async-webapp---gevent--psycopg2--flask
https://github.com/adgaudio/async-webapp---gevent--psycopg2--flask
Entry file: async-webapp---gevent--psycopg2--flask/app.py
Scanned: 2016-10-12 11:50:14.080925
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

maxcountryman/chatter
https://github.com/maxcountryman/chatter
Entry file: chatter/chatter/__init__.py
Scanned: 2016-10-12 11:50:17.456391
No vulnerabilities found.


zeak/pyProx
https://github.com/zeak/pyProx
Entry file: pyProx/pyProx.py
Scanned: 2016-10-12 11:50:21.682947
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

subchild/iStockUtils
https://github.com/subchild/iStockUtils
Entry file: iStockUtils/istockutils.py
Scanned: 2016-10-12 11:50:25.114441
No vulnerabilities found.


tsoporan/read.list
https://github.com/tsoporan/read.list
Entry file: None
Scanned: 2016-10-12 11:50:46.484740
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/tsoporan/read.list.

pallets/flask
https://github.com/pallets/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 11:55:21.638541
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

gigq/flasktodo
https://github.com/gigq/flasktodo
Entry file: flasktodo/application.py
Scanned: 2016-10-12 11:55:23.492755
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flosch/simpleapi
https://github.com/flosch/simpleapi
Entry file: simpleapi/example_project/server/flask1/app.py
Scanned: 2016-10-12 11:55:25.915194
No vulnerabilities found.


codebykat/robotkitten
https://github.com/codebykat/robotkitten
Entry file: None
Scanned: 2016-10-12 11:55:44.905155
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/codebykat/robotkitten.

mitsuhiko/flask-oauth
https://github.com/mitsuhiko/flask-oauth
Entry file: flask-oauth/example/facebook.py
Scanned: 2016-10-12 11:56:18.994942
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-openid
https://github.com/mitsuhiko/flask-openid
Entry file: flask-openid/flask_openid.py
Scanned: 2016-10-12 11:56:19.983892
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

artisonian/flaskengine
https://github.com/artisonian/flaskengine
Entry file: flaskengine/flaskengine/__init__.py
Scanned: 2016-10-12 11:56:25.211555
No vulnerabilities found.


toomoresuch/template-gae-with-flask
https://github.com/toomoresuch/template-gae-with-flask
Entry file: template-gae-with-flask/application.py
Scanned: 2016-10-12 11:56:26.706709
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: template-gae-with-flask/flask.py

aljoscha/shot-o-matic
https://github.com/aljoscha/shot-o-matic
Entry file: shot-o-matic/shotomatic.py
Scanned: 2016-10-12 11:57:19.741620
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-sqlalchemy
https://github.com/mitsuhiko/flask-sqlalchemy
Entry file: flask-sqlalchemy/flask_sqlalchemy/__init__.py
Scanned: 2016-10-12 11:57:22.956761
No vulnerabilities found.


mitsuhiko/flask-fungiform
https://github.com/mitsuhiko/flask-fungiform
Entry file: flask-fungiform/examples/example.py
Scanned: 2016-10-12 11:57:25.310716
No vulnerabilities found.


fsouza/talks
https://github.com/fsouza/talks
Entry file: talks/flask/app.py
Scanned: 2016-10-12 11:57:26.295718
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

unbracketed/flapp
https://github.com/unbracketed/flapp
Entry file: flapp/flapp/project_template/application.py
Scanned: 2016-10-12 11:57:26.802105
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dcolish/flask-markdown
https://github.com/dcolish/flask-markdown
Entry file: flask-markdown/tests/test_markdown.py
Scanned: 2016-10-12 11:58:21.327935
No vulnerabilities found.


blossom/flask-gae-skeleton
https://github.com/blossom/flask-gae-skeleton
Entry file: flask-gae-skeleton/gae/main.py
Scanned: 2016-10-12 11:58:21.825770
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kijun/flask-methodhack
https://github.com/kijun/flask-methodhack
Entry file: flask-methodhack/flaskext/methodhack.py
Scanned: 2016-10-12 11:58:25.162199
No vulnerabilities found.


viniciusfs/pasted-flask
https://github.com/viniciusfs/pasted-flask
Entry file: pasted-flask/pasted.py
Scanned: 2016-10-12 11:58:26.506619
Vulnerability 1:
File: pasted-flask/pasted.py
 > User input at line 219, trigger word "form[": 
	hexdigest = calc_md5(request.form['code'])
Reassigned in: 
	File: pasted-flask/pasted.py
	 > Line 221: paste = query_db('select * from pasted where md5 = ?', [hexdigest],one=True)
	File: pasted-flask/pasted.py
	 > Line 225: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 231: paste_id = cur.lastrowid
	File: pasted-flask/pasted.py
	 > Line 232: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 234: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 203: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 207: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 209: ret_MAYBE_FUNCTION_NAME = render_template('form.html',original=paste)
	File: pasted-flask/pasted.py
	 > Line 213: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 217: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
File: pasted-flask/pasted.py
 > reaches line 229, trigger word "execute(": 
	cur = g.db.execute('insert into pasted (code, md5, viewed_at, parent) values (?, ?, ?, ?)', [request.form['code'], hexdigest, viewed_at, request.form['parent']])



Cornu/Brain
https://github.com/Cornu/Brain
Entry file: Brain/brain/__init__.py
Scanned: 2016-10-12 11:58:29.748422
Vulnerability 1:
File: Brain/brain/controllers/text.py
 > User input at line 43, trigger word "get(": 
	key = request.form.get('search')
File: Brain/brain/controllers/text.py
 > reaches line 44, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('/' + key)



jbochi/scrum-you
https://github.com/jbochi/scrum-you
Entry file: scrum-you/application.py
Scanned: 2016-10-12 11:58:47.319699
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

miracle2k/flask-assets
https://github.com/miracle2k/flask-assets
Entry file: flask-assets/tests/test_config.py
Scanned: 2016-10-12 11:59:23.945036
No vulnerabilities found.


jgumbley/flask-payment
https://github.com/jgumbley/flask-payment
Entry file: flask-payment/tests.py
Scanned: 2016-10-12 11:59:25.480635
No vulnerabilities found.


eugenkiss/Simblin
https://github.com/eugenkiss/Simblin
Entry file: Simblin/simblin/__init__.py
Scanned: 2016-10-12 11:59:25.994046
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jugyo/flask-gae-template
https://github.com/jugyo/flask-gae-template
Entry file: flask-gae-template/app.py
Scanned: 2016-10-12 11:59:27.822835
No vulnerabilities found.


swanson/flask-embedly
https://github.com/swanson/flask-embedly
Entry file: flask-embedly/example/app.py
Scanned: 2016-10-12 11:59:29.178735
No vulnerabilities found.


LightStyle/Python-Board
https://github.com/LightStyle/Python-Board
Entry file: Python-Board/src/index.py
Scanned: 2016-10-12 11:59:30.505459
No vulnerabilities found.


miku/flask-gae-stub
https://github.com/miku/flask-gae-stub
Entry file: flask-gae-stub/flask/app.py
Scanned: 2016-10-12 11:59:31.017526
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

derwiki/wordisms_flask
https://github.com/derwiki/wordisms_flask
Entry file: wordisms_flask/www/main.py
Scanned: 2016-10-12 11:59:47.548423
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flebel/cisco79xx_phone_directory
https://github.com/flebel/cisco79xx_phone_directory
Entry file: cisco79xx_phone_directory/cisco79xx_phone_directory.py
Scanned: 2016-10-12 12:00:21.889466
No vulnerabilities found.


jkossen/imposter
https://github.com/jkossen/imposter
Entry file: None
Scanned: 2016-10-12 12:00:27.163888
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/jkossen/imposter.

sublee/subleekr
https://github.com/sublee/subleekr
Entry file: subleekr/subleekr/app.py
Scanned: 2016-10-12 12:00:31.704163
No vulnerabilities found.


akhodakivskiy/flask
https://github.com/akhodakivskiy/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 12:00:33.939244
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

thadeusb/flask-cache
https://github.com/thadeusb/flask-cache
Entry file: flask-cache/examples/hello.py
Scanned: 2016-10-12 12:00:36.490418
No vulnerabilities found.


kamalgill/flask-appengine-template
https://github.com/kamalgill/flask-appengine-template
Entry file: flask-appengine-template/src/lib/flask/sessions.py
Scanned: 2016-10-12 12:00:41.763282
No vulnerabilities found.


sublee/flask-autoindex
https://github.com/sublee/flask-autoindex
Entry file: flask-autoindex/flask_autoindex/__init__.py
Scanned: 2016-10-12 12:00:50.414701
No vulnerabilities found.


ericmoritz/flaskcma
https://github.com/ericmoritz/flaskcma
Entry file: flaskcma/flaskcma/app.py
Scanned: 2016-10-12 12:01:22.804336
No vulnerabilities found.


indexofire/flasky
https://github.com/indexofire/flasky
Entry file: flasky/flasky/flask/app.py
Scanned: 2016-10-12 12:01:24.326954
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ericmoritz/flask-auth
https://github.com/ericmoritz/flask-auth
Entry file: flask-auth/flaskext/auth/tests/workflow.py
Scanned: 2016-10-12 12:01:28.762048
No vulnerabilities found.


sublee/flask-silk
https://github.com/sublee/flask-silk
Entry file: flask-silk/test.py
Scanned: 2016-10-12 12:01:35.726036
No vulnerabilities found.


proudlygeek/proudlygeek-blog
https://github.com/proudlygeek/proudlygeek-blog
Entry file: proudlygeek-blog/flask/app.py
Scanned: 2016-10-12 12:01:36.316101
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

JunKikuchi/flask-gae
https://github.com/JunKikuchi/flask-gae
Entry file: flask-gae/lib/flask/app.py
Scanned: 2016-10-12 12:01:36.810388
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

glenbot/flask-tweetfeed
https://github.com/glenbot/flask-tweetfeed
Entry file: flask-tweetfeed/tweetfeedapp.py
Scanned: 2016-10-12 12:01:38.022774
No vulnerabilities found.


fsouza/palestra-flask-2010-giran
https://github.com/fsouza/palestra-flask-2010-giran
Entry file: palestra-flask-2010-giran/projetos/projetos.py
Scanned: 2016-10-12 12:01:43.408100
No vulnerabilities found.


shiloa/flask-clean
https://github.com/shiloa/flask-clean
Entry file: flask-clean/app.py
Scanned: 2016-10-12 12:01:48.799094
No vulnerabilities found.


dag/flask-genshi
https://github.com/dag/flask-genshi
Entry file: flask-genshi/examples/flaskr/flaskr.py
Scanned: 2016-10-12 12:02:30.166471
No vulnerabilities found.


raliste/Flaskito
https://github.com/raliste/Flaskito
Entry file: Flaskito/flaskito/__init__.py
Scanned: 2016-10-12 12:02:34.352294
No vulnerabilities found.


mikewest/flask-pyplaceholder
https://github.com/mikewest/flask-pyplaceholder
Entry file: flask-pyplaceholder/generator.py
Scanned: 2016-10-12 12:02:39.092885
No vulnerabilities found.


whalesalad/arbesko-files
https://github.com/whalesalad/arbesko-files
Entry file: arbesko-files/files/__init__.py
Scanned: 2016-10-12 12:02:44.028999
No vulnerabilities found.


danjac/Flask-Script
https://github.com/danjac/Flask-Script
Entry file: Flask-Script/tests.py
Scanned: 2016-10-12 12:03:23.188540
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

danjac/Flask-WTF
https://github.com/danjac/Flask-WTF
Entry file: Flask-WTF/examples/recaptcha/app.py
Scanned: 2016-10-12 12:03:28.019595
No vulnerabilities found.


danjac/Flask-Mail
https://github.com/danjac/Flask-Mail
Entry file: Flask-Mail/tests.py
Scanned: 2016-10-12 12:03:33.039504
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cropd/crashkurs-flask
https://github.com/cropd/crashkurs-flask
Entry file: crashkurs-flask/flask/app.py
Scanned: 2016-10-12 12:03:37.019949
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hasgeek/github-hook
https://github.com/hasgeek/github-hook
Entry file: github-hook/github-hook.py
Scanned: 2016-10-12 12:03:38.305599
No vulnerabilities found.


pygloo/bewype-flask-controllers
https://github.com/pygloo/bewype-flask-controllers
Entry file: bewype-flask-controllers/bewype/flask/_app.py
Scanned: 2016-10-12 12:03:39.677816
No vulnerabilities found.


sontek-archive/redditor-stats
https://github.com/sontek-archive/redditor-stats
Entry file: redditor-stats/web.py
Scanned: 2016-10-12 12:03:44.581522
No vulnerabilities found.


Frozen-Flask/Frozen-Flask
https://github.com/Frozen-Flask/Frozen-Flask
Entry file: Frozen-Flask/flask_frozen/__init__.py
Scanned: 2016-10-12 12:04:23.724289
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

cobrateam/flask-mongoalchemy
https://github.com/cobrateam/flask-mongoalchemy
Entry file: flask-mongoalchemy/flask_mongoalchemy/__init__.py
Scanned: 2016-10-12 12:04:27.711280
No vulnerabilities found.


Flask-FlatPages/Flask-FlatPages
https://github.com/Flask-FlatPages/Flask-FlatPages
Entry file: Flask-FlatPages/tests/test_flask_flatpages.py
Scanned: 2016-10-12 12:04:29.235883
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

fsouza/flask-rest-example
https://github.com/fsouza/flask-rest-example
Entry file: flask-rest-example/library.py
Scanned: 2016-10-12 12:04:34.671436
Vulnerability 1:
File: flask-rest-example/library.py
 > User input at line 63, trigger word "form[": 
	name = request.form['name']
Reassigned in: 
	File: flask-rest-example/library.py
	 > Line 64: book = Book(id=2, name=name)
File: flask-rest-example/library.py
 > reaches line 65, trigger word "flash(": 
	flash('Book %s sucessful saved!' % book.name)



pilt/flask-versioned
https://github.com/pilt/flask-versioned
Entry file: flask-versioned/test_versioned.py
Scanned: 2016-10-12 12:04:36.067823
No vulnerabilities found.


tokibito/flask-hgwebcommit
https://github.com/tokibito/flask-hgwebcommit
Entry file: flask-hgwebcommit/hgwebcommit/__init__.py
Scanned: 2016-10-12 12:04:40.818594
Vulnerability 1:
File: flask-hgwebcommit/hgwebcommit/views.py
 > User input at line 97, trigger word ".data": 
	message = operation_repo(repo, form.data['operation'], form.data['files'], form.data['commit_message'])
File: flask-hgwebcommit/hgwebcommit/views.py
 > reaches line 98, trigger word "flash(": 
	flash(message)



Nassty/flask-gae
https://github.com/Nassty/flask-gae
Entry file: flask-gae/lib/flask/app.py
Scanned: 2016-10-12 12:04:43.327054
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sgk/BulkDM
https://github.com/sgk/BulkDM
Entry file: BulkDM/application.py
Scanned: 2016-10-12 12:04:49.821017
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sontek-archive/redditor-stats
https://github.com/sontek-archive/redditor-stats
Entry file: redditor-stats/web.py
Scanned: 2016-10-12 12:05:27.667744
No vulnerabilities found.


zzzsochi/Flask-Gravatar
https://github.com/zzzsochi/Flask-Gravatar
Entry file: Flask-Gravatar/tests/test_core.py
Scanned: 2016-10-12 12:05:35.701436
No vulnerabilities found.


dag/flask-zodb
https://github.com/dag/flask-zodb
Entry file: flask-zodb/flask_zodb.py
Scanned: 2016-10-12 12:05:36.205198
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

zen4ever/route53manager
https://github.com/zen4ever/route53manager
Entry file: route53manager/route53/__init__.py
Scanned: 2016-10-12 12:05:37.689483
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-kitchensink
https://github.com/mitsuhiko/flask-kitchensink
Entry file: flask-kitchensink/example-code/hello.py
Scanned: 2016-10-12 12:05:38.186808
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

eyeseast/flask-docviewer
https://github.com/eyeseast/flask-docviewer
Entry file: flask-docviewer/docviewer/app.py
Scanned: 2016-10-12 12:05:40.391480
No vulnerabilities found.


dag/flask-attest
https://github.com/dag/flask-attest
Entry file: flask-attest/tests.py
Scanned: 2016-10-12 12:05:43.897677
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

ekalinin/flask-noextref
https://github.com/ekalinin/flask-noextref
Entry file: flask-noextref/test_noextref.py
Scanned: 2016-10-12 12:05:51.246056
No vulnerabilities found.


teohm/flitter
https://github.com/teohm/flitter
Entry file: flitter/flitter/__init__.py
Scanned: 2016-10-12 12:06:31.682444
Vulnerability 1:
File: flitter/flitter/controllers/user.py
 > User input at line 19, trigger word "form[": 
	username = request.form['username']
Reassigned in: 
	File: flitter/flitter/controllers/user.py
	 > Line 24: session['user'] = username
	File: flitter/flitter/controllers/user.py
	 > Line 26: ret_MAYBE_FUNCTION_NAME = redirect(url_for('entry.entries',username=username))
	File: flitter/flitter/controllers/user.py
	 > Line 30: ret_MAYBE_FUNCTION_NAME = render_template('signup.html',error=error)
	File: flitter/flitter/controllers/user.py
	 > Line 15: ret_MAYBE_FUNCTION_NAME = redirect_to_user_page()
File: flitter/flitter/controllers/user.py
 > reaches line 25, trigger word "flash(": 
	flash('Welcome, {0}.'.format(username))



aaront/calcmymarks2
https://github.com/aaront/calcmymarks2
Entry file: calcmymarks2/main.py
Scanned: 2016-10-12 12:06:35.424739
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-feedback
https://github.com/mitsuhiko/flask-feedback
Entry file: flask-feedback/feedback.py
Scanned: 2016-10-12 12:06:38.501265
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

wilsaj/flask-admin-old
https://github.com/wilsaj/flask-admin-old
Entry file: flask-admin-old/test_admin.py
Scanned: 2016-10-12 12:06:52.840414
No vulnerabilities found.


leandrosilva/flaskito
https://github.com/leandrosilva/flaskito
Entry file: flaskito/src/flaskito.py
Scanned: 2016-10-12 12:06:53.348744
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/Flask-API-Server
https://github.com/marchon/Flask-API-Server
Entry file: Flask-API-Server/apiserver/tests/app.py
Scanned: 2016-10-12 12:06:54.656291
No vulnerabilities found.


kapilreddy/Shabda-Sangraha
https://github.com/kapilreddy/Shabda-Sangraha
Entry file: Shabda-Sangraha/dict.py
Scanned: 2016-10-12 12:07:25.723386
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tooxie/flask-syrinx
https://github.com/tooxie/flask-syrinx
Entry file: flask-syrinx/syrinx/__init__.py
Scanned: 2016-10-12 12:07:28.222070
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joshourisman/flask-shortly
https://github.com/joshourisman/flask-shortly
Entry file: flask-shortly/shortly/__init__.py
Scanned: 2016-10-12 12:07:36.155691
No vulnerabilities found.


jamiltron/fitgen
https://github.com/jamiltron/fitgen
Entry file: fitgen/fitgen.py
Scanned: 2016-10-12 12:07:39.634963
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tomviner/Flask-Name-that-actor-or-movie
https://github.com/tomviner/Flask-Name-that-actor-or-movie
Entry file: Flask-Name-that-actor-or-movie/namer.py
Scanned: 2016-10-12 12:07:54.619638
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/flylons
https://github.com/marchon/flylons
Entry file: flylons/application/__init__.py
Scanned: 2016-10-12 12:07:56.149703
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/checkinmapper
https://github.com/marchon/checkinmapper
Entry file: checkinmapper/checkinmapper.py
Scanned: 2016-10-12 12:08:26.749423
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

comfuture/simplesite
https://github.com/comfuture/simplesite
Entry file: simplesite/simplesite/core.py
Scanned: 2016-10-12 12:08:28.235760
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

zachwill/flask-engine
https://github.com/zachwill/flask-engine
Entry file: flask-engine/libs/flask/sessions.py
Scanned: 2016-10-12 12:08:37.851052
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

spantaleev/flask-sijax
https://github.com/spantaleev/flask-sijax
Entry file: flask-sijax/examples/comet.py
Scanned: 2016-10-12 12:08:40.342604
No vulnerabilities found.


utahta/Flask-MVC-Pattern
https://github.com/utahta/Flask-MVC-Pattern
Entry file: Flask-MVC-Pattern/main.py
Scanned: 2016-10-12 12:08:41.555144
No vulnerabilities found.


jzempel/flask-exceptional
https://github.com/jzempel/flask-exceptional
Entry file: flask-exceptional/flask_exceptional.py
Scanned: 2016-10-12 12:08:55.053773
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

qsnake/flask
https://github.com/qsnake/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 12:08:57.728894
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

joeyespo/flask-scaffold
https://github.com/joeyespo/flask-scaffold
Entry file: flask-scaffold/[appname].py
Scanned: 2016-10-12 12:09:27.257834
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

iwebhosting/collectd-flask
https://github.com/iwebhosting/collectd-flask
Entry file: collectd-flask/collectdflask.py
Scanned: 2016-10-12 12:09:29.609269
No vulnerabilities found.


yxm0513/flask-ims
https://github.com/yxm0513/flask-ims
Entry file: flask-ims/flask/sessions.py
Scanned: 2016-10-12 12:09:32.164454
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fay/flask-skeleton
https://github.com/fay/flask-skeleton
Entry file: flask-skeleton/app/__init__.py
Scanned: 2016-10-12 12:09:39.247408
No vulnerabilities found.


joshourisman/flask-beans
https://github.com/joshourisman/flask-beans
Entry file: flask-beans/beans.py
Scanned: 2016-10-12 12:09:40.567081
No vulnerabilities found.


jjinux/pyteladventure
https://github.com/jjinux/pyteladventure
Entry file: pyteladventure/pyteladventure/__init__.py
Scanned: 2016-10-12 12:09:41.105620
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.List'>)

mchambliss/flask
https://github.com/mchambliss/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 12:09:58.381620
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

robi42/backbone-flask
https://github.com/robi42/backbone-flask
Entry file: backbone-flask/app.py
Scanned: 2016-10-12 12:10:38.903926
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

suzanshakya/flask-clevercss
https://github.com/suzanshakya/flask-clevercss
Entry file: flask-clevercss/example/runserver.py
Scanned: 2016-10-12 12:10:41.436829
No vulnerabilities found.


joshfinnie/Flask-shrtn
https://github.com/joshfinnie/Flask-shrtn
Entry file: Flask-shrtn/Flask-shrtn.py
Scanned: 2016-10-12 12:10:41.974436
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tomatohater/goonhilly
https://github.com/tomatohater/goonhilly
Entry file: goonhilly/goonhilly.py
Scanned: 2016-10-12 12:10:57.755633
No vulnerabilities found.


jmoiron/jmoiron.net
https://github.com/jmoiron/jmoiron.net
Entry file: None
Scanned: 2016-10-12 12:10:58.301544
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

fzuslide/video_new
https://github.com/fzuslide/video_new
Entry file: video_new/application.py
Scanned: 2016-10-12 12:11:29.589033
No vulnerabilities found.


tomatohater/lydon
https://github.com/tomatohater/lydon
Entry file: lydon/lydon/__init__.py
Scanned: 2016-10-12 12:11:30.941624
No vulnerabilities found.


williamratcliff/django-feedback
https://github.com/williamratcliff/django-feedback
Entry file: django-feedback/feedback.py
Scanned: 2016-10-12 12:11:40.861992
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joelbm24/blog
https://github.com/joelbm24/blog
Entry file: blog/flaskr.py
Scanned: 2016-10-12 12:11:42.348631
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hoprocker/mylons
https://github.com/hoprocker/mylons
Entry file: mylons/lib/python2.5/site-packages/Flask-0.6.1-py2.5.egg/flask/app.py
Scanned: 2016-10-12 12:11:56.920396
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

crisisking/bsg-raffle
https://github.com/crisisking/bsg-raffle
Entry file: bsg-raffle/raffle.py
Scanned: 2016-10-12 12:11:58.259096
Vulnerability 1:
File: bsg-raffle/raffle.py
 > User input at line 39, trigger word "form[": 
	user_id = int(request.form['user_id'])
File: bsg-raffle/raffle.py
 > reaches line 42, trigger word "execute(": 
	g.db.execute('INSERT INTO winners(participant_id, prize_name)
            VALUES (?, ?)', (user_id, prize))

Vulnerability 2:
File: bsg-raffle/raffle.py
 > User input at line 40, trigger word "form[": 
	prize = request.form['prize']
Reassigned in: 
	File: bsg-raffle/raffle.py
	 > Line 49: ret_MAYBE_FUNCTION_NAME = render_template('winner_added.html',name=username[0], prize=prize)
File: bsg-raffle/raffle.py
 > reaches line 42, trigger word "execute(": 
	g.db.execute('INSERT INTO winners(participant_id, prize_name)
            VALUES (?, ?)', (user_id, prize))

Vulnerability 3:
File: bsg-raffle/raffle.py
 > User input at line 66, trigger word "form[": 
	username = request.form['username']
File: bsg-raffle/raffle.py
 > reaches line 68, trigger word "execute(": 
	g.db.execute('INSERT INTO participants(name)
                VALUES (?)', (username))

Vulnerability 4:
File: bsg-raffle/raffle.py
 > User input at line 66, trigger word "form[": 
	username = request.form['username']
File: bsg-raffle/raffle.py
 > reaches line 70, trigger word "flash(": 
	flash('%s added successfully!' % username)



adamgreig/pyautopull
https://github.com/adamgreig/pyautopull
Entry file: pyautopull/pyautopull.py
Scanned: 2016-10-12 12:11:59.453870
No vulnerabilities found.


sean-/flask-skeleton
https://github.com/sean-/flask-skeleton
Entry file: None
Scanned: 2016-10-12 12:12:31.989693
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/sean-/flask-skeleton.

Runscope/httpbin
https://github.com/Runscope/httpbin
Entry file: httpbin/httpbin/filters.py
Scanned: 2016-10-12 12:12:33.536901
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.FunctionDef'>)

hasgeek/flask-lastuser
https://github.com/hasgeek/flask-lastuser
Entry file: flask-lastuser/tests/test_mergeuser.py
Scanned: 2016-10-12 12:12:38.510543
No vulnerabilities found.


BooBSD/flask-odesk
https://github.com/BooBSD/flask-odesk
Entry file: flask-odesk/tests.py
Scanned: 2016-10-12 12:12:39.997657
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cool-shark/redimon
https://github.com/cool-shark/redimon
Entry file: redimon/src/redimon/app.py
Scanned: 2016-10-12 12:12:42.408167
No vulnerabilities found.


pcsanwald/flask_site
https://github.com/pcsanwald/flask_site
Entry file: flask_site/mysite.py
Scanned: 2016-10-12 12:12:57.842988
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

suzanshakya/flask-clevercss
https://github.com/suzanshakya/flask-clevercss
Entry file: flask-clevercss/example/runserver.py
Scanned: 2016-10-12 12:13:00.224529
No vulnerabilities found.


dag/flask-sassy
https://github.com/dag/flask-sassy
Entry file: flask-sassy/tests/__init__.py
Scanned: 2016-10-12 12:13:30.485664
No vulnerabilities found.


charlieevett/jiffy-portal
https://github.com/charlieevett/jiffy-portal
Entry file: jiffy-portal/portal/app.py
Scanned: 2016-10-12 12:13:31.793183
No vulnerabilities found.


tomekwojcik/Flask-Module-Static-Files
https://github.com/tomekwojcik/Flask-Module-Static-Files
Entry file: Flask-Module-Static-Files/stest/__init__.py
Scanned: 2016-10-12 12:13:35.402936
No vulnerabilities found.


justjkk/dotpath
https://github.com/justjkk/dotpath
Entry file: dotpath/run.py
Scanned: 2016-10-12 12:13:37.904416
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

almet/semantic-bookclub
https://github.com/almet/semantic-bookclub
Entry file: semantic-bookclub/app/web.py
Scanned: 2016-10-12 12:13:41.579333
Vulnerability 1:
File: semantic-bookclub/app/web.py
 > User input at line 81, trigger word ".data": 
	book_title = dict(self.book.choices)[self.book.data]
File: semantic-bookclub/app/web.py
 > reaches line 82, trigger word "flash(": 
	flash('%s have successfully borrowed %s' % (self.borrower.data, book_title))

Vulnerability 2:
File: semantic-bookclub/app/web.py
 > User input at line 101, trigger word ".data": 
	member = Member.get_by(foaf_givenName=self.member.data).one()
File: semantic-bookclub/app/web.py
 > reaches line 105, trigger word "flash(": 
	flash('%s now owns %s' % (member.foaf_givenName.first, book.dcterms_title.first))

Vulnerability 3:
File: semantic-bookclub/app/web.py
 > User input at line 102, trigger word ".data": 
	book = Book.get_by(dcterms_identifier=self.book.data).one()
File: semantic-bookclub/app/web.py
 > reaches line 105, trigger word "flash(": 
	flash('%s now owns %s' % (member.foaf_givenName.first, book.dcterms_title.first))



t9md/snippy
https://github.com/t9md/snippy
Entry file: snippy/snippy.py
Scanned: 2016-10-12 12:13:43.532933
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

stehem/Tywna
https://github.com/stehem/Tywna
Entry file: Tywna/application/__init__.py
Scanned: 2016-10-12 12:14:02.079328
No vulnerabilities found.


hoprocker/mylons
https://github.com/hoprocker/mylons
Entry file: mylons/lib/python2.5/site-packages/Flask-0.6.1-py2.5.egg/flask/app.py
Scanned: 2016-10-12 12:14:02.620172
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

maxcountryman/bitpit-https-bridge
https://github.com/maxcountryman/bitpit-https-bridge
Entry file: bitpit-https-bridge/httpstobitpit/__init__.py
Scanned: 2016-10-12 12:14:03.831115
No vulnerabilities found.


maxcountryman/flask-bcrypt
https://github.com/maxcountryman/flask-bcrypt
Entry file: flask-bcrypt/flask_bcrypt.py
Scanned: 2016-10-12 12:14:33.558663
No vulnerabilities found.


kennethreitz-archive/flask-rest
https://github.com/kennethreitz-archive/flask-rest
Entry file: flask-rest/haystack/core.py
Scanned: 2016-10-12 12:14:38.504566
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tdryer/flask-forum
https://github.com/tdryer/flask-forum
Entry file: flask-forum/app.py
Scanned: 2016-10-12 12:14:41.853407
Vulnerability 1:
File: flask-forum/app.py
 > User input at line 124, trigger word ".data": 
	new_topic_id = post_topic(form.subject.data, form.content.data)
Reassigned in: 
	File: flask-forum/app.py
	 > Line 127: ret_MAYBE_FUNCTION_NAME = render_template('newtopic.html',form=form)
File: flask-forum/app.py
 > reaches line 126, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('/topic/' + new_topic_id)

Vulnerability 2:
File: flask-forum/app.py
 > User input at line 196, trigger word ".data": 
	username = form.username.data
File: flask-forum/app.py
 > reaches line 199, trigger word "execute(": 
	g.db.execute('INSERT INTO users (username, password_hash)                 values (?, ?)', [username, pw_hash])

Vulnerability 3:
File: flask-forum/app.py
 > User input at line 197, trigger word ".data": 
	password = form.password1.data
Reassigned in: 
	File: flask-forum/app.py
	 > Line 198: pw_hash = hashpw(password, gensalt())
File: flask-forum/app.py
 > reaches line 199, trigger word "execute(": 
	g.db.execute('INSERT INTO users (username, password_hash)                 values (?, ?)', [username, pw_hash])



dqminh/flask-mongoobject
https://github.com/dqminh/flask-mongoobject
Entry file: flask-mongoobject/examples_hello.py
Scanned: 2016-10-12 12:14:42.353361
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

gmonnerat/flask-sandbox
https://github.com/gmonnerat/flask-sandbox
Entry file: flask-sandbox/hello/hello.py
Scanned: 2016-10-12 12:14:44.539449
No vulnerabilities found.


DarkSector/wombat
https://github.com/DarkSector/wombat
Entry file: wombat/wombatdb.py
Scanned: 2016-10-12 12:14:58.049244
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lOlIl/Flask---Local-election
https://github.com/lOlIl/Flask---Local-election
Entry file: Flask---Local-election/app.py
Scanned: 2016-10-12 12:15:03.596872
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

paulftw/appengine-flask-template
https://github.com/paulftw/appengine-flask-template
Entry file: appengine-flask-template/app/app.py
Scanned: 2016-10-12 12:15:05.145597
No vulnerabilities found.


flores/aquadoc
https://github.com/flores/aquadoc
Entry file: aquadoc/aquadoc.py
Scanned: 2016-10-12 12:15:33.031328
No vulnerabilities found.


jorgeatorres/cotufa
https://github.com/jorgeatorres/cotufa
Entry file: cotufa/cotufa.py
Scanned: 2016-10-12 12:15:35.553712
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mbr/flask-kvsession
https://github.com/mbr/flask-kvsession
Entry file: flask-kvsession/tests/conftest.py
Scanned: 2016-10-12 12:15:44.525849
No vulnerabilities found.


radekstepan/Flask-Skeleton-App
https://github.com/radekstepan/Flask-Skeleton-App
Entry file: Flask-Skeleton-App/flask_app.py
Scanned: 2016-10-12 12:15:59.342887
No vulnerabilities found.


utahta/flask-on-fluxflex
https://github.com/utahta/flask-on-fluxflex
Entry file: flask-on-fluxflex/app/__init__.py
Scanned: 2016-10-12 12:16:05.171936
No vulnerabilities found.


femmerling/brunch-flask-gae-skeleton
https://github.com/femmerling/brunch-flask-gae-skeleton
Entry file: brunch-flask-gae-skeleton/gae/main.py
Scanned: 2016-10-12 12:16:30.806499
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

amcameron/gchartsdemo
https://github.com/amcameron/gchartsdemo
Entry file: gchartsdemo/charts.py
Scanned: 2016-10-12 12:16:33.244522
No vulnerabilities found.


bagyr/flaskPage
https://github.com/bagyr/flaskPage
Entry file: flaskPage/__init__.py
Scanned: 2016-10-12 12:16:36.447848
No vulnerabilities found.


sbook/flask-script
https://github.com/sbook/flask-script
Entry file: flask-script/tests.py
Scanned: 2016-10-12 12:16:43.917209
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joemarct/flask-gae-app
https://github.com/joemarct/flask-gae-app
Entry file: flask-gae-app/flask/app.py
Scanned: 2016-10-12 12:16:45.461156
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

Bhagyashree-Mandora/The-Python-Task
https://github.com/Bhagyashree-Mandora/The-Python-Task
Entry file: The-Python-Task/main.py
Scanned: 2016-10-12 12:16:58.963418
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

piratesolutions/ps-website
https://github.com/piratesolutions/ps-website
Entry file: ps-website/app.py
Scanned: 2016-10-12 12:17:04.451166
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

samrat/blogengine
https://github.com/samrat/blogengine
Entry file: blogengine/blogengine.py
Scanned: 2016-10-12 12:17:04.952873
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

TimFletcher/cmprss
https://github.com/TimFletcher/cmprss
Entry file: cmprss/cmprss.py
Scanned: 2016-10-12 12:17:31.496648
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

andyvanee/mappy
https://github.com/andyvanee/mappy
Entry file: mappy/mappy.py
Scanned: 2016-10-12 12:17:33.033407
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

barnslig/foreveralonebook
https://github.com/barnslig/foreveralonebook
Entry file: foreveralonebook/foreveralonebook.py
Scanned: 2016-10-12 12:17:40.966467
Vulnerability 1:
File: foreveralonebook/foreveralonebook.py
 > User input at line 47, trigger word "form[": 
	entry = escape(request.form['entry'])
File: foreveralonebook/foreveralonebook.py
 > reaches line 57, trigger word "execute(": 
	g.db.cur.execute('INSERT INTO feabook_posts (u_id, content) VALUES ({0}, '{1}');'.format(session['u_id'], entry))

Vulnerability 2:
File: foreveralonebook/foreveralonebook.py
 > User input at line 113, trigger word "form[": 
	password = hashlib.sha1(request.form['new_pw']).hexdigest()
File: foreveralonebook/foreveralonebook.py
 > reaches line 115, trigger word "execute(": 
	g.db.cur.execute('UPDATE feabook_user SET password = '{0}' WHERE id = '{1}';'.format(password, session['u_id']))

Vulnerability 3:
File: foreveralonebook/foreveralonebook.py
 > User input at line 151, trigger word "form[": 
	username = escape(request.form['username'])
Reassigned in: 
	File: foreveralonebook/foreveralonebook.py
	 > Line 171: session['username'] = username
	File: foreveralonebook/foreveralonebook.py
	 > Line 172: session['u_id'] = rows[0][0]
File: foreveralonebook/foreveralonebook.py
 > reaches line 157, trigger word "execute(": 
	g.db.cur.execute('SELECT username FROM feabook_user WHERE username = '{0}';'.format(username))

Vulnerability 4:
File: foreveralonebook/foreveralonebook.py
 > User input at line 151, trigger word "form[": 
	username = escape(request.form['username'])
Reassigned in: 
	File: foreveralonebook/foreveralonebook.py
	 > Line 171: session['username'] = username
	File: foreveralonebook/foreveralonebook.py
	 > Line 172: session['u_id'] = rows[0][0]
File: foreveralonebook/foreveralonebook.py
 > reaches line 164, trigger word "execute(": 
	g.db.cur.execute('INSERT INTO feabook_user (username, password) VALUES ('{0}', '{1}');'.format(username, password))

Vulnerability 5:
File: foreveralonebook/foreveralonebook.py
 > User input at line 152, trigger word "form[": 
	password = hashlib.sha1(request.form['password']).hexdigest()
File: foreveralonebook/foreveralonebook.py
 > reaches line 164, trigger word "execute(": 
	g.db.cur.execute('INSERT INTO feabook_user (username, password) VALUES ('{0}', '{1}');'.format(username, password))

Vulnerability 6:
File: foreveralonebook/foreveralonebook.py
 > User input at line 151, trigger word "form[": 
	username = escape(request.form['username'])
Reassigned in: 
	File: foreveralonebook/foreveralonebook.py
	 > Line 171: session['username'] = username
	File: foreveralonebook/foreveralonebook.py
	 > Line 172: session['u_id'] = rows[0][0]
File: foreveralonebook/foreveralonebook.py
 > reaches line 169, trigger word "execute(": 
	g.db.cur.execute('SELECT id, username FROM feabook_user WHERE username = '{0}';'.format(username))

Vulnerability 7:
File: foreveralonebook/foreveralonebook.py
 > User input at line 193, trigger word "form[": 
	username = escape(request.form['username'])
Reassigned in: 
	File: foreveralonebook/foreveralonebook.py
	 > Line 222: session['username'] = username
	File: foreveralonebook/foreveralonebook.py
	 > Line 223: session['u_id'] = rows[0][0]
File: foreveralonebook/foreveralonebook.py
 > reaches line 197, trigger word "execute(": 
	g.db.cur.execute('SELECT id, username, password FROM feabook_user WHERE username = '{0}' AND password = '{1}';'.format(username, password))

Vulnerability 8:
File: foreveralonebook/foreveralonebook.py
 > User input at line 194, trigger word "form[": 
	password = hashlib.sha1(request.form['password']).hexdigest()
File: foreveralonebook/foreveralonebook.py
 > reaches line 197, trigger word "execute(": 
	g.db.cur.execute('SELECT id, username, password FROM feabook_user WHERE username = '{0}' AND password = '{1}';'.format(username, password))



geek22com/referral_dashboard_engine
https://github.com/geek22com/referral_dashboard_engine
Entry file: referral_dashboard_engine/heymoose/__init__.py
Scanned: 2016-10-12 12:17:42.492704
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dqminh/flask-lettuce
https://github.com/dqminh/flask-lettuce
Entry file: flask-lettuce/test.py
Scanned: 2016-10-12 12:17:59.097593
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

radekstepan/FlaskBudget
https://github.com/radekstepan/FlaskBudget
Entry file: FlaskBudget/budget.py
Scanned: 2016-10-12 12:18:05.068596
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

UfSoft/Flask-MenuBuilder
https://github.com/UfSoft/Flask-MenuBuilder
Entry file: Flask-MenuBuilder/tests/test_menuitem.py
Scanned: 2016-10-12 12:18:32.528617
No vulnerabilities found.


gregglind/flask-tool
https://github.com/gregglind/flask-tool
Entry file: flask-tool/flasktool/console.py
Scanned: 2016-10-12 12:18:33.025150
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kblin/flask-downloader
https://github.com/kblin/flask-downloader
Entry file: flask-downloader/tests.py
Scanned: 2016-10-12 12:18:37.533900
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

maxcountryman/flog
https://github.com/maxcountryman/flog
Entry file: flog/flog/__init__.py
Scanned: 2016-10-12 12:18:41.118091
No vulnerabilities found.


sublee/Flask-Handler
https://github.com/sublee/Flask-Handler
Entry file: None
Scanned: 2016-10-12 12:18:43.369480
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/sublee/Flask-Handler.

Ramblurr/pyqdb
https://github.com/Ramblurr/pyqdb
Entry file: pyqdb/src/pyqdb.py
Scanned: 2016-10-12 12:18:59.829996
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

zackster/DijScrape--flask-rewrite-
https://github.com/zackster/DijScrape--flask-rewrite-
Entry file: DijScrape--flask-rewrite-/dijscrape.py
Scanned: 2016-10-12 12:19:06.204963
No vulnerabilities found.


asenchi/pomp
https://github.com/asenchi/pomp
Entry file: pomp/pomp/pomp.py
Scanned: 2016-10-12 12:19:07.426265
No vulnerabilities found.


tshirtman/snakenest
https://github.com/tshirtman/snakenest
Entry file: snakenest/main.py
Scanned: 2016-10-12 12:19:32.915416
No vulnerabilities found.


jvreeland/Python-Web-Service-for-Android-GMaps-AsyncTask-Demo
https://github.com/jvreeland/Python-Web-Service-for-Android-GMaps-AsyncTask-Demo
Entry file: Python-Web-Service-for-Android-GMaps-AsyncTask-Demo/gmaps.py
Scanned: 2016-10-12 12:19:33.425214
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: Python-Web-Service-for-Android-GMaps-AsyncTask-Demo/env/lib/python2.7/genericpath.py

triposo/geocodecache
https://github.com/triposo/geocodecache
Entry file: geocodecache/geocodecache.py
Scanned: 2016-10-12 12:19:37.940476
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

toastwaffle/ToDoQuick
https://github.com/toastwaffle/ToDoQuick
Entry file: ToDoQuick/todoquick.py
Scanned: 2016-10-12 12:19:40.460543
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

coleifer/flask-peewee
https://github.com/coleifer/flask-peewee
Entry file: flask-peewee/example/app.py
Scanned: 2016-10-12 12:19:49.036506
Vulnerability 1:
File: flask-peewee/example/admin.py
 > User input at line 27, trigger word "get(": 
	next = request.form.get('next') or self.dashboard_url()
File: flask-peewee/example/admin.py
 > reaches line 28, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect(next)



jeanphix/Flask-Dashed
https://github.com/jeanphix/Flask-Dashed
Entry file: Flask-Dashed/examples/sqlalchemy_backend.py
Scanned: 2016-10-12 12:19:52.247429
No vulnerabilities found.


jarus/flask-mongokit
https://github.com/jarus/flask-mongokit
Entry file: flask-mongokit/tests/test_base.py
Scanned: 2016-10-12 12:20:00.749606
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

namlook/flask-apibee
https://github.com/namlook/flask-apibee
Entry file: flask-apibee/example/app.py
Scanned: 2016-10-12 12:20:06.771773
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

voluntas/heroku-template-flask
https://github.com/voluntas/heroku-template-flask
Entry file: heroku-template-flask/snowflake/__init__.py
Scanned: 2016-10-12 12:20:33.367822
No vulnerabilities found.


Deepwalker/Flask-Bundle
https://github.com/Deepwalker/Flask-Bundle
Entry file: Flask-Bundle/samples/simple.py
Scanned: 2016-10-12 12:20:40.819091
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sunlightlabs/flask-districtoffices
https://github.com/sunlightlabs/flask-districtoffices
Entry file: flask-districtoffices/districtoffices.py
Scanned: 2016-10-12 12:20:44.568020
No vulnerabilities found.


quanticle/flask_blog
https://github.com/quanticle/flask_blog
Entry file: flask_blog/blog.py
Scanned: 2016-10-12 12:21:01.019698
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

garrettr/haps
https://github.com/garrettr/haps
Entry file: haps/quickstart.py
Scanned: 2016-10-12 12:21:06.535766
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dsully/sitter
https://github.com/dsully/sitter
Entry file: sitter/sitter/__init__.py
Scanned: 2016-10-12 12:21:32.540916
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ahri/nodeblog
https://github.com/ahri/nodeblog
Entry file: nodeblog/blog.py
Scanned: 2016-10-12 12:21:34.040130
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

maxcountryman/celeb
https://github.com/maxcountryman/celeb
Entry file: celeb/celeb/__init__.py
Scanned: 2016-10-12 12:21:38.533610
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/PO
https://github.com/marchon/PO
Entry file: PO/main.py
Scanned: 2016-10-12 12:21:41.755232
No vulnerabilities found.


slok/xlarrakoetxeaorg
https://github.com/slok/xlarrakoetxeaorg
Entry file: xlarrakoetxeaorg/mysite/blog/__init__.py
Scanned: 2016-10-12 12:21:45.942104
No vulnerabilities found.


boboppie/pyLiftOver
https://github.com/boboppie/pyLiftOver
Entry file: pyLiftOver/flask/lift-over-app.py
Scanned: 2016-10-12 12:21:46.427439
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

no0p/homepage
https://github.com/no0p/homepage
Entry file: homepage/site.py
Scanned: 2016-10-12 12:21:54.888876
No vulnerabilities found.


tjosten/python-push
https://github.com/tjosten/python-push
Entry file: python-push/push.py
Scanned: 2016-10-12 12:22:02.119525
No vulnerabilities found.


Joshkunz/PyChannel
https://github.com/Joshkunz/PyChannel
Entry file: PyChannel/PyChannel/__init__.py
Scanned: 2016-10-12 12:22:06.623856
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cbess/ytlinker
https://github.com/cbess/ytlinker
Entry file: ytlinker/flask/app.py
Scanned: 2016-10-12 12:22:07.113311
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

openshift/flask-example
https://github.com/openshift/flask-example
Entry file: flask-example/main.py
Scanned: 2016-10-12 12:22:34.352514
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

wasabi0522/flaskr
https://github.com/wasabi0522/flaskr
Entry file: flaskr/flaskr/__init__.py
Scanned: 2016-10-12 12:22:48.859681
No vulnerabilities found.


amehta/Flaskly
https://github.com/amehta/Flaskly
Entry file: Flaskly/flaskly.py
Scanned: 2016-10-12 12:23:02.614207
Vulnerability 1:
File: Flaskly/flaskly.py
 > User input at line 73, trigger word "form[": 
	url = request.form['long_url']
Reassigned in: 
	File: Flaskly/flaskly.py
	 > Line 74: short = pickShortUrl(url)
File: Flaskly/flaskly.py
 > reaches line 75, trigger word "flash(": 
	flash('Short Url http:/localhost/' + short)



fyears/flaskr-redis
https://github.com/fyears/flaskr-redis
Entry file: flaskr-redis/app.py
Scanned: 2016-10-12 12:23:08.424484
No vulnerabilities found.


Jc2k/flask-example
https://github.com/Jc2k/flask-example
Entry file: flask-example/main.py
Scanned: 2016-10-12 12:23:32.967891
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

brainTrain/flasktest
https://github.com/brainTrain/flasktest
Entry file: flasktest/hello.py
Scanned: 2016-10-12 12:23:36.678545
No vulnerabilities found.


proles/flaskr
https://github.com/proles/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 12:23:40.017868
No vulnerabilities found.


joeyespo/hello-redis-tasks
https://github.com/joeyespo/hello-redis-tasks
Entry file: hello-redis-tasks/hello_redis_tasks.py
Scanned: 2016-10-12 12:23:41.529599
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cemk/flask-expander
https://github.com/cemk/flask-expander
Entry file: flask-expander/expand.py
Scanned: 2016-10-12 12:23:45.860918
No vulnerabilities found.


pygraz/old-flask-website
https://github.com/pygraz/old-flask-website
Entry file: old-flask-website/pygraz_website/__init__.py
Scanned: 2016-10-12 12:23:47.374795
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

thomasballinger/Utok
https://github.com/thomasballinger/Utok
Entry file: Utok/webapp.py
Scanned: 2016-10-12 12:24:07.803901
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lcruz/Igualitos-appengine
https://github.com/lcruz/Igualitos-appengine
Entry file: Igualitos-appengine/config.py
Scanned: 2016-10-12 12:24:08.307123
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hettan/MyPortfolio
https://github.com/hettan/MyPortfolio
Entry file: MyPortfolio/web/myFlaskProject.py
Scanned: 2016-10-12 12:24:33.827218
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lcruz/igualitos
https://github.com/lcruz/igualitos
Entry file: igualitos/config.py
Scanned: 2016-10-12 12:24:36.147290
No vulnerabilities found.


agonzalezro/gplus-blog
https://github.com/agonzalezro/gplus-blog
Entry file: gplus-blog/gplusblog/__init__.py
Scanned: 2016-10-12 12:24:40.473477
No vulnerabilities found.


fwenzel/strassendeutsch
https://github.com/fwenzel/strassendeutsch
Entry file: strassendeutsch/woerterbuch/__init__.py
Scanned: 2016-10-12 12:24:45.449410
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lzyy/chat
https://github.com/lzyy/chat
Entry file: chat/src/app.py
Scanned: 2016-10-12 12:25:03.054136
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ferhensil/flask-example
https://github.com/ferhensil/flask-example
Entry file: flask-example/main.py
Scanned: 2016-10-12 12:25:08.545560
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jeanphix/flask-dashed-demo
https://github.com/jeanphix/flask-dashed-demo
Entry file: flask-dashed-demo/app.py
Scanned: 2016-10-12 12:25:34.557590
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kenkam/msgbrd
https://github.com/kenkam/msgbrd
Entry file: msgbrd/app.py
Scanned: 2016-10-12 12:25:36.042594
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

grigouze/flask-jenkins-radiator
https://github.com/grigouze/flask-jenkins-radiator
Entry file: flask-jenkins-radiator/radiator/radiator.py
Scanned: 2016-10-12 12:25:40.532820
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rduplain/flask-jquery-autosave-example
https://github.com/rduplain/flask-jquery-autosave-example
Entry file: flask-jquery-autosave-example/app.py
Scanned: 2016-10-12 12:25:43.027713
No vulnerabilities found.


kracekumar/Gummi
https://github.com/kracekumar/Gummi
Entry file: Gummi/gummi/tests/test.py
Scanned: 2016-10-12 12:25:45.523943
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ivoscc/qchaes
https://github.com/ivoscc/qchaes
Entry file: qchaes/runserver.py
Scanned: 2016-10-12 12:25:53.490277
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fdemmer/flask-principal
https://github.com/fdemmer/flask-principal
Entry file: flask-principal/tests/test_principal.py
Scanned: 2016-10-12 12:26:03.984227
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dasevilla/evernote-oauth-example
https://github.com/dasevilla/evernote-oauth-example
Entry file: evernote-oauth-example/webapp.py
Scanned: 2016-10-12 12:26:10.257573
No vulnerabilities found.


zeninthehome/flaskr
https://github.com/zeninthehome/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 12:26:36.043686
No vulnerabilities found.


joshfinnie/Flacker-News
https://github.com/joshfinnie/Flacker-News
Entry file: Flacker-News/flacker-news/app.py
Scanned: 2016-10-12 12:26:36.532682
No vulnerabilities found.
An Error occurred while scanning the repo: 'NoneType' object has no attribute 'label'

moneill/uber-flask
https://github.com/moneill/uber-flask
Entry file: uber-flask/uber.py
Scanned: 2016-10-12 12:26:41.127210
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: uber-flask/env/lib/python2.7/genericpath.py

nubela/radar-backend
https://github.com/nubela/radar-backend
Entry file: radar-backend/src/radar.py
Scanned: 2016-10-12 12:26:42.631278
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

TxSSC/the-questionator
https://github.com/TxSSC/the-questionator
Entry file: the-questionator/questionator/__init__.py
Scanned: 2016-10-12 12:26:46.127026
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

satonaoya/flask-epio-skelton
https://github.com/satonaoya/flask-epio-skelton
Entry file: flask-epio-skelton/app.py
Scanned: 2016-10-12 12:26:49.342735
No vulnerabilities found.


marksteve/bookmarks
https://github.com/marksteve/bookmarks
Entry file: bookmarks/bookmarks.py
Scanned: 2016-10-12 12:26:54.694335
No vulnerabilities found.


paradoxxxzero/polldance
https://github.com/paradoxxxzero/polldance
Entry file: polldance/dance.py
Scanned: 2016-10-12 12:27:05.063307
No vulnerabilities found.


flebel/Egami
https://github.com/flebel/Egami
Entry file: Egami/egami.py
Scanned: 2016-10-12 12:27:10.518027
No vulnerabilities found.


mitsuhiko/flask-pastebin
https://github.com/mitsuhiko/flask-pastebin
Entry file: flask-pastebin/pastebin.py
Scanned: 2016-10-12 12:27:35.669546
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

maxcountryman/flask-seasurf
https://github.com/maxcountryman/flask-seasurf
Entry file: flask-seasurf/test_seasurf.py
Scanned: 2016-10-12 12:27:40.187109
No vulnerabilities found.


maxcountryman/logmon
https://github.com/maxcountryman/logmon
Entry file: logmon/logmon/__init__.py
Scanned: 2016-10-12 12:27:44.108433
No vulnerabilities found.


hasgeek/coaster
https://github.com/hasgeek/coaster
Entry file: coaster/tests/test_render_with.py
Scanned: 2016-10-12 12:27:48.849550
No vulnerabilities found.


craigkerstiens/flask-helloworld
https://github.com/craigkerstiens/flask-helloworld
Entry file: flask-helloworld/app.py
Scanned: 2016-10-12 12:27:50.180842
No vulnerabilities found.


jarodl/flask-github
https://github.com/jarodl/flask-github
Entry file: flask-github/example/example.py
Scanned: 2016-10-12 12:27:54.968873
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

ahri/flask-mustache
https://github.com/ahri/flask-mustache
Entry file: flask-mustache/tests/test_mustache.py
Scanned: 2016-10-12 12:28:05.274701
No vulnerabilities found.


gears/flask-gears
https://github.com/gears/flask-gears
Entry file: flask-gears/example/app.py
Scanned: 2016-10-12 12:28:10.642112
No vulnerabilities found.


mitsuhiko/tugraz-flask-demo
https://github.com/mitsuhiko/tugraz-flask-demo
Entry file: tugraz-flask-demo/pastebin.py
Scanned: 2016-10-12 12:28:36.683726
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

mattoufoutu/flask-project-templates
https://github.com/mattoufoutu/flask-project-templates
Entry file: None
Scanned: 2016-10-12 12:28:37.925599
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/mattoufoutu/flask-project-templates.

svieira/Budget-Manager
https://github.com/svieira/Budget-Manager
Entry file: None
Scanned: 2016-10-12 12:28:48.442112
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/svieira/Budget-Manager.

solarmist/Flaskr
https://github.com/solarmist/Flaskr
Entry file: Flaskr/flaskr.py
Scanned: 2016-10-12 12:28:50.719980
No vulnerabilities found.


cybertoast/flask-router
https://github.com/cybertoast/flask-router
Entry file: flask-router/test_router.py
Scanned: 2016-10-12 12:29:05.437150
No vulnerabilities found.


srusskih/Flask-application-template
https://github.com/srusskih/Flask-application-template
Entry file: Flask-application-template/myapp/myapp.py
Scanned: 2016-10-12 12:29:12.294736
No vulnerabilities found.


Rootbuzz/heroku-basic-flask-app
https://github.com/Rootbuzz/heroku-basic-flask-app
Entry file: heroku-basic-flask-app/sso.py
Scanned: 2016-10-12 12:29:37.614441
No vulnerabilities found.


adgaudio/async-webapp---gevent--psycopg2--flask
https://github.com/adgaudio/async-webapp---gevent--psycopg2--flask
Entry file: async-webapp---gevent--psycopg2--flask/app.py
Scanned: 2016-10-12 12:29:38.101795
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

maxcountryman/chatter
https://github.com/maxcountryman/chatter
Entry file: chatter/chatter/__init__.py
Scanned: 2016-10-12 12:29:43.574357
No vulnerabilities found.


zeak/pyProx
https://github.com/zeak/pyProx
Entry file: pyProx/pyProx.py
Scanned: 2016-10-12 12:29:44.059332
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

subchild/iStockUtils
https://github.com/subchild/iStockUtils
Entry file: iStockUtils/istockutils.py
Scanned: 2016-10-12 12:29:48.387438
No vulnerabilities found.


tsoporan/read.list
https://github.com/tsoporan/read.list
Entry file: None
Scanned: 2016-10-12 12:29:50.880827
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

dcrosta/flask-pymongo
https://github.com/dcrosta/flask-pymongo
Entry file: flask-pymongo/examples/wiki/wiki.py
Scanned: 2016-10-12 12:30:06.266805
No vulnerabilities found.


jamesward/flaskbars
https://github.com/jamesward/flaskbars
Entry file: flaskbars/web.py
Scanned: 2016-10-12 12:30:11.659081
No vulnerabilities found.


jarus/flask-fillin
https://github.com/jarus/flask-fillin
Entry file: flask-fillin/test_app/__init__.py
Scanned: 2016-10-12 12:30:13.034255
No vulnerabilities found.


noisebridge/flask-noiselist
https://github.com/noisebridge/flask-noiselist
Entry file: flask-noiselist/src/noiselist/__init__.py
Scanned: 2016-10-12 12:30:38.451330
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

givp/Flask-MongoDB-Project
https://github.com/givp/Flask-MongoDB-Project
Entry file: Flask-MongoDB-Project/myapp.py
Scanned: 2016-10-12 12:30:39.722056
No vulnerabilities found.


maxcountryman/logmon
https://github.com/maxcountryman/logmon
Entry file: logmon/logmon/__init__.py
Scanned: 2016-10-12 12:30:44.191916
No vulnerabilities found.


wgkoro/flask_mongodb
https://github.com/wgkoro/flask_mongodb
Entry file: flask_mongodb/app/app.py
Scanned: 2016-10-12 12:30:45.416344
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

danbruegge/flaskeleton
https://github.com/danbruegge/flaskeleton
Entry file: flaskeleton/app/__init__.py
Scanned: 2016-10-12 12:30:50.020440
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

spoqa/flask-beaker
https://github.com/spoqa/flask-beaker
Entry file: flask-beaker/test_beaker.py
Scanned: 2016-10-12 12:31:06.235956
No vulnerabilities found.


BenjaminMalley/FlaskUser
https://github.com/BenjaminMalley/FlaskUser
Entry file: FlaskUser/tests/user_api_tests.py
Scanned: 2016-10-12 12:31:12.673652
No vulnerabilities found.


mattoufoutu/flask-project-templates
https://github.com/mattoufoutu/flask-project-templates
Entry file: None
Scanned: 2016-10-12 12:31:13.164116
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/mattoufoutu/flask-project-templates.

jparise/flask-facebook
https://github.com/jparise/flask-facebook
Entry file: flask-facebook/tests/test_facebook.py
Scanned: 2016-10-12 12:31:38.555192
No vulnerabilities found.


codeb2cc/flask-examples
https://github.com/codeb2cc/flask-examples
Entry file: flask-examples/minitwit/minitwit.py
Scanned: 2016-10-12 12:31:40.113004
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.If'>)

Opentaste/bombolone
https://github.com/Opentaste/bombolone
Entry file: bombolone/bombolone/app.py
Scanned: 2016-10-12 12:31:48.273874
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ahamilton55/flaskr
https://github.com/ahamilton55/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 12:31:49.633292
No vulnerabilities found.


rbastian/flaskr
https://github.com/rbastian/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 12:31:50.840477
No vulnerabilities found.


RyanMcG/Bits-Books
https://github.com/RyanMcG/Bits-Books
Entry file: Bits-Books/web.py
Scanned: 2016-10-12 12:31:56.266286
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

practo/r5d4
https://github.com/practo/r5d4
Entry file: r5d4/r5d4/__init__.py
Scanned: 2016-10-12 12:31:57.697824
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

youknowone/flask-skeleton
https://github.com/youknowone/flask-skeleton
Entry file: None
Scanned: 2016-10-12 12:32:06.228708
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/youknowone/flask-skeleton.

nourlcn/flask-note
https://github.com/nourlcn/flask-note
Entry file: flask-note/note.py
Scanned: 2016-10-12 12:32:18.456588
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

w1mvy/flask_on_gae
https://github.com/w1mvy/flask_on_gae
Entry file: flask_on_gae/src/main.py
Scanned: 2016-10-12 12:32:21.068044
No vulnerabilities found.


yukatou/flask-board_test
https://github.com/yukatou/flask-board_test
Entry file: flask-board_test/board/__init__.py
Scanned: 2016-10-12 12:32:39.452633
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

neilmiddleton/heroku_flask_example
https://github.com/neilmiddleton/heroku_flask_example
Entry file: heroku_flask_example/web.py
Scanned: 2016-10-12 12:32:40.693972
No vulnerabilities found.


dhathorn/Blaskr
https://github.com/dhathorn/Blaskr
Entry file: Blaskr/blaskr/__init__.py
Scanned: 2016-10-12 12:32:45.278255
No vulnerabilities found.


drewlustro/trackcircle
https://github.com/drewlustro/trackcircle
Entry file: None
Scanned: 2016-10-12 12:32:56.525274
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

nicolaiarocci/flask-mimerender
https://github.com/nicolaiarocci/flask-mimerender
Entry file: flask-mimerender/src/example.py
Scanned: 2016-10-12 12:33:07.666462
No vulnerabilities found.


ducu/rq-dashboard
https://github.com/ducu/rq-dashboard
Entry file: rq-dashboard/rq_dashboard/cli.py
Scanned: 2016-10-12 12:33:15.066186
No vulnerabilities found.


ryands/flasknews
https://github.com/ryands/flasknews
Entry file: flasknews/news.py
Scanned: 2016-10-12 12:33:20.431971
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rsenk330/Flask-Cake
https://github.com/rsenk330/Flask-Cake
Entry file: Flask-Cake/flask_cake/tests/test_cake.py
Scanned: 2016-10-12 12:33:41.158791
No vulnerabilities found.


jasonwyatt/Flask-ErrorMail
https://github.com/jasonwyatt/Flask-ErrorMail
Entry file: Flask-ErrorMail/example/simple.py
Scanned: 2016-10-12 12:33:42.579437
No vulnerabilities found.


brocaar/flask-views
https://github.com/brocaar/flask-views
Entry file: flask-views/flask_views/tests/functional/base.py
Scanned: 2016-10-12 12:33:50.725248
No vulnerabilities found.


simonz05/flask-wtf
https://github.com/simonz05/flask-wtf
Entry file: flask-wtf/examples/recaptcha/app.py
Scanned: 2016-10-12 12:33:59.192452
No vulnerabilities found.


nivardus/flask-sl
https://github.com/nivardus/flask-sl
Entry file: flask-sl/examples/app.py
Scanned: 2016-10-12 12:34:00.526309
No vulnerabilities found.


andersoncardoso/flaskle
https://github.com/andersoncardoso/flaskle
Entry file: flaskle/flaskle.py
Scanned: 2016-10-12 12:34:01.867088
No vulnerabilities found.


ferronrsmith/flask_projects
https://github.com/ferronrsmith/flask_projects
Entry file: flask_projects/flask_orm/ormapp.py
Scanned: 2016-10-12 12:34:11.852743
No vulnerabilities found.


spanners/flask-blog
https://github.com/spanners/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 12:34:14.129259
No vulnerabilities found.


kvesteri/flask-generic-views
https://github.com/kvesteri/flask-generic-views
Entry file: flask-generic-views/tests/__init__.py
Scanned: 2016-10-12 12:34:20.703612
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

ehazlett/coiapi-flask
https://github.com/ehazlett/coiapi-flask
Entry file: coiapi-flask/coiapi/__init__.py
Scanned: 2016-10-12 12:34:40.118743
No vulnerabilities found.


rmasters/progress-flask
https://github.com/rmasters/progress-flask
Entry file: progress-flask/progress.py
Scanned: 2016-10-12 12:34:45.806811
No vulnerabilities found.


RDFLib/rdflib-web
https://github.com/RDFLib/rdflib-web
Entry file: rdflib-web/rdflib_web/lod.py
Scanned: 2016-10-12 12:34:51.597665
Vulnerability 1:
File: rdflib-web/rdflib_web/lod.py
 > User input at line 515, trigger word ".data": 
	path = 'lod.data'
Reassigned in: 
	File: rdflib-web/rdflib_web/lod.py
	 > Line 518: path = 'lod.page'
	File: rdflib-web/rdflib_web/lod.py
	 > Line 532: ret_MAYBE_FUNCTION_NAME = redirect(url, 303)
File: rdflib-web/rdflib_web/lod.py
 > reaches line 523, trigger word "url_for(": 
	url = url_for(path,type_=type_, label=label, format_=ext)

Vulnerability 2:
File: rdflib-web/rdflib_web/lod.py
 > User input at line 515, trigger word ".data": 
	path = 'lod.data'
Reassigned in: 
	File: rdflib-web/rdflib_web/lod.py
	 > Line 518: path = 'lod.page'
	File: rdflib-web/rdflib_web/lod.py
	 > Line 532: ret_MAYBE_FUNCTION_NAME = redirect(url, 303)
File: rdflib-web/rdflib_web/lod.py
 > reaches line 525, trigger word "url_for(": 
	url = url_for(path,type_=type_, label=label)

Vulnerability 3:
File: rdflib-web/rdflib_web/lod.py
 > User input at line 515, trigger word ".data": 
	path = 'lod.data'
Reassigned in: 
	File: rdflib-web/rdflib_web/lod.py
	 > Line 518: path = 'lod.page'
	File: rdflib-web/rdflib_web/lod.py
	 > Line 532: ret_MAYBE_FUNCTION_NAME = redirect(url, 303)
File: rdflib-web/rdflib_web/lod.py
 > reaches line 528, trigger word "url_for(": 
	url = url_for(path,label=label, format_=ext)

Vulnerability 4:
File: rdflib-web/rdflib_web/lod.py
 > User input at line 515, trigger word ".data": 
	path = 'lod.data'
Reassigned in: 
	File: rdflib-web/rdflib_web/lod.py
	 > Line 518: path = 'lod.page'
	File: rdflib-web/rdflib_web/lod.py
	 > Line 532: ret_MAYBE_FUNCTION_NAME = redirect(url, 303)
File: rdflib-web/rdflib_web/lod.py
 > reaches line 530, trigger word "url_for(": 
	url = url_for(path,label=label)

Vulnerability 5:
File: rdflib-web/rdflib_web/lod.py
 > User input at line 511, trigger word "get(": 
	mimetype = mimeutils.best_match([mimeutils.RDFXML_MIME, mimeutils.N3_MIME, mimeutils.NTRIPLES_MIME, mimeutils.HTML_MIME], request.headers.get('Accept'))
Reassigned in: 
	File: rdflib-web/rdflib_web/lod.py
	 > Line 516: ext = '.' + mimeutils.mime_to_format(mimetype)
	File: rdflib-web/rdflib_web/lod.py
	 > Line 519: ext = ''
	File: rdflib-web/rdflib_web/lod.py
	 > Line 523: url = url_for(path,type_=type_, label=label, format_=ext)
	File: rdflib-web/rdflib_web/lod.py
	 > Line 525: url = url_for(path,type_=type_, label=label)
	File: rdflib-web/rdflib_web/lod.py
	 > Line 528: url = url_for(path,label=label, format_=ext)
	File: rdflib-web/rdflib_web/lod.py
	 > Line 530: url = url_for(path,label=label)
File: rdflib-web/rdflib_web/lod.py
 > reaches line 532, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect(url, 303)



zen4ever/goose-in-flask
https://github.com/zen4ever/goose-in-flask
Entry file: goose-in-flask/application.py
Scanned: 2016-10-12 12:35:07.251034
No vulnerabilities found.


thinker007/flaskr
https://github.com/thinker007/flaskr
Entry file: flaskr/flaskr/flaskr.py
Scanned: 2016-10-12 12:35:08.649063
No vulnerabilities found.


FND/Flask-RoutingManifest
https://github.com/FND/Flask-RoutingManifest
Entry file: Flask-RoutingManifest/test/test_manifest.py
Scanned: 2016-10-12 12:35:09.862719
No vulnerabilities found.


Fluxx/trappist
https://github.com/Fluxx/trappist
Entry file: trappist/tests/test_app.py
Scanned: 2016-10-12 12:35:11.519641
No vulnerabilities found.


babymastodon/host_flask
https://github.com/babymastodon/host_flask
Entry file: host_flask/templates/wsgi/template.py
Scanned: 2016-10-12 12:35:21.394963
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cirode/test_flask_app
https://github.com/cirode/test_flask_app
Entry file: None
Scanned: 2016-10-12 12:35:44.194251
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/cirode/test_flask_app.

Opentaste/tiramisu-homepage
https://github.com/Opentaste/tiramisu-homepage
Entry file: tiramisu-homepage/libs/flask/app.py
Scanned: 2016-10-12 12:35:54.183192
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fogleman/Boggle
https://github.com/fogleman/Boggle
Entry file: Boggle/__init__.py
Scanned: 2016-10-12 12:36:01.288871
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hickford/footballer-or-pasta
https://github.com/hickford/footballer-or-pasta
Entry file: footballer-or-pasta/app.py
Scanned: 2016-10-12 12:36:11.584076
No vulnerabilities found.


drnlm/Sutekh-Web
https://github.com/drnlm/Sutekh-Web
Entry file: Sutekh-Web/sutekhweb.py
Scanned: 2016-10-12 12:36:15.100548
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mahmoudhossam/blog
https://github.com/mahmoudhossam/blog
Entry file: blog/flaskr.py
Scanned: 2016-10-12 12:36:20.594107
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

polera/practical_python_deployments
https://github.com/polera/practical_python_deployments
Entry file: practical_python_deployments/app.py
Scanned: 2016-10-12 12:36:41.030412
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

eamonbanta/simple_calendar
https://github.com/eamonbanta/simple_calendar
Entry file: simple_calendar/index.py
Scanned: 2016-10-12 12:36:46.864304
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flask-admin/flask-admin
https://github.com/flask-admin/flask-admin
Entry file: flask-admin/flask_admin/tests/test_form_upload.py
Scanned: 2016-10-12 12:37:10.543104
No vulnerabilities found.


maxcountryman/flask-login
https://github.com/maxcountryman/flask-login
Entry file: flask-login/test_login.py
Scanned: 2016-10-12 12:37:13.089082
Vulnerability 1:
File: flask-login/flask_login/login_manager.py
 > User input at line 393, trigger word "get(": 
	cookie_name = config.get('REMEMBER_COOKIE_NAME', COOKIE_NAME)
File: flask-login/flask_login/login_manager.py
 > reaches line 412, trigger word "set_cookie(": 
	response.set_cookie(cookie_name,value=data, expires=expires, domain=domain, path=path, secure=secure, httponly=httponly)



mattupstate/flask-security
https://github.com/mattupstate/flask-security
Entry file: flask-security/tests/conftest.py
Scanned: 2016-10-12 12:37:16.549372
No vulnerabilities found.


jfinkels/flask-restless
https://github.com/jfinkels/flask-restless
Entry file: flask-restless/examples/clients/jquery/__main__.py
Scanned: 2016-10-12 12:37:21.667422
No vulnerabilities found.


lepture/flask-wtf
https://github.com/lepture/flask-wtf
Entry file: flask-wtf/examples/recaptcha/app.py
Scanned: 2016-10-12 12:37:24.784198
No vulnerabilities found.


smurfix/flask-script
https://github.com/smurfix/flask-script
Entry file: flask-script/tests.py
Scanned: 2016-10-12 12:37:25.272012
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mattupstate/flask-mail
https://github.com/mattupstate/flask-mail
Entry file: flask-mail/tests.py
Scanned: 2016-10-12 12:37:42.926416
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown :-(

jarus/flask-testing
https://github.com/jarus/flask-testing
Entry file: flask-testing/examples/twill_site/todos/__init__.py
Scanned: 2016-10-12 12:37:45.726699
No vulnerabilities found.


jpvanhal/flask-split
https://github.com/jpvanhal/flask-split
Entry file: flask-split/tests/__init__.py
Scanned: 2016-10-12 12:37:47.169207
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

gyllstromk/Flask-WhooshAlchemy
https://github.com/gyllstromk/Flask-WhooshAlchemy
Entry file: Flask-WhooshAlchemy/test/test_all.py
Scanned: 2016-10-12 12:37:52.788283
No vulnerabilities found.


dormouse/Flask_Docs_ZhCn
https://github.com/dormouse/Flask_Docs_ZhCn
Entry file: Flask_Docs_ZhCn/flask/sessions.py
Scanned: 2016-10-12 12:38:05.440332
No vulnerabilities found.


mattupstate/flask-social-example
https://github.com/mattupstate/flask-social-example
Entry file: flask-social-example/app/__init__.py
Scanned: 2016-10-12 12:38:13.261863
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dplepage/flask-raptor
https://github.com/dplepage/flask-raptor
Entry file: flask-raptor/tests.py
Scanned: 2016-10-12 12:38:23.759291
No vulnerabilities found.


mdipierro/gluino
https://github.com/mdipierro/gluino
Entry file: gluino/flask_example.py
Scanned: 2016-10-12 12:38:47.310039
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lanius/flask-mitten
https://github.com/lanius/flask-mitten
Entry file: flask-mitten/example/app.py
Scanned: 2016-10-12 12:38:48.609016
No vulnerabilities found.


iwanbk/flasktor
https://github.com/iwanbk/flasktor
Entry file: flasktor/flasktor.py
Scanned: 2016-10-12 12:38:52.837797
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rafaelnovello/Flaskbook
https://github.com/rafaelnovello/Flaskbook
Entry file: Flaskbook/maps.py
Scanned: 2016-10-12 12:39:01.050575
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

benselme/flask-makotemplates
https://github.com/benselme/flask-makotemplates
Entry file: flask-makotemplates/tests/test_mako.py
Scanned: 2016-10-12 12:39:13.419400
No vulnerabilities found.


burningion/Flask-Dotcloud
https://github.com/burningion/Flask-Dotcloud
Entry file: Flask-Dotcloud/project/webapp/app.py
Scanned: 2016-10-12 12:39:14.620725
No vulnerabilities found.


jmstaley/virtualenvwrapper.flask
https://github.com/jmstaley/virtualenvwrapper.flask
Entry file: None
Scanned: 2016-10-12 12:39:18.912625
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/jmstaley/virtualenvwrapper.flask.

asciimoo/potion
https://github.com/asciimoo/potion
Entry file: potion/potion/webapp.py
Scanned: 2016-10-12 12:39:25.510107
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mgdelacroix/gist-flask
https://github.com/mgdelacroix/gist-flask
Entry file: gist-flask/gist-flask.py
Scanned: 2016-10-12 12:39:27.797364
No vulnerabilities found.


radiosilence/Flask-Suave
https://github.com/radiosilence/Flask-Suave
Entry file: None
Scanned: 2016-10-12 12:39:43.477065
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/radiosilence/Flask-Suave.

synchrone/skyms
https://github.com/synchrone/skyms
Entry file: skyms/skyms/app.py
Scanned: 2016-10-12 12:39:46.824038
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jason2506/flask-reqarg
https://github.com/jason2506/flask-reqarg
Entry file: flask-reqarg/tests/test_reqarg.py
Scanned: 2016-10-12 12:40:13.917607
No vulnerabilities found.


ngilbert/flask_blog
https://github.com/ngilbert/flask_blog
Entry file: flask_blog/blog.py
Scanned: 2016-10-12 12:40:14.401726
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

maskota/flask-starter
https://github.com/maskota/flask-starter
Entry file: flask-starter/app/__init__.py
Scanned: 2016-10-12 12:40:19.615635
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mateo41/simpleRest
https://github.com/mateo41/simpleRest
Entry file: simpleRest/sdge_rest.py
Scanned: 2016-10-12 12:40:28.576033
No vulnerabilities found.


ghallberg/stuffster
https://github.com/ghallberg/stuffster
Entry file: stuffster/stuffster.py
Scanned: 2016-10-12 12:40:44.000489
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

robin-wittler/easypeasy
https://github.com/robin-wittler/easypeasy
Entry file: easypeasy/blog.py
Scanned: 2016-10-12 12:40:49.868150
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tonyblundell/socialdump
https://github.com/tonyblundell/socialdump
Entry file: socialdump/socialdump.py
Scanned: 2016-10-12 12:40:54.545461
No vulnerabilities found.


samalba/geventwebsocket-on-dotcloud
https://github.com/samalba/geventwebsocket-on-dotcloud
Entry file: geventwebsocket-on-dotcloud/app.py
Scanned: 2016-10-12 12:41:14.230769
No vulnerabilities found.


FND/statusq
https://github.com/FND/statusq
Entry file: statusq/statusq/__init__.py
Scanned: 2016-10-12 12:41:15.529179
No vulnerabilities found.


octaflop/mrna
https://github.com/octaflop/mrna
Entry file: mrna/mrna/app.py
Scanned: 2016-10-12 12:41:19.812870
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jasonmc/Tweets-GAE-app
https://github.com/jasonmc/Tweets-GAE-app
Entry file: Tweets-GAE-app/libs/flask/app.py
Scanned: 2016-10-12 12:41:26.660813
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

gcollazo/bcapi
https://github.com/gcollazo/bcapi
Entry file: bcapi/bcapi.py
Scanned: 2016-10-12 12:41:28.965031
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

EtnaTraining/todolist-python-server
https://github.com/EtnaTraining/todolist-python-server
Entry file: todolist-python-server/server.py
Scanned: 2016-10-12 12:41:47.674704
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

simakazi/webcarcollection
https://github.com/simakazi/webcarcollection
Entry file: webcarcollection/webcarcollection/__init__.py
Scanned: 2016-10-12 12:41:52.570411
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

guzelgoz/hezenhotel
https://github.com/guzelgoz/hezenhotel
Entry file: hezenhotel/hezenhotel.py
Scanned: 2016-10-12 12:41:57.943676
No vulnerabilities found.


hansonkd/FlaskBootstrapSecurity
https://github.com/hansonkd/FlaskBootstrapSecurity
Entry file: None
Scanned: 2016-10-12 12:42:15.926133
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/hansonkd/FlaskBootstrapSecurity.

playpauseandstop/Flask-Dropbox
https://github.com/playpauseandstop/Flask-Dropbox
Entry file: Flask-Dropbox/testapp/app.py
Scanned: 2016-10-12 12:42:17.682901
No vulnerabilities found.


RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask
https://github.com/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask
Entry file: None
Scanned: 2016-10-12 12:42:20.318147
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask.

lmeunier/flaskup
https://github.com/lmeunier/flaskup
Entry file: flaskup/flaskup/__init__.py
Scanned: 2016-10-12 12:42:29.657703
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ajford/flask-sendmail
https://github.com/ajford/flask-sendmail
Entry file: flask-sendmail/tests.py
Scanned: 2016-10-12 12:42:45.029953
No vulnerabilities found.


playpauseandstop/Flask-LazyViews
https://github.com/playpauseandstop/Flask-LazyViews
Entry file: None
Scanned: 2016-10-12 12:42:48.603213
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/playpauseandstop/Flask-LazyViews.

elmcitylabs/ECL-Facebook
https://github.com/elmcitylabs/ECL-Facebook
Entry file: ECL-Facebook/examples/flask_example/example_app.py
Scanned: 2016-10-12 12:42:51.463265
No vulnerabilities found.


tokuda109/flask-docs-ja
https://github.com/tokuda109/flask-docs-ja
Entry file: flask-docs-ja/setup.py
Scanned: 2016-10-12 12:43:07.747654
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rafaelnovello/Flaskbook
https://github.com/rafaelnovello/Flaskbook
Entry file: Flaskbook/maps.py
Scanned: 2016-10-12 12:43:16.691849
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

benselme/flask-makotemplates
https://github.com/benselme/flask-makotemplates
Entry file: flask-makotemplates/tests/test_mako.py
Scanned: 2016-10-12 12:43:20.028950
No vulnerabilities found.


joealcorn/PyPaste
https://github.com/joealcorn/PyPaste
Entry file: PyPaste/PyPaste/__init__.py
Scanned: 2016-10-12 12:43:26.779417
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

wooptoo/flask-seed
https://github.com/wooptoo/flask-seed
Entry file: flask-seed/app.py
Scanned: 2016-10-12 12:43:29.967992
Vulnerability 1:
File: flask-seed/app.py
 > User input at line 67, trigger word "form[": 
	user = request.form['name']
Reassigned in: 
	File: flask-seed/app.py
	 > Line 73: d = 'name''email'useremail
	File: flask-seed/app.py
	 > Line 75: d = 'error''user exists'
File: flask-seed/app.py
 > reaches line 77, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify(d)

Vulnerability 2:
File: flask-seed/app.py
 > User input at line 68, trigger word "form[": 
	email = request.form['email']
Reassigned in: 
	File: flask-seed/app.py
	 > Line 73: d = 'name''email'useremail
	File: flask-seed/app.py
	 > Line 75: d = 'error''user exists'
File: flask-seed/app.py
 > reaches line 77, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify(d)



fanzeyi/wobbuffet
https://github.com/fanzeyi/wobbuffet
Entry file: wobbuffet/wobbuffet.py
Scanned: 2016-10-12 12:43:56.753808
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

higumachan/flask_twitter
https://github.com/higumachan/flask_twitter
Entry file: flask_twitter/example/app.py
Scanned: 2016-10-12 12:44:05.072341
No vulnerabilities found.


djworth/flask-sessions
https://github.com/djworth/flask-sessions
Entry file: flask-sessions/web.py
Scanned: 2016-10-12 12:44:17.786111
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

axil/flask-test
https://github.com/axil/flask-test
Entry file: flask-test/hello.py
Scanned: 2016-10-12 12:44:26.466281
No vulnerabilities found.


dtotheb/Flask-Control
https://github.com/dtotheb/Flask-Control
Entry file: Flask-Control/FlaskControl.py
Scanned: 2016-10-12 12:44:30.770086
Vulnerability 1:
File: Flask-Control/FlaskControl.py
 > User input at line 30, trigger word "get(": 
	pid = request.args.get('pid')
Reassigned in: 
	File: Flask-Control/FlaskControl.py
	 > Line 32: ret_MAYBE_FUNCTION_NAME = redirect(url_for('procs',p=pid))
File: Flask-Control/FlaskControl.py
 > reaches line 31, trigger word "subprocess.call(": 
	subprocess.call(['kill', pid])



yoshiki256/flask_bbs
https://github.com/yoshiki256/flask_bbs
Entry file: flask_bbs/flaskr.py
Scanned: 2016-10-12 12:44:46.026841
No vulnerabilities found.


robotment/flask-twitter
https://github.com/robotment/flask-twitter
Entry file: flask-twitter/twitter/__init__.py
Scanned: 2016-10-12 12:44:49.448523
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

nickah/Flask-Blog
https://github.com/nickah/Flask-Blog
Entry file: Flask-Blog/blog.py
Scanned: 2016-10-12 12:44:51.621589
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

paulbarbu/flask-upload
https://github.com/paulbarbu/flask-upload
Entry file: flask-upload/index.py
Scanned: 2016-10-12 12:44:56.965606
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

zwass/Heroku-Flask-Starter
https://github.com/zwass/Heroku-Flask-Starter
Entry file: Heroku-Flask-Starter/app.py
Scanned: 2016-10-12 12:45:16.679572
No vulnerabilities found.


aparrish/Simple-Flask-Example
https://github.com/aparrish/Simple-Flask-Example
Entry file: Simple-Flask-Example/concord.py
Scanned: 2016-10-12 12:45:17.963417
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

benbenben1010/flask-shark-experiment
https://github.com/benbenben1010/flask-shark-experiment
Entry file: flask-shark-experiment/src/rooms.py
Scanned: 2016-10-12 12:45:23.183319
No vulnerabilities found.


xlevus/appengine-flask-template
https://github.com/xlevus/appengine-flask-template
Entry file: appengine-flask-template/web.py
Scanned: 2016-10-12 12:45:27.409179
No vulnerabilities found.


30loops/flask-on-30loops
https://github.com/30loops/flask-on-30loops
Entry file: flask-on-30loops/hello.py
Scanned: 2016-10-12 12:45:31.605401
No vulnerabilities found.


melpomene/Berlin-Books-Flask
https://github.com/melpomene/Berlin-Books-Flask
Entry file: Berlin-Books-Flask/main.py
Scanned: 2016-10-12 12:45:47.055541
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mateo41/simpleRest
https://github.com/mateo41/simpleRest
Entry file: simpleRest/sdge_rest.py
Scanned: 2016-10-12 12:45:49.471414
No vulnerabilities found.


samalba/geventwebsocket-on-dotcloud
https://github.com/samalba/geventwebsocket-on-dotcloud
Entry file: geventwebsocket-on-dotcloud/app.py
Scanned: 2016-10-12 12:45:51.655630
No vulnerabilities found.


yoshiki256/flaskr_on_fluxflex
https://github.com/yoshiki256/flaskr_on_fluxflex
Entry file: flaskr_on_fluxflex/flaskr.py
Scanned: 2016-10-12 12:45:56.879128
No vulnerabilities found.


mygulamali/Geodesics
https://github.com/mygulamali/Geodesics
Entry file: Geodesics/geodesics.py
Scanned: 2016-10-12 12:46:17.724665
No vulnerabilities found.


rmasters/mdpages
https://github.com/rmasters/mdpages
Entry file: mdpages/mdpages.py
Scanned: 2016-10-12 12:46:18.912863
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

vmihailenco/ndbunq-example
https://github.com/vmihailenco/ndbunq-example
Entry file: ndbunq-example/app/app.py
Scanned: 2016-10-12 12:46:21.113208
No vulnerabilities found.


gofetch/fetchweb
https://github.com/gofetch/fetchweb
Entry file: fetchweb/fetchweb/__init__.py
Scanned: 2016-10-12 12:46:28.657938
Vulnerability 1:
File: fetchweb/fetchweb/views.py
 > User input at line 144, trigger word "files[": 
	file = request.files['file']
Reassigned in: 
	File: fetchweb/fetchweb/views.py
	 > Line 147: filename = secure_filename(file.filename)
File: fetchweb/fetchweb/views.py
 > reaches line 148, trigger word "flash(": 
	flash('uploaded file: %s' % filename)

Vulnerability 2:
File: fetchweb/fetchweb/views.py
 > User input at line 145, trigger word "form[": 
	url = request.form['torrent-url']
File: fetchweb/fetchweb/views.py
 > reaches line 150, trigger word "flash(": 
	flash('uploaded url: %s' % url)



vr3v3n/TODO
https://github.com/vr3v3n/TODO
Entry file: TODO/todo.py
Scanned: 2016-10-12 12:46:31.960895
No vulnerabilities found.


robertberry/rbrt-blog
https://github.com/robertberry/rbrt-blog
Entry file: rbrt-blog/blog.py
Scanned: 2016-10-12 12:46:47.337209
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

yoshiki256/shingeki_mederu_python
https://github.com/yoshiki256/shingeki_mederu_python
Entry file: shingeki_mederu_python/shingeki.py
Scanned: 2016-10-12 12:46:49.642980
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cjmeyer/quincy
https://github.com/cjmeyer/quincy
Entry file: None
Scanned: 2016-10-12 12:46:52.152731
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/cjmeyer/quincy.

rdallasgray/archie-webservice
https://github.com/rdallasgray/archie-webservice
Entry file: archie-webservice/archie/__init__.py
Scanned: 2016-10-12 12:47:22.087507
No vulnerabilities found.


swinton/Closest-UK-City
https://github.com/swinton/Closest-UK-City
Entry file: Closest-UK-City/webapp.py
Scanned: 2016-10-12 12:47:23.298291
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jamalzkhan/dropshare
https://github.com/jamalzkhan/dropshare
Entry file: dropshare/app.py
Scanned: 2016-10-12 12:47:24.582414
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flyingclimber/LegalTally
https://github.com/flyingclimber/LegalTally
Entry file: LegalTally/legaltally.py
Scanned: 2016-10-12 12:47:28.893515
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

playpauseandstop/Flask-Dropbox
https://github.com/playpauseandstop/Flask-Dropbox
Entry file: Flask-Dropbox/testapp/app.py
Scanned: 2016-10-12 12:47:52.487951
No vulnerabilities found.


jpvanhal/flask-basicauth
https://github.com/jpvanhal/flask-basicauth
Entry file: flask-basicauth/test_basicauth.py
Scanned: 2016-10-12 12:48:07.310499
No vulnerabilities found.


mattupstate/flask-negotiate
https://github.com/mattupstate/flask-negotiate
Entry file: flask-negotiate/tests.py
Scanned: 2016-10-12 12:48:18.678245
No vulnerabilities found.


ajford/flask-sendmail
https://github.com/ajford/flask-sendmail
Entry file: flask-sendmail/tests.py
Scanned: 2016-10-12 12:48:23.999775
No vulnerabilities found.


dileeshvar/flask
https://github.com/dileeshvar/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 12:48:48.779924
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

jpvanhal/flask-xuacompatible
https://github.com/jpvanhal/flask-xuacompatible
Entry file: flask-xuacompatible/flask_xuacompatible.py
Scanned: 2016-10-12 12:48:50.985522
No vulnerabilities found.


ihor/FlaskTest
https://github.com/ihor/FlaskTest
Entry file: FlaskTest/FileShare/app.py
Scanned: 2016-10-12 12:48:52.300289
No vulnerabilities found.


mrigor/url-shortener
https://github.com/mrigor/url-shortener
Entry file: url-shortener/url_shortener.py
Scanned: 2016-10-12 12:48:58.516906
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

gumho/minimal-flask-gae-template
https://github.com/gumho/minimal-flask-gae-template
Entry file: minimal-flask-gae-template/packages/flask/sessions.py
Scanned: 2016-10-12 12:49:09.395375
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jamesward/hello-python-flask
https://github.com/jamesward/hello-python-flask
Entry file: hello-python-flask/web.py
Scanned: 2016-10-12 12:49:18.648274
No vulnerabilities found.


khanhnguyenqk/flask-example
https://github.com/khanhnguyenqk/flask-example
Entry file: flask-example/main.py
Scanned: 2016-10-12 12:49:24.620516
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fnava621/flask-blog
https://github.com/fnava621/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 12:49:51.906325
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-blog/venv/lib/python2.7/genericpath.py

higumachan/ladytile_flask
https://github.com/higumachan/ladytile_flask
Entry file: ladytile_flask/app.py
Scanned: 2016-10-12 12:49:53.086849
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

gkoberger/gkoberger-flask
https://github.com/gkoberger/gkoberger-flask
Entry file: gkoberger-flask/app.py
Scanned: 2016-10-12 12:49:59.337330
No vulnerabilities found.


teerytko/nokiantorpedo-flask
https://github.com/teerytko/nokiantorpedo-flask
Entry file: nokiantorpedo-flask/src/userapp.py
Scanned: 2016-10-12 12:50:00.689165
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

Pewpewarrows/Prometheus-Flask
https://github.com/Pewpewarrows/Prometheus-Flask
Entry file: None
Scanned: 2016-10-12 12:50:10.723881
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/Pewpewarrows/Prometheus-Flask.

jrheard/task-flask
https://github.com/jrheard/task-flask
Entry file: task-flask/task-flask/app.py
Scanned: 2016-10-12 12:50:19.001811
No vulnerabilities found.


alekzvik/testing-fs
https://github.com/alekzvik/testing-fs
Entry file: testing-fs/simple_app.py
Scanned: 2016-10-12 12:50:25.200362
No vulnerabilities found.


yefim/TwilioPusherFlask
https://github.com/yefim/TwilioPusherFlask
Entry file: TwilioPusherFlask/app.py
Scanned: 2016-10-12 12:50:35.632372
No vulnerabilities found.


rduplain/flask-svg-example
https://github.com/rduplain/flask-svg-example
Entry file: flask-svg-example/app.py
Scanned: 2016-10-12 12:50:36.864404
No vulnerabilities found.


nulogy/competition-flask-bootstrap
https://github.com/nulogy/competition-flask-bootstrap
Entry file: competition-flask-bootstrap/app.py
Scanned: 2016-10-12 12:50:38.056787
No vulnerabilities found.


pythonclt/cltwit
https://github.com/pythonclt/cltwit
Entry file: cltwit/minitwit.py
Scanned: 2016-10-12 12:50:49.433564
No vulnerabilities found.


mikejarrett/company-time-clock
https://github.com/mikejarrett/company-time-clock
Entry file: company-time-clock/timeclock/webapp/__init__.py
Scanned: 2016-10-12 12:50:53.909464
No vulnerabilities found.


lyaunzbe/Foo
https://github.com/lyaunzbe/Foo
Entry file: Foo/foo.py
Scanned: 2016-10-12 12:50:55.101124
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fnava621/heroku-flaskstyle-test
https://github.com/fnava621/heroku-flaskstyle-test
Entry file: heroku-flaskstyle-test/app.py
Scanned: 2016-10-12 12:51:04.503886
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: heroku-flaskstyle-test/.#app.py

gofetch/fetchweb
https://github.com/gofetch/fetchweb
Entry file: fetchweb/fetchweb/__init__.py
Scanned: 2016-10-12 12:51:09.151487
Vulnerability 1:
File: fetchweb/fetchweb/views.py
 > User input at line 144, trigger word "files[": 
	file = request.files['file']
Reassigned in: 
	File: fetchweb/fetchweb/views.py
	 > Line 147: filename = secure_filename(file.filename)
File: fetchweb/fetchweb/views.py
 > reaches line 148, trigger word "flash(": 
	flash('uploaded file: %s' % filename)

Vulnerability 2:
File: fetchweb/fetchweb/views.py
 > User input at line 145, trigger word "form[": 
	url = request.form['torrent-url']
File: fetchweb/fetchweb/views.py
 > reaches line 150, trigger word "flash(": 
	flash('uploaded url: %s' % url)



rDaffa/Firstlight-Alarm
https://github.com/rDaffa/Firstlight-Alarm
Entry file: Firstlight-Alarm/app.py
Scanned: 2016-10-12 12:51:19.408719
No vulnerabilities found.


metllord/stumble_score_py
https://github.com/metllord/stumble_score_py
Entry file: stumble_score_py/web.py
Scanned: 2016-10-12 12:51:26.325642
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tetsuharu/tawlkbox
https://github.com/tetsuharu/tawlkbox
Entry file: tawlkbox/__init__.py
Scanned: 2016-10-12 12:51:27.513616
No vulnerabilities found.


mbr/flask-bootstrap
https://github.com/mbr/flask-bootstrap
Entry file: flask-bootstrap/sample_application/__init__.py
Scanned: 2016-10-12 12:51:42.023936
No vulnerabilities found.


closeio/flask-mongorest
https://github.com/closeio/flask-mongorest
Entry file: flask-mongorest/example/app.py
Scanned: 2016-10-12 12:51:51.468672
No vulnerabilities found.


mattupstate/flask-principal
https://github.com/mattupstate/flask-principal
Entry file: flask-principal/tests/test_principal.py
Scanned: 2016-10-12 12:51:52.951769
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dansimau/flask-bootstrap
https://github.com/dansimau/flask-bootstrap
Entry file: flask-bootstrap/app/__init__.py
Scanned: 2016-10-12 12:51:55.681426
No vulnerabilities found.


thrisp/flask-celery-example
https://github.com/thrisp/flask-celery-example
Entry file: flask-celery-example/app.py
Scanned: 2016-10-12 12:52:01.990956
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jhezjkp/flask-principal
https://github.com/jhezjkp/flask-principal
Entry file: flask-principal/tests/test_principal.py
Scanned: 2016-10-12 12:52:08.474128
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

yefim/flask-heroku-sample
https://github.com/yefim/flask-heroku-sample
Entry file: flask-heroku-sample/app.py
Scanned: 2016-10-12 12:52:19.711991
No vulnerabilities found.


whichlight/flask-tweepy-oauth
https://github.com/whichlight/flask-tweepy-oauth
Entry file: flask-tweepy-oauth/server.py
Scanned: 2016-10-12 12:52:25.949429
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kofrasa/flask-apputils
https://github.com/kofrasa/flask-apputils
Entry file: flask-apputils/tests/routing/__init__.py
Scanned: 2016-10-12 12:52:39.003331
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cpdean/heroku-flask-postgresql-template
https://github.com/cpdean/heroku-flask-postgresql-template
Entry file: heroku-flask-postgresql-template/app.py
Scanned: 2016-10-12 12:52:40.198650
No vulnerabilities found.


asascience-open/Flask_Social_Auth
https://github.com/asascience-open/Flask_Social_Auth
Entry file: Flask_Social_Auth/flask_social_auth/__init__.py
Scanned: 2016-10-12 12:52:50.440694
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

aldryncore/webservices
https://github.com/aldryncore/webservices
Entry file: webservices/examples/flask_app/app.py
Scanned: 2016-10-12 12:52:54.755768
No vulnerabilities found.


mattupstate/flask-stache
https://github.com/mattupstate/flask-stache
Entry file: flask-stache/example/__init__.py
Scanned: 2016-10-12 12:52:56.066601
No vulnerabilities found.


rdegges/flask-skel
https://github.com/rdegges/flask-skel
Entry file: flask-skel/skel/__init__.py
Scanned: 2016-10-12 12:53:02.292390
No vulnerabilities found.


svieira/Flask-HipPocket
https://github.com/svieira/Flask-HipPocket
Entry file: Flask-HipPocket/flask_hippocket/pocket.py
Scanned: 2016-10-12 12:53:09.738539
Vulnerability 1:
File: Flask-HipPocket/flask_hippocket/tests/mapper.py
 > User input at line 38, trigger word "get(": 
	rv = tc.get('/')
File: Flask-HipPocket/flask_hippocket/tests/mapper.py
 > reaches line 39, trigger word "url_for(": 
	self.assertTrue('The url for url_for('endpoint_name') is /' in rv.data.decode('utf-8'))



honza/oauth-service
https://github.com/honza/oauth-service
Entry file: oauth-service/frontend/app.py
Scanned: 2016-10-12 12:53:26.563521
No vulnerabilities found.


albertmatyi/flaskgaellery
https://github.com/albertmatyi/flaskgaellery
Entry file: flaskgaellery/flask/sessions.py
Scanned: 2016-10-12 12:53:30.508973
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dougwt/ilmd-flask
https://github.com/dougwt/ilmd-flask
Entry file: ilmd-flask/app/__init__.py
Scanned: 2016-10-12 12:53:40.499417
No vulnerabilities found.


dpflug/flask-barcodes
https://github.com/dpflug/flask-barcodes
Entry file: flask-barcodes/barcodes/__init__.py
Scanned: 2016-10-12 12:53:41.700784
No vulnerabilities found.


feltnerm/flask-boilerplate
https://github.com/feltnerm/flask-boilerplate
Entry file: flask-boilerplate/apps/__init__.py
Scanned: 2016-10-12 12:53:51.403437
No vulnerabilities found.


Dorianux/flask-yafowil
https://github.com/Dorianux/flask-yafowil
Entry file: flask-yafowil/example/srv.py
Scanned: 2016-10-12 12:53:55.936994
No vulnerabilities found.


linyupark/flaskapps
https://github.com/linyupark/flaskapps
Entry file: flaskapps/example/__init__.py
Scanned: 2016-10-12 12:53:57.235942
No vulnerabilities found.


tophatmonocle/lti_tool_provider_example_flask
https://github.com/tophatmonocle/lti_tool_provider_example_flask
Entry file: lti_tool_provider_example_flask/tool_provider.py
Scanned: 2016-10-12 12:54:02.551298
No vulnerabilities found.


bradmontgomery/mempy-flask-tutorial
https://github.com/bradmontgomery/mempy-flask-tutorial
Entry file: mempy-flask-tutorial/hello.py
Scanned: 2016-10-12 12:54:09.883369
No vulnerabilities found.


jaav/flaskbone1
https://github.com/jaav/flaskbone1
Entry file: flaskbone1/src/flask/sessions.py
Scanned: 2016-10-12 12:54:28.440201
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

grimpy/lxcweb
https://github.com/grimpy/lxcweb
Entry file: lxcweb/lxcweb.py
Scanned: 2016-10-12 12:54:30.329048
No vulnerabilities found.


tophatmonocle/lti_tool_consumer_example_flask
https://github.com/tophatmonocle/lti_tool_consumer_example_flask
Entry file: lti_tool_consumer_example_flask/tool_consumer.py
Scanned: 2016-10-12 12:54:42.043666
No vulnerabilities found.


mbowcock/flask-rest
https://github.com/mbowcock/flask-rest
Entry file: flask-rest/haystack/core.py
Scanned: 2016-10-12 12:54:50.569148
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

newsapps/flask-bakery
https://github.com/newsapps/flask-bakery
Entry file: flask-bakery/app.py
Scanned: 2016-10-12 12:54:55.851291
No vulnerabilities found.


mnbbrown/flask-sample
https://github.com/mnbbrown/flask-sample
Entry file: flask-sample/guild/app.py
Scanned: 2016-10-12 12:54:58.167280
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

vmihailenco/flask-hello
https://github.com/vmihailenco/flask-hello
Entry file: flask-hello/blibb_api/hello.py
Scanned: 2016-10-12 12:55:03.378873
No vulnerabilities found.


mbr/flask-obscurity
https://github.com/mbr/flask-obscurity
Entry file: flask-obscurity/tests/test_extension.py
Scanned: 2016-10-12 12:55:10.729474
No vulnerabilities found.


yiwinking/flask_project
https://github.com/yiwinking/flask_project
Entry file: flask_project/flaskr.py
Scanned: 2016-10-12 12:55:20.975521
No vulnerabilities found.


bdelbosc/restapp
https://github.com/bdelbosc/restapp
Entry file: restapp/restapp/__init__.py
Scanned: 2016-10-12 12:55:27.375253
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

miguel250/miguelpz-core
https://github.com/miguel250/miguelpz-core
Entry file: miguelpz-core/app/config/__init__.py
Scanned: 2016-10-12 12:55:30.815852
No vulnerabilities found.


rduplain/flask-svg-example
https://github.com/rduplain/flask-svg-example
Entry file: flask-svg-example/app.py
Scanned: 2016-10-12 12:55:40.057828
No vulnerabilities found.


sergray/Flask-MailErrors
https://github.com/sergray/Flask-MailErrors
Entry file: Flask-MailErrors/tests.py
Scanned: 2016-10-12 12:55:42.296884
No vulnerabilities found.


kalimatas/writedownme
https://github.com/kalimatas/writedownme
Entry file: writedownme/flask/sessions.py
Scanned: 2016-10-12 12:55:57.222261
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dbrgn/schlagzeilengenerator
https://github.com/dbrgn/schlagzeilengenerator
Entry file: schlagzeilengenerator/app/app.py
Scanned: 2016-10-12 12:55:58.962705
No vulnerabilities found.


martyanov/minitwit
https://github.com/martyanov/minitwit
Entry file: minitwit/minitwit.py
Scanned: 2016-10-12 12:56:04.382142
No vulnerabilities found.


sethtrain/buntin.org
https://github.com/sethtrain/buntin.org
Entry file: None
Scanned: 2016-10-12 12:56:10.605182
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/sethtrain/buntin.org.

karanlyons/bestthing
https://github.com/karanlyons/bestthing
Entry file: bestthing/bestthing/__init__.py
Scanned: 2016-10-12 12:56:21.958535
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sneeu/board
https://github.com/sneeu/board
Entry file: board/board.py
Scanned: 2016-10-12 12:56:30.699222
No vulnerabilities found.


omerk/spotify-http-control
https://github.com/omerk/spotify-http-control
Entry file: spotify-http-control/control.py
Scanned: 2016-10-12 12:56:40.970356
No vulnerabilities found.


mfa/weight-app
https://github.com/mfa/weight-app
Entry file: weight-app/weight/main.py
Scanned: 2016-10-12 12:56:44.230905
Vulnerability 1:
File: weight-app/weight/views.py
 > User input at line 43, trigger word "get(": 
	next = request.args.get('next')
Reassigned in: 
	File: weight-app/weight/views.py
	 > Line 46: ret_MAYBE_FUNCTION_NAME = render_template('login.html',form=form)
File: weight-app/weight/views.py
 > reaches line 44, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect(next or url_for('.index'))

Vulnerability 2:
File: weight-app/weight/views.py
 > User input at line 43, trigger word "get(": 
	next = request.args.get('next')
Reassigned in: 
	File: weight-app/weight/views.py
	 > Line 46: ret_MAYBE_FUNCTION_NAME = render_template('login.html',form=form)
File: weight-app/weight/views.py
 > reaches line 44, trigger word "url_for(": 
	ret_MAYBE_FUNCTION_NAME = redirect(next or url_for('.index'))

Vulnerability 3:
File: weight-app/weight/views.py
 > User input at line 103, trigger word "get(": 
	wid = request.args.get('wid')
Reassigned in: 
	File: weight-app/weight/views.py
	 > Line 107: elem = Weight.query.get(wid)
	File: weight-app/weight/views.py
	 > Line 123: form = WeightForm(obj=elem)
	File: weight-app/weight/views.py
	 > Line 129: form = WeightForm()
	File: weight-app/weight/views.py
	 > Line 138: elem = Weight(weight=request.form['weight'])
	File: weight-app/weight/views.py
	 > Line 166: form.scale_name.data = elem.scale_name
	File: weight-app/weight/views.py
	 > Line 170: form.scale_name.data = u1.default_scale_name
	File: weight-app/weight/views.py
	 > Line 172: ret_MAYBE_FUNCTION_NAME = render_template('weight_edit.html',form=form, wrange=range(wmin, wmax))
	File: weight-app/weight/views.py
	 > Line 187: ret_MAYBE_FUNCTION_NAME = render_template('weight_list.html',elements=elements.items, paginate=elements, show_comment=False)
File: weight-app/weight/views.py
 > reaches line 154, trigger word "flash(": 
	flash('Data saved [%s with %s]' % (elem.wdate, elem.weight), 'info')

Vulnerability 4:
File: weight-app/weight/views.py
 > User input at line 107, trigger word "get(": 
	elem = Weight.query.get(wid)
Reassigned in: 
	File: weight-app/weight/views.py
	 > Line 123: form = WeightForm(obj=elem)
	File: weight-app/weight/views.py
	 > Line 129: form = WeightForm()
	File: weight-app/weight/views.py
	 > Line 138: elem = Weight(weight=request.form['weight'])
	File: weight-app/weight/views.py
	 > Line 166: form.scale_name.data = elem.scale_name
	File: weight-app/weight/views.py
	 > Line 170: form.scale_name.data = u1.default_scale_name
	File: weight-app/weight/views.py
	 > Line 172: ret_MAYBE_FUNCTION_NAME = render_template('weight_edit.html',form=form, wrange=range(wmin, wmax))
	File: weight-app/weight/views.py
	 > Line 187: ret_MAYBE_FUNCTION_NAME = render_template('weight_list.html',elements=elements.items, paginate=elements, show_comment=False)
File: weight-app/weight/views.py
 > reaches line 154, trigger word "flash(": 
	flash('Data saved [%s with %s]' % (elem.wdate, elem.weight), 'info')

Vulnerability 5:
File: weight-app/weight/views.py
 > User input at line 138, trigger word "form[": 
	elem = Weight(weight=request.form['weight'])
Reassigned in: 
	File: weight-app/weight/views.py
	 > Line 107: elem = Weight.query.get(wid)
	File: weight-app/weight/views.py
	 > Line 123: form = WeightForm(obj=elem)
	File: weight-app/weight/views.py
	 > Line 129: form = WeightForm()
	File: weight-app/weight/views.py
	 > Line 166: form.scale_name.data = elem.scale_name
	File: weight-app/weight/views.py
	 > Line 170: form.scale_name.data = u1.default_scale_name
	File: weight-app/weight/views.py
	 > Line 172: ret_MAYBE_FUNCTION_NAME = render_template('weight_edit.html',form=form, wrange=range(wmin, wmax))
	File: weight-app/weight/views.py
	 > Line 187: ret_MAYBE_FUNCTION_NAME = render_template('weight_list.html',elements=elements.items, paginate=elements, show_comment=False)
File: weight-app/weight/views.py
 > reaches line 154, trigger word "flash(": 
	flash('Data saved [%s with %s]' % (elem.wdate, elem.weight), 'info')



dsosby/pycanoed
https://github.com/dsosby/pycanoed
Entry file: pycanoed/app.py
Scanned: 2016-10-12 12:56:54.124340
No vulnerabilities found.


danlamanna/Jackhammer-Gateway
https://github.com/danlamanna/Jackhammer-Gateway
Entry file: Jackhammer-Gateway/api.py
Scanned: 2016-10-12 12:56:56.475325
No vulnerabilities found.


digiblink/reflaskr
https://github.com/digiblink/reflaskr
Entry file: reflaskr/app.py
Scanned: 2016-10-12 12:56:59.070047
No vulnerabilities found.


Maplecroft/Ansel
https://github.com/Maplecroft/Ansel
Entry file: Ansel/app.py
Scanned: 2016-10-12 12:57:10.919864
No vulnerabilities found.


mattupstate/flask-rq
https://github.com/mattupstate/flask-rq
Entry file: flask-rq/tests/flaskrq_tests.py
Scanned: 2016-10-12 12:57:31.052963
No vulnerabilities found.


klen/Flask-Foundation
https://github.com/klen/Flask-Foundation
Entry file: Flask-Foundation/base/app.py
Scanned: 2016-10-12 12:57:42.852093
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ib-lundgren/flask-oauthprovider
https://github.com/ib-lundgren/flask-oauthprovider
Entry file: flask-oauthprovider/examples/client.py
Scanned: 2016-10-12 12:57:44.708991
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sashka/flask-googleauth
https://github.com/sashka/flask-googleauth
Entry file: flask-googleauth/flask_googleauth.py
Scanned: 2016-10-12 12:57:53.078523
No vulnerabilities found.


benselme/flask-mako
https://github.com/benselme/flask-mako
Entry file: flask-mako/flask_mako.py
Scanned: 2016-10-12 12:57:57.643986
No vulnerabilities found.


chriszf/flask_todolist
https://github.com/chriszf/flask_todolist
Entry file: flask_todolist/todolist/model.py
Scanned: 2016-10-12 12:58:10.819268
No vulnerabilities found.


srusskih/flask-uploads
https://github.com/srusskih/flask-uploads
Entry file: flask-uploads/tests/test-uploads.py
Scanned: 2016-10-12 12:58:23.349387
No vulnerabilities found.


Kozea/Flask-WeasyPrint
https://github.com/Kozea/Flask-WeasyPrint
Entry file: Flask-WeasyPrint/flask_weasyprint/tests.py
Scanned: 2016-10-12 12:58:28.920582
No vulnerabilities found.


mattupstate/flask-environments
https://github.com/mattupstate/flask-environments
Entry file: flask-environments/tests/__init__.py
Scanned: 2016-10-12 12:58:31.289403
No vulnerabilities found.


kofrasa/flask-apputils
https://github.com/kofrasa/flask-apputils
Entry file: flask-apputils/tests/routing/__init__.py
Scanned: 2016-10-12 12:58:44.268178
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

DeaconDesperado/Flask-SQLAlchemy-Example
https://github.com/DeaconDesperado/Flask-SQLAlchemy-Example
Entry file: Flask-SQLAlchemy-Example/testapp.py
Scanned: 2016-10-12 12:58:53.536171
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

closeio/flask-common
https://github.com/closeio/flask-common
Entry file: flask-common/tests/__init__.py
Scanned: 2016-10-12 12:58:58.503067
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ahri/flask-snooze
https://github.com/ahri/flask-snooze
Entry file: flask-snooze/tests/test_snooze.py
Scanned: 2016-10-12 12:58:59.818705
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jokull/flask-halalchemy
https://github.com/jokull/flask-halalchemy
Entry file: flask-halalchemy/test_example.py
Scanned: 2016-10-12 12:59:05.129345
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kofrasa/flaskapp
https://github.com/kofrasa/flaskapp
Entry file: flaskapp/flaskapp/application.py
Scanned: 2016-10-12 12:59:11.432783
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tomasd/flask-emailactivation
https://github.com/tomasd/flask-emailactivation
Entry file: flask-emailactivation/tests/test_activation.py
Scanned: 2016-10-12 12:59:23.769079
No vulnerabilities found.


asgoel/flask-twitter
https://github.com/asgoel/flask-twitter
Entry file: flask-twitter/twitter/__init__.py
Scanned: 2016-10-12 12:59:41.225433
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

AnIrishDuck/flask-mako-legacy
https://github.com/AnIrishDuck/flask-mako-legacy
Entry file: flask-mako-legacy/test_flask_mako.py
Scanned: 2016-10-12 12:59:45.586936
No vulnerabilities found.


fdb/fliki
https://github.com/fdb/fliki
Entry file: fliki/fliki.py
Scanned: 2016-10-12 12:59:53.834703
No vulnerabilities found.


lazy-coders/mt_scrapper
https://github.com/lazy-coders/mt_scrapper
Entry file: mt_scrapper/mt_scrapper.py
Scanned: 2016-10-12 13:00:00.596999
No vulnerabilities found.


Senso/fiasco-flask
https://github.com/Senso/fiasco-flask
Entry file: fiasco-flask/fiasco/__init__.py
Scanned: 2016-10-12 13:00:02.056635
Vulnerability 1:
File: fiasco-flask/fiasco/views.py
 > User input at line 109, trigger word ".data": 
	playset = models.Playset(name=form.name.data, desc=form.description.data, owner=session['uid'])
Reassigned in: 
	File: fiasco-flask/fiasco/views.py
	 > Line 119: n_table = models.Details(playset.id, 'need', need_detail)
	File: fiasco-flask/fiasco/views.py
	 > Line 120: o_table = models.Details(playset.id, 'object', obj_detail)
	File: fiasco-flask/fiasco/views.py
	 > Line 121: l_table = models.Details(playset.id, 'location', loc_detail)
	File: fiasco-flask/fiasco/views.py
	 > Line 122: r_table = models.Details(playset.id, 'relationship', rel_detail)
	File: fiasco-flask/fiasco/views.py
	 > Line 133: ret_MAYBE_FUNCTION_NAME = render_template('new_playset.html',error=error, form=form)
	File: fiasco-flask/fiasco/views.py
	 > Line 102: ret_MAYBE_FUNCTION_NAME = redirect(url_for('login'))
File: fiasco-flask/fiasco/views.py
 > reaches line 131, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('/edit_playset/' + str(playset.id))



encodes/flask-snippet
https://github.com/encodes/flask-snippet
Entry file: flask-snippet/app/__init__.py
Scanned: 2016-10-12 13:00:06.035374
Vulnerability 1:
File: flask-snippet/app/users/views.py
 > User input at line 35, trigger word ".data": 
	user = User.query.filter_by(email=form.email.data).first()
Reassigned in: 
	File: flask-snippet/app/users/views.py
	 > Line 40: session['user_id'] = user.id
File: flask-snippet/app/users/views.py
 > reaches line 41, trigger word "flash(": 
	flash('Welcome %s' % user.name)



SmartViking/MaBlag
https://github.com/SmartViking/MaBlag
Entry file: MaBlag/blog.py
Scanned: 2016-10-12 13:00:24.708351
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

keithfancher/Flaskr
https://github.com/keithfancher/Flaskr
Entry file: Flaskr/flaskr.py
Scanned: 2016-10-12 13:00:30.015953
No vulnerabilities found.


daviddedden/flaskr
https://github.com/daviddedden/flaskr
Entry file: flaskr/test.py
Scanned: 2016-10-12 13:00:36.674004
No vulnerabilities found.


tophatmonocle/lti_tool_provider_example_flask
https://github.com/tophatmonocle/lti_tool_provider_example_flask
Entry file: lti_tool_provider_example_flask/tool_provider.py
Scanned: 2016-10-12 13:00:43.013222
No vulnerabilities found.


filipecifali/Flask-Ping-Site
https://github.com/filipecifali/Flask-Ping-Site
Entry file: Flask-Ping-Site/flaskSite.py
Scanned: 2016-10-12 13:00:46.366107
No vulnerabilities found.


DanielKinsman/flask-pyjs-jsonrpc-test
https://github.com/DanielKinsman/flask-pyjs-jsonrpc-test
Entry file: flask-pyjs-jsonrpc-test/web.py
Scanned: 2016-10-12 13:00:54.651434
No vulnerabilities found.


whichlight/flask-couchdb-binary-image-labeler
https://github.com/whichlight/flask-couchdb-binary-image-labeler
Entry file: flask-couchdb-binary-image-labeler/server.py
Scanned: 2016-10-12 13:01:01.551915
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tophatmonocle/lti_tool_consumer_example_flask
https://github.com/tophatmonocle/lti_tool_consumer_example_flask
Entry file: lti_tool_consumer_example_flask/tool_consumer.py
Scanned: 2016-10-12 13:01:06.324098
No vulnerabilities found.


melignus/Appengine-Help-Desk
https://github.com/melignus/Appengine-Help-Desk
Entry file: Appengine-Help-Desk/app.py
Scanned: 2016-10-12 13:01:18.184328
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dustinmm80/flask_test
https://github.com/dustinmm80/flask_test
Entry file: flask_test/app.py
Scanned: 2016-10-12 13:01:24.656466
No vulnerabilities found.


curiousleo/kardiopraxis-flask
https://github.com/curiousleo/kardiopraxis-flask
Entry file: kardiopraxis-flask/kardiopraxis.py
Scanned: 2016-10-12 13:01:58.524020
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

encodes/flask-finance
https://github.com/encodes/flask-finance
Entry file: flask-finance/app/__init__.py
Scanned: 2016-10-12 13:01:59.842438
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ramin32/Flask-Template
https://github.com/ramin32/Flask-Template
Entry file: Flask-Template/project_name/__init__.py
Scanned: 2016-10-12 13:02:03.039611
No vulnerabilities found.


toastercup/flask-scormcloud
https://github.com/toastercup/flask-scormcloud
Entry file: flask-scormcloud/manage.py
Scanned: 2016-10-12 13:02:06.346959
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

weldan/flask_setup
https://github.com/weldan/flask_setup
Entry file: flask_setup/app.py
Scanned: 2016-10-12 13:02:12.657298
No vulnerabilities found.


michellesun/flask_ms
https://github.com/michellesun/flask_ms
Entry file: flask_ms/flaskr.py
Scanned: 2016-10-12 13:02:25.574561
No vulnerabilities found.


shea256/flask-project-template
https://github.com/shea256/flask-project-template
Entry file: flask-project-template/app.py
Scanned: 2016-10-12 13:02:35.461214
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-project-template/venv/lib/python2.7/genericpath.py

Kinghack/flask-oauth-china
https://github.com/Kinghack/flask-oauth-china
Entry file: flask-oauth-china/example/facebook.py
Scanned: 2016-10-12 13:02:37.044397
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

StefanWallin/python-Flask-lab
https://github.com/StefanWallin/python-Flask-lab
Entry file: python-Flask-lab/app.py
Scanned: 2016-10-12 13:02:44.304432
No vulnerabilities found.


rvause/project-base-flask
https://github.com/rvause/project-base-flask
Entry file: None
Scanned: 2016-10-12 13:02:55.075196
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/rvause/project-base-flask.

emilianox/opener
https://github.com/emilianox/opener
Entry file: opener/opener.py
Scanned: 2016-10-12 13:03:00.417339
No vulnerabilities found.


oksana-slu/sqlfla
https://github.com/oksana-slu/sqlfla
Entry file: sqlfla/eventor/__init__.py
Scanned: 2016-10-12 13:03:06.427888
No vulnerabilities found.
An Error occurred while scanning the repo: 'NoneType' object has no attribute 'label'

johngriffin/ldpy-api
https://github.com/johngriffin/ldpy-api
Entry file: ldpy-api/app.py
Scanned: 2016-10-12 13:03:07.721029
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

nryoung/Array-Size
https://github.com/nryoung/Array-Size
Entry file: Array-Size/raid.py
Scanned: 2016-10-12 13:03:13.036701
No vulnerabilities found.


ciaron/pandaflask_old
https://github.com/ciaron/pandaflask_old
Entry file: pandaflask_old/pandachrome.py
Scanned: 2016-10-12 13:03:37.132845
Vulnerability 1:
File: pandaflask_old/pandachrome.py
 > User input at line 208, trigger word "get(": 
	title = request.form.get('title')
Reassigned in: 
	File: pandaflask_old/pandachrome.py
	 > Line 217: category = Category(title=title, description=description, owner_id=owner.id)
File: pandaflask_old/pandachrome.py
 > reaches line 218, trigger word "flash(": 
	flash('successfully created new category ' + title)

Vulnerability 2:
File: pandaflask_old/pandachrome.py
 > User input at line 230, trigger word "get(": 
	title = request.form.get('title')
Reassigned in: 
	File: pandaflask_old/pandachrome.py
	 > Line 240: project = Project(title=title, description=description, category_id=category_id, owner_id=owner.id)
File: pandaflask_old/pandachrome.py
 > reaches line 241, trigger word "flash(": 
	flash('successfully created new project ' + title + ', category ' + category_id)

Vulnerability 3:
File: pandaflask_old/pandachrome.py
 > User input at line 232, trigger word "get(": 
	category_id = request.form.get('category_id')
Reassigned in: 
	File: pandaflask_old/pandachrome.py
	 > Line 240: project = Project(title=title, description=description, category_id=category_id, owner_id=owner.id)
File: pandaflask_old/pandachrome.py
 > reaches line 241, trigger word "flash(": 
	flash('successfully created new project ' + title + ', category ' + category_id)



dlitvakb/MOVEapp
https://github.com/dlitvakb/MOVEapp
Entry file: MOVEapp/appserver.py
Scanned: 2016-10-12 13:03:38.745269
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

clee/boilerplate
https://github.com/clee/boilerplate
Entry file: boilerplate/boilerplate.py
Scanned: 2016-10-12 13:03:44.982625
No vulnerabilities found.


hvnsweeting/mtaskflask
https://github.com/hvnsweeting/mtaskflask
Entry file: mtaskflask/mtask.py
Scanned: 2016-10-12 13:03:47.421687
No vulnerabilities found.


keithfancher/Stories
https://github.com/keithfancher/Stories
Entry file: Stories/stories.py
Scanned: 2016-10-12 13:03:55.831750
No vulnerabilities found.


t20/henhealth
https://github.com/t20/henhealth
Entry file: henhealth/hen.py
Scanned: 2016-10-12 13:04:01.726293
No vulnerabilities found.


klinkin/vksunshine
https://github.com/klinkin/vksunshine
Entry file: vksunshine/vksunshine/application.py
Scanned: 2016-10-12 13:04:09.553183
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

ChrisAnn/FRog
https://github.com/ChrisAnn/FRog
Entry file: FRog/FRog.py
Scanned: 2016-10-12 13:04:10.786763
No vulnerabilities found.


hirish/DinnerDesignr
https://github.com/hirish/DinnerDesignr
Entry file: DinnerDesignr/dinnerDesignr.py
Scanned: 2016-10-12 13:04:13.906876
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jakecoffman/flask-tutorial
https://github.com/jakecoffman/flask-tutorial
Entry file: flask-tutorial/part 6 - databases/flaskr.py
Scanned: 2016-10-12 13:04:33.882139
No vulnerabilities found.


syrusakbary/Flask-SuperAdmin
https://github.com/syrusakbary/Flask-SuperAdmin
Entry file: Flask-SuperAdmin/flask_superadmin/tests/test_model.py
Scanned: 2016-10-12 13:04:43.296498
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

guotie/flaskbbs
https://github.com/guotie/flaskbbs
Entry file: flaskbbs/flaskcommon/auth/views.py
Scanned: 2016-10-12 13:04:46.487607
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rdegges/flask-dynamo
https://github.com/rdegges/flask-dynamo
Entry file: flask-dynamo/tests/test_manager.py
Scanned: 2016-10-12 13:04:48.991646
No vulnerabilities found.


maxcountryman/flask-themes
https://github.com/maxcountryman/flask-themes
Entry file: flask-themes/tests/test-themes.py
Scanned: 2016-10-12 13:04:56.707715
No vulnerabilities found.


klen/Flask-Collect
https://github.com/klen/Flask-Collect
Entry file: Flask-Collect/flask_collect/collect.py
Scanned: 2016-10-12 13:05:02.624962
No vulnerabilities found.


kvesteri/flask-storage
https://github.com/kvesteri/flask-storage
Entry file: flask-storage/tests/__init__.py
Scanned: 2016-10-12 13:05:11.976758
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

thesteve0/openshift-mongo-flask-example
https://github.com/thesteve0/openshift-mongo-flask-example
Entry file: openshift-mongo-flask-example/wsgi/myflaskapp.py
Scanned: 2016-10-12 13:05:13.423039
No vulnerabilities found.


zeraholladay/Flask-Oauth2-Example
https://github.com/zeraholladay/Flask-Oauth2-Example
Entry file: Flask-Oauth2-Example/app.py
Scanned: 2016-10-12 13:05:34.275471
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mtth/kit
https://github.com/mtth/kit
Entry file: kit/examples/poller/poller/app/views.py
Scanned: 2016-10-12 13:05:45.137207
No vulnerabilities found.


codecool/flask-app-structure
https://github.com/codecool/flask-app-structure
Entry file: flask-app-structure/myapp/__init__.py
Scanned: 2016-10-12 13:05:46.626977
No vulnerabilities found.


DeaconDesperado/Flask-SQLAlchemy-Example
https://github.com/DeaconDesperado/Flask-SQLAlchemy-Example
Entry file: Flask-SQLAlchemy-Example/testapp.py
Scanned: 2016-10-12 13:05:47.113148
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kvesteri/flask-test
https://github.com/kvesteri/flask-test
Entry file: flask-test/tests/__init__.py
Scanned: 2016-10-12 13:05:56.715689
No vulnerabilities found.


ipconfiger/pyImageServer
https://github.com/ipconfiger/pyImageServer
Entry file: pyImageServer/serv.py
Scanned: 2016-10-12 13:06:12.045633
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

Khan/flask-wtf
https://github.com/Khan/flask-wtf
Entry file: flask-wtf/examples/recaptcha/app.py
Scanned: 2016-10-12 13:06:16.087352
No vulnerabilities found.


ravenac95/flask-command
https://github.com/ravenac95/flask-command
Entry file: flask-command/tests/fixtures/factory_app.py
Scanned: 2016-10-12 13:06:27.426933
No vulnerabilities found.


encodes/flask-snippet
https://github.com/encodes/flask-snippet
Entry file: flask-snippet/app/__init__.py
Scanned: 2016-10-12 13:06:47.340887
Vulnerability 1:
File: flask-snippet/app/users/views.py
 > User input at line 35, trigger word ".data": 
	user = User.query.filter_by(email=form.email.data).first()
Reassigned in: 
	File: flask-snippet/app/users/views.py
	 > Line 40: session['user_id'] = user.id
File: flask-snippet/app/users/views.py
 > reaches line 41, trigger word "flash(": 
	flash('Welcome %s' % user.name)



vaus/Flaskyll
https://github.com/vaus/Flaskyll
Entry file: Flaskyll/scripts/flaskyll.py
Scanned: 2016-10-12 13:06:48.629387
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

christianpbrink/flaskdemo
https://github.com/christianpbrink/flaskdemo
Entry file: flaskdemo/src/flaskdemo/__init__.py
Scanned: 2016-10-12 13:06:57.004546
No vulnerabilities found.


vsergeyev/flasklutskio
https://github.com/vsergeyev/flasklutskio
Entry file: flasklutskio/app.py
Scanned: 2016-10-12 13:07:02.208082
No vulnerabilities found.


lb1a/flaskplay
https://github.com/lb1a/flaskplay
Entry file: flaskplay/flaskr.py
Scanned: 2016-10-12 13:07:05.522263
No vulnerabilities found.


fdb/helloflask
https://github.com/fdb/helloflask
Entry file: helloflask/helloflask.py
Scanned: 2016-10-12 13:07:12.775375
No vulnerabilities found.


gparuthi/FlaskServer
https://github.com/gparuthi/FlaskServer
Entry file: FlaskServer/server.py
Scanned: 2016-10-12 13:07:35.015874
No vulnerabilities found.


iambibhas/flask-blog
https://github.com/iambibhas/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 13:07:46.012549
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-blog/venv/lib/python2.7/genericpath.py

alexisbellido/flask-basics
https://github.com/alexisbellido/flask-basics
Entry file: flask-basics/hello.py
Scanned: 2016-10-12 13:07:49.377384
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

akaptur/Flask-tutorial
https://github.com/akaptur/Flask-tutorial
Entry file: Flask-tutorial/flask_app.py
Scanned: 2016-10-12 13:07:57.602640
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ihptru/Ubot-flask
https://github.com/ihptru/Ubot-flask
Entry file: Ubot-flask/ubotflask.py
Scanned: 2016-10-12 13:08:02.811997
No vulnerabilities found.


Dipsomaniac/Flask-Mixer
https://github.com/Dipsomaniac/Flask-Mixer
Entry file: Flask-Mixer/tests/__init__.py
Scanned: 2016-10-12 13:08:06.493025
No vulnerabilities found.


bx2/handbag-flask
https://github.com/bx2/handbag-flask
Entry file: handbag-flask/flaskapp-template/app.py
Scanned: 2016-10-12 13:08:13.725345
No vulnerabilities found.


whoeverest/NSND-Upvoting
https://github.com/whoeverest/NSND-Upvoting
Entry file: NSND-Upvoting/upvote-list.py
Scanned: 2016-10-12 13:08:35.891237
No vulnerabilities found.


naudo/flask-hello-world
https://github.com/naudo/flask-hello-world
Entry file: flask-hello-world/app.py
Scanned: 2016-10-12 13:08:45.813047
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-hello-world/venv/lib/python2.7/genericpath.py

Smil3y/MyFlaskr
https://github.com/Smil3y/MyFlaskr
Entry file: MyFlaskr/flaskr.py
Scanned: 2016-10-12 13:08:58.116558
No vulnerabilities found.


jonathancone/helloflask
https://github.com/jonathancone/helloflask
Entry file: helloflask/app.py
Scanned: 2016-10-12 13:09:03.954453
No vulnerabilities found.


vicould/simple_blog
https://github.com/vicould/simple_blog
Entry file: simple_blog/blog.py
Scanned: 2016-10-12 13:09:06.535283
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.DictComp'>)

rafax/flush
https://github.com/rafax/flush
Entry file: flush/flush.py
Scanned: 2016-10-12 13:09:14.707096
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fenbox/chord
https://github.com/fenbox/chord
Entry file: chord/chord.py
Scanned: 2016-10-12 13:09:16.100953
No vulnerabilities found.


R2Drink2/r2drink2-server
https://github.com/R2Drink2/r2drink2-server
Entry file: None
Scanned: 2016-10-12 13:09:29.521179
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/R2Drink2/r2drink2-server.

mafrosis/youtube-dl
https://github.com/mafrosis/youtube-dl
Entry file: youtube-dl/youtube_dl/__init__.py
Scanned: 2016-10-12 13:09:37.377731
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mrwilson/git-serve
https://github.com/mrwilson/git-serve
Entry file: git-serve/git_serve/app.py
Scanned: 2016-10-12 13:09:47.160282
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

allaud/Sufx
https://github.com/allaud/Sufx
Entry file: Sufx/app.py
Scanned: 2016-10-12 13:09:51.324123
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

miniatureape/etsy-api-demo
https://github.com/miniatureape/etsy-api-demo
Entry file: etsy-api-demo/app.py
Scanned: 2016-10-12 13:09:58.709380
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

troythewolfe/nNest
https://github.com/troythewolfe/nNest
Entry file: None
Scanned: 2016-10-12 13:10:08.287042
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/troythewolfe/nNest.

andor44/lohere-
https://github.com/andor44/lohere-
Entry file: lohere-/lohereminusz.py
Scanned: 2016-10-12 13:10:09.837871
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Subscript'>)

richard-to/dashgourd-web-api
https://github.com/richard-to/dashgourd-web-api
Entry file: dashgourd-web-api/example/app.py
Scanned: 2016-10-12 13:10:14.102310
No vulnerabilities found.


pyloque/doumail_machine
https://github.com/pyloque/doumail_machine
Entry file: doumail_machine/main.py
Scanned: 2016-10-12 13:10:17.039812
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

clee/boilerplate
https://github.com/clee/boilerplate
Entry file: boilerplate/boilerplate.py
Scanned: 2016-10-12 13:10:30.363281
No vulnerabilities found.


ashutoshrishi/adventuresontheweb
https://github.com/ashutoshrishi/adventuresontheweb
Entry file: adventuresontheweb/flask/sessions.py
Scanned: 2016-10-12 13:10:41.174355
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

trenta3dev/wafwfy
https://github.com/trenta3dev/wafwfy
Entry file: wafwfy/wafwfy/__init__.py
Scanned: 2016-10-12 13:10:43.585764
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

bendavis78/irclog
https://github.com/bendavis78/irclog
Entry file: irclog/app.py
Scanned: 2016-10-12 13:10:47.886744
No vulnerabilities found.


practo/MyCQ
https://github.com/practo/MyCQ
Entry file: MyCQ/mycq/__init__.py
Scanned: 2016-10-12 13:10:51.381249
No vulnerabilities found.


sijinjoseph/multunus-puzzle
https://github.com/sijinjoseph/multunus-puzzle
Entry file: multunus-puzzle/src/app.py
Scanned: 2016-10-12 13:11:00.519742
Vulnerability 1:
File: multunus-puzzle/src/app.py
 > User input at line 21, trigger word "form[": 
	redirect_to = url_for('tagcloud',twitterhandle=request.form['handle'])
Reassigned in: 
	File: multunus-puzzle/src/app.py
	 > Line 24: ret_MAYBE_FUNCTION_NAME = render_template('index.html')
File: multunus-puzzle/src/app.py
 > reaches line 22, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect(redirect_to)



gaker/slides
https://github.com/gaker/slides
Entry file: slides/slides.py
Scanned: 2016-10-12 13:11:05.162249
No vulnerabilities found.


addumb/toyapp
https://github.com/addumb/toyapp
Entry file: toyapp/toy/__init__.py
Scanned: 2016-10-12 13:11:16.558195
Vulnerability 1:
File: toyapp/toy/views.py
 > User input at line 77, trigger word "form[": 
	val = float(request.form['value'])
Reassigned in: 
	File: toyapp/toy/views.py
	 > Line 86: ret_MAYBE_FUNCTION_NAME = 'Setting %s to %s at %s' % (key, val, str(ts))
File: toyapp/toy/views.py
 > reaches line 83, trigger word "execute(": 
	g.db.execute('insert into events (key, value, ts) values (?, ?, ?)', (key, val, ts))

Vulnerability 2:
File: toyapp/toy/views.py
 > User input at line 79, trigger word "form[": 
	ts = float(request.form['ts'])
Reassigned in: 
	File: toyapp/toy/views.py
	 > Line 81: ts = time.time()
	File: toyapp/toy/views.py
	 > Line 86: ret_MAYBE_FUNCTION_NAME = 'Setting %s to %s at %s' % (key, val, str(ts))
File: toyapp/toy/views.py
 > reaches line 83, trigger word "execute(": 
	g.db.execute('insert into events (key, value, ts) values (?, ?, ?)', (key, val, ts))



petezhut/BigDay
https://github.com/petezhut/BigDay
Entry file: BigDay/app.py
Scanned: 2016-10-12 13:11:30.989786
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

akabaker/remote_rgb
https://github.com/akabaker/remote_rgb
Entry file: remote_rgb/app.py
Scanned: 2016-10-12 13:11:38.271123
No vulnerabilities found.


kyubuns/favme
https://github.com/kyubuns/favme
Entry file: favme/hello.py
Scanned: 2016-10-12 13:11:42.614613
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joelverhagen/flask-rauth
https://github.com/joelverhagen/flask-rauth
Entry file: flask-rauth/example/facebook.py
Scanned: 2016-10-12 13:11:52.924250
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BinOp'>)

mattupstate/flask-security-example
https://github.com/mattupstate/flask-security-example
Entry file: flask-security-example/app.py
Scanned: 2016-10-12 13:11:59.354066
No vulnerabilities found.


MichaelDiBernardo/ddd-flask-example
https://github.com/MichaelDiBernardo/ddd-flask-example
Entry file: ddd-flask-example/blogex/blogex_app.py
Scanned: 2016-10-12 13:12:05.744774
No vulnerabilities found.


FelixLoether/flask-image-upload-thing
https://github.com/FelixLoether/flask-image-upload-thing
Entry file: flask-image-upload-thing/example.py
Scanned: 2016-10-12 13:12:11.994286
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jjjjeeffff/flask-skeleton
https://github.com/jjjjeeffff/flask-skeleton
Entry file: None
Scanned: 2016-10-12 13:12:14.539710
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/jjjjeeffff/flask-skeleton.

mgood/flask-failsafe
https://github.com/mgood/flask-failsafe
Entry file: flask-failsafe/test/test_app.py
Scanned: 2016-10-12 13:12:17.059555
No vulnerabilities found.


arvindkhadri/flask-social
https://github.com/arvindkhadri/flask-social
Entry file: flask-social/tests/test_app/__init__.py
Scanned: 2016-10-12 13:12:39.630176
No vulnerabilities found.


dantezhu/flask_util_js
https://github.com/dantezhu/flask_util_js
Entry file: flask_util_js/examples/main.py
Scanned: 2016-10-12 13:12:43.113923
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kielpedia/flask-sqlalchemy-postgres-heroku-example
https://github.com/kielpedia/flask-sqlalchemy-postgres-heroku-example
Entry file: flask-sqlalchemy-postgres-heroku-example/Flasktest/__init__.py
Scanned: 2016-10-12 13:12:52.904325
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

yamatt/flask-blog
https://github.com/yamatt/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 13:12:59.468185
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-blog/venv/lib/python2.7/genericpath.py

marconi/flask-chat
https://github.com/marconi/flask-chat
Entry file: flask-chat/chat.py
Scanned: 2016-10-12 13:13:07.071325
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rjurney/enron-python-flask-cassandra-pig
https://github.com/rjurney/enron-python-flask-cassandra-pig
Entry file: enron-python-flask-cassandra-pig/index.py
Scanned: 2016-10-12 13:13:11.440649
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

KaviCorp/flask_pysaml2
https://github.com/KaviCorp/flask_pysaml2
Entry file: flask_pysaml2/tests/test_saml.py
Scanned: 2016-10-12 13:13:16.267570
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

paulchakravarti/flask-skeleton
https://github.com/paulchakravarti/flask-skeleton
Entry file: None
Scanned: 2016-10-12 13:13:38.776063
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/paulchakravarti/flask-skeleton.

tomekwojcik/flask-htauth
https://github.com/tomekwojcik/flask-htauth
Entry file: flask-htauth/example.py
Scanned: 2016-10-12 13:13:43.965794
No vulnerabilities found.


skual/backend-flask
https://github.com/skual/backend-flask
Entry file: None
Scanned: 2016-10-12 13:13:49.404256
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/skual/backend-flask.

memeticlabs/flask-mongokit
https://github.com/memeticlabs/flask-mongokit
Entry file: flask-mongokit/tests/test_base.py
Scanned: 2016-10-12 13:14:00.431464
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mokshaproject/moksha-flask-hello_world
https://github.com/mokshaproject/moksha-flask-hello_world
Entry file: moksha-flask-hello_world/tutorial.py
Scanned: 2016-10-12 13:14:16.751782
No vulnerabilities found.


geekforbrains/squid
https://github.com/geekforbrains/squid
Entry file: squid/run.py
Scanned: 2016-10-12 13:14:18.430023
No vulnerabilities found.


fallingfree/flask-principal-simple-example
https://github.com/fallingfree/flask-principal-simple-example
Entry file: flask-principal-simple-example/auth.py
Scanned: 2016-10-12 13:14:32.881458
Vulnerability 1:
File: flask-principal-simple-example/auth.py
 > User input at line 136, trigger word ".data": 
	user = User.query.filter(User.username == form.username.data).first()
File: flask-principal-simple-example/auth.py
 > reaches line 143, trigger word "flash(": 
	flash('欢迎你, %s' % user.username)



trilan/stencil-flask
https://github.com/trilan/stencil-flask
Entry file: stencil-flask/stencil_flask/template/{app_name}/__init__.py
Scanned: 2016-10-12 13:14:43.665918
No vulnerabilities found.


yangjiandong/flaskr
https://github.com/yangjiandong/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 13:14:50.117381
No vulnerabilities found.


NEETFUTURE/flaskr
https://github.com/NEETFUTURE/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 13:14:54.535962
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

narendranag/Flaskr
https://github.com/narendranag/Flaskr
Entry file: Flaskr/flaskr.py
Scanned: 2016-10-12 13:15:07.353136
No vulnerabilities found.


luanfonceca/flaskbook
https://github.com/luanfonceca/flaskbook
Entry file: flaskbook/mange.py
Scanned: 2016-10-12 13:15:12.738485
No vulnerabilities found.


johnschimmel/ITP-DWD-Fall2012-Week3-First-Server
https://github.com/johnschimmel/ITP-DWD-Fall2012-Week3-First-Server
Entry file: ITP-DWD-Fall2012-Week3-First-Server/app.py
Scanned: 2016-10-12 13:15:17.156799
No vulnerabilities found.


saltycrane/flask-principal-example
https://github.com/saltycrane/flask-principal-example
Entry file: flask-principal-example/main.py
Scanned: 2016-10-12 13:15:18.381670
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

KrzysztofWilczek/FlaskMaschines
https://github.com/KrzysztofWilczek/FlaskMaschines
Entry file: FlaskMaschines/app.py
Scanned: 2016-10-12 13:15:34.750181
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

trenta3dev/ziga
https://github.com/trenta3dev/ziga
Entry file: ziga/ziga/__init__.py
Scanned: 2016-10-12 13:15:41.121804
No vulnerabilities found.


DeaconDesperado/flask_skel
https://github.com/DeaconDesperado/flask_skel
Entry file: flask_skel/listener.py
Scanned: 2016-10-12 13:15:54.551823
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

calebmadrigal/flask-adventures
https://github.com/calebmadrigal/flask-adventures
Entry file: flask-adventures/annuity_calculator.py
Scanned: 2016-10-12 13:16:02.388685
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchibbins/simple-flask
https://github.com/marchibbins/simple-flask
Entry file: simple-flask/simple-flask.py
Scanned: 2016-10-12 13:16:17.660627
No vulnerabilities found.


iambibhas/flask-blog
https://github.com/iambibhas/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 13:16:18.199177
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-blog/venv/lib/python2.7/genericpath.py

imiric/flask-scaffold
https://github.com/imiric/flask-scaffold
Entry file: flask-scaffold/[appname].py
Scanned: 2016-10-12 13:16:41.207937
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

arvs/CURC-flask
https://github.com/arvs/CURC-flask
Entry file: CURC-flask/app.py
Scanned: 2016-10-12 13:16:56.693226
No vulnerabilities found.


suneel0101/flask-adventure
https://github.com/suneel0101/flask-adventure
Entry file: flask-adventure/app.py
Scanned: 2016-10-12 13:16:57.961160
No vulnerabilities found.


memeticlabs/Redis-Flask
https://github.com/memeticlabs/Redis-Flask
Entry file: Redis-Flask/flask_redis.py
Scanned: 2016-10-12 13:17:03.223743
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

DartmouthHackerClub/flask_template
https://github.com/DartmouthHackerClub/flask_template
Entry file: flask_template/app.py
Scanned: 2016-10-12 13:17:08.563856
Vulnerability 1:
File: flask_template/flask_cas.py
 > User input at line 19, trigger word "get(": 
	r = requests.get(validate_url)
Reassigned in: 
	File: flask_template/flask_cas.py
	 > Line 20: doc = etree.fromstring(r.text)
File: flask_template/flask_cas.py
 > reaches line 22, trigger word "replace(": 
	ret_MAYBE_FUNCTION_NAME = dict(((key.replace('{http://www.yale.edu/tp/cas}', ''), value) for (key, value) in recursive_dict(doc[0])[1].items()))



bozoid/testblog
https://github.com/bozoid/testblog
Entry file: testblog/index.py
Scanned: 2016-10-12 13:17:19.672932
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: testblog/venv/lib/python2.7/genericpath.py

alfredhq/alfred-listener
https://github.com/alfredhq/alfred-listener
Entry file: alfred-listener/alfred_listener/__init__.py
Scanned: 2016-10-12 13:17:21.237882
No vulnerabilities found.


dhruvbaldawa/cj_calc
https://github.com/dhruvbaldawa/cj_calc
Entry file: cj_calc/app.py
Scanned: 2016-10-12 13:17:22.640533
No vulnerabilities found.


openplans/shareabouts-flask-client
https://github.com/openplans/shareabouts-flask-client
Entry file: None
Scanned: 2016-10-12 13:17:44.486359
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/openplans/shareabouts-flask-client.

hagino3000/flask-project-template
https://github.com/hagino3000/flask-project-template
Entry file: flask-project-template/app.py
Scanned: 2016-10-12 13:17:45.070074
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-project-template/venv/lib/python2.7/genericpath.py

imaimiami/heroku_flask_template
https://github.com/imaimiami/heroku_flask_template
Entry file: heroku_flask_template/app/__init__.py
Scanned: 2016-10-12 13:17:59.229191
No vulnerabilities found.


jhorman/sample-flask-project
https://github.com/jhorman/sample-flask-project
Entry file: sample-flask-project/app.py
Scanned: 2016-10-12 13:18:03.581829
No vulnerabilities found.


infinitylx/test-task
https://github.com/infinitylx/test-task
Entry file: test-task/application.py
Scanned: 2016-10-12 13:18:15.032205
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

amaudy/flaskr-tutorial
https://github.com/amaudy/flaskr-tutorial
Entry file: flaskr-tutorial/flaskr.py
Scanned: 2016-10-12 13:18:21.416547
No vulnerabilities found.


gavinb/flaskr-eb
https://github.com/gavinb/flaskr-eb
Entry file: flaskr-eb/flaskr.py
Scanned: 2016-10-12 13:18:22.701371
No vulnerabilities found.


vkukushkin88/test_books
https://github.com/vkukushkin88/test_books
Entry file: test_books/db/db_models.py
Scanned: 2016-10-12 13:18:42.501846
No vulnerabilities found.


nicolashery/safire
https://github.com/nicolashery/safire
Entry file: safire/app.py
Scanned: 2016-10-12 13:18:45.755713
No vulnerabilities found.


fjarri/publicfields-backend
https://github.com/fjarri/publicfields-backend
Entry file: publicfields-backend/backend/__init__.py
Scanned: 2016-10-12 13:18:53.187355
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BinOp'>)

sdornan/imgination
https://github.com/sdornan/imgination
Entry file: imgination/application.py
Scanned: 2016-10-12 13:18:59.709915
No vulnerabilities found.


Citizen01/Kozea-project1
https://github.com/Citizen01/Kozea-project1
Entry file: Kozea-project1/index.py
Scanned: 2016-10-12 13:19:06.654375
Vulnerability 1:
File: Kozea-project1/index.py
 > User input at line 110, trigger word "get(": 
	username = request.form.get('username')
Reassigned in: 
	File: Kozea-project1/index.py
	 > Line 122: session['username'] = username
	File: Kozea-project1/index.py
	 > Line 123: session['id'] = User.query.filter_by(username=username).first().id
	File: Kozea-project1/index.py
	 > Line 121: session['logged_in'] = True
File: Kozea-project1/index.py
 > reaches line 124, trigger word "flash(": 
	flash('Welcome on Kozupload, %s !' % username, 'success')



noise/fortune-redis
https://github.com/noise/fortune-redis
Entry file: fortune-redis/fortune_server.py
Scanned: 2016-10-12 13:19:12.312959
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ipedrazas/surl
https://github.com/ipedrazas/surl
Entry file: surl/shortener.py
Scanned: 2016-10-12 13:19:14.640729
Vulnerability 1:
File: surl/shortener.py
 > User input at line 88, trigger word "form[": 
	link = request.form['link']
Reassigned in: 
	File: surl/shortener.py
	 > Line 92: url = objects.find_one('link'link)
File: surl/shortener.py
 > reaches line 95, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('url'URL + url['url_id'])

Vulnerability 2:
File: surl/shortener.py
 > User input at line 88, trigger word "form[": 
	link = request.form['link']
Reassigned in: 
	File: surl/shortener.py
	 > Line 92: url = objects.find_one('link'link)
File: surl/shortener.py
 > reaches line 97, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('url'URL + short_id(link))



dash1291/grabset
https://github.com/dash1291/grabset
Entry file: grabset/grabset.py
Scanned: 2016-10-12 13:19:22.020201
No vulnerabilities found.


alexmic/trippin
https://github.com/alexmic/trippin
Entry file: trippin/server.py
Scanned: 2016-10-12 13:19:25.036109
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

aquaya/sawyer
https://github.com/aquaya/sawyer
Entry file: sawyer/application/__init__.py
Scanned: 2016-10-12 13:19:35.785832
No vulnerabilities found.


metermaid/thirstybot
https://github.com/metermaid/thirstybot
Entry file: thirstybot/app.py
Scanned: 2016-10-12 13:19:43.821589
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

timney/meblog
https://github.com/timney/meblog
Entry file: meblog/app.py
Scanned: 2016-10-12 13:19:51.008304
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

oxtopus/barkeeper
https://github.com/oxtopus/barkeeper
Entry file: barkeeper/barkeeper/app.py
Scanned: 2016-10-12 13:19:59.748767
No vulnerabilities found.


ngopal/quote_generator
https://github.com/ngopal/quote_generator
Entry file: quote_generator/main.py
Scanned: 2016-10-12 13:20:04.384353
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

wesleyk/WhoPaid
https://github.com/wesleyk/WhoPaid
Entry file: WhoPaid/WhoPaid.py
Scanned: 2016-10-12 13:20:09.823973
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

smanek/challenge
https://github.com/smanek/challenge
Entry file: challenge/challenge.py
Scanned: 2016-10-12 13:20:15.313877
No vulnerabilities found.


neocxi/coursemonitor
https://github.com/neocxi/coursemonitor
Entry file: coursemonitor/flask/sessions.py
Scanned: 2016-10-12 13:20:25.720493
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

alfg/inviteme
https://github.com/alfg/inviteme
Entry file: inviteme/inviteme.py
Scanned: 2016-10-12 13:20:27.064471
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kfigaj/FizzBuzzPro
https://github.com/kfigaj/FizzBuzzPro
Entry file: FizzBuzzPro/FizzBuzzPro/fizzbuzz.py
Scanned: 2016-10-12 13:20:35.347105
No vulnerabilities found.


richardneish/lists
https://github.com/richardneish/lists
Entry file: lists/lists/__init__.py
Scanned: 2016-10-12 13:20:43.658444
No vulnerabilities found.


MalphasWats/pyDimension
https://github.com/MalphasWats/pyDimension
Entry file: pyDimension/pyDimension/__init__.py
Scanned: 2016-10-12 13:20:47.070330
Vulnerability 1:
File: pyDimension/pyDimension/views.py
 > User input at line 43, trigger word "form[": 
	filename = request.form['filename']
Reassigned in: 
	File: pyDimension/pyDimension/views.py
	 > Line 45: filename = '%s.txt' % safe_title
	File: pyDimension/pyDimension/views.py
	 > Line 48: articleFile = codecs.open('%s/%s' % (app.config['DRAFTS_ROOT_DIR'], filename),encoding='utf-8', mode='w')
	File: pyDimension/pyDimension/views.py
	 > Line 59: filename = '%s_%s' % (date, get_safe_filename(request.form['filename']))
	File: pyDimension/pyDimension/views.py
	 > Line 61: filename = get_safe_filename(request.form['filename'])
	File: pyDimension/pyDimension/views.py
	 > Line 64: filename = '%s_%s.txt' % (date, safe_title)
File: pyDimension/pyDimension/views.py
 > reaches line 50, trigger word "flash(": 
	flash('There was a problem accessing the file %s/%s' % (app.config['DRAFTS_ROOT_DIR'], filename),category='error')

Vulnerability 2:
File: pyDimension/pyDimension/views.py
 > User input at line 59, trigger word "form[": 
	filename = '%s_%s' % (date, get_safe_filename(request.form['filename']))
Reassigned in: 
	File: pyDimension/pyDimension/views.py
	 > Line 43: filename = request.form['filename']
	File: pyDimension/pyDimension/views.py
	 > Line 45: filename = '%s.txt' % safe_title
	File: pyDimension/pyDimension/views.py
	 > Line 48: articleFile = codecs.open('%s/%s' % (app.config['DRAFTS_ROOT_DIR'], filename),encoding='utf-8', mode='w')
	File: pyDimension/pyDimension/views.py
	 > Line 61: filename = get_safe_filename(request.form['filename'])
	File: pyDimension/pyDimension/views.py
	 > Line 64: filename = '%s_%s.txt' % (date, safe_title)
File: pyDimension/pyDimension/views.py
 > reaches line 50, trigger word "flash(": 
	flash('There was a problem accessing the file %s/%s' % (app.config['DRAFTS_ROOT_DIR'], filename),category='error')

Vulnerability 3:
File: pyDimension/pyDimension/views.py
 > User input at line 61, trigger word "form[": 
	filename = get_safe_filename(request.form['filename'])
Reassigned in: 
	File: pyDimension/pyDimension/views.py
	 > Line 43: filename = request.form['filename']
	File: pyDimension/pyDimension/views.py
	 > Line 45: filename = '%s.txt' % safe_title
	File: pyDimension/pyDimension/views.py
	 > Line 48: articleFile = codecs.open('%s/%s' % (app.config['DRAFTS_ROOT_DIR'], filename),encoding='utf-8', mode='w')
	File: pyDimension/pyDimension/views.py
	 > Line 59: filename = '%s_%s' % (date, get_safe_filename(request.form['filename']))
	File: pyDimension/pyDimension/views.py
	 > Line 64: filename = '%s_%s.txt' % (date, safe_title)
File: pyDimension/pyDimension/views.py
 > reaches line 50, trigger word "flash(": 
	flash('There was a problem accessing the file %s/%s' % (app.config['DRAFTS_ROOT_DIR'], filename),category='error')

Vulnerability 4:
File: pyDimension/pyDimension/access_control.py
 > User input at line 20, trigger word "form[": 
	next = request.form['next']
Reassigned in: 
	File: pyDimension/pyDimension/access_control.py
	 > Line 27: ret_MAYBE_FUNCTION_NAME = redirect(url_for('control_panel'))
	File: pyDimension/pyDimension/access_control.py
	 > Line 31: ret_MAYBE_FUNCTION_NAME = render_template('login.html',next=request.args.get('next'))
File: pyDimension/pyDimension/access_control.py
 > reaches line 25, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect(next)



DanielleSucher/Text-Donation
https://github.com/DanielleSucher/Text-Donation
Entry file: Text-Donation/app.py
Scanned: 2016-10-12 13:20:52.433497
No vulnerabilities found.


flask-restful/flask-restful
https://github.com/flask-restful/flask-restful
Entry file: flask-restful/flask_restful/__init__.py
Scanned: 2016-10-12 13:21:08.123430
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BinOp'>)

rozza/flask-tumblelog
https://github.com/rozza/flask-tumblelog
Entry file: flask-tumblelog/tumblelog/__init__.py
Scanned: 2016-10-12 13:21:10.459300
No vulnerabilities found.


lixxu/flask-paginate
https://github.com/lixxu/flask-paginate
Entry file: flask-paginate/example/app.py
Scanned: 2016-10-12 13:21:16.731464
No vulnerabilities found.


e-dard/flask-s3
https://github.com/e-dard/flask-s3
Entry file: flask-s3/test_flask_static.py
Scanned: 2016-10-12 13:21:28.427980
No vulnerabilities found.


singingwolfboy/flask-misaka
https://github.com/singingwolfboy/flask-misaka
Entry file: flask-misaka/tests.py
Scanned: 2016-10-12 13:21:48.597468
No vulnerabilities found.


rangermeier/flaskberry
https://github.com/rangermeier/flaskberry
Entry file: flaskberry/flaskberry/__init__.py
Scanned: 2016-10-12 13:22:03.325416
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

magaman384/flask-autocomplete
https://github.com/magaman384/flask-autocomplete
Entry file: flask-autocomplete/tests/test.py
Scanned: 2016-10-12 13:22:16.721238
No vulnerabilities found.


GrexIt/flask-login-oauth2
https://github.com/GrexIt/flask-login-oauth2
Entry file: None
Scanned: 2016-10-12 13:22:28.528499
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/GrexIt/flask-login-oauth2.

kielpedia/flask-sqlalchemy-postgres-heroku-example
https://github.com/kielpedia/flask-sqlalchemy-postgres-heroku-example
Entry file: flask-sqlalchemy-postgres-heroku-example/Flasktest/__init__.py
Scanned: 2016-10-12 13:22:35.018578
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

renstrom/passbook_flask_example
https://github.com/renstrom/passbook_flask_example
Entry file: passbook_flask_example/app.py
Scanned: 2016-10-12 13:22:44.353855
No vulnerabilities found.


teozkr/Flask-Pushrod
https://github.com/teozkr/Flask-Pushrod
Entry file: Flask-Pushrod/examples/pushrodr/step3.py
Scanned: 2016-10-12 13:22:54.442338
No vulnerabilities found.


KaviCorp/flask_pysaml2
https://github.com/KaviCorp/flask_pysaml2
Entry file: flask_pysaml2/tests/test_saml.py
Scanned: 2016-10-12 13:23:00.943356
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

MostAwesomeDude/flask-holster
https://github.com/MostAwesomeDude/flask-holster
Entry file: flask-holster/test.py
Scanned: 2016-10-12 13:23:06.648868
No vulnerabilities found.


stevenewey/ssedemo
https://github.com/stevenewey/ssedemo
Entry file: ssedemo/sse_server.py
Scanned: 2016-10-12 13:23:22.907803
No vulnerabilities found.


LarryEitel/gsapi
https://github.com/LarryEitel/gsapi
Entry file: gsapi/gsapi/run.py
Scanned: 2016-10-12 13:23:27.129004
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

gracedme/flaskblog
https://github.com/gracedme/flaskblog
Entry file: flaskblog/flat.py
Scanned: 2016-10-12 13:23:29.222341
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flaskblog/env/lib/python2.7/genericpath.py

car34/flasktut
https://github.com/car34/flasktut
Entry file: flasktut/app/__init__.py
Scanned: 2016-10-12 13:23:36.587309
No vulnerabilities found.


Pokom/flasking
https://github.com/Pokom/flasking
Entry file: flasking/flaskr.py
Scanned: 2016-10-12 13:23:48.556240
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flasking/venv/lib/python2.7/genericpath.py

jasonamyers/flaskr
https://github.com/jasonamyers/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 13:23:49.069797
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

nirix-old/flaskapp
https://github.com/nirix-old/flaskapp
Entry file: flaskapp/flaskapp/application.py
Scanned: 2016-10-12 13:23:52.578829
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

femmerling/EmeraldBox
https://github.com/femmerling/EmeraldBox
Entry file: EmeraldBox/app/__init__.py
Scanned: 2016-10-12 13:24:07.464481
No vulnerabilities found.


corysandahl/FlaskAPI
https://github.com/corysandahl/FlaskAPI
Entry file: FlaskAPI/ProdAPI.py
Scanned: 2016-10-12 13:24:08.728415
No vulnerabilities found.


pearkes/invite
https://github.com/pearkes/invite
Entry file: invite/app.py
Scanned: 2016-10-12 13:24:12.050691
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

MalphasWats/flask-blueprint-loader
https://github.com/MalphasWats/flask-blueprint-loader
Entry file: flask-blueprint-loader/dashboard/dashboard.py
Scanned: 2016-10-12 13:24:24.363949
No vulnerabilities found.


tswast/cryptogram-flask
https://github.com/tswast/cryptogram-flask
Entry file: cryptogram-flask/cryptogram.py
Scanned: 2016-10-12 13:24:29.119141
No vulnerabilities found.


Fibio/flask-mongoset
https://github.com/Fibio/flask-mongoset
Entry file: flask-mongoset/flask_mongoset.py
Scanned: 2016-10-12 13:24:38.110207
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

suneel0101/flask-hn
https://github.com/suneel0101/flask-hn
Entry file: flask-hn/app.py
Scanned: 2016-10-12 13:24:45.330288
No vulnerabilities found.


lvidarte/flask-examples
https://github.com/lvidarte/flask-examples
Entry file: flask-examples/minitwit/minitwit.py
Scanned: 2016-10-12 13:24:49.845267
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.If'>)

mstriemer/todo-flask
https://github.com/mstriemer/todo-flask
Entry file: todo-flask/todo.py
Scanned: 2016-10-12 13:24:54.054162
No vulnerabilities found.


tribbettz/flask-microblog
https://github.com/tribbettz/flask-microblog
Entry file: flask-microblog/app/__init__.py
Scanned: 2016-10-12 13:25:02.450867
No vulnerabilities found.


codecool/flask-uploads
https://github.com/codecool/flask-uploads
Entry file: flask-uploads/test-uploads.py
Scanned: 2016-10-12 13:25:12.892028
No vulnerabilities found.


nirix-old/mantid_flask
https://github.com/nirix-old/mantid_flask
Entry file: None
Scanned: 2016-10-12 13:25:25.359928
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/nirix-old/mantid_flask.

DartmouthHackerClub/blitzlistr-flask
https://github.com/DartmouthHackerClub/blitzlistr-flask
Entry file: blitzlistr-flask/app.py
Scanned: 2016-10-12 13:25:29.685293
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

otsuarez/flask-blog
https://github.com/otsuarez/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 13:25:30.219965
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-blog/venv/lib/python2.7/genericpath.py

philwade/flask-presentation
https://github.com/philwade/flask-presentation
Entry file: flask-presentation/code/loop.py
Scanned: 2016-10-12 13:25:38.254344
No vulnerabilities found.


mattdeboard/flask-cloudfront
https://github.com/mattdeboard/flask-cloudfront
Entry file: flask-cloudfront/flask_cloudfront/tests/base.py
Scanned: 2016-10-12 13:25:45.595652
No vulnerabilities found.


apjd/flask-gae
https://github.com/apjd/flask-gae
Entry file: flask-gae/lib/flask/app.py
Scanned: 2016-10-12 13:25:50.129142
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

demitri/DMFlaskTemplate
https://github.com/demitri/DMFlaskTemplate
Entry file: DMFlaskTemplate/myapplication/myapplication/__init__.py
Scanned: 2016-10-12 13:26:03.077933
No vulnerabilities found.


Zanfa/Twilio-SMS-Voting
https://github.com/Zanfa/Twilio-SMS-Voting
Entry file: Twilio-SMS-Voting/server.py
Scanned: 2016-10-12 13:26:10.579397
No vulnerabilities found.


jvoisin/pyste
https://github.com/jvoisin/pyste
Entry file: pyste/flaskr.py
Scanned: 2016-10-12 13:26:12.873364
Vulnerability 1:
File: pyste/flaskr.py
 > User input at line 57, trigger word "form[": 
	delta = datetime.timedelta(seconds=int(request.form['expiration']))
Reassigned in: 
	File: pyste/flaskr.py
	 > Line 58: expiration = datetime.datetime.now() + delta
	File: pyste/flaskr.py
	 > Line 60: expiration = datetime.datetime(1, 1, 1)
File: pyste/flaskr.py
 > reaches line 69, trigger word "execute(": 
	g.db.execute('INSERT INTO PASTE (id, title, expiration, content) VALUES (?, ?, ?, ?)', (identifier, request.form['title'], expiration, paste))

Vulnerability 2:
File: pyste/flaskr.py
 > User input at line 62, trigger word "form[": 
	identifier = hashlib.sha1(request.form['input'] + time.ctime()).hexdigest()[8]
Reassigned in: 
	File: pyste/flaskr.py
	 > Line 78: ret_MAYBE_FUNCTION_NAME = render_template('index.html',identifier=identifier, url=request.url)
	File: pyste/flaskr.py
	 > Line 79: ret_MAYBE_FUNCTION_NAME = render_template('index.html')
	File: pyste/flaskr.py
	 > Line 55: ret_MAYBE_FUNCTION_NAME = render_template('index.html')
File: pyste/flaskr.py
 > reaches line 69, trigger word "execute(": 
	g.db.execute('INSERT INTO PASTE (id, title, expiration, content) VALUES (?, ?, ?, ?)', (identifier, request.form['title'], expiration, paste))

Vulnerability 3:
File: pyste/flaskr.py
 > User input at line 63, trigger word "form[": 
	paste = highlight(request.form['input'], guess_lexer(request.form['input']), HtmlFormatter(linenos='table'))
File: pyste/flaskr.py
 > reaches line 69, trigger word "execute(": 
	g.db.execute('INSERT INTO PASTE (id, title, expiration, content) VALUES (?, ?, ?, ?)', (identifier, request.form['title'], expiration, paste))



codeanu/flask-login-oauth2
https://github.com/codeanu/flask-login-oauth2
Entry file: None
Scanned: 2016-10-12 13:26:25.372040
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/codeanu/flask-login-oauth2.

sclabs/flask.gilgi.org
https://github.com/sclabs/flask.gilgi.org
Entry file: None
Scanned: 2016-10-12 13:26:46.442681
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/sclabs/flask.gilgi.org.

MalphasWats/instruments
https://github.com/MalphasWats/instruments
Entry file: instruments/instruments/__init__.py
Scanned: 2016-10-12 13:26:53.030298
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

msapoz/toothsometreats
https://github.com/msapoz/toothsometreats
Entry file: toothsometreats/toothsome.py
Scanned: 2016-10-12 13:26:55.372450
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

george25c/helloflask
https://github.com/george25c/helloflask
Entry file: helloflask/app.py
Scanned: 2016-10-12 13:27:03.644724
No vulnerabilities found.


nirix/alchemyflask
https://github.com/nirix/alchemyflask
Entry file: alchemyflask/app.py
Scanned: 2016-10-12 13:27:10.909958
No vulnerabilities found.


pwyf/IATI-Implementation-Schedules
https://github.com/pwyf/IATI-Implementation-Schedules
Entry file: IATI-Implementation-Schedules/impschedules/__init__.py
Scanned: 2016-10-12 13:27:17.130121
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sigmavirus24/subscribed
https://github.com/sigmavirus24/subscribed
Entry file: subscribed/subscribed/app.py
Scanned: 2016-10-12 13:27:26.481977
No vulnerabilities found.


gbaldera/todo
https://github.com/gbaldera/todo
Entry file: todo/todo/__init__.py
Scanned: 2016-10-12 13:27:30.264255
No vulnerabilities found.


mgill25/Blog
https://github.com/mgill25/Blog
Entry file: Blog/Blog/__init__.py
Scanned: 2016-10-12 13:27:38.080369
No vulnerabilities found.


hernamesbarbara/NAICS
https://github.com/hernamesbarbara/NAICS
Entry file: NAICS/app.py
Scanned: 2016-10-12 13:27:54.489834
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

scwu/Evernote-Blog-Engine
https://github.com/scwu/Evernote-Blog-Engine
Entry file: Evernote-Blog-Engine/blog.py
Scanned: 2016-10-12 13:27:55.783947
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ybz/yaniv_bz
https://github.com/ybz/yaniv_bz
Entry file: yaniv_bz/app.py
Scanned: 2016-10-12 13:28:14.032735
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Lambda'>)

jul/wsgi_social_experminet
https://github.com/jul/wsgi_social_experminet
Entry file: wsgi_social_experminet/www/socialize.py
Scanned: 2016-10-12 13:28:27.286165
No vulnerabilities found.


bezfeng/skinmd-frontend
https://github.com/bezfeng/skinmd-frontend
Entry file: skinmd-frontend/script_server.py
Scanned: 2016-10-12 13:28:35.890902
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

barosl/photox
https://github.com/barosl/photox
Entry file: photox/photox.py
Scanned: 2016-10-12 13:28:37.217309
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

thomasboyt/txtRPG
https://github.com/thomasboyt/txtRPG
Entry file: txtRPG/rpg_app/__init__.py
Scanned: 2016-10-12 13:28:38.471760
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

smanek/challenge
https://github.com/smanek/challenge
Entry file: challenge/challenge.py
Scanned: 2016-10-12 13:28:52.408420
No vulnerabilities found.


hacksu/ksu-flash-info
https://github.com/hacksu/ksu-flash-info
Entry file: ksu-flash-info/app.py
Scanned: 2016-10-12 13:28:56.969312
No vulnerabilities found.


adamcharnock/docsite
https://github.com/adamcharnock/docsite
Entry file: docsite/server.py
Scanned: 2016-10-12 13:29:04.208287
No vulnerabilities found.


qnub/cavy
https://github.com/qnub/cavy
Entry file: cavy/project/flask/sessions.py
Scanned: 2016-10-12 13:29:17.606269
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

DazWorrall/flask-sse
https://github.com/DazWorrall/flask-sse
Entry file: flask-sse/example/example.py
Scanned: 2016-10-12 13:29:37.578339
No vulnerabilities found.


hobbeswalsh/flask-sillywalk
https://github.com/hobbeswalsh/flask-sillywalk
Entry file: flask-sillywalk/flask_sillywalk/sillywalk.py
Scanned: 2016-10-12 13:29:39.126072
No vulnerabilities found.


twip/flask_twip
https://github.com/twip/flask_twip
Entry file: flask_twip/examples/heroku/app.py
Scanned: 2016-10-12 13:29:47.659278
No vulnerabilities found.


doobeh/Flask-S3-Uploader
https://github.com/doobeh/Flask-S3-Uploader
Entry file: Flask-S3-Uploader/app.py
Scanned: 2016-10-12 13:29:57.502712
No vulnerabilities found.


tzulberti/Flask-PyPi-Proxy
https://github.com/tzulberti/Flask-PyPi-Proxy
Entry file: Flask-PyPi-Proxy/flask_pypi_proxy/app.py
Scanned: 2016-10-12 13:30:13.677935
No vulnerabilities found.


rehandalal/flask-funnel
https://github.com/rehandalal/flask-funnel
Entry file: flask-funnel/flask_funnel/tests/test_funnel.py
Scanned: 2016-10-12 13:30:31.383107
No vulnerabilities found.


rbin/OctoFlask
https://github.com/rbin/OctoFlask
Entry file: OctoFlask/__init__.py
Scanned: 2016-10-12 13:30:33.884427
No vulnerabilities found.


mimming/python-flask-google-api-starter
https://github.com/mimming/python-flask-google-api-starter
Entry file: python-flask-google-api-starter/cal.py
Scanned: 2016-10-12 13:30:38.108452
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

MichelleGlauser/Flask
https://github.com/MichelleGlauser/Flask
Entry file: Flask/test_hello.py
Scanned: 2016-10-12 13:30:47.829311
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tzangms/python-websocket-example
https://github.com/tzangms/python-websocket-example
Entry file: python-websocket-example/app/__init__.py
Scanned: 2016-10-12 13:30:57.550211
No vulnerabilities found.


jakecoffman/flask-bootstrap
https://github.com/jakecoffman/flask-bootstrap
Entry file: flask-bootstrap/flaskr.py
Scanned: 2016-10-12 13:31:05.454313
No vulnerabilities found.


lomatus/flask2sae
https://github.com/lomatus/flask2sae
Entry file: flask2sae/1/app/__init__.py
Scanned: 2016-10-12 13:31:13.920013
No vulnerabilities found.


Roasbeef/FlaskrNews
https://github.com/Roasbeef/FlaskrNews
Entry file: FlaskrNews/libs/flask/sessions.py
Scanned: 2016-10-12 13:31:19.748548
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marksteve/flask-stathat
https://github.com/marksteve/flask-stathat
Entry file: flask-stathat/example.py
Scanned: 2016-10-12 13:31:29.163057
No vulnerabilities found.


byslee3/Flask_Tutorial
https://github.com/byslee3/Flask_Tutorial
Entry file: Flask_Tutorial/flaskr.py
Scanned: 2016-10-12 13:31:33.537966
No vulnerabilities found.


gzb1985/flask-boilerplate
https://github.com/gzb1985/flask-boilerplate
Entry file: flask-boilerplate/flask_boilerplate/__init__.py
Scanned: 2016-10-12 13:31:39.722575
No vulnerabilities found.


scolex/flask-forum
https://github.com/scolex/flask-forum
Entry file: flask-forum/app/__init__.py
Scanned: 2016-10-12 13:31:40.934856
No vulnerabilities found.


bwghughes/flasksse
https://github.com/bwghughes/flasksse
Entry file: flasksse/app.py
Scanned: 2016-10-12 13:31:48.133318
No vulnerabilities found.


soccermetrics/flask-skeleton
https://github.com/soccermetrics/flask-skeleton
Entry file: None
Scanned: 2016-10-12 13:31:57.135181
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/soccermetrics/flask-skeleton.

kvesteri/flask-jinjahelpers
https://github.com/kvesteri/flask-jinjahelpers
Entry file: flask-jinjahelpers/tests/__init__.py
Scanned: 2016-10-12 13:32:05.471905
No vulnerabilities found.


jmhobbs/redboard
https://github.com/jmhobbs/redboard
Entry file: redboard/src/redboard_server.py
Scanned: 2016-10-12 13:32:13.810791
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kates/flask-mold
https://github.com/kates/flask-mold
Entry file: flask-mold/app.py
Scanned: 2016-10-12 13:32:17.454370
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

JanStevens/ArduinoPi-Python
https://github.com/JanStevens/ArduinoPi-Python
Entry file: ArduinoPi-Python/main.py
Scanned: 2016-10-12 13:32:29.802002
No vulnerabilities found.


landakram/microblog
https://github.com/landakram/microblog
Entry file: microblog/app.py
Scanned: 2016-10-12 13:32:34.202474
No vulnerabilities found.


mies/wercker-flask-api
https://github.com/mies/wercker-flask-api
Entry file: wercker-flask-api/app.py
Scanned: 2016-10-12 13:32:39.410707
No vulnerabilities found.


dengmin/base_framework_flask
https://github.com/dengmin/base_framework_flask
Entry file: None
Scanned: 2016-10-12 13:32:41.701117
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/dengmin/base_framework_flask.

tquach/talent-curator
https://github.com/tquach/talent-curator
Entry file: talent-curator/talent_curator/__init__.py
Scanned: 2016-10-12 13:32:53.788810
No vulnerabilities found.


vitalk/flask-mailer
https://github.com/vitalk/flask-mailer
Entry file: flask-mailer/tests/conftest.py
Scanned: 2016-10-12 13:32:55.453309
No vulnerabilities found.


drdaeman/flask-toybox
https://github.com/drdaeman/flask-toybox
Entry file: flask-toybox/tests/test_negotiation.py
Scanned: 2016-10-12 13:32:58.933590
No vulnerabilities found.


lorden/flaskeleton
https://github.com/lorden/flaskeleton
Entry file: flaskeleton/app/__init__.py
Scanned: 2016-10-12 13:33:05.427999
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

daneoshiga/flaskr
https://github.com/daneoshiga/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 13:33:13.973328
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

Khady/flaskdotahorrible
https://github.com/Khady/flaskdotahorrible
Entry file: flaskdotahorrible/dota2.py
Scanned: 2016-10-12 13:33:23.762190
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

Ruke89/FlaskSite
https://github.com/Ruke89/FlaskSite
Entry file: FlaskSite/runServer.py
Scanned: 2016-10-12 13:33:34.737411
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tribbettz/flask-mongo-tumblelog
https://github.com/tribbettz/flask-mongo-tumblelog
Entry file: flask-mongo-tumblelog/app/__init__.py
Scanned: 2016-10-12 13:33:40.530268
No vulnerabilities found.


tobiasandtobias/flask-assetslite
https://github.com/tobiasandtobias/flask-assetslite
Entry file: flask-assetslite/tests/tests.py
Scanned: 2016-10-12 13:33:41.929248
No vulnerabilities found.


zhangcheng/Flask-Sandbox
https://github.com/zhangcheng/Flask-Sandbox
Entry file: Flask-Sandbox/src/app.py
Scanned: 2016-10-12 13:33:49.267220
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kracekumar/flask-apache
https://github.com/kracekumar/flask-apache
Entry file: flask-apache/app.py
Scanned: 2016-10-12 13:33:58.960301
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

bcho-archive/flask-bootstrap
https://github.com/bcho-archive/flask-bootstrap
Entry file: flask-bootstrap/origin/app.py
Scanned: 2016-10-12 13:34:06.177263
No vulnerabilities found.


standyro/flask-testbed
https://github.com/standyro/flask-testbed
Entry file: flask-testbed/test.py
Scanned: 2016-10-12 13:34:15.428278
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sfermigier/flask-linktester
https://github.com/sfermigier/flask-linktester
Entry file: flask-linktester/tests/dummy_app.py
Scanned: 2016-10-12 13:34:17.942940
No vulnerabilities found.


mstriemer/todo-flask
https://github.com/mstriemer/todo-flask
Entry file: todo-flask/todo.py
Scanned: 2016-10-12 13:34:41.133211
No vulnerabilities found.


kageurufu/flask-couchdb
https://github.com/kageurufu/flask-couchdb
Entry file: flask-couchdb/example/guestbook.py
Scanned: 2016-10-12 13:34:42.553418
No vulnerabilities found.


jharkins/restful-flask
https://github.com/jharkins/restful-flask
Entry file: restful-flask/rest_ideas.py
Scanned: 2016-10-12 13:34:49.786309
No vulnerabilities found.


yeradis/flask-nanoblog
https://github.com/yeradis/flask-nanoblog
Entry file: flask-nanoblog/nanoblog/__init__.py
Scanned: 2016-10-12 13:34:56.249264
No vulnerabilities found.


lubiana/flask-quotedb
https://github.com/lubiana/flask-quotedb
Entry file: flask-quotedb/app/__init__.py
Scanned: 2016-10-12 13:34:59.479633
No vulnerabilities found.


mercul3s/flask_tutorial
https://github.com/mercul3s/flask_tutorial
Entry file: flask_tutorial/flaskr.py
Scanned: 2016-10-12 13:35:06.752767
No vulnerabilities found.


SAFeSEA/pyEssayAnalyser
https://github.com/SAFeSEA/pyEssayAnalyser
Entry file: pyEssayAnalyser/src/pyEssayAnalyser.py
Scanned: 2016-10-12 13:35:20.438932
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-js-hostname-example
https://github.com/mitsuhiko/flask-js-hostname-example
Entry file: flask-js-hostname-example/testapp.py
Scanned: 2016-10-12 13:35:37.151566
No vulnerabilities found.


proto/flask-simple-blog
https://github.com/proto/flask-simple-blog
Entry file: flask-simple-blog/app.py
Scanned: 2016-10-12 13:35:41.349056
No vulnerabilities found.


colinkahn/flask-redis-browserid
https://github.com/colinkahn/flask-redis-browserid
Entry file: flask-redis-browserid/run.py
Scanned: 2016-10-12 13:35:42.569808
No vulnerabilities found.


pleomax00/flask-mongo-skel
https://github.com/pleomax00/flask-mongo-skel
Entry file: flask-mongo-skel/src/thirdparty/flask/sessions.py
Scanned: 2016-10-12 13:36:03.056853
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

iolab12/python_flask_demo
https://github.com/iolab12/python_flask_demo
Entry file: python_flask_demo/todo.py
Scanned: 2016-10-12 13:36:16.828192
No vulnerabilities found.


eneldoserrata/flask-python-dominicana-apps
https://github.com/eneldoserrata/flask-python-dominicana-apps
Entry file: flask-python-dominicana-apps/app/__init__.py
Scanned: 2016-10-12 13:36:19.030930
No vulnerabilities found.


shinderuman/python_flask_helloworld
https://github.com/shinderuman/python_flask_helloworld
Entry file: python_flask_helloworld/app.py
Scanned: 2016-10-12 13:36:35.410503
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: python_flask_helloworld/lib/python2.7/genericpath.py

ilyapuchka/PyObjC-FlaskAdmin
https://github.com/ilyapuchka/PyObjC-FlaskAdmin
Entry file: PyObjC-FlaskAdmin/myadmin/__init__.py
Scanned: 2016-10-12 13:36:37.759284
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tnebel/minitwit
https://github.com/tnebel/minitwit
Entry file: minitwit/minitwit.py
Scanned: 2016-10-12 13:36:56.530186
No vulnerabilities found.


renn999/PyBlogtle
https://github.com/renn999/PyBlogtle
Entry file: None
Scanned: 2016-10-12 13:37:00.814029
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/renn999/PyBlogtle.

bezfeng/skinmd-frontend
https://github.com/bezfeng/skinmd-frontend
Entry file: skinmd-frontend/script_server.py
Scanned: 2016-10-12 13:37:30.770965
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

orangejulius/jlink
https://github.com/orangejulius/jlink
Entry file: jlink/jlink.py
Scanned: 2016-10-12 13:37:38.036192
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sramana/meetup-photos
https://github.com/sramana/meetup-photos
Entry file: meetup-photos/main.py
Scanned: 2016-10-12 13:37:42.567358
No vulnerabilities found.


DartmouthHackerClub/dnd_search
https://github.com/DartmouthHackerClub/dnd_search
Entry file: dnd_search/app.py
Scanned: 2016-10-12 13:37:43.877160
No vulnerabilities found.


bigsnarfdude/netflix_examples
https://github.com/bigsnarfdude/netflix_examples
Entry file: netflix_examples/flask_hello_world.py
Scanned: 2016-10-12 13:37:50.197722
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kierandarcy/qrimage
https://github.com/kierandarcy/qrimage
Entry file: qrimage/app.py
Scanned: 2016-10-12 13:37:56.533033
No vulnerabilities found.


ekaputra07/poredit
https://github.com/ekaputra07/poredit
Entry file: poredit/poredit/poredit.py
Scanned: 2016-10-12 13:38:01.310990
No vulnerabilities found.


jualvarez/worktracker
https://github.com/jualvarez/worktracker
Entry file: worktracker/worktracker.py
Scanned: 2016-10-12 13:38:08.688458
Vulnerability 1:
File: worktracker/worktracker.py
 > User input at line 146, trigger word "get(": 
	project = g.db.query(Project).get(id)
Reassigned in: 
	File: worktracker/worktracker.py
	 > Line 142: project = None
	File: worktracker/worktracker.py
	 > Line 154: project = Project(request.form['name'])
	File: worktracker/worktracker.py
	 > Line 159: ret_MAYBE_FUNCTION_NAME = render_template('project_show.html',project=project, projects=projects)
File: worktracker/worktracker.py
 > reaches line 158, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('%s%d' % (url_for('project_show'), project.id))

Vulnerability 2:
File: worktracker/worktracker.py
 > User input at line 154, trigger word "form[": 
	project = Project(request.form['name'])
Reassigned in: 
	File: worktracker/worktracker.py
	 > Line 142: project = None
	File: worktracker/worktracker.py
	 > Line 146: project = g.db.query(Project).get(id)
	File: worktracker/worktracker.py
	 > Line 159: ret_MAYBE_FUNCTION_NAME = render_template('project_show.html',project=project, projects=projects)
File: worktracker/worktracker.py
 > reaches line 158, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('%s%d' % (url_for('project_show'), project.id))

Vulnerability 3:
File: worktracker/worktracker.py
 > User input at line 146, trigger word "get(": 
	project = g.db.query(Project).get(id)
Reassigned in: 
	File: worktracker/worktracker.py
	 > Line 142: project = None
	File: worktracker/worktracker.py
	 > Line 154: project = Project(request.form['name'])
	File: worktracker/worktracker.py
	 > Line 159: ret_MAYBE_FUNCTION_NAME = render_template('project_show.html',project=project, projects=projects)
File: worktracker/worktracker.py
 > reaches line 158, trigger word "url_for(": 
	ret_MAYBE_FUNCTION_NAME = redirect('%s%d' % (url_for('project_show'), project.id))

Vulnerability 4:
File: worktracker/worktracker.py
 > User input at line 154, trigger word "form[": 
	project = Project(request.form['name'])
Reassigned in: 
	File: worktracker/worktracker.py
	 > Line 142: project = None
	File: worktracker/worktracker.py
	 > Line 146: project = g.db.query(Project).get(id)
	File: worktracker/worktracker.py
	 > Line 159: ret_MAYBE_FUNCTION_NAME = render_template('project_show.html',project=project, projects=projects)
File: worktracker/worktracker.py
 > reaches line 158, trigger word "url_for(": 
	ret_MAYBE_FUNCTION_NAME = redirect('%s%d' % (url_for('project_show'), project.id))



rochacon/simple-gapps-group-signup
https://github.com/rochacon/simple-gapps-group-signup
Entry file: simple-gapps-group-signup/app.py
Scanned: 2016-10-12 13:38:17.943142
No vulnerabilities found.


Timothee/Passeplat
https://github.com/Timothee/Passeplat
Entry file: Passeplat/passeplat.py
Scanned: 2016-10-12 13:38:20.287871
No vulnerabilities found.


blazarus/Link-Shortener
https://github.com/blazarus/Link-Shortener
Entry file: Link-Shortener/linkshort/__init__.py
Scanned: 2016-10-12 13:38:31.560362
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cenobites/flask-jsonrpc
https://github.com/cenobites/flask-jsonrpc
Entry file: flask-jsonrpc/run.py
Scanned: 2016-10-12 13:38:45.200719
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

insynchq/flask-googlelogin
https://github.com/insynchq/flask-googlelogin
Entry file: flask-googlelogin/example_offline.py
Scanned: 2016-10-12 13:38:51.180471
No vulnerabilities found.


shea256/flask-app-generator
https://github.com/shea256/flask-app-generator
Entry file: flask-app-generator/resources/basic_app/app.py
Scanned: 2016-10-12 13:38:57.615558
No vulnerabilities found.


albertogg/flask-bootstrap-skel
https://github.com/albertogg/flask-bootstrap-skel
Entry file: flask-bootstrap-skel/application/__init__.py
Scanned: 2016-10-12 13:39:01.603545
No vulnerabilities found.


alecthomas/flask_injector
https://github.com/alecthomas/flask_injector
Entry file: flask_injector/flask_injector_tests.py
Scanned: 2016-10-12 13:39:09.356330
No vulnerabilities found.


ema/flask-moresql
https://github.com/ema/flask-moresql
Entry file: flask-moresql/flask_moresql.py
Scanned: 2016-10-12 13:39:18.775509
No vulnerabilities found.


gregorynicholas/flask-gae_blobstore
https://github.com/gregorynicholas/flask-gae_blobstore
Entry file: flask-gae_blobstore/flask_gae_blobstore_tests.py
Scanned: 2016-10-12 13:39:33.343477
No vulnerabilities found.


icecreammatt/flask-empty
https://github.com/icecreammatt/flask-empty
Entry file: flask-empty/app/__init__.py
Scanned: 2016-10-12 13:39:43.937267
No vulnerabilities found.


david-torres/flask-quickstart
https://github.com/david-torres/flask-quickstart
Entry file: flask-quickstart/application/__init__.py
Scanned: 2016-10-12 13:39:48.038419
No vulnerabilities found.


rahulbot/GV-GetToKnow-flask
https://github.com/rahulbot/GV-GetToKnow-flask
Entry file: GV-GetToKnow-flask/gettoknow.py
Scanned: 2016-10-12 13:39:58.158202
No vulnerabilities found.


oturing/flask-br
https://github.com/oturing/flask-br
Entry file: flask-br/examples/flaskr/flaskr.py
Scanned: 2016-10-12 13:40:02.932922
No vulnerabilities found.


ismaild/flaskr-bdd
https://github.com/ismaild/flaskr-bdd
Entry file: flaskr-bdd/flaskr.py
Scanned: 2016-10-12 13:40:09.235049
No vulnerabilities found.


regadas/flask-tornado-websocket
https://github.com/regadas/flask-tornado-websocket
Entry file: flask-tornado-websocket/app/__init__.py
Scanned: 2016-10-12 13:40:19.567686
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lomatus/flask2sae
https://github.com/lomatus/flask2sae
Entry file: flask2sae/1/app/__init__.py
Scanned: 2016-10-12 13:40:22.003146
No vulnerabilities found.


yaniv-aknin/aknin-flask-skeleton
https://github.com/yaniv-aknin/aknin-flask-skeleton
Entry file: aknin-flask-skeleton/application/app.py
Scanned: 2016-10-12 13:40:47.985078
No vulnerabilities found.


marksteve/flask-stathat
https://github.com/marksteve/flask-stathat
Entry file: flask-stathat/example.py
Scanned: 2016-10-12 13:40:52.308830
No vulnerabilities found.


pengfei-xue/openshift-flask-mongdb
https://github.com/pengfei-xue/openshift-flask-mongdb
Entry file: openshift-flask-mongdb/blog/main.py
Scanned: 2016-10-12 13:40:59.931906
Vulnerability 1:
File: openshift-flask-mongdb/blog/blueprints/apis/views.py
 > User input at line 27, trigger word "get(": 
	term = request.args.get('term', None)
File: openshift-flask-mongdb/blog/blueprints/apis/views.py
 > reaches line 33, trigger word "filter(": 
	result = list(filter(term.lower() in tag.lower(), set(result)))



ncweinhold/flask-knockout-example
https://github.com/ncweinhold/flask-knockout-example
Entry file: flask-knockout-example/app.py
Scanned: 2016-10-12 13:41:02.180501
No vulnerabilities found.


gkoberger/flask-heroku
https://github.com/gkoberger/flask-heroku
Entry file: flask-heroku/app.py
Scanned: 2016-10-12 13:41:09.886356
No vulnerabilities found.


theho/flask-riak-skeleton
https://github.com/theho/flask-riak-skeleton
Entry file: None
Scanned: 2016-10-12 13:41:20.946708
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/theho/flask-riak-skeleton.

davirtavares/flask-complexform
https://github.com/davirtavares/flask-complexform
Entry file: flask-complexform/testeflask.py
Scanned: 2016-10-12 13:41:40.132495
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

brab/flaskr
https://github.com/brab/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 13:41:42.626186
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lmeunier/flasktodo
https://github.com/lmeunier/flasktodo
Entry file: flasktodo/application.py
Scanned: 2016-10-12 13:41:51.668143
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lqwinters/Flaskr
https://github.com/lqwinters/Flaskr
Entry file: Flaskr/flaskr.py
Scanned: 2016-10-12 13:42:02.367955
No vulnerabilities found.


thermosilla/flaskapp
https://github.com/thermosilla/flaskapp
Entry file: flaskapp/flaskapp/application.py
Scanned: 2016-10-12 13:42:08.875822
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marcus-darden/flask1
https://github.com/marcus-darden/flask1
Entry file: flask1/app.py
Scanned: 2016-10-12 13:42:22.585366
No vulnerabilities found.


Alir3z4/flask-microblog-sqlalchemy
https://github.com/Alir3z4/flask-microblog-sqlalchemy
Entry file: flask-microblog-sqlalchemy/app/__init__.py
Scanned: 2016-10-12 13:42:34.326724
No vulnerabilities found.


seansawyer/foh
https://github.com/seansawyer/foh
Entry file: foh/foh/__init__.py
Scanned: 2016-10-12 13:42:40.683688
No vulnerabilities found.


feik/flask-blog
https://github.com/feik/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 13:42:43.222828
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-blog/venv/lib/python2.7/genericpath.py

randallm/whatsthehomework_flask
https://github.com/randallm/whatsthehomework_flask
Entry file: whatsthehomework_flask/wth/__init__.py
Scanned: 2016-10-12 13:42:53.124644
No vulnerabilities found.


robottaway/flask_websocket
https://github.com/robottaway/flask_websocket
Entry file: flask_websocket/app/__init__.py
Scanned: 2016-10-12 13:43:02.829495
No vulnerabilities found.


vladke/flask-blog
https://github.com/vladke/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 13:43:09.383104
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-blog/venv/lib/python2.7/genericpath.py

protunt/flask-blog
https://github.com/protunt/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 13:43:22.452199
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-blog/venv/lib/python2.7/genericpath.py

makotoworld/flask-example
https://github.com/makotoworld/flask-example
Entry file: flask-example/main.py
Scanned: 2016-10-12 13:43:33.980359
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mikepea/flask_playing
https://github.com/mikepea/flask_playing
Entry file: None
Scanned: 2016-10-12 13:43:41.289941
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/mikepea/flask_playing.

feigner/flask-testbed
https://github.com/feigner/flask-testbed
Entry file: flask-testbed/test.py
Scanned: 2016-10-12 13:43:43.850532
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

smileyteresa/flask-blog
https://github.com/smileyteresa/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 13:43:48.389628
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-blog/venv/lib/python2.7/genericpath.py

naot-said/test-flask
https://github.com/naot-said/test-flask
Entry file: test-flask/hello.py
Scanned: 2016-10-12 13:43:53.709265
No vulnerabilities found.


shabda/learning_flask
https://github.com/shabda/learning_flask
Entry file: learning_flask/flaskr/flaskr.py
Scanned: 2016-10-12 13:44:00.011379
No vulnerabilities found.


RainCT/flask-template-with-social
https://github.com/RainCT/flask-template-with-social
Entry file: flask-template-with-social/webapp/__init__.py
Scanned: 2016-10-12 13:44:23.961396
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rdmurphy/flask-reservoir-jsonp-wrapper
https://github.com/rdmurphy/flask-reservoir-jsonp-wrapper
Entry file: flask-reservoir-jsonp-wrapper/grabber.py
Scanned: 2016-10-12 13:44:45.213195
No vulnerabilities found.


gagansaini/example-python-flask
https://github.com/gagansaini/example-python-flask
Entry file: example-python-flask/app.py
Scanned: 2016-10-12 13:44:50.281278
No vulnerabilities found.


ncweinhold/flask-code-sharing
https://github.com/ncweinhold/flask-code-sharing
Entry file: flask-code-sharing/pasteapp/__init__.py
Scanned: 2016-10-12 13:44:54.775632
No vulnerabilities found.


iolab12/flask_demo_2
https://github.com/iolab12/flask_demo_2
Entry file: flask_demo_2/polls.py
Scanned: 2016-10-12 13:45:03.673385
No vulnerabilities found.


plaes/wirexfers-flask-demo
https://github.com/plaes/wirexfers-flask-demo
Entry file: wirexfers-flask-demo/wirexfers_flask_demo/__init__.py
Scanned: 2016-10-12 13:45:11.003410
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Dict'>)

yeojz/skeleton-bottle-flask
https://github.com/yeojz/skeleton-bottle-flask
Entry file: skeleton-bottle-flask/thirdparty/flask/sessions.py
Scanned: 2016-10-12 13:45:26.656319
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

drawcode/flask-template-basic
https://github.com/drawcode/flask-template-basic
Entry file: flask-template-basic/app/__init__.py
Scanned: 2016-10-12 13:45:27.990834
Vulnerability 1:
File: flask-template-basic/app/users/views.py
 > User input at line 33, trigger word ".data": 
	user = User.query.filter_by(email=form.email.data).first()
Reassigned in: 
	File: flask-template-basic/app/users/views.py
	 > Line 38: session['user_id'] = user.id
File: flask-template-basic/app/users/views.py
 > reaches line 39, trigger word "flash(": 
	flash('Welcome %s' % user.name)



nanorepublica/secret-santa
https://github.com/nanorepublica/secret-santa
Entry file: secret-santa/secret_santa.py
Scanned: 2016-10-12 13:45:36.697018
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ardinor/yamazumi
https://github.com/ardinor/yamazumi
Entry file: yamazumi/yamazumi/__init__.py
Scanned: 2016-10-12 13:45:41.910962
No vulnerabilities found.


seme0021/flaskr-reader
https://github.com/seme0021/flaskr-reader
Entry file: flaskr-reader/app.py
Scanned: 2016-10-12 13:45:46.900635
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

vijaym123/FaceDetection-SimpleCVandFlask
https://github.com/vijaym123/FaceDetection-SimpleCVandFlask
Entry file: FaceDetection-SimpleCVandFlask/upload.py
Scanned: 2016-10-12 13:45:54.744315
No vulnerabilities found.


ryanc/mmmpaste
https://github.com/ryanc/mmmpaste
Entry file: mmmpaste/mmmpaste/__init__.py
Scanned: 2016-10-12 13:46:01.527853
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rowandh/pytorrent
https://github.com/rowandh/pytorrent
Entry file: pytorrent/bt/Tracker.py
Scanned: 2016-10-12 13:46:22.817717
No vulnerabilities found.


gatesphere/ptah
https://github.com/gatesphere/ptah
Entry file: ptah/sitebuilder.py
Scanned: 2016-10-12 13:46:28.140704
No vulnerabilities found.


ericevenchick/site
https://github.com/ericevenchick/site
Entry file: site/site.py
Scanned: 2016-10-12 13:46:45.010055
No vulnerabilities found.


wantsomechocolate/PythonWebsite
https://github.com/wantsomechocolate/PythonWebsite
Entry file: PythonWebsite/app.py
Scanned: 2016-10-12 13:46:53.281970
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jineshpaloor/Mysite
https://github.com/jineshpaloor/Mysite
Entry file: Mysite/home.py
Scanned: 2016-10-12 13:46:54.740602
No vulnerabilities found.


schinken/py-powerctrl
https://github.com/schinken/py-powerctrl
Entry file: py-powerctrl/main.py
Scanned: 2016-10-12 13:47:01.478781
No vulnerabilities found.


rudolpho/kazapp
https://github.com/rudolpho/kazapp
Entry file: kazapp/kazapp.py
Scanned: 2016-10-12 13:47:05.519818
No vulnerabilities found.


daleobrien/bootflask
https://github.com/daleobrien/bootflask
Entry file: bootflask/main.py
Scanned: 2016-10-12 13:47:12.270256
No vulnerabilities found.


nerdguy/httpfirmata
https://github.com/nerdguy/httpfirmata
Entry file: httpfirmata/httpfirmata/server.py
Scanned: 2016-10-12 13:47:23.817518
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

anusharanganathan/diskMonitor
https://github.com/anusharanganathan/diskMonitor
Entry file: diskMonitor/webui.py
Scanned: 2016-10-12 13:47:29.168196
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

leibatt/forms
https://github.com/leibatt/forms
Entry file: forms/form_serv.py
Scanned: 2016-10-12 13:47:35.498099
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tjstum/isawyou-too
https://github.com/tjstum/isawyou-too
Entry file: isawyou-too/isy/__init__.py
Scanned: 2016-10-12 13:47:43.873754
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

Foxboron/FoxBlog
https://github.com/Foxboron/FoxBlog
Entry file: FoxBlog/app/__init__.py
Scanned: 2016-10-12 13:47:54.805667
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

unbit/uwsgicc
https://github.com/unbit/uwsgicc
Entry file: uwsgicc/uwsgicc.py
Scanned: 2016-10-12 13:47:56.424543
No vulnerabilities found.


jmhobbs/batsdboard
https://github.com/jmhobbs/batsdboard
Entry file: batsdboard/src/batsdboard_server.py
Scanned: 2016-10-12 13:48:01.647280
No vulnerabilities found.


LarryEitel/pyfem
https://github.com/LarryEitel/pyfem
Entry file: pyfem/pyfem/app.py
Scanned: 2016-10-12 13:48:06.576963
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hciudad/webhook_listener
https://github.com/hciudad/webhook_listener
Entry file: webhook_listener/app.py
Scanned: 2016-10-12 13:48:11.785953
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sagnew/secret_santa
https://github.com/sagnew/secret_santa
Entry file: secret_santa/app.py
Scanned: 2016-10-12 13:48:32.936241
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

vc4a/vc4a-python-example
https://github.com/vc4a/vc4a-python-example
Entry file: vc4a-python-example/app.py
Scanned: 2016-10-12 13:48:44.635456
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lpolepeddi/intro-to-flask
https://github.com/lpolepeddi/intro-to-flask
Entry file: intro-to-flask/intro_to_flask/__init__.py
Scanned: 2016-10-12 13:48:55.424395
No vulnerabilities found.


miguelgrinberg/microblog
https://github.com/miguelgrinberg/microblog
Entry file: microblog/app/__init__.py
Scanned: 2016-10-12 13:48:57.830594
No vulnerabilities found.


saltycrane/flask-jquery-ajax-example
https://github.com/saltycrane/flask-jquery-ajax-example
Entry file: None
Scanned: 2016-10-12 13:49:02.023053
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/saltycrane/flask-jquery-ajax-example.

jdiez17/flask-paypal
https://github.com/jdiez17/flask-paypal
Entry file: flask-paypal/app.py
Scanned: 2016-10-12 13:49:05.277442
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BinOp'>)

gregorynicholas/flask-xsrf
https://github.com/gregorynicholas/flask-xsrf
Entry file: flask-xsrf/flask_xsrf.py
Scanned: 2016-10-12 13:49:12.678515
No vulnerabilities found.


tarbell-project/tarbell
https://github.com/tarbell-project/tarbell
Entry file: tarbell/tarbell/app.py
Scanned: 2016-10-12 13:49:31.498211
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

trtg/flask_assets_tutorial
https://github.com/trtg/flask_assets_tutorial
Entry file: flask_assets_tutorial/example/__init__.py
Scanned: 2016-10-12 13:49:33.272926
No vulnerabilities found.


allanlei/flask-email
https://github.com/allanlei/flask-email
Entry file: flask-email/tests/__init__.py
Scanned: 2016-10-12 13:49:36.988683
No vulnerabilities found.


maxcnunes/flaskgaedemo
https://github.com/maxcnunes/flaskgaedemo
Entry file: flaskgaedemo/main.py
Scanned: 2016-10-12 13:50:04.505876
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

domenicosolazzo/flask_examples
https://github.com/domenicosolazzo/flask_examples
Entry file: flask_examples/logger_example.py
Scanned: 2016-10-12 13:50:05.868971
No vulnerabilities found.


akostyuk/flask-dbmigrate
https://github.com/akostyuk/flask-dbmigrate
Entry file: flask-dbmigrate/tests.py
Scanned: 2016-10-12 13:50:25.702059
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

50onRed/phillypug-flask
https://github.com/50onRed/phillypug-flask
Entry file: phillypug-flask/phillypug/app.py
Scanned: 2016-10-12 13:50:32.994836
No vulnerabilities found.


booo/flask-gtfs
https://github.com/booo/flask-gtfs
Entry file: None
Scanned: 2016-10-12 13:50:45.840718
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/booo/flask-gtfs.

Blender3D/Flask-LESS
https://github.com/Blender3D/Flask-LESS
Entry file: Flask-LESS/flask_less.py
Scanned: 2016-10-12 13:50:49.161501
No vulnerabilities found.


sagarrakshe/flaskr
https://github.com/sagarrakshe/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 13:50:54.664985
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hex/flaskr
https://github.com/hex/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 13:50:56.164066
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

faruken/flask-web.py-jvm
https://github.com/faruken/flask-web.py-jvm
Entry file: None
Scanned: 2016-10-12 13:51:05.877306
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/faruken/flask-web.py-jvm.

cheesysam/flaskDemo
https://github.com/cheesysam/flaskDemo
Entry file: flaskDemo/flaskDemo.py
Scanned: 2016-10-12 13:51:14.524800
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

eddawong/FlaskStudy
https://github.com/eddawong/FlaskStudy
Entry file: FlaskStudy/main.py
Scanned: 2016-10-12 13:51:25.811469
No vulnerabilities found.


nerevu/prometheus
https://github.com/nerevu/prometheus
Entry file: prometheus/app/__init__.py
Scanned: 2016-10-12 13:51:36.590628
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

floweb/liensdujour
https://github.com/floweb/liensdujour
Entry file: liensdujour/liensdujour/liensdujour.py
Scanned: 2016-10-12 13:51:38.233468
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

becdot/adventures-in-text
https://github.com/becdot/adventures-in-text
Entry file: adventures-in-text/db_methods.py
Scanned: 2016-10-12 13:51:47.390862
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dirn/Flask-Simon
https://github.com/dirn/Flask-Simon
Entry file: Flask-Simon/examples/flaskr/flaskr.py
Scanned: 2016-10-12 13:51:49.885114
No vulnerabilities found.


parryjacob/flask-boilerplate
https://github.com/parryjacob/flask-boilerplate
Entry file: flask-boilerplate/project/__init__.py
Scanned: 2016-10-12 13:51:56.261210
No vulnerabilities found.


scottdnz/flask_skeleton
https://github.com/scottdnz/flask_skeleton
Entry file: flask_skeleton/flask_skeleton/config.py
Scanned: 2016-10-12 13:51:57.678062
No vulnerabilities found.
An Error occurred while scanning the repo: 'NoneType' object has no attribute 'label'

protunt/flask-blog
https://github.com/protunt/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 13:52:02.221598
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-blog/venv/lib/python2.7/genericpath.py

jpercent/flask-control
https://github.com/jpercent/flask-control
Entry file: flask-control/example.py
Scanned: 2016-10-12 13:52:06.467372
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

caub/flask-geo
https://github.com/caub/flask-geo
Entry file: flask-geo/myMap.py
Scanned: 2016-10-12 13:52:15.266945
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

Ceasar/pocket_flask
https://github.com/Ceasar/pocket_flask
Entry file: pocket_flask/app/__init__.py
Scanned: 2016-10-12 13:52:27.097817
No vulnerabilities found.


masayang/flask_dev
https://github.com/masayang/flask_dev
Entry file: flask_dev/flaskr/flaskr_app/__init__.py
Scanned: 2016-10-12 13:52:33.710558
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rhyselsmore/flask-modus
https://github.com/rhyselsmore/flask-modus
Entry file: flask-modus/test_flask_modus.py
Scanned: 2016-10-12 13:52:37.996067
No vulnerabilities found.


pavlenko-volodymyr/flask-study
https://github.com/pavlenko-volodymyr/flask-study
Entry file: flask-study/src/app/__init__.py
Scanned: 2016-10-12 13:52:47.258072
No vulnerabilities found.


slizadel/flask-gitrcv
https://github.com/slizadel/flask-gitrcv
Entry file: flask-gitrcv/flask-gitrcv/gitrcv.py
Scanned: 2016-10-12 13:52:50.464100
No vulnerabilities found.


apjd/flask-heroku
https://github.com/apjd/flask-heroku
Entry file: flask-heroku/flasky.py
Scanned: 2016-10-12 13:52:56.731837
No vulnerabilities found.


scardine/flask-locale
https://github.com/scardine/flask-locale
Entry file: flask-locale/tests/__init__.py
Scanned: 2016-10-12 13:52:58.072817
No vulnerabilities found.


CMGS/poll
https://github.com/CMGS/poll
Entry file: poll/app.py
Scanned: 2016-10-12 13:53:11.859555
No vulnerabilities found.


hoh/perfume
https://github.com/hoh/perfume
Entry file: perfume/perfume/__init__.py
Scanned: 2016-10-12 13:53:15.695519
No vulnerabilities found.


alph486/SimpleFlaskAPI
https://github.com/alph486/SimpleFlaskAPI
Entry file: SimpleFlaskAPI/app.py
Scanned: 2016-10-12 13:53:26.959463
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

JunilJacob/Paint-app-using-Flask
https://github.com/JunilJacob/Paint-app-using-Flask
Entry file: Paint-app-using-Flask/hello.py
Scanned: 2016-10-12 13:53:34.619987
Vulnerability 1:
File: Paint-app-using-Flask/hello.py
 > User input at line 12, trigger word "form[": 
	name = request.form['pname']
Reassigned in: 
	File: Paint-app-using-Flask/hello.py
	 > Line 15: image = (name, data)
	File: Paint-app-using-Flask/hello.py
	 > Line 16: iname = (name)
File: Paint-app-using-Flask/hello.py
 > reaches line 18, trigger word "execute(": 
	c.execute('DELETE FROM Image WHERE file=?', iname)

Vulnerability 2:
File: Paint-app-using-Flask/hello.py
 > User input at line 11, trigger word "form[": 
	data = request.form['pdata']
Reassigned in: 
	File: Paint-app-using-Flask/hello.py
	 > Line 15: image = (name, data)
	File: Paint-app-using-Flask/hello.py
	 > Line 33: data = ''
	File: Paint-app-using-Flask/hello.py
	 > Line 37: ret_MAYBE_FUNCTION_NAME = resp
	File: Paint-app-using-Flask/hello.py
	 > Line 39: ret_MAYBE_FUNCTION_NAME = 'Image not Found'
	File: Paint-app-using-Flask/hello.py
	 > Line 42: ret_MAYBE_FUNCTION_NAME = render_template('paint.html')
File: Paint-app-using-Flask/hello.py
 > reaches line 19, trigger word "execute(": 
	c.execute('INSERT INTO Image VALUES (?,?)', image)

Vulnerability 3:
File: Paint-app-using-Flask/hello.py
 > User input at line 12, trigger word "form[": 
	name = request.form['pname']
Reassigned in: 
	File: Paint-app-using-Flask/hello.py
	 > Line 15: image = (name, data)
	File: Paint-app-using-Flask/hello.py
	 > Line 16: iname = (name)
File: Paint-app-using-Flask/hello.py
 > reaches line 19, trigger word "execute(": 
	c.execute('INSERT INTO Image VALUES (?,?)', image)

Vulnerability 4:
File: Paint-app-using-Flask/hello.py
 > User input at line 11, trigger word "form[": 
	data = request.form['pdata']
Reassigned in: 
	File: Paint-app-using-Flask/hello.py
	 > Line 15: image = (name, data)
	File: Paint-app-using-Flask/hello.py
	 > Line 33: data = ''
	File: Paint-app-using-Flask/hello.py
	 > Line 37: ret_MAYBE_FUNCTION_NAME = resp
	File: Paint-app-using-Flask/hello.py
	 > Line 39: ret_MAYBE_FUNCTION_NAME = 'Image not Found'
	File: Paint-app-using-Flask/hello.py
	 > Line 42: ret_MAYBE_FUNCTION_NAME = render_template('paint.html')
File: Paint-app-using-Flask/hello.py
 > reaches line 36, trigger word "render_template(": 
	resp = Response('<script>var data=JSON.parse(' ' + data + ' ');</script>' + render_template('paint.html'),status=200, mimetype='html')



dimfox/flask-mega-tutorial
https://github.com/dimfox/flask-mega-tutorial
Entry file: flask-mega-tutorial/app/__init__.py
Scanned: 2016-10-12 13:53:38.868558
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

liuxuecheng/python_flask_guestbook
https://github.com/liuxuecheng/python_flask_guestbook
Entry file: python_flask_guestbook/main.py
Scanned: 2016-10-12 13:53:48.144709
No vulnerabilities found.


callahad/temp-flask-persona-demo
https://github.com/callahad/temp-flask-persona-demo
Entry file: temp-flask-persona-demo/example.py
Scanned: 2016-10-12 13:53:57.097975
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joshsee/GAE-flask-cms
https://github.com/joshsee/GAE-flask-cms
Entry file: GAE-flask-cms/flask/sessions.py
Scanned: 2016-10-12 13:54:01.495134
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joshkurz/exi
https://github.com/joshkurz/exi
Entry file: exi/exi/tests/security/test_app/__init__.py
Scanned: 2016-10-12 13:54:04.828414
No vulnerabilities found.


marsella/andrea
https://github.com/marsella/andrea
Entry file: andrea/init.py
Scanned: 2016-10-12 13:54:20.388868
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: andrea/venv/lib/python2.7/genericpath.py

ffiiccuuss/torouterui
https://github.com/ffiiccuuss/torouterui
Entry file: torouterui/torouterui/__init__.py
Scanned: 2016-10-12 13:54:28.061837
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

thoughtnirvana/redux
https://github.com/thoughtnirvana/redux
Entry file: redux/main.py
Scanned: 2016-10-12 13:54:35.515263
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dogrdon/txtr
https://github.com/dogrdon/txtr
Entry file: txtr/txtr.py
Scanned: 2016-10-12 13:54:44.602440
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

booo/baedproject
https://github.com/booo/baedproject
Entry file: baedproject/app.py
Scanned: 2016-10-12 13:54:48.839661
No vulnerabilities found.


embr/multithon
https://github.com/embr/multithon
Entry file: multithon/multithon.py
Scanned: 2016-10-12 13:54:52.593537
No vulnerabilities found.


skinofstars/monkey
https://github.com/skinofstars/monkey
Entry file: monkey/app.py
Scanned: 2016-10-12 13:54:57.847174
No vulnerabilities found.


zhoutuo/dota2bbq
https://github.com/zhoutuo/dota2bbq
Entry file: dota2bbq/wsgi.py
Scanned: 2016-10-12 13:55:07.124512
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mattoufoutu/TrendnetStalker
https://github.com/mattoufoutu/TrendnetStalker
Entry file: TrendnetStalker/TrendnetStalker/__init__.py
Scanned: 2016-10-12 13:55:08.457080
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kalimatas/herokuflask
https://github.com/kalimatas/herokuflask
Entry file: herokuflask/app.py
Scanned: 2016-10-12 13:55:14.674758
No vulnerabilities found.


norbert/helloflask
https://github.com/norbert/helloflask
Entry file: helloflask/app.py
Scanned: 2016-10-12 13:55:16.910689
No vulnerabilities found.


ahawker/jpool
https://github.com/ahawker/jpool
Entry file: None
Scanned: 2016-10-12 13:55:29.077388
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/ahawker/jpool.

Pusungwi/lobotomizer
https://github.com/Pusungwi/lobotomizer
Entry file: None
Scanned: 2016-10-12 13:55:34.445606
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/Pusungwi/lobotomizer.

perjo927/Portfolio
https://github.com/perjo927/Portfolio
Entry file: Portfolio/server.py
Scanned: 2016-10-12 13:55:43.570832
No vulnerabilities found.


cyrilaub/myMap_python
https://github.com/cyrilaub/myMap_python
Entry file: myMap_python/myMap.py
Scanned: 2016-10-12 13:55:50.225618
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sburns/switchboard
https://github.com/sburns/switchboard
Entry file: switchboard/sample_app.py
Scanned: 2016-10-12 13:55:52.524029
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

takosuke/pizzasuicideclub
https://github.com/takosuke/pizzasuicideclub
Entry file: pizzasuicideclub/psc_app/__init__.py
Scanned: 2016-10-12 13:56:05.567672
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.If'>)

MaxPresman/tempymail
https://github.com/MaxPresman/tempymail
Entry file: tempymail/flask_frontend.py
Scanned: 2016-10-12 13:56:07.179239
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

bogdan-kulynych/cloudlectures
https://github.com/bogdan-kulynych/cloudlectures
Entry file: cloudlectures/flask/sessions.py
Scanned: 2016-10-12 13:56:10.669756
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

neilduncan/FlickrPlaceholders
https://github.com/neilduncan/FlickrPlaceholders
Entry file: FlickrPlaceholders/main.py
Scanned: 2016-10-12 13:56:17.367424
No vulnerabilities found.


sysr-q/phi
https://github.com/sysr-q/phi
Entry file: phi/phi/phi.py
Scanned: 2016-10-12 13:56:30.666941
No vulnerabilities found.


DanielleSucher/BookQueue
https://github.com/DanielleSucher/BookQueue
Entry file: BookQueue/app.py
Scanned: 2016-10-12 13:56:35.005309
Vulnerability 1:
File: BookQueue/app.py
 > User input at line 145, trigger word "form[": 
	from_email = request.form['sender'].lower()
File: BookQueue/app.py
 > reaches line 146, trigger word "filter(": 
	query = User.query.filter(User.email == from_email)



msergdeez/vwcontrol
https://github.com/msergdeez/vwcontrol
Entry file: vwcontrol/vwcontrol.py
Scanned: 2016-10-12 13:56:41.913658
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

amaterasu-/placeholder
https://github.com/amaterasu-/placeholder
Entry file: placeholder/image.py
Scanned: 2016-10-12 13:56:50.113250
No vulnerabilities found.


mjhea0/flask-intro
https://github.com/mjhea0/flask-intro
Entry file: flask-intro/routes.py
Scanned: 2016-10-12 13:57:11.181347
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mikeboers/Flask-Images
https://github.com/mikeboers/Flask-Images
Entry file: Flask-Images/tests/__init__.py
Scanned: 2016-10-12 13:57:13.368099
No vulnerabilities found.


bkabrda/flask-whooshee
https://github.com/bkabrda/flask-whooshee
Entry file: flask-whooshee/test.py
Scanned: 2016-10-12 13:57:16.112110
No vulnerabilities found.


koon-kai/kiblog
https://github.com/koon-kai/kiblog
Entry file: kiblog/app.py
Scanned: 2016-10-12 13:57:29.266217
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

deepgully/me
https://github.com/deepgully/me
Entry file: me/settings.py
Scanned: 2016-10-12 13:57:41.306585
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

berlotto/flask-app-template
https://github.com/berlotto/flask-app-template
Entry file: flask-app-template/app/__init__.py
Scanned: 2016-10-12 13:57:42.663685
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

corydolphin/flask-jsonpify
https://github.com/corydolphin/flask-jsonpify
Entry file: flask-jsonpify/test.py
Scanned: 2016-10-12 13:57:51.079518
No vulnerabilities found.


mickey06/Flask-principal-example
https://github.com/mickey06/Flask-principal-example
Entry file: Flask-principal-example/FPrincipals.py
Scanned: 2016-10-12 13:57:54.505401
No vulnerabilities found.


crazygit/flask
https://github.com/crazygit/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 13:57:59.433515
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

joelrojo/flask
https://github.com/joelrojo/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 13:58:07.301392
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

wingu/flask_filters
https://github.com/wingu/flask_filters
Entry file: flask_filters/test_flask_filters.py
Scanned: 2016-10-12 13:58:18.599340
No vulnerabilities found.


seanrose/box-arcade
https://github.com/seanrose/box-arcade
Entry file: box-arcade/app/__init__.py
Scanned: 2016-10-12 13:58:34.075958
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

techniq/flask-wdb
https://github.com/techniq/flask-wdb
Entry file: flask-wdb/example.py
Scanned: 2016-10-12 13:58:36.998524
No vulnerabilities found.


eadmundo/flask-static-blog
https://github.com/eadmundo/flask-static-blog
Entry file: flask-static-blog/app/__init__.py
Scanned: 2016-10-12 13:58:51.913481
No vulnerabilities found.


BuongiornoMIP/Reding
https://github.com/BuongiornoMIP/Reding
Entry file: Reding/reding/app.py
Scanned: 2016-10-12 13:58:57.051779
No vulnerabilities found.


mphuie/flask_base
https://github.com/mphuie/flask_base
Entry file: flask_base/myapp/__init__.py
Scanned: 2016-10-12 13:59:01.966744
No vulnerabilities found.


colwilson/flask-lazyapi
https://github.com/colwilson/flask-lazyapi
Entry file: flask-lazyapi/demo_server.py
Scanned: 2016-10-12 13:59:08.506139
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

asgoel/Merge-flask
https://github.com/asgoel/Merge-flask
Entry file: Merge-flask/app.py
Scanned: 2016-10-12 13:59:16.522055
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

xiechao06/Flask-DataBrowser
https://github.com/xiechao06/Flask-DataBrowser
Entry file: Flask-DataBrowser/flask_databrowser/test/basetest.py
Scanned: 2016-10-12 13:59:22.550139
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ajuna/car-registration
https://github.com/ajuna/car-registration
Entry file: None
Scanned: 2016-10-12 13:59:23.835577
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/ajuna/car-registration.

gregimba/Vodka
https://github.com/gregimba/Vodka
Entry file: Vodka/app.py
Scanned: 2016-10-12 13:59:31.482769
No vulnerabilities found.


corydolphin/flask-olinauth
https://github.com/corydolphin/flask-olinauth
Entry file: flask-olinauth/example.py
Scanned: 2016-10-12 13:59:52.862278
No vulnerabilities found.


theho/flask-wsgi
https://github.com/theho/flask-wsgi
Entry file: flask-wsgi/wsgi.py
Scanned: 2016-10-12 13:59:56.167444
No vulnerabilities found.


0atman/flask-basic
https://github.com/0atman/flask-basic
Entry file: flask-basic/flask-basic.py
Scanned: 2016-10-12 14:00:08.975947
No vulnerabilities found.


danielestevez/flasktutorial
https://github.com/danielestevez/flasktutorial
Entry file: flasktutorial/app/__init__.py
Scanned: 2016-10-12 14:00:24.371826
No vulnerabilities found.


adityaathalye/flaskr
https://github.com/adityaathalye/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 14:00:29.911883
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

knowshan/flaskey
https://github.com/knowshan/flaskey
Entry file: flaskey/app/__init__.py
Scanned: 2016-10-12 14:00:44.759415
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

pityonline/flaskr
https://github.com/pityonline/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 14:00:52.287735
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

andyr/flaskapp
https://github.com/andyr/flaskapp
Entry file: flaskapp/flaskapp/application.py
Scanned: 2016-10-12 14:00:55.809647
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

clmns/flasktest
https://github.com/clmns/flasktest
Entry file: flasktest/nachh/app.py
Scanned: 2016-10-12 14:01:01.239899
No vulnerabilities found.


zfdang/memcached-in-openshift
https://github.com/zfdang/memcached-in-openshift
Entry file: memcached-in-openshift/wsgi/main.py
Scanned: 2016-10-12 14:01:14.199811
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

Masagin/FlaskCelery
https://github.com/Masagin/FlaskCelery
Entry file: FlaskCelery/flask.py
Scanned: 2016-10-12 14:01:19.511769
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ConceptPending/flaskTemplate
https://github.com/ConceptPending/flaskTemplate
Entry file: flaskTemplate/server.py
Scanned: 2016-10-12 14:01:27.819418
No vulnerabilities found.


AlexMost/Flask-starter
https://github.com/AlexMost/Flask-starter
Entry file: Flask-starter/app.py
Scanned: 2016-10-12 14:01:37.643195
No vulnerabilities found.


prabeesh/Studentapp-Flask
https://github.com/prabeesh/Studentapp-Flask
Entry file: Studentapp-Flask/test.py
Scanned: 2016-10-12 14:01:44.946614
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

garethpaul/flask-sample
https://github.com/garethpaul/flask-sample
Entry file: flask-sample/guild/app.py
Scanned: 2016-10-12 14:01:52.470648
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

denz/flask_introspect
https://github.com/denz/flask_introspect
Entry file: flask_introspect/test/test_blueprint.py
Scanned: 2016-10-12 14:02:01.396127
No vulnerabilities found.


EvilDmitri/flask-mikroblog
https://github.com/EvilDmitri/flask-mikroblog
Entry file: flask-mikroblog/app/__init__.py
Scanned: 2016-10-12 14:02:09.819587
No vulnerabilities found.


ekfriis/flask-mbtiles
https://github.com/ekfriis/flask-mbtiles
Entry file: flask-mbtiles/mbtileserver.py
Scanned: 2016-10-12 14:02:14.113834
No vulnerabilities found.


hyaticua/flask-blog
https://github.com/hyaticua/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 14:02:19.713415
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-blog/venv/lib/python2.7/genericpath.py

maxcnunes/flask_bravi
https://github.com/maxcnunes/flask_bravi
Entry file: flask_bravi/braviapp/__init__.py
Scanned: 2016-10-12 14:02:25.218704
No vulnerabilities found.


naveenpremchand02/flask_url
https://github.com/naveenpremchand02/flask_url
Entry file: flask_url/url.py
Scanned: 2016-10-12 14:02:38.010159
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

zhemao/flask_demo
https://github.com/zhemao/flask_demo
Entry file: flask_demo/application.py
Scanned: 2016-10-12 14:02:57.305603
No vulnerabilities found.


dproni/flask_test
https://github.com/dproni/flask_test
Entry file: flask_test/flask_test.py
Scanned: 2016-10-12 14:03:01.598882
No vulnerabilities found.


thearchduke/flask-boiler
https://github.com/thearchduke/flask-boiler
Entry file: None
Scanned: 2016-10-12 14:03:15.144559
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

StefanKjartansson/bower-flask
https://github.com/StefanKjartansson/bower-flask
Entry file: bower-flask/server.py
Scanned: 2016-10-12 14:03:16.365624
No vulnerabilities found.


scardine/flask-locale
https://github.com/scardine/flask-locale
Entry file: flask-locale/tests/__init__.py
Scanned: 2016-10-12 14:03:20.755631
No vulnerabilities found.


tanayseven/Voix
https://github.com/tanayseven/Voix
Entry file: None
Scanned: 2016-10-12 14:03:31.271274
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

gatesphere/flaskr-flask-tutorial
https://github.com/gatesphere/flaskr-flask-tutorial
Entry file: flaskr-flask-tutorial/flaskr/flaskr.py
Scanned: 2016-10-12 14:03:32.657102
No vulnerabilities found.


xiechao06/Flask-NavBar
https://github.com/xiechao06/Flask-NavBar
Entry file: Flask-NavBar/flask_nav_bar.py
Scanned: 2016-10-12 14:03:39.106663
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cpdean/flask-oauth-tutorial
https://github.com/cpdean/flask-oauth-tutorial
Entry file: flask-oauth-tutorial/flaskr.py
Scanned: 2016-10-12 14:03:45.464058
No vulnerabilities found.


SalemHarrache-Archive/flask_chat_eventsource
https://github.com/SalemHarrache-Archive/flask_chat_eventsource
Entry file: flask_chat_eventsource/server.py
Scanned: 2016-10-12 14:03:54.805228
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

nsfyn55/flask-mega-tutorial
https://github.com/nsfyn55/flask-mega-tutorial
Entry file: flask-mega-tutorial/app/__init__.py
Scanned: 2016-10-12 14:03:57.384359
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

callahad/temp-flask-persona-demo
https://github.com/callahad/temp-flask-persona-demo
Entry file: temp-flask-persona-demo/example.py
Scanned: 2016-10-12 14:04:00.879160
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kishorekdty/paint_using_flask
https://github.com/kishorekdty/paint_using_flask
Entry file: None
Scanned: 2016-10-12 14:04:10.199020
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/kishorekdty/paint_using_flask.

bazerk/baz-flask-base
https://github.com/bazerk/baz-flask-base
Entry file: baz-flask-base/app/app.py
Scanned: 2016-10-12 14:04:17.156305
Vulnerability 1:
File: baz-flask-base/app/frontend/views.py
 > User input at line 48, trigger word "get(": 
	form = LoginForm(login=request.args.get('login', None), next=request.args.get('next', None))
Reassigned in: 
	File: baz-flask-base/app/frontend/views.py
	 > Line 52: user = User.authenticate(form.login.data, form.password.data, bcrypt.check_password_hash)
	File: baz-flask-base/app/frontend/views.py
	 > Line 57: session['user_id'] = user.id
	File: baz-flask-base/app/frontend/views.py
	 > Line 65: ret_MAYBE_FUNCTION_NAME = render_template('frontend/login.html',form=form)
File: baz-flask-base/app/frontend/views.py
 > reaches line 61, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('')

Vulnerability 2:
File: baz-flask-base/app/frontend/views.py
 > User input at line 52, trigger word ".data": 
	user = User.authenticate(form.login.data, form.password.data, bcrypt.check_password_hash)
Reassigned in: 
	File: baz-flask-base/app/frontend/views.py
	 > Line 57: session['user_id'] = user.id
File: baz-flask-base/app/frontend/views.py
 > reaches line 61, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('')



ryanolson/flask-couchdb-schematics
https://github.com/ryanolson/flask-couchdb-schematics
Entry file: flask-couchdb-schematics/example/guestbook.py
Scanned: 2016-10-12 14:04:21.776661
No vulnerabilities found.


pouyan-ghasemi/flask-sql-cms
https://github.com/pouyan-ghasemi/flask-sql-cms
Entry file: flask-sql-cms/app.py
Scanned: 2016-10-12 14:04:33.980272
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joshsee/GAE-flask-cms
https://github.com/joshsee/GAE-flask-cms
Entry file: GAE-flask-cms/flask/sessions.py
Scanned: 2016-10-12 14:04:34.524232
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rasheedh/Heroku-Paint-Using-Flask
https://github.com/rasheedh/Heroku-Paint-Using-Flask
Entry file: None
Scanned: 2016-10-12 14:04:39.782075
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/rasheedh/Heroku-Paint-Using-Flask.

Andrey-Khobnya/flask-sessions-mongo
https://github.com/Andrey-Khobnya/flask-sessions-mongo
Entry file: flask-sessions-mongo/flask-sessions-mongo/examples/loginsession.py
Scanned: 2016-10-12 14:04:46.076094
No vulnerabilities found.


rodreegez/flask-twitter-auth
https://github.com/rodreegez/flask-twitter-auth
Entry file: None
Scanned: 2016-10-12 14:04:58.955568
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/rodreegez/flask-twitter-auth.

texuf/myflaskproject
https://github.com/texuf/myflaskproject
Entry file: myflaskproject/hello.py
Scanned: 2016-10-12 14:05:02.267423
No vulnerabilities found.


kshitizrimal/flaskr-modified
https://github.com/kshitizrimal/flaskr-modified
Entry file: flaskr-modified/flaskr.py
Scanned: 2016-10-12 14:05:14.763481
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sreekanthkaralmanna/heroku-paint-app-using-flask
https://github.com/sreekanthkaralmanna/heroku-paint-app-using-flask
Entry file: None
Scanned: 2016-10-12 14:05:26.093791
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/sreekanthkaralmanna/heroku-paint-app-using-flask.

prasanthkumara/Heroku-Paint-App-Using--Flask
https://github.com/prasanthkumara/Heroku-Paint-App-Using--Flask
Entry file: None
Scanned: 2016-10-12 14:05:35.474076
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/prasanthkumara/Heroku-Paint-App-Using--Flask.

pyxze/PyxzeCorpus
https://github.com/pyxze/PyxzeCorpus
Entry file: PyxzeCorpus/corpus.py
Scanned: 2016-10-12 14:05:40.772630
No vulnerabilities found.


mikewallace1979/milk
https://github.com/mikewallace1979/milk
Entry file: milk/milk.py
Scanned: 2016-10-12 14:05:47.165348
No vulnerabilities found.


ariamoraine/kitten-generator
https://github.com/ariamoraine/kitten-generator
Entry file: kitten-generator/flaskhello.py
Scanned: 2016-10-12 14:05:55.473987
No vulnerabilities found.


goonpug/goonpug-stats
https://github.com/goonpug/goonpug-stats
Entry file: goonpug-stats/goonpug/__init__.py
Scanned: 2016-10-12 14:06:00.884202
No vulnerabilities found.


csesoc/bark-core
https://github.com/csesoc/bark-core
Entry file: bark-core/bark/__init__.py
Scanned: 2016-10-12 14:06:03.931092
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

crcsmnky/thehotspot
https://github.com/crcsmnky/thehotspot
Entry file: thehotspot/v2/app.py
Scanned: 2016-10-12 14:06:11.985896
No vulnerabilities found.


etscrivner/sovereign-states
https://github.com/etscrivner/sovereign-states
Entry file: sovereign-states/sovereign_states/api.py
Scanned: 2016-10-12 14:06:17.428656
No vulnerabilities found.


croach/cheap-and-scalable-webistes-with-flask-code
https://github.com/croach/cheap-and-scalable-webistes-with-flask-code
Entry file: cheap-and-scalable-webistes-with-flask-code/generator.py
Scanned: 2016-10-12 14:06:21.779113
No vulnerabilities found.


sreedathns/paint-app-using-heroku-and-flask
https://github.com/sreedathns/paint-app-using-heroku-and-flask
Entry file: None
Scanned: 2016-10-12 14:06:25.990895
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/sreedathns/paint-app-using-heroku-and-flask.

nesv/cask
https://github.com/nesv/cask
Entry file: None
Scanned: 2016-10-12 14:06:36.490663
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/nesv/cask.

igrishaev/youtube-python-api-sample
https://github.com/igrishaev/youtube-python-api-sample
Entry file: youtube-python-api-sample/app.py
Scanned: 2016-10-12 14:06:43.732209
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

chadgh/chessy
https://github.com/chadgh/chessy
Entry file: None
Scanned: 2016-10-12 14:06:51.277068
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

lee212/fg-ws
https://github.com/lee212/fg-ws
Entry file: fg-ws/fgws/ws/FGWSApps.py
Scanned: 2016-10-12 14:06:55.601786
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

simplyluke/dothis
https://github.com/simplyluke/dothis
Entry file: dothis/dothis.py
Scanned: 2016-10-12 14:07:03.414136
No vulnerabilities found.


fusic-com/flask-todo
https://github.com/fusic-com/flask-todo
Entry file: flask-todo/backend/app.py
Scanned: 2016-10-12 14:07:18.660308
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kljensen/async-flask-sqlalchemy-example
https://github.com/kljensen/async-flask-sqlalchemy-example
Entry file: async-flask-sqlalchemy-example/server.py
Scanned: 2016-10-12 14:07:21.978036
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fusic-com/flask-webcache
https://github.com/fusic-com/flask-webcache
Entry file: flask-webcache/contrib/sleepycalc/app.py
Scanned: 2016-10-12 14:07:26.379245
No vulnerabilities found.


rehandalal/flask-mobility
https://github.com/rehandalal/flask-mobility
Entry file: flask-mobility/flask_mobility/tests/test_decorators.py
Scanned: 2016-10-12 14:07:37.048211
Vulnerability 1:
File: flask-mobility/flask_mobility/tests/test_decorators.py
 > User input at line 46, trigger word "get(": 
	MOBILE_COOKIE = self.app.config.get('MOBILE_COOKIE')
File: flask-mobility/flask_mobility/tests/test_decorators.py
 > reaches line 48, trigger word "set_cookie(": 
	self.client.set_cookie('localhost', MOBILE_COOKIE, 'on')

Vulnerability 2:
File: flask-mobility/flask_mobility/tests/test_decorators.py
 > User input at line 46, trigger word "get(": 
	MOBILE_COOKIE = self.app.config.get('MOBILE_COOKIE')
File: flask-mobility/flask_mobility/tests/test_decorators.py
 > reaches line 51, trigger word "set_cookie(": 
	self.client.set_cookie('localhost', MOBILE_COOKIE, 'off')

Vulnerability 3:
File: flask-mobility/flask_mobility/tests/test_decorators.py
 > User input at line 67, trigger word "get(": 
	MOBILE_COOKIE = self.app.config.get('MOBILE_COOKIE')
File: flask-mobility/flask_mobility/tests/test_decorators.py
 > reaches line 69, trigger word "set_cookie(": 
	self.client.set_cookie('localhost', MOBILE_COOKIE, 'on')

Vulnerability 4:
File: flask-mobility/flask_mobility/tests/test_decorators.py
 > User input at line 67, trigger word "get(": 
	MOBILE_COOKIE = self.app.config.get('MOBILE_COOKIE')
File: flask-mobility/flask_mobility/tests/test_decorators.py
 > reaches line 72, trigger word "set_cookie(": 
	self.client.set_cookie('localhost', MOBILE_COOKIE, 'off')

Vulnerability 5:
File: flask-mobility/flask_mobility/tests/test_mobility.py
 > User input at line 33, trigger word "get(": 
	MOBILE_COOKIE = self.config.get('MOBILE_COOKIE')
File: flask-mobility/flask_mobility/tests/test_mobility.py
 > reaches line 36, trigger word "set_cookie(": 
	self.app.set_cookie('localhost', MOBILE_COOKIE, 'on')

Vulnerability 6:
File: flask-mobility/flask_mobility/tests/test_mobility.py
 > User input at line 33, trigger word "get(": 
	MOBILE_COOKIE = self.config.get('MOBILE_COOKIE')
File: flask-mobility/flask_mobility/tests/test_mobility.py
 > reaches line 40, trigger word "set_cookie(": 
	self.app.set_cookie('localhost', MOBILE_COOKIE, 'off')



kelp404/Flask-GAE
https://github.com/kelp404/Flask-GAE
Entry file: None
Scanned: 2016-10-12 14:07:44.772996
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

wbolster/flask-uuid
https://github.com/wbolster/flask-uuid
Entry file: flask-uuid/test_flask_uuid.py
Scanned: 2016-10-12 14:07:57.135328
No vulnerabilities found.


pyr/url-shortener
https://github.com/pyr/url-shortener
Entry file: url-shortener/url_shortener.py
Scanned: 2016-10-12 14:08:03.133113
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

danielholmstrom/flask-alchemyview
https://github.com/danielholmstrom/flask-alchemyview
Entry file: flask-alchemyview/tests/test_with_flask_sqlalchemy.py
Scanned: 2016-10-12 14:08:13.061182
No vulnerabilities found.


kommmy/Flask
https://github.com/kommmy/Flask
Entry file: Flask/test_hello.py
Scanned: 2016-10-12 14:08:17.585202
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

DavidWittman/csrgenerator.com
https://github.com/DavidWittman/csrgenerator.com
Entry file: None
Scanned: 2016-10-12 14:08:23.202910
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/DavidWittman/csrgenerator.com.

vovantics/flask-bluebone
https://github.com/vovantics/flask-bluebone
Entry file: flask-bluebone/app/app.py
Scanned: 2016-10-12 14:08:26.893467
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

vmi356/filemanager
https://github.com/vmi356/filemanager
Entry file: filemanager/manager.py
Scanned: 2016-10-12 14:08:38.272180
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jaysonsantos/jinja-assets-compressor
https://github.com/jaysonsantos/jinja-assets-compressor
Entry file: jinja-assets-compressor/jac/contrib/flask.py
Scanned: 2016-10-12 14:08:57.153282
No vulnerabilities found.


1000ch/flask-handson
https://github.com/1000ch/flask-handson
Entry file: flask-handson/flaskr/__init__.py
Scanned: 2016-10-12 14:09:00.563973
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ajuna/car-registration
https://github.com/ajuna/car-registration
Entry file: None
Scanned: 2016-10-12 14:09:04.061809
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/ajuna/car-registration.

cratejoy/flask-experiment
https://github.com/cratejoy/flask-experiment
Entry file: flask-experiment/test/test.py
Scanned: 2016-10-12 14:09:23.785358
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rbika/flaskm
https://github.com/rbika/flaskm
Entry file: flaskm/flaskm.py
Scanned: 2016-10-12 14:09:27.311048
No vulnerabilities found.


jishnujagajeeve/Flaskr
https://github.com/jishnujagajeeve/Flaskr
Entry file: Flaskr/app.py
Scanned: 2016-10-12 14:09:37.664353
No vulnerabilities found.


openfree/flaskr
https://github.com/openfree/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 14:09:41.193216
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

catfive/flaskr
https://github.com/catfive/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 14:09:47.740620
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

Basher51/Flaskr
https://github.com/Basher51/Flaskr
Entry file: Flaskr/app.py
Scanned: 2016-10-12 14:09:57.065365
No vulnerabilities found.


nabetama/flaskr
https://github.com/nabetama/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 14:10:00.564179
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mikedll/flasksqlitedemo
https://github.com/mikedll/flasksqlitedemo
Entry file: flasksqlitedemo/app.py
Scanned: 2016-10-12 14:10:09.420506
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sagnew/Prank-Roulette
https://github.com/sagnew/Prank-Roulette
Entry file: Prank-Roulette/app.py
Scanned: 2016-10-12 14:10:19.439521
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kaste/FlaskDeferredHandler
https://github.com/kaste/FlaskDeferredHandler
Entry file: FlaskDeferredHandler/flask_handler_test.py
Scanned: 2016-10-12 14:10:20.754539
No vulnerabilities found.


adityaathalye/flaskr2
https://github.com/adityaathalye/flaskr2
Entry file: flaskr2/app.py
Scanned: 2016-10-12 14:10:24.038789
No vulnerabilities found.


jpscaletti/authcode
https://github.com/jpscaletti/authcode
Entry file: authcode/examples/default/app.py
Scanned: 2016-10-12 14:10:31.152460
No vulnerabilities found.


abulte/flask-arduino-websocket-sqlite
https://github.com/abulte/flask-arduino-websocket-sqlite
Entry file: flask-arduino-websocket-sqlite/app.py
Scanned: 2016-10-12 14:10:38.635020
No vulnerabilities found.


edouardswiac/linkstash-flask
https://github.com/edouardswiac/linkstash-flask
Entry file: linkstash-flask/app.py
Scanned: 2016-10-12 14:11:01.459969
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

samgclarke/flask-microblog
https://github.com/samgclarke/flask-microblog
Entry file: flask-microblog/app/__init__.py
Scanned: 2016-10-12 14:11:14.414431
No vulnerabilities found.


GerardoGR/flask-boilerplate
https://github.com/GerardoGR/flask-boilerplate
Entry file: flask-boilerplate/appname/appname/__init__.py
Scanned: 2016-10-12 14:11:21.737656
No vulnerabilities found.


futuregrid/flask_cm
https://github.com/futuregrid/flask_cm
Entry file: flask_cm/examples/forms/app.py
Scanned: 2016-10-12 14:11:30.418500
No vulnerabilities found.


shunyata/flask-helloworld
https://github.com/shunyata/flask-helloworld
Entry file: flask-helloworld/app.py
Scanned: 2016-10-12 14:11:38.780791
No vulnerabilities found.


stephen-allison/basic-flask
https://github.com/stephen-allison/basic-flask
Entry file: None
Scanned: 2016-10-12 14:11:43.179853
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/stephen-allison/basic-flask.

bollwyvl/flask-reloaded
https://github.com/bollwyvl/flask-reloaded
Entry file: None
Scanned: 2016-10-12 14:11:50.594946
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/bollwyvl/flask-reloaded.

mies/flask-heroku
https://github.com/mies/flask-heroku
Entry file: flask-heroku/main.py
Scanned: 2016-10-12 14:11:58.907363
No vulnerabilities found.


mattolsen1/flask_tumblelog
https://github.com/mattolsen1/flask_tumblelog
Entry file: flask_tumblelog/tumblelog/__init__.py
Scanned: 2016-10-12 14:12:02.378413
No vulnerabilities found.


jonomillin/learning-flask
https://github.com/jonomillin/learning-flask
Entry file: learning-flask/hello.py
Scanned: 2016-10-12 14:12:11.364609
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kitanata/flask-demo
https://github.com/kitanata/flask-demo
Entry file: flask-demo/part3.py
Scanned: 2016-10-12 14:12:14.715784
No vulnerabilities found.


rahulthrissur/Flask_app
https://github.com/rahulthrissur/Flask_app
Entry file: Flask_app/test.py
Scanned: 2016-10-12 14:12:22.041835
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

DanAlbert/flask-guestbook
https://github.com/DanAlbert/flask-guestbook
Entry file: flask-guestbook/guestbook.py
Scanned: 2016-10-12 14:12:25.354179
No vulnerabilities found.


toastercup/flask-social
https://github.com/toastercup/flask-social
Entry file: flask-social/social/__init__.py
Scanned: 2016-10-12 14:12:39.682272
No vulnerabilities found.


mozillazg/flask-demo
https://github.com/mozillazg/flask-demo
Entry file: None
Scanned: 2016-10-12 14:12:44.211471
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/mozillazg/flask-demo.

nthfloor/Flask_learn
https://github.com/nthfloor/Flask_learn
Entry file: Flask_learn/login_system/flskr.py
Scanned: 2016-10-12 14:12:56.373798
No vulnerabilities found.


kirkeby/empty-flask
https://github.com/kirkeby/empty-flask
Entry file: empty-flask/app/app.py
Scanned: 2016-10-12 14:12:59.855990
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flyingsparx/MongoFlask
https://github.com/flyingsparx/MongoFlask
Entry file: MongoFlask/application.py
Scanned: 2016-10-12 14:13:03.174718
No vulnerabilities found.


berlotto/hero-flask
https://github.com/berlotto/hero-flask
Entry file: hero-flask/hero/__init__.py
Scanned: 2016-10-12 14:13:08.497694
No vulnerabilities found.


hoest/flask-bardienst
https://github.com/hoest/flask-bardienst
Entry file: flask-bardienst/bardienst/__init__.py
Scanned: 2016-10-12 14:13:14.810387
No vulnerabilities found.


rehandalal/buchner
https://github.com/rehandalal/buchner
Entry file: buchner/buchner/project-template/PROJECTMODULE/main.py
Scanned: 2016-10-12 14:13:27.977167
No vulnerabilities found.


vitalk/flask-staticutils
https://github.com/vitalk/flask-staticutils
Entry file: flask-staticutils/tests/test_app/__init__.py
Scanned: 2016-10-12 14:13:29.396898
No vulnerabilities found.


danillosouza/flask-boilerplate
https://github.com/danillosouza/flask-boilerplate
Entry file: flask-boilerplate/app/__init__.py
Scanned: 2016-10-12 14:13:39.950983
Vulnerability 1:
File: flask-boilerplate/app/users/views.py
 > User input at line 36, trigger word ".data": 
	user = User.query.filter_by(email=form.email.data).first()
Reassigned in: 
	File: flask-boilerplate/app/users/views.py
	 > Line 41: session['user_id'] = user.id
File: flask-boilerplate/app/users/views.py
 > reaches line 42, trigger word "flash(": 
	flash('Welcome %s' % user.name)



dogrdon/flask-map
https://github.com/dogrdon/flask-map
Entry file: None
Scanned: 2016-10-12 14:13:48.960781
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

chiwong/flask_quickstart
https://github.com/chiwong/flask_quickstart
Entry file: flask_quickstart/hello.py
Scanned: 2016-10-12 14:13:55.533246
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask_quickstart/venv_hello/lib/python2.6/genericpath.py

archieyang/flask_app
https://github.com/archieyang/flask_app
Entry file: flask_app/flask_app.py
Scanned: 2016-10-12 14:14:04.279892
Vulnerability 1:
File: flask_app/flask_app.py
 > User input at line 50, trigger word "form[": 
	secured_pwd = secure_hash(salt, request.form['password'])
File: flask_app/flask_app.py
 > reaches line 52, trigger word "execute(": 
	g.db.execute('insert into users ( username, salt, password ) values (?, ?, ?)', [request.form['username'], salt, secured_pwd])



sapid/Flask-Community
https://github.com/sapid/Flask-Community
Entry file: None
Scanned: 2016-10-12 14:14:06.412066
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/sapid/Flask-Community.

eudaimonious/HangmanWebsite
https://github.com/eudaimonious/HangmanWebsite
Entry file: HangmanWebsite/application_hangman.py
Scanned: 2016-10-12 14:14:18.660263
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

grimkeke/miniblog
https://github.com/grimkeke/miniblog
Entry file: miniblog/app/__init__.py
Scanned: 2016-10-12 14:14:23.783419
No vulnerabilities found.


bracken1983/flaskBlogDemo
https://github.com/bracken1983/flaskBlogDemo
Entry file: flaskBlogDemo/flask-sqlalchemy-test.py
Scanned: 2016-10-12 14:14:33.242977
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mmcgahan/flask-labs-bb
https://github.com/mmcgahan/flask-labs-bb
Entry file: flask-labs-bb/flask_labs/__init__.py
Scanned: 2016-10-12 14:14:37.839789
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Dict'>)

jaseemkp/flask-students-app
https://github.com/jaseemkp/flask-students-app
Entry file: flask-students-app/students.py
Scanned: 2016-10-12 14:14:44.655092
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

daisuzu/flask-app-sample
https://github.com/daisuzu/flask-app-sample
Entry file: flask-app-sample/db.py
Scanned: 2016-10-12 14:14:51.969177
No vulnerabilities found.


rasheedh/Paint-Using-Flask---Mongodb-
https://github.com/rasheedh/Paint-Using-Flask---Mongodb-
Entry file: None
Scanned: 2016-10-12 14:15:01.445379
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/rasheedh/Paint-Using-Flask---Mongodb-.

ipfans/openshift-flask-template
https://github.com/ipfans/openshift-flask-template
Entry file: openshift-flask-template/wsgi/mainapp.py
Scanned: 2016-10-12 14:15:05.922820
No vulnerabilities found.


minhtuev/flask-google-map-example
https://github.com/minhtuev/flask-google-map-example
Entry file: flask-google-map-example/server.py
Scanned: 2016-10-12 14:15:09.220508
No vulnerabilities found.


garbados/flask-the-gauntlet
https://github.com/garbados/flask-the-gauntlet
Entry file: flask-the-gauntlet/app.py
Scanned: 2016-10-12 14:15:15.524905
No vulnerabilities found.


penpyt/flask-couchdb-auth
https://github.com/penpyt/flask-couchdb-auth
Entry file: flask-couchdb-auth/example/guestbook.py
Scanned: 2016-10-12 14:15:26.548677
No vulnerabilities found.


rodreegez/flask-twitter-auth
https://github.com/rodreegez/flask-twitter-auth
Entry file: None
Scanned: 2016-10-12 14:15:34.055573
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/rodreegez/flask-twitter-auth.

DamnedFacts/flask-hello-world
https://github.com/DamnedFacts/flask-hello-world
Entry file: flask-hello-world/app.py
Scanned: 2016-10-12 14:15:39.677582
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-hello-world/venv/lib/python2.7/genericpath.py

pinchsoft/flask-newrelic-dotcloud
https://github.com/pinchsoft/flask-newrelic-dotcloud
Entry file: flask-newrelic-dotcloud/app.py
Scanned: 2016-10-12 14:15:44.980232
No vulnerabilities found.


NoxDineen/microblog
https://github.com/NoxDineen/microblog
Entry file: microblog/app/__init__.py
Scanned: 2016-10-12 14:16:00.883788
No vulnerabilities found.


PurplePilot/zanzeeba
https://github.com/PurplePilot/zanzeeba
Entry file: zanzeeba/appstd.py
Scanned: 2016-10-12 14:16:11.809248
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

Pitxon/sivir
https://github.com/Pitxon/sivir
Entry file: sivir/app.py
Scanned: 2016-10-12 14:16:13.113657
No vulnerabilities found.


philangist/url-shorten
https://github.com/philangist/url-shorten
Entry file: url-shorten/shorten.py
Scanned: 2016-10-12 14:16:16.528591
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fabionatali/DigiWebStats
https://github.com/fabionatali/DigiWebStats
Entry file: DigiWebStats/app.py
Scanned: 2016-10-12 14:16:25.182827
No vulnerabilities found.


confessin/addressbook
https://github.com/confessin/addressbook
Entry file: addressbook/addressbook.py
Scanned: 2016-10-12 14:16:26.488498
No vulnerabilities found.


nafur/flmpc
https://github.com/nafur/flmpc
Entry file: flmpc/main.py
Scanned: 2016-10-12 14:16:35.959709
No vulnerabilities found.


ariamoraine/kitten-generator
https://github.com/ariamoraine/kitten-generator
Entry file: kitten-generator/flaskhello.py
Scanned: 2016-10-12 14:16:41.298150
No vulnerabilities found.


hit9/flask-sign-in-with-github.py
https://github.com/hit9/flask-sign-in-with-github.py
Entry file: None
Scanned: 2016-10-12 14:16:45.597744
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/hit9/flask-sign-in-with-github.py.

Kaibin/Condom_Data_Server
https://github.com/Kaibin/Condom_Data_Server
Entry file: Condom_Data_Server/app.py
Scanned: 2016-10-12 14:16:53.029816
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

honestappalachia/honest_site
https://github.com/honestappalachia/honest_site
Entry file: honest_site/run.py
Scanned: 2016-10-12 14:17:01.442880
Vulnerability 1:
File: honest_site/run.py
 > User input at line 36, trigger word "get(": 
	template = page.meta.get('template', 'default.html')
File: honest_site/run.py
 > reaches line 37, trigger word "render_template(": 
	ret_MAYBE_FUNCTION_NAME = render_template(template,page=page)



daikeshi/one-dollar-metasearch-engine
https://github.com/daikeshi/one-dollar-metasearch-engine
Entry file: one-dollar-metasearch-engine/app/__init__.py
Scanned: 2016-10-12 14:17:10.643261
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

honestappalachia/honest_hiddenservice
https://github.com/honestappalachia/honest_hiddenservice
Entry file: honest_hiddenservice/run.py
Scanned: 2016-10-12 14:17:17.215458
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mattupstate/flask-social
https://github.com/mattupstate/flask-social
Entry file: flask-social/tests/test_app/__init__.py
Scanned: 2016-10-12 14:17:28.193815
No vulnerabilities found.


xiyoulaoyuanjia/flaskapp
https://github.com/xiyoulaoyuanjia/flaskapp
Entry file: flaskapp/flaskapp/application.py
Scanned: 2016-10-12 14:17:35.720956
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mattupstate/flask-jsonschema
https://github.com/mattupstate/flask-jsonschema
Entry file: flask-jsonschema/tests.py
Scanned: 2016-10-12 14:17:42.085778
No vulnerabilities found.


jawr/flask-contact
https://github.com/jawr/flask-contact
Entry file: flask-contact/main.py
Scanned: 2016-10-12 14:17:46.475497
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

trustrachel/Flask-FeatureFlags
https://github.com/trustrachel/Flask-FeatureFlags
Entry file: Flask-FeatureFlags/tests/fixtures.py
Scanned: 2016-10-12 14:17:54.259278
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

rahulkmr/flask-bigapp-template
https://github.com/rahulkmr/flask-bigapp-template
Entry file: flask-bigapp-template/main.py
Scanned: 2016-10-12 14:18:02.355204
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

whtsky/Flask-WeRoBot
https://github.com/whtsky/Flask-WeRoBot
Entry file: Flask-WeRoBot/flask_werobot.py
Scanned: 2016-10-12 14:18:07.817573
No vulnerabilities found.


kienpham2000/airbrake-flask
https://github.com/kienpham2000/airbrake-flask
Entry file: airbrake-flask/setup.py
Scanned: 2016-10-12 14:18:14.376667
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

stef/flask-tlsauth
https://github.com/stef/flask-tlsauth
Entry file: flask-tlsauth/demo/webapp.py
Scanned: 2016-10-12 14:18:16.690910
No vulnerabilities found.


OpenTechSchool/python-flask-code
https://github.com/OpenTechSchool/python-flask-code
Entry file: python-flask-code/core/files-templates/catseverywhere.py
Scanned: 2016-10-12 14:18:26.048684
No vulnerabilities found.


aahluwal/flask
https://github.com/aahluwal/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 14:18:36.443439
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

kennethreitz/elephant
https://github.com/kennethreitz/elephant
Entry file: elephant/elephant.py
Scanned: 2016-10-12 14:18:43.004086
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rollbar/rollbar-flask-example
https://github.com/rollbar/rollbar-flask-example
Entry file: rollbar-flask-example/hello.py
Scanned: 2016-10-12 14:18:47.344037
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lqez/flasky
https://github.com/lqez/flasky
Entry file: flasky/flasky/flask/app.py
Scanned: 2016-10-12 14:18:53.897501
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

florapdx/My-Blog
https://github.com/florapdx/My-Blog
Entry file: My-Blog/sitebuilder.py
Scanned: 2016-10-12 14:19:13.175715
No vulnerabilities found.


clef/sample-flask
https://github.com/clef/sample-flask
Entry file: sample-flask/app.py
Scanned: 2016-10-12 14:19:14.599813
No vulnerabilities found.


Jd007/flask-rest
https://github.com/Jd007/flask-rest
Entry file: flask-rest/haystack/core.py
Scanned: 2016-10-12 14:19:25.629617
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

simonvc/rover-wasd-server
https://github.com/simonvc/rover-wasd-server
Entry file: rover-wasd-server/wasd_server.py
Scanned: 2016-10-12 14:19:30.000431
No vulnerabilities found.


zeuxisoo/python-flask-social-oauth-facebook
https://github.com/zeuxisoo/python-flask-social-oauth-facebook
Entry file: None
Scanned: 2016-10-12 14:19:37.329461
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/zeuxisoo/python-flask-social-oauth-facebook.

lpolepeddi/sightings
https://github.com/lpolepeddi/sightings
Entry file: sightings/routes.py
Scanned: 2016-10-12 14:19:53.016186
No vulnerabilities found.


sholsapp/flask-skeleton
https://github.com/sholsapp/flask-skeleton
Entry file: None
Scanned: 2016-10-12 14:19:54.019420
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/sholsapp/flask-skeleton.

adatlabor/soa-demo
https://github.com/adatlabor/soa-demo
Entry file: soa-demo/service.py
Scanned: 2016-10-12 14:20:07.942172
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Dict'>)

speakingcode/pres-soa-flask-backbone
https://github.com/speakingcode/pres-soa-flask-backbone
Entry file: pres-soa-flask-backbone/notes.py
Scanned: 2016-10-12 14:20:17.268883
No vulnerabilities found.


stef/tlsauth
https://github.com/stef/tlsauth
Entry file: tlsauth/flask-demo/webapp.py
Scanned: 2016-10-12 14:20:18.688554
No vulnerabilities found.


kirang89/flask-boiler
https://github.com/kirang89/flask-boiler
Entry file: None
Scanned: 2016-10-12 14:20:26.191949
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

topherjaynes/flasktut
https://github.com/topherjaynes/flasktut
Entry file: flasktut/app/__init__.py
Scanned: 2016-10-12 14:20:38.672786
No vulnerabilities found.


aerialdomo/flaskblog
https://github.com/aerialdomo/flaskblog
Entry file: flaskblog/flat.py
Scanned: 2016-10-12 14:20:43.252396
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flaskblog/env/lib/python2.7/genericpath.py

jonascj/flaskr
https://github.com/jonascj/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 14:20:53.784197
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

microamp/flaskel
https://github.com/microamp/flaskel
Entry file: flaskel/flaskel/__init__.py
Scanned: 2016-10-12 14:20:55.252521
No vulnerabilities found.


a2lin/flaskapp
https://github.com/a2lin/flaskapp
Entry file: flaskapp/flaskapp/application.py
Scanned: 2016-10-12 14:21:01.777433
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

pinoytech/flaskapp
https://github.com/pinoytech/flaskapp
Entry file: flaskapp/flaskapp/application.py
Scanned: 2016-10-12 14:21:07.280744
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

thinboy92/flasktuts
https://github.com/thinboy92/flasktuts
Entry file: flasktuts/app/__init__.py
Scanned: 2016-10-12 14:21:15.820849
No vulnerabilities found.


aahluwal/flaskagain
https://github.com/aahluwal/flaskagain
Entry file: flaskagain/judgement.py
Scanned: 2016-10-12 14:21:24.385541
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flaskagain/renv/lib/python2.7/genericpath.py

elboby/flask-config-override
https://github.com/elboby/flask-config-override
Entry file: flask-config-override/flask_config_override/test/test_cookie.py
Scanned: 2016-10-12 14:21:27.820137
No vulnerabilities found.


MrFichter/flask1
https://github.com/MrFichter/flask1
Entry file: flask1/flask1.py
Scanned: 2016-10-12 14:21:29.127831
No vulnerabilities found.


guilhermecomum/FlaskTutorial
https://github.com/guilhermecomum/FlaskTutorial
Entry file: FlaskTutorial/flaskr/flaskr.py
Scanned: 2016-10-12 14:21:39.224809
No vulnerabilities found.


sherzberg/flask-native-package
https://github.com/sherzberg/flask-native-package
Entry file: flask-native-package/application.py
Scanned: 2016-10-12 14:21:55.164410
No vulnerabilities found.


landakram/squeak
https://github.com/landakram/squeak
Entry file: squeak/app.py
Scanned: 2016-10-12 14:21:56.687860
No vulnerabilities found.


xrefor/flask_tut
https://github.com/xrefor/flask_tut
Entry file: flask_tut/flaskr.py
Scanned: 2016-10-12 14:22:03.039727
No vulnerabilities found.


y2bishop2y/vagrant.flask
https://github.com/y2bishop2y/vagrant.flask
Entry file: None
Scanned: 2016-10-12 14:22:08.478991
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/y2bishop2y/vagrant.flask.

markchadwick/flask-empty
https://github.com/markchadwick/flask-empty
Entry file: flask-empty/main.py
Scanned: 2016-10-12 14:22:15.827343
No vulnerabilities found.


McrCoderDojo/Flask-Webapps
https://github.com/McrCoderDojo/Flask-Webapps
Entry file: Flask-Webapps/flask1.py
Scanned: 2016-10-12 14:22:28.737539
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BinOp'>)

xjdrew/flask-demo
https://github.com/xjdrew/flask-demo
Entry file: None
Scanned: 2016-10-12 14:22:29.233147
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/xjdrew/flask-demo.

aerialdomo/flask_microblog
https://github.com/aerialdomo/flask_microblog
Entry file: flask_microblog/app/__init__.py
Scanned: 2016-10-12 14:22:42.353570
No vulnerabilities found.


xrefor/flask_stuff
https://github.com/xrefor/flask_stuff
Entry file: flask_stuff/main.py
Scanned: 2016-10-12 14:22:55.173036
No vulnerabilities found.


akbarovs/flask-sandbox
https://github.com/akbarovs/flask-sandbox
Entry file: flask-sandbox/app.py
Scanned: 2016-10-12 14:22:56.477124
No vulnerabilities found.


jcerise/flask-photos
https://github.com/jcerise/flask-photos
Entry file: flask-photos/app.py
Scanned: 2016-10-12 14:23:03.816918
No vulnerabilities found.


adesst/flask-blog
https://github.com/adesst/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 14:23:08.386904
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-blog/venv/lib/python2.7/genericpath.py

Hardtack/Flask-Router
https://github.com/Hardtack/Flask-Router
Entry file: Flask-Router/flask_router/tests.py
Scanned: 2016-10-12 14:23:19.661941
No vulnerabilities found.


smdmustaffa/PythonFlask
https://github.com/smdmustaffa/PythonFlask
Entry file: PythonFlask/app/routes.py
Scanned: 2016-10-12 14:23:28.992842
No vulnerabilities found.


jinzhangg/flask-helloworld
https://github.com/jinzhangg/flask-helloworld
Entry file: flask-helloworld/app.py
Scanned: 2016-10-12 14:23:30.332755
No vulnerabilities found.


bogavante/mitsuhiko-flask
https://github.com/bogavante/mitsuhiko-flask
Entry file: mitsuhiko-flask/setup.py
Scanned: 2016-10-12 14:23:43.337775
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hardez/Flask-Skeleton
https://github.com/hardez/Flask-Skeleton
Entry file: Flask-Skeleton/app/__init__.py
Scanned: 2016-10-12 14:23:56.636336
No vulnerabilities found.


stfy86/pruebitasFlask
https://github.com/stfy86/pruebitasFlask
Entry file: pruebitasFlask/practica4/src/app/__init__.py
Scanned: 2016-10-12 14:24:09.896929
No vulnerabilities found.


kracekumar/test-flask
https://github.com/kracekumar/test-flask
Entry file: test-flask/app.py
Scanned: 2016-10-12 14:24:17.758582
No vulnerabilities found.


charliecrissman/microblog
https://github.com/charliecrissman/microblog
Entry file: microblog/app/__init__.py
Scanned: 2016-10-12 14:24:29.595252
No vulnerabilities found.


gourneau/anode
https://github.com/gourneau/anode
Entry file: anode/app.py
Scanned: 2016-10-12 14:24:39.514823
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mmahnken/Flask_to_do_list
https://github.com/mmahnken/Flask_to_do_list
Entry file: Flask_to_do_list/tipsy.py
Scanned: 2016-10-12 14:24:56.553443
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

abulte/Flask-Bootstrap-Fanstatic
https://github.com/abulte/Flask-Bootstrap-Fanstatic
Entry file: Flask-Bootstrap-Fanstatic/application/__init__.py
Scanned: 2016-10-12 14:25:04.368316
No vulnerabilities found.


jennyferpinto/Flask_Part_1
https://github.com/jennyferpinto/Flask_Part_1
Entry file: Flask_Part_1/tipsy.py
Scanned: 2016-10-12 14:25:09.900585
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

stephanienkram/Flask-Log-Tracker
https://github.com/stephanienkram/Flask-Log-Tracker
Entry file: Flask-Log-Tracker/main.py
Scanned: 2016-10-12 14:25:26.696193
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mwmeyer/minimal-flask-socketserver
https://github.com/mwmeyer/minimal-flask-socketserver
Entry file: minimal-flask-socketserver/flash_socket.py
Scanned: 2016-10-12 14:25:30.812243
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rasheedh/Paint-Using-Flask---Mongodb-
https://github.com/rasheedh/Paint-Using-Flask---Mongodb-
Entry file: None
Scanned: 2016-10-12 14:25:31.303219
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/rasheedh/Paint-Using-Flask---Mongodb-.

isms/flask-phonebank-dashboard
https://github.com/isms/flask-phonebank-dashboard
Entry file: flask-phonebank-dashboard/app.py
Scanned: 2016-10-12 14:25:40.310993
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

elboby/flask-test-template
https://github.com/elboby/flask-test-template
Entry file: None
Scanned: 2016-10-12 14:25:46.639964
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/elboby/flask-test-template.

ndrwdn/flat_flask_layout
https://github.com/ndrwdn/flat_flask_layout
Entry file: flat_flask_layout/sitebuilder.py
Scanned: 2016-10-12 14:25:56.971584
No vulnerabilities found.


jpanganiban/flask-heroku-kickstart
https://github.com/jpanganiban/flask-heroku-kickstart
Entry file: None
Scanned: 2016-10-12 14:25:58.385813
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/jpanganiban/flask-heroku-kickstart.

justinxreese/ajax-calculator-flask
https://github.com/justinxreese/ajax-calculator-flask
Entry file: None
Scanned: 2016-10-12 14:26:08.523470
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

prabeesh/Paintapp-Javascript-Canvas-Flask
https://github.com/prabeesh/Paintapp-Javascript-Canvas-Flask
Entry file: Paintapp-Javascript-Canvas-Flask/test.py
Scanned: 2016-10-12 14:26:09.826953
Vulnerability 1:
File: Paintapp-Javascript-Canvas-Flask/test.py
 > User input at line 34, trigger word "form[": 
	imgname = request.form['imagename']
Reassigned in: 
	File: Paintapp-Javascript-Canvas-Flask/test.py
	 > Line 16: imgname = (imagename)
	File: Paintapp-Javascript-Canvas-Flask/test.py
	 > Line 23: imgname = row[0]
	File: Paintapp-Javascript-Canvas-Flask/test.py
	 > Line 37: data = (imgname, imgdata)
File: Paintapp-Javascript-Canvas-Flask/test.py
 > reaches line 19, trigger word "execute(": 
	cur.execute('SELECT * FROM Image WHERE imgname=?', imgname)

Vulnerability 2:
File: Paintapp-Javascript-Canvas-Flask/test.py
 > User input at line 34, trigger word "form[": 
	imgname = request.form['imagename']
Reassigned in: 
	File: Paintapp-Javascript-Canvas-Flask/test.py
	 > Line 16: imgname = (imagename)
	File: Paintapp-Javascript-Canvas-Flask/test.py
	 > Line 23: imgname = row[0]
	File: Paintapp-Javascript-Canvas-Flask/test.py
	 > Line 37: data = (imgname, imgdata)
File: Paintapp-Javascript-Canvas-Flask/test.py
 > reaches line 42, trigger word "execute(": 
	cur.execute('INSERT INTO Image VALUES(?, ?)', data)

Vulnerability 3:
File: Paintapp-Javascript-Canvas-Flask/test.py
 > User input at line 35, trigger word "form[": 
	imgdata = request.form['string']
Reassigned in: 
	File: Paintapp-Javascript-Canvas-Flask/test.py
	 > Line 24: imgdata = row[1]
	File: Paintapp-Javascript-Canvas-Flask/test.py
	 > Line 25: ret_MAYBE_FUNCTION_NAME = render_template('paint.html',saved=imgdata)
	File: Paintapp-Javascript-Canvas-Flask/test.py
	 > Line 28: ret_MAYBE_FUNCTION_NAME = resp
	File: Paintapp-Javascript-Canvas-Flask/test.py
	 > Line 30: ret_MAYBE_FUNCTION_NAME = render_template('paint.html')
	File: Paintapp-Javascript-Canvas-Flask/test.py
	 > Line 37: data = (imgname, imgdata)
	File: Paintapp-Javascript-Canvas-Flask/test.py
	 > Line 46: ret_MAYBE_FUNCTION_NAME = resp
File: Paintapp-Javascript-Canvas-Flask/test.py
 > reaches line 42, trigger word "execute(": 
	cur.execute('INSERT INTO Image VALUES(?, ?)', data)



godber/flask-mobile-switch
https://github.com/godber/flask-mobile-switch
Entry file: flask-mobile-switch/missionops/missionops/__init__.py
Scanned: 2016-10-12 14:26:19.477874
No vulnerabilities found.


naveenpremchand02/paintapp-using-Flask
https://github.com/naveenpremchand02/paintapp-using-Flask
Entry file: None
Scanned: 2016-10-12 14:26:20.769600
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/naveenpremchand02/paintapp-using-Flask.

orkunozbek/deploy_test
https://github.com/orkunozbek/deploy_test
Entry file: deploy_test/app_pack/__init__.py
Scanned: 2016-10-12 14:26:30.103292
No vulnerabilities found.


emi1337/movie_rater
https://github.com/emi1337/movie_rater
Entry file: movie_rater/judgement.py
Scanned: 2016-10-12 14:26:39.175190
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

chrismeono1022/movie-ratings
https://github.com/chrismeono1022/movie-ratings
Entry file: movie-ratings/judgement.py
Scanned: 2016-10-12 14:26:45.235004
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

y2bishop2y/microengine
https://github.com/y2bishop2y/microengine
Entry file: microengine/lib/flask_sqlalchemy.py
Scanned: 2016-10-12 14:26:52.236265
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ajith-herga/searchflask
https://github.com/ajith-herga/searchflask
Entry file: searchflask/new_world.py
Scanned: 2016-10-12 14:26:57.852527
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

akshar-raaj/flaks
https://github.com/akshar-raaj/flaks
Entry file: flaks/hello.py
Scanned: 2016-10-12 14:26:59.141050
No vulnerabilities found.


soniacs/cabinet
https://github.com/soniacs/cabinet
Entry file: cabinet/app/__init__.py
Scanned: 2016-10-12 14:27:05.788612
Vulnerability 1:
File: cabinet/app/views/clients.py
 > User input at line 33, trigger word "form[": 
	client = Client(name=request.form['name'], company=request.form['company'], website=request.form['website'], twitter=request.form['twitter'], email=request.form['email'], telephone=request.form['telephone'], skype=request.form['skype'], street=request.form['street'], street_2=request.form['street_2'], city=request.form['city'], state=request.form['state'], postcode=request.form['postcode'], country=request.form['country'], notes=request.form['notes'])
File: cabinet/app/views/clients.py
 > reaches line 50, trigger word "flash(": 
	flash('Client '%s' was added.' % client.name)

Vulnerability 2:
File: cabinet/app/views/clients.py
 > User input at line 60, trigger word "get(": 
	client = Client.query.get(client_id)
Reassigned in: 
	File: cabinet/app/views/clients.py
	 > Line 80: ret_MAYBE_FUNCTION_NAME = render_template('clients/edit.html',title='Edit %s' % client.name, client=client)
	File: cabinet/app/views/clients.py
	 > Line 84: ret_MAYBE_FUNCTION_NAME = redirect(url_for('login'))
	File: cabinet/app/views/clients.py
	 > Line 79: ret_MAYBE_FUNCTION_NAME = redirect(url_for('clients'))
File: cabinet/app/views/clients.py
 > reaches line 78, trigger word "flash(": 
	flash('Client '%s' has been updated.' % client.name)

Vulnerability 3:
File: cabinet/app/views/clients.py
 > User input at line 89, trigger word "get(": 
	client = Client.query.get(client_id)
Reassigned in: 
	File: cabinet/app/views/clients.py
	 > Line 95: ret_MAYBE_FUNCTION_NAME = render_template('clients/delete.html',title='Delete %s' % client.name, client=client)
	File: cabinet/app/views/clients.py
	 > Line 99: ret_MAYBE_FUNCTION_NAME = redirect(url_for('login'))
	File: cabinet/app/views/clients.py
	 > Line 94: ret_MAYBE_FUNCTION_NAME = redirect(url_for('clients'))
File: cabinet/app/views/clients.py
 > reaches line 93, trigger word "flash(": 
	flash('Client '%s' has been deleted.' % client.name)

Vulnerability 4:
File: cabinet/app/views/invoices.py
 > User input at line 31, trigger word "get(": 
	client = Client.query.get(request.form['client'])
Reassigned in: 
	File: cabinet/app/views/invoices.py
	 > Line 33: invoice = Invoice(name=request.form['name'], currency=request.form['currency'], status=request.form['status'], notes=request.form['notes'], payment=request.form['payment'], internal_notes=request.form['internal_notes'], client=client, project=project)
File: cabinet/app/views/invoices.py
 > reaches line 47, trigger word "flash(": 
	flash('Invoice '%s' was added.' % invoice.name)

Vulnerability 5:
File: cabinet/app/views/invoices.py
 > User input at line 31, trigger word "form[": 
	client = Client.query.get(request.form['client'])
Reassigned in: 
	File: cabinet/app/views/invoices.py
	 > Line 33: invoice = Invoice(name=request.form['name'], currency=request.form['currency'], status=request.form['status'], notes=request.form['notes'], payment=request.form['payment'], internal_notes=request.form['internal_notes'], client=client, project=project)
File: cabinet/app/views/invoices.py
 > reaches line 47, trigger word "flash(": 
	flash('Invoice '%s' was added.' % invoice.name)

Vulnerability 6:
File: cabinet/app/views/invoices.py
 > User input at line 32, trigger word "get(": 
	project = Project.query.get(request.form['project'])
Reassigned in: 
	File: cabinet/app/views/invoices.py
	 > Line 33: invoice = Invoice(name=request.form['name'], currency=request.form['currency'], status=request.form['status'], notes=request.form['notes'], payment=request.form['payment'], internal_notes=request.form['internal_notes'], client=client, project=project)
File: cabinet/app/views/invoices.py
 > reaches line 47, trigger word "flash(": 
	flash('Invoice '%s' was added.' % invoice.name)

Vulnerability 7:
File: cabinet/app/views/invoices.py
 > User input at line 32, trigger word "form[": 
	project = Project.query.get(request.form['project'])
Reassigned in: 
	File: cabinet/app/views/invoices.py
	 > Line 33: invoice = Invoice(name=request.form['name'], currency=request.form['currency'], status=request.form['status'], notes=request.form['notes'], payment=request.form['payment'], internal_notes=request.form['internal_notes'], client=client, project=project)
File: cabinet/app/views/invoices.py
 > reaches line 47, trigger word "flash(": 
	flash('Invoice '%s' was added.' % invoice.name)

Vulnerability 8:
File: cabinet/app/views/invoices.py
 > User input at line 33, trigger word "form[": 
	invoice = Invoice(name=request.form['name'], currency=request.form['currency'], status=request.form['status'], notes=request.form['notes'], payment=request.form['payment'], internal_notes=request.form['internal_notes'], client=client, project=project)
File: cabinet/app/views/invoices.py
 > reaches line 47, trigger word "flash(": 
	flash('Invoice '%s' was added.' % invoice.name)

Vulnerability 9:
File: cabinet/app/views/invoices.py
 > User input at line 59, trigger word "get(": 
	invoice = Invoice.query.get(invoice_id)
Reassigned in: 
	File: cabinet/app/views/invoices.py
	 > Line 80: ret_MAYBE_FUNCTION_NAME = render_template('invoices/edit.html',title='Edit Invoice %s' % invoice.name, invoice=invoice, clients=clients, projects=projects)
	File: cabinet/app/views/invoices.py
	 > Line 86: ret_MAYBE_FUNCTION_NAME = redirect(url_for('login'))
	File: cabinet/app/views/invoices.py
	 > Line 79: ret_MAYBE_FUNCTION_NAME = redirect(url_for('invoices'))
File: cabinet/app/views/invoices.py
 > reaches line 78, trigger word "flash(": 
	flash('Invoice '%s' has been updated.' % invoice.name)

Vulnerability 10:
File: cabinet/app/views/invoices.py
 > User input at line 91, trigger word "get(": 
	invoice = Invoice.query.get(invoice_id)
Reassigned in: 
	File: cabinet/app/views/invoices.py
	 > Line 97: ret_MAYBE_FUNCTION_NAME = render_template('invoices/delete.html',title='Delete Invoice %s' % invoice.name, invoice=invoice)
	File: cabinet/app/views/invoices.py
	 > Line 101: ret_MAYBE_FUNCTION_NAME = redirect(url_for('login'))
	File: cabinet/app/views/invoices.py
	 > Line 96: ret_MAYBE_FUNCTION_NAME = redirect(url_for('invoices'))
File: cabinet/app/views/invoices.py
 > reaches line 95, trigger word "flash(": 
	flash('Invoice '%s' has been deleted.' % invoice.name)

Vulnerability 11:
File: cabinet/app/views/projects.py
 > User input at line 30, trigger word "get(": 
	client = Client.query.get(request.form['client'])
Reassigned in: 
	File: cabinet/app/views/projects.py
	 > Line 31: project = Project(name=request.form['name'], description=request.form['description'], status=request.form['status'], hourly_rate=request.form['hourly_rate'], quote=request.form['quote'], notes=request.form['notes'], client=client)
File: cabinet/app/views/projects.py
 > reaches line 43, trigger word "flash(": 
	flash('Project '%s' was added.' % project.name)

Vulnerability 12:
File: cabinet/app/views/projects.py
 > User input at line 30, trigger word "form[": 
	client = Client.query.get(request.form['client'])
Reassigned in: 
	File: cabinet/app/views/projects.py
	 > Line 31: project = Project(name=request.form['name'], description=request.form['description'], status=request.form['status'], hourly_rate=request.form['hourly_rate'], quote=request.form['quote'], notes=request.form['notes'], client=client)
File: cabinet/app/views/projects.py
 > reaches line 43, trigger word "flash(": 
	flash('Project '%s' was added.' % project.name)

Vulnerability 13:
File: cabinet/app/views/projects.py
 > User input at line 31, trigger word "form[": 
	project = Project(name=request.form['name'], description=request.form['description'], status=request.form['status'], hourly_rate=request.form['hourly_rate'], quote=request.form['quote'], notes=request.form['notes'], client=client)
File: cabinet/app/views/projects.py
 > reaches line 43, trigger word "flash(": 
	flash('Project '%s' was added.' % project.name)

Vulnerability 14:
File: cabinet/app/views/projects.py
 > User input at line 54, trigger word "get(": 
	project = Project.query.get(project_id)
Reassigned in: 
	File: cabinet/app/views/projects.py
	 > Line 71: ret_MAYBE_FUNCTION_NAME = render_template('projects/edit.html',title='Edit %s' % project.name, project=project, clients=clients)
	File: cabinet/app/views/projects.py
	 > Line 76: ret_MAYBE_FUNCTION_NAME = redirect(url_for('login'))
	File: cabinet/app/views/projects.py
	 > Line 70: ret_MAYBE_FUNCTION_NAME = redirect(url_for('projects'))
File: cabinet/app/views/projects.py
 > reaches line 69, trigger word "flash(": 
	flash('Project '%s' has been updated.' % project.name)

Vulnerability 15:
File: cabinet/app/views/projects.py
 > User input at line 81, trigger word "get(": 
	project = Project.query.get(project_id)
Reassigned in: 
	File: cabinet/app/views/projects.py
	 > Line 87: ret_MAYBE_FUNCTION_NAME = render_template('projects/delete.html',title='Delete %s' % project.name, project=project)
	File: cabinet/app/views/projects.py
	 > Line 91: ret_MAYBE_FUNCTION_NAME = redirect(url_for('login'))
	File: cabinet/app/views/projects.py
	 > Line 86: ret_MAYBE_FUNCTION_NAME = redirect(url_for('projects'))
File: cabinet/app/views/projects.py
 > reaches line 85, trigger word "flash(": 
	flash('Project '%s' has been deleted.' % project.name)



MattStockton/manpage
https://github.com/MattStockton/manpage
Entry file: manpage/app.py
Scanned: 2016-10-12 14:27:10.965731
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

qzio/tododis
https://github.com/qzio/tododis
Entry file: tododis/app.py
Scanned: 2016-10-12 14:27:20.060868
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ternup/caddisfly-heroku
https://github.com/ternup/caddisfly-heroku
Entry file: caddisfly-heroku/app.py
Scanned: 2016-10-12 14:27:21.359383
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

aromanovich/flask-webtest
https://github.com/aromanovich/flask-webtest
Entry file: flask-webtest/tests/core.py
Scanned: 2016-10-12 14:27:58.597218
No vulnerabilities found.


ashcrow/flask-track-usage
https://github.com/ashcrow/flask-track-usage
Entry file: flask-track-usage/test/__init__.py
Scanned: 2016-10-12 14:28:00.370453
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lepture/flask-shorturl
https://github.com/lepture/flask-shorturl
Entry file: flask-shorturl/test_shorturl.py
Scanned: 2016-10-12 14:28:05.780972
No vulnerabilities found.


mharrys/flask-blog
https://github.com/mharrys/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 14:28:10.333890
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-blog/venv/lib/python2.7/genericpath.py

kienpham2000/airbrake-flask
https://github.com/kienpham2000/airbrake-flask
Entry file: airbrake-flask/setup.py
Scanned: 2016-10-12 14:28:18.837176
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sintezcs/flask
https://github.com/sintezcs/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 14:28:33.735828
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

wangzexin/flask
https://github.com/wangzexin/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 14:28:40.646868
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

samsolariusleo/Flask
https://github.com/samsolariusleo/Flask
Entry file: Flask/test_hello.py
Scanned: 2016-10-12 14:28:48.188398
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tornado-utils/tornado-restless
https://github.com/tornado-utils/tornado-restless
Entry file: tornado-restless/tests/base.py
Scanned: 2016-10-12 14:28:59.977043
No vulnerabilities found.


adamgreenhall/flask-haml-sass-coffee-template
https://github.com/adamgreenhall/flask-haml-sass-coffee-template
Entry file: flask-haml-sass-coffee-template/app.py
Scanned: 2016-10-12 14:29:05.794183
No vulnerabilities found.


prakhar1989/flask-tuts
https://github.com/prakhar1989/flask-tuts
Entry file: flask-tuts/lesson-2/blogs/__init__.py
Scanned: 2016-10-12 14:29:23.378312
No vulnerabilities found.


Treeki/bitBoard
https://github.com/Treeki/bitBoard
Entry file: bitBoard/bitBoard/__init__.py
Scanned: 2016-10-12 14:29:32.670512
Vulnerability 1:
File: bitBoard/bitBoard/views/board.py
 > User input at line 696, trigger word "get(": 
	thread = Thread.query.get(thread_id)
Reassigned in: 
	File: bitBoard/bitBoard/views/board.py
	 > Line 703: forum = thread.forum
	File: bitBoard/bitBoard/views/board.py
	 > Line 704: url = thread.move_url
	File: bitBoard/bitBoard/views/board.py
	 > Line 730: form = MoveThreadForm(destforum=thread.forum_id)
	File: bitBoard/bitBoard/views/board.py
	 > Line 734: new_forum_id = form.destforum.data
	File: bitBoard/bitBoard/views/board.py
	 > Line 741: old_forum = thread.forum
	File: bitBoard/bitBoard/views/board.py
	 > Line 743: old_forum.post_count -= thread.post_count
	File: bitBoard/bitBoard/views/board.py
	 > Line 745: thread.forum_id = new_forum_id
	File: bitBoard/bitBoard/views/board.py
	 > Line 749: new_forum.post_count += thread.post_count
	File: bitBoard/bitBoard/views/board.py
	 > Line 757: ret_MAYBE_FUNCTION_NAME = redirect(thread.url,code=303)
	File: bitBoard/bitBoard/views/board.py
	 > Line 760: ret_MAYBE_FUNCTION_NAME = render_template('move_thread.html',form=form, forum=forum, thread=thread, url=url)
File: bitBoard/bitBoard/views/board.py
 > reaches line 710, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect(url,code=301)

Vulnerability 2:
File: bitBoard/bitBoard/views/board.py
 > User input at line 775, trigger word "get(": 
	thread = Thread.query.get(thread_id)
Reassigned in: 
	File: bitBoard/bitBoard/views/board.py
	 > Line 782: forum = thread.forum
	File: bitBoard/bitBoard/views/board.py
	 > Line 785: url = thread.sticky_url
	File: bitBoard/bitBoard/views/board.py
	 > Line 787: url = thread.lock_url
	File: bitBoard/bitBoard/views/board.py
	 > Line 791: url = thread.follow_url
	File: bitBoard/bitBoard/views/board.py
	 > Line 808: old_value = thread.is_stickied
	File: bitBoard/bitBoard/views/board.py
	 > Line 822: old_value = thread.is_locked
	File: bitBoard/bitBoard/views/board.py
	 > Line 836: old_value = thread.is_followed_by(g.user)
	File: bitBoard/bitBoard/views/board.py
	 > Line 866: ret_MAYBE_FUNCTION_NAME = jsonify(toast=msg, link_title=link_title)
	File: bitBoard/bitBoard/views/board.py
	 > Line 869: ret_MAYBE_FUNCTION_NAME = form.redirect(url=thread.url)
	File: bitBoard/bitBoard/views/board.py
	 > Line 871: ret_MAYBE_FUNCTION_NAME = render_template('confirm.html',form=form, crumbs_type='thread', forum=forum, thread=thread, final_crumb='%s Thread' % cap_verb, message=message, url=url)
File: bitBoard/bitBoard/views/board.py
 > reaches line 802, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect(url,code=301)

Vulnerability 3:
File: bitBoard/bitBoard/views/base.py
 > User input at line 49, trigger word "get(": 
	target = get_redirect_target() or url
Reassigned in: 
	File: bitBoard/bitBoard/views/base.py
	 > Line 48: ret_MAYBE_FUNCTION_NAME = redirect(self.next.data)
File: bitBoard/bitBoard/views/base.py
 > reaches line 50, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect(target or url_for(endpoint,values),code=303)

Vulnerability 4:
File: bitBoard/bitBoard/views/base.py
 > User input at line 49, trigger word "get(": 
	target = get_redirect_target() or url
Reassigned in: 
	File: bitBoard/bitBoard/views/base.py
	 > Line 48: ret_MAYBE_FUNCTION_NAME = redirect(self.next.data)
File: bitBoard/bitBoard/views/base.py
 > reaches line 50, trigger word "url_for(": 
	ret_MAYBE_FUNCTION_NAME = redirect(target or url_for(endpoint,values),code=303)



byu-osl/familytree-sample-app
https://github.com/byu-osl/familytree-sample-app
Entry file: familytree-sample-app/app.py
Scanned: 2016-10-12 14:29:36.093621
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kmiasko/flask-barcode
https://github.com/kmiasko/flask-barcode
Entry file: flask-barcode/wsgi.py
Scanned: 2016-10-12 14:29:41.520214
No vulnerabilities found.


jayzcode/helloflask
https://github.com/jayzcode/helloflask
Entry file: helloflask/hello.py
Scanned: 2016-10-12 14:29:51.633809
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: helloflask/vene/lib/python2.6/genericpath.py

btomashvili/flasb
https://github.com/btomashvili/flasb
Entry file: None
Scanned: 2016-10-12 14:30:07.467859
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/btomashvili/flasb.

maxcountryman/flask-simpleoauth
https://github.com/maxcountryman/flask-simpleoauth
Entry file: flask-simpleoauth/flask_simpleoauth/app.py
Scanned: 2016-10-12 14:30:11.830984
Vulnerability 1:
File: flask-simpleoauth/flask_simpleoauth/frontend.py
 > User input at line 30, trigger word "get(": 
	next_url = request.args.get('next_url', url_for('.index'))
Reassigned in: 
	File: flask-simpleoauth/flask_simpleoauth/frontend.py
	 > Line 37: ret_MAYBE_FUNCTION_NAME = render_template('login.html',form=form)
File: flask-simpleoauth/flask_simpleoauth/frontend.py
 > reaches line 30, trigger word "url_for(": 
	next_url = request.args.get('next_url', url_for('.index'))

Vulnerability 2:
File: flask-simpleoauth/flask_simpleoauth/frontend.py
 > User input at line 30, trigger word "get(": 
	next_url = request.args.get('next_url', url_for('.index'))
Reassigned in: 
	File: flask-simpleoauth/flask_simpleoauth/frontend.py
	 > Line 37: ret_MAYBE_FUNCTION_NAME = render_template('login.html',form=form)
File: flask-simpleoauth/flask_simpleoauth/frontend.py
 > reaches line 36, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect(next_url)

Vulnerability 3:
File: flask-simpleoauth/flask_simpleoauth/frontend.py
 > User input at line 42, trigger word "get(": 
	next_url = request.args.get('next_url', url_for('.login'))
File: flask-simpleoauth/flask_simpleoauth/frontend.py
 > reaches line 42, trigger word "url_for(": 
	next_url = request.args.get('next_url', url_for('.login'))

Vulnerability 4:
File: flask-simpleoauth/flask_simpleoauth/frontend.py
 > User input at line 42, trigger word "get(": 
	next_url = request.args.get('next_url', url_for('.login'))
File: flask-simpleoauth/flask_simpleoauth/frontend.py
 > reaches line 44, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect(next_url)



bayazee/flask-mosession
https://github.com/bayazee/flask-mosession
Entry file: flask-mosession/example/example.py
Scanned: 2016-10-12 14:30:21.275097
No vulnerabilities found.


speakingcode/pres-soa-flask-backbone
https://github.com/speakingcode/pres-soa-flask-backbone
Entry file: pres-soa-flask-backbone/notes.py
Scanned: 2016-10-12 14:30:25.540683
No vulnerabilities found.


krushton/flask-api-example
https://github.com/krushton/flask-api-example
Entry file: flask-api-example/app.py
Scanned: 2016-10-12 14:30:31.920519
No vulnerabilities found.


bootandy/flask-sample
https://github.com/bootandy/flask-sample
Entry file: flask-sample/guild/app.py
Scanned: 2016-10-12 14:30:34.441859
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

damour/flaskr
https://github.com/damour/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 14:30:40.974561
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

roshow/flasktutorial
https://github.com/roshow/flasktutorial
Entry file: None
Scanned: 2016-10-12 14:30:56.334252
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

jph98/flaskdmg
https://github.com/jph98/flaskdmg
Entry file: flaskdmg/flaskexample.py
Scanned: 2016-10-12 14:30:59.648459
No vulnerabilities found.


akshar-raaj/flaskr
https://github.com/akshar-raaj/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 14:31:01.185267
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fabin/Flaskr
https://github.com/fabin/Flaskr
Entry file: Flaskr/flaskr.py
Scanned: 2016-10-12 14:31:06.626325
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lee814/flaskr
https://github.com/lee814/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 14:31:11.124999
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

codergirl/flaskbabar
https://github.com/codergirl/flaskbabar
Entry file: flaskbabar/hello.py
Scanned: 2016-10-12 14:31:21.573031
Vulnerability 1:
File: flaskbabar/hello.py
 > User input at line 44, trigger word "get(": 
	new_user = BabarUser(request.args.get('username'), request.args.get('email'))
Reassigned in: 
	File: flaskbabar/hello.py
	 > Line 47: json = new_user.id'username''email'new_user.namenew_user.email
File: flaskbabar/hello.py
 > reaches line 48, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify(json)

Vulnerability 2:
File: flaskbabar/hello.py
 > User input at line 61, trigger word "get(": 
	the_user = db.session.query(BabarUser).filter_by(id=request.args.get('user_id')).first()
Reassigned in: 
	File: flaskbabar/hello.py
	 > Line 70: new_task = Task(user_id=the_user.id, name=task_name, description=task_description, dismissable=dismissable, due_date=due_date, active=True)
	File: flaskbabar/hello.py
	 > Line 73: json = new_task.idget_task_view(new_task)
File: flaskbabar/hello.py
 > reaches line 74, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify(json)

Vulnerability 3:
File: flaskbabar/hello.py
 > User input at line 62, trigger word "get(": 
	task_name = request.args.get('name')
Reassigned in: 
	File: flaskbabar/hello.py
	 > Line 70: new_task = Task(user_id=the_user.id, name=task_name, description=task_description, dismissable=dismissable, due_date=due_date, active=True)
	File: flaskbabar/hello.py
	 > Line 73: json = new_task.idget_task_view(new_task)
File: flaskbabar/hello.py
 > reaches line 74, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify(json)

Vulnerability 4:
File: flaskbabar/hello.py
 > User input at line 63, trigger word "get(": 
	task_description = request.args.get('description')
Reassigned in: 
	File: flaskbabar/hello.py
	 > Line 70: new_task = Task(user_id=the_user.id, name=task_name, description=task_description, dismissable=dismissable, due_date=due_date, active=True)
	File: flaskbabar/hello.py
	 > Line 73: json = new_task.idget_task_view(new_task)
File: flaskbabar/hello.py
 > reaches line 74, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify(json)

Vulnerability 5:
File: flaskbabar/hello.py
 > User input at line 64, trigger word "get(": 
	dismissable = request.args.get('dismissable')
Reassigned in: 
	File: flaskbabar/hello.py
	 > Line 66: dismissable = True
	File: flaskbabar/hello.py
	 > Line 70: new_task = Task(user_id=the_user.id, name=task_name, description=task_description, dismissable=dismissable, due_date=due_date, active=True)
	File: flaskbabar/hello.py
	 > Line 73: json = new_task.idget_task_view(new_task)
File: flaskbabar/hello.py
 > reaches line 74, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify(json)

Vulnerability 6:
File: flaskbabar/hello.py
 > User input at line 67, trigger word "get(": 
	due_date = request.args.get('due_date')
Reassigned in: 
	File: flaskbabar/hello.py
	 > Line 69: due_date = datetime.datetime.fromtimestamp(float(due_date))
	File: flaskbabar/hello.py
	 > Line 70: new_task = Task(user_id=the_user.id, name=task_name, description=task_description, dismissable=dismissable, due_date=due_date, active=True)
	File: flaskbabar/hello.py
	 > Line 73: json = new_task.idget_task_view(new_task)
File: flaskbabar/hello.py
 > reaches line 74, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify(json)



rajendrakrp/GAE-Flask-OpenID
https://github.com/rajendrakrp/GAE-Flask-OpenID
Entry file: GAE-Flask-OpenID/flask/sessions.py
Scanned: 2016-10-12 14:31:27.089519
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

JLtheking/FlaskExample
https://github.com/JLtheking/FlaskExample
Entry file: FlaskExample/routes.py
Scanned: 2016-10-12 14:31:32.642352
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

Aussiroth/FlaskPractical
https://github.com/Aussiroth/FlaskPractical
Entry file: FlaskPractical/flask/routes.py
Scanned: 2016-10-12 14:31:36.204879
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

dorajistyle/proposal_center_python_flask_sqlalchemy_jade
https://github.com/dorajistyle/proposal_center_python_flask_sqlalchemy_jade
Entry file: proposal_center_python_flask_sqlalchemy_jade/application/__init__.py
Scanned: 2016-10-12 14:31:43.217840
No vulnerabilities found.


Bob-Thomas/webshopFlask
https://github.com/Bob-Thomas/webshopFlask
Entry file: webshopFlask/webshop.py
Scanned: 2016-10-12 14:31:56.156789
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

haburibe/flask-myapps
https://github.com/haburibe/flask-myapps
Entry file: flask-myapps/todos/todos.py
Scanned: 2016-10-12 14:32:00.465628
No vulnerabilities found.


mykolasmith/flask-leaderboard
https://github.com/mykolasmith/flask-leaderboard
Entry file: flask-leaderboard/leaderboard/__init__.py
Scanned: 2016-10-12 14:32:02.946518
No vulnerabilities found.


betobaz/app_flask
https://github.com/betobaz/app_flask
Entry file: app_flask/app/routes.py
Scanned: 2016-10-12 14:32:07.383223
No vulnerabilities found.


redfive/python-flask
https://github.com/redfive/python-flask
Entry file: python-flask/rest/__init__.py
Scanned: 2016-10-12 14:32:13.528859
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

atbaker/flask-tutorial
https://github.com/atbaker/flask-tutorial
Entry file: flask-tutorial/app/__init__.py
Scanned: 2016-10-12 14:32:33.097668
No vulnerabilities found.


fabin/Flask-Upload
https://github.com/fabin/Flask-Upload
Entry file: Flask-Upload/upload/__init__.py
Scanned: 2016-10-12 14:32:36.409157
Vulnerability 1:
File: Flask-Upload/upload/__init__.py
 > User input at line 24, trigger word "files[": 
	uploadedFile = request.files['file']
Reassigned in: 
	File: Flask-Upload/upload/__init__.py
	 > Line 26: filename = uploadedFile.filename
	File: Flask-Upload/upload/__init__.py
	 > Line 36: ret_MAYBE_FUNCTION_NAME = '
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File (in package)</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '
File: Flask-Upload/upload/__init__.py
 > reaches line 33, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect(s.put(DOMAIN_NAME, filename, ob))



gabrielengel/learn-flask
https://github.com/gabrielengel/learn-flask
Entry file: learn-flask/01-minimal/minimal.py
Scanned: 2016-10-12 14:32:42.768203
No vulnerabilities found.


mutaku/alfred_flask
https://github.com/mutaku/alfred_flask
Entry file: alfred_flask/alfred.py
Scanned: 2016-10-12 14:33:00.588958
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marcilioleite/flask-saude
https://github.com/marcilioleite/flask-saude
Entry file: flask-saude/app/__init__.py
Scanned: 2016-10-12 14:33:04.352135
No vulnerabilities found.


erikgrueter/flask_app
https://github.com/erikgrueter/flask_app
Entry file: None
Scanned: 2016-10-12 14:33:07.664209
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/erikgrueter/flask_app.

elimgoodman/Personnel-Flask
https://github.com/elimgoodman/Personnel-Flask
Entry file: Personnel-Flask/app/__init__.py
Scanned: 2016-10-12 14:33:13.580290
No vulnerabilities found.


bradmerlin/porty_flask
https://github.com/bradmerlin/porty_flask
Entry file: porty_flask/app.py
Scanned: 2016-10-12 14:33:38.139489
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

asap/watchman.flask
https://github.com/asap/watchman.flask
Entry file: None
Scanned: 2016-10-12 14:33:43.457320
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/asap/watchman.flask.

marksteve/flask-nsq
https://github.com/marksteve/flask-nsq
Entry file: flask-nsq/test.py
Scanned: 2016-10-12 14:33:51.801908
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

Duelist/ianb-flask
https://github.com/Duelist/ianb-flask
Entry file: ianb-flask/ianb/__init__.py
Scanned: 2016-10-12 14:34:03.747577
No vulnerabilities found.


Joinhack/agent
https://github.com/Joinhack/agent
Entry file: agent/flask_sqlalchemy.py
Scanned: 2016-10-12 14:34:08.825599
Vulnerability 1:
File: agent/agent/views/user.py
 > User input at line 44, trigger word "form[": 
	area = request.form['area']
Reassigned in: 
	File: agent/agent/views/user.py
	 > Line 46: reg = Region(type=3, name=name, parent_id=area)
	File: agent/agent/views/user.py
	 > Line 49: data = 'value''content''selected'reg.idreg.nameTrue
File: agent/agent/views/user.py
 > reaches line 50, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('code''data'0data)

Vulnerability 2:
File: agent/agent/views/user.py
 > User input at line 45, trigger word "form[": 
	name = request.form['section']
Reassigned in: 
	File: agent/agent/views/user.py
	 > Line 46: reg = Region(type=3, name=name, parent_id=area)
	File: agent/agent/views/user.py
	 > Line 49: data = 'value''content''selected'reg.idreg.nameTrue
File: agent/agent/views/user.py
 > reaches line 50, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('code''data'0data)

Vulnerability 3:
File: agent/agent/views/house.py
 > User input at line 12, trigger word "get(": 
	loginid = session.get(LOGINID)
Reassigned in: 
	File: agent/agent/views/house.py
	 > Line 15: user = um.getByLoginId(loginid)
	File: agent/agent/views/house.py
	 > Line 16: company = um.getUserCompany(user)
	File: agent/agent/views/house.py
	 > Line 17: cities = dm.getCitiesOfCompany(company)
File: agent/agent/views/house.py
 > reaches line 18, trigger word "render_template(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('code''content'0render_template('/house/community_add.html',cities=cities))

Vulnerability 4:
File: agent/agent/views/house.py
 > User input at line 12, trigger word "get(": 
	loginid = session.get(LOGINID)
Reassigned in: 
	File: agent/agent/views/house.py
	 > Line 15: user = um.getByLoginId(loginid)
	File: agent/agent/views/house.py
	 > Line 16: company = um.getUserCompany(user)
	File: agent/agent/views/house.py
	 > Line 17: cities = dm.getCitiesOfCompany(company)
File: agent/agent/views/house.py
 > reaches line 18, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('code''content'0render_template('/house/community_add.html',cities=cities))

Vulnerability 5:
File: agent/agent/views/house.py
 > User input at line 34, trigger word "get(": 
	loginid = session.get(LOGINID)
Reassigned in: 
	File: agent/agent/views/house.py
	 > Line 36: user = um.getByLoginId(loginid)
	File: agent/agent/views/house.py
	 > Line 38: data = cmgmt.queryCommunitiesByUserId(user, q)
	File: agent/agent/views/house.py
	 > Line 33: ret_MAYBE_FUNCTION_NAME = jsonify('code''msg'-1'unkown query')
File: agent/agent/views/house.py
 > reaches line 39, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('code''data'0toselect(data))

Vulnerability 6:
File: agent/agent/views/house.py
 > User input at line 45, trigger word "form[": 
	community_name = request.form['community']
Reassigned in: 
	File: agent/agent/views/house.py
	 > Line 55: community = Community(name=community_name, location=location)
File: agent/agent/views/house.py
 > reaches line 67, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('code''data'0'value''content'community.idcommunity.name)

Vulnerability 7:
File: agent/agent/views/house.py
 > User input at line 46, trigger word "form[": 
	location = request.form['location']
Reassigned in: 
	File: agent/agent/views/house.py
	 > Line 55: community = Community(name=community_name, location=location)
File: agent/agent/views/house.py
 > reaches line 67, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('code''data'0'value''content'community.idcommunity.name)



lachezar/tada_backend
https://github.com/lachezar/tada_backend
Entry file: tada_backend/todo.py
Scanned: 2016-10-12 14:34:13.568485
No vulnerabilities found.


luxuia/gene_designer
https://github.com/luxuia/gene_designer
Entry file: gene_designer/geneDesigne.py
Scanned: 2016-10-12 14:34:30.346157
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

stephanienkram/Flask-Money-Tracker
https://github.com/stephanienkram/Flask-Money-Tracker
Entry file: Flask-Money-Tracker/main.py
Scanned: 2016-10-12 14:34:38.021489
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cismet/sqlparse-flask-webservice
https://github.com/cismet/sqlparse-flask-webservice
Entry file: sqlparse-flask-webservice/sqlparse_webservice.py
Scanned: 2016-10-12 14:34:40.193911
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jonascj/flask_logger_test
https://github.com/jonascj/flask_logger_test
Entry file: flask_logger_test/flask_logger_test.py
Scanned: 2016-10-12 14:34:43.508762
No vulnerabilities found.


rubinovitz/flask-gevent-boiler
https://github.com/rubinovitz/flask-gevent-boiler
Entry file: flask-gevent-boiler/app.py
Scanned: 2016-10-12 14:34:51.852930
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rartavia/flask-babel-example
https://github.com/rartavia/flask-babel-example
Entry file: flask-babel-example/flask-babel-example.py
Scanned: 2016-10-12 14:35:01.202546
No vulnerabilities found.


bradmerlin/mxit-spock_flask
https://github.com/bradmerlin/mxit-spock_flask
Entry file: mxit-spock_flask/app.py
Scanned: 2016-10-12 14:35:04.762651
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

elidickinson/flask-proxy-demo
https://github.com/elidickinson/flask-proxy-demo
Entry file: flask-proxy-demo/hello.py
Scanned: 2016-10-12 14:35:08.089074
No vulnerabilities found.


luckypool/flask-blueprints-template
https://github.com/luckypool/flask-blueprints-template
Entry file: flask-blueprints-template/hello/__init__.py
Scanned: 2016-10-12 14:35:23.886799
No vulnerabilities found.


dylanvee/flask-hello-world
https://github.com/dylanvee/flask-hello-world
Entry file: flask-hello-world/app.py
Scanned: 2016-10-12 14:35:25.438255
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-hello-world/venv/lib/python2.7/genericpath.py

chrismeono1022/microblog_flask_tutorial
https://github.com/chrismeono1022/microblog_flask_tutorial
Entry file: microblog_flask_tutorial/app/__init__.py
Scanned: 2016-10-12 14:35:40.320868
No vulnerabilities found.


adamjmarkham/flask-micro-blog
https://github.com/adamjmarkham/flask-micro-blog
Entry file: flask-micro-blog/micro_blog_flask.py
Scanned: 2016-10-12 14:35:43.741730
No vulnerabilities found.


krushton/flask-location-example
https://github.com/krushton/flask-location-example
Entry file: flask-location-example/app.py
Scanned: 2016-10-12 14:35:52.094806
No vulnerabilities found.


david-torres/flask-rest-quickstart
https://github.com/david-torres/flask-rest-quickstart
Entry file: flask-rest-quickstart/application/__init__.py
Scanned: 2016-10-12 14:36:04.936574
No vulnerabilities found.


bradmerlin/mxit-blackjack_flask
https://github.com/bradmerlin/mxit-blackjack_flask
Entry file: mxit-blackjack_flask/app.py
Scanned: 2016-10-12 14:36:11.670591
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

andyhmltn/stripe-flask-test
https://github.com/andyhmltn/stripe-flask-test
Entry file: stripe-flask-test/main.py
Scanned: 2016-10-12 14:36:14.083667
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

manuclementz/shrt
https://github.com/manuclementz/shrt
Entry file: shrt/app.py
Scanned: 2016-10-12 14:36:26.902706
No vulnerabilities found.


jsutterfield/flaskr-buildout
https://github.com/jsutterfield/flaskr-buildout
Entry file: flaskr-buildout/src/flaskr/flaskr.py
Scanned: 2016-10-12 14:36:38.295831
No vulnerabilities found.


geunieve/ratemyfirefart
https://github.com/geunieve/ratemyfirefart
Entry file: ratemyfirefart/views.py
Scanned: 2016-10-12 14:36:40.644897
No vulnerabilities found.


wangxiaoxiao88/python-bookmanager
https://github.com/wangxiaoxiao88/python-bookmanager
Entry file: python-bookmanager/app.py
Scanned: 2016-10-12 14:36:44.098696
No vulnerabilities found.


Syerram/maintenance-server
https://github.com/Syerram/maintenance-server
Entry file: maintenance-server/run.py
Scanned: 2016-10-12 14:36:52.448419
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

corydolphin/boilerflask-facebook
https://github.com/corydolphin/boilerflask-facebook
Entry file: boilerflask-facebook/boilerflask/__init__.py
Scanned: 2016-10-12 14:37:02.202137
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ajith-herga/searchflask
https://github.com/ajith-herga/searchflask
Entry file: searchflask/new_world.py
Scanned: 2016-10-12 14:37:04.716175
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

subdesign/temp_Flaskblog
https://github.com/subdesign/temp_Flaskblog
Entry file: temp_Flaskblog/app.py
Scanned: 2016-10-12 14:37:09.305204
No vulnerabilities found.


bettertest-org/flask_app_skeleton_on_gae
https://github.com/bettertest-org/flask_app_skeleton_on_gae
Entry file: flask_app_skeleton_on_gae/lib/flask/sessions.py
Scanned: 2016-10-12 14:37:16.193267
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

liontree/lemonbook
https://github.com/liontree/lemonbook
Entry file: lemonbook/__init__.py
Scanned: 2016-10-12 14:37:29.163011
Vulnerability 1:
File: lemonbook/common/flask_login.py
 > User input at line 227, trigger word "get(": 
	cookie_name = config.get('REMEMBER_COOKIE_NAME', COOKIE_NAME)
File: lemonbook/common/flask_login.py
 > reaches line 237, trigger word "set_cookie(": 
	response.set_cookie(cookie_name, data,expires=expires, domain=domain)

Vulnerability 2:
File: lemonbook/views/notes.py
 > User input at line 50, trigger word "form[": 
	date = request.form['date'].strip()
Reassigned in: 
	File: lemonbook/views/notes.py
	 > Line 55: date = date.replace('/', '')
	File: lemonbook/views/notes.py
	 > Line 48: ret_MAYBE_FUNCTION_NAME = render_template('latest.html',contents=contents)
	File: lemonbook/views/notes.py
	 > Line 53: ret_MAYBE_FUNCTION_NAME = redirect(url_for('latest'))
File: lemonbook/views/notes.py
 > reaches line 56, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect(url_for('date',id=user_id, date=date))

Vulnerability 3:
File: lemonbook/views/notes.py
 > User input at line 50, trigger word "form[": 
	date = request.form['date'].strip()
Reassigned in: 
	File: lemonbook/views/notes.py
	 > Line 55: date = date.replace('/', '')
	File: lemonbook/views/notes.py
	 > Line 48: ret_MAYBE_FUNCTION_NAME = render_template('latest.html',contents=contents)
	File: lemonbook/views/notes.py
	 > Line 53: ret_MAYBE_FUNCTION_NAME = redirect(url_for('latest'))
File: lemonbook/views/notes.py
 > reaches line 56, trigger word "url_for(": 
	ret_MAYBE_FUNCTION_NAME = redirect(url_for('date',id=user_id, date=date))



abhiomkar/contacts-rest
https://github.com/abhiomkar/contacts-rest
Entry file: contacts-rest/contacts.py
Scanned: 2016-10-12 14:37:30.456581
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

Giorgix/thor
https://github.com/Giorgix/thor
Entry file: thor/thor.py
Scanned: 2016-10-12 14:37:34.887173
No vulnerabilities found.


lhr530124/nozomiServer
https://github.com/lhr530124/nozomiServer
Entry file: nozomiServer/app.py
Scanned: 2016-10-12 14:37:44.390970
No vulnerabilities found.


lepture/flask-oauthlib
https://github.com/lepture/flask-oauthlib
Entry file: flask-oauthlib/flask_oauthlib/provider/oauth1.py
Scanned: 2016-10-12 14:37:55.550971
Vulnerability 1:
File: flask-oauthlib/flask_oauthlib/provider/oauth1.py
 > User input at line 87, trigger word "get(": 
	error_endpoint = self.app.config.get('OAUTH1_PROVIDER_ERROR_ENDPOINT')
Reassigned in: 
	File: flask-oauthlib/flask_oauthlib/provider/oauth1.py
	 > Line 90: ret_MAYBE_FUNCTION_NAME = '/oauth/errors'
	File: flask-oauthlib/flask_oauthlib/provider/oauth1.py
	 > Line 86: ret_MAYBE_FUNCTION_NAME = error_uri
File: flask-oauthlib/flask_oauthlib/provider/oauth1.py
 > reaches line 89, trigger word "url_for(": 
	ret_MAYBE_FUNCTION_NAME = url_for(error_endpoint)

Vulnerability 2:
File: flask-oauthlib/flask_oauthlib/provider/oauth2.py
 > User input at line 104, trigger word "get(": 
	error_endpoint = self.app.config.get('OAUTH2_PROVIDER_ERROR_ENDPOINT')
Reassigned in: 
	File: flask-oauthlib/flask_oauthlib/provider/oauth2.py
	 > Line 107: ret_MAYBE_FUNCTION_NAME = '/oauth/errors'
	File: flask-oauthlib/flask_oauthlib/provider/oauth2.py
	 > Line 103: ret_MAYBE_FUNCTION_NAME = error_uri
File: flask-oauthlib/flask_oauthlib/provider/oauth2.py
 > reaches line 106, trigger word "url_for(": 
	ret_MAYBE_FUNCTION_NAME = url_for(error_endpoint)

Vulnerability 3:
File: flask-oauthlib/flask_oauthlib/provider/oauth2.py
 > User input at line 447, trigger word "get(": 
	redirect_uri = credentials.get('redirect_uri')
Reassigned in: 
	File: flask-oauthlib/flask_oauthlib/provider/oauth2.py
	 > Line 464: ret_MAYBE_FUNCTION_NAME = redirect(add_params_to_uri(self.error_uri, 'error'str(e)))
	File: flask-oauthlib/flask_oauthlib/provider/oauth2.py
	 > Line 455: ret_MAYBE_FUNCTION_NAME = create_response(ret)
	File: flask-oauthlib/flask_oauthlib/provider/oauth2.py
	 > Line 458: ret_MAYBE_FUNCTION_NAME = redirect(e.in_uri(self.error_uri))
File: flask-oauthlib/flask_oauthlib/provider/oauth2.py
 > reaches line 461, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect(e.in_uri(redirect_uri or self.error_uri))



miguelgrinberg/Flask-HTTPAuth
https://github.com/miguelgrinberg/Flask-HTTPAuth
Entry file: Flask-HTTPAuth/examples/basic_auth.py
Scanned: 2016-10-12 14:38:02.451558
No vulnerabilities found.


cburmeister/flask-bones
https://github.com/cburmeister/flask-bones
Entry file: flask-bones/app/__init__.py
Scanned: 2016-10-12 14:38:06.989823
No vulnerabilities found.


sysr-q/flask-nsa
https://github.com/sysr-q/flask-nsa
Entry file: flask-nsa/example_app.py
Scanned: 2016-10-12 14:38:12.318094
No vulnerabilities found.


lepture/flask-storage
https://github.com/lepture/flask-storage
Entry file: flask-storage/tests/__init__.py
Scanned: 2016-10-12 14:38:13.827581
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

plastboks/Flaskmarks
https://github.com/plastboks/Flaskmarks
Entry file: Flaskmarks/flaskmarks/__init__.py
Scanned: 2016-10-12 14:38:38.435685
Vulnerability 1:
File: Flaskmarks/flaskmarks/views/auth.py
 > User input at line 33, trigger word ".data": 
	u = User.by_uname_or_email(form.username.data)
File: Flaskmarks/flaskmarks/views/auth.py
 > reaches line 38, trigger word "flash(": 
	flash('Welcome %s.' % u.username,category='success')



martinp/jarvis2
https://github.com/martinp/jarvis2
Entry file: jarvis2/app/main.py
Scanned: 2016-10-12 14:38:45.072281
No vulnerabilities found.


akhilchandran/flask
https://github.com/akhilchandran/flask
Entry file: flask/setup.py
Scanned: 2016-10-12 14:38:45.967538
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

JamesHoover/Flask
https://github.com/JamesHoover/Flask
Entry file: Flask/test_hello.py
Scanned: 2016-10-12 14:38:52.520913
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dhanababu-nyros/flask-sqlalchemy
https://github.com/dhanababu-nyros/flask-sqlalchemy
Entry file: flask-sqlalchemy/run.py
Scanned: 2016-10-12 14:39:02.841743
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

klen/mixer
https://github.com/klen/mixer
Entry file: mixer/tests/test_flask.py
Scanned: 2016-10-12 14:39:08.636688
No vulnerabilities found.


wrobstory/mcflyin
https://github.com/wrobstory/mcflyin
Entry file: mcflyin/mcflyin/application.py
Scanned: 2016-10-12 14:39:16.032149
No vulnerabilities found.


Hardtack/Flask-Negotiation
https://github.com/Hardtack/Flask-Negotiation
Entry file: Flask-Negotiation/tests/test_negotiation.py
Scanned: 2016-10-12 14:39:25.593617
No vulnerabilities found.


marksteve/flask-redisconfig
https://github.com/marksteve/flask-redisconfig
Entry file: flask-redisconfig/example.py
Scanned: 2016-10-12 14:39:42.015269
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

benhosmer/flask-zurb
https://github.com/benhosmer/flask-zurb
Entry file: flask-zurb/app.py
Scanned: 2016-10-12 14:39:50.739116
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mies/getting-started-flask-redis
https://github.com/mies/getting-started-flask-redis
Entry file: getting-started-flask-redis/app.py
Scanned: 2016-10-12 14:39:54.180776
No vulnerabilities found.


eriktaubeneck/flask-twitter-oembedder
https://github.com/eriktaubeneck/flask-twitter-oembedder
Entry file: flask-twitter-oembedder/tests/test_flask_twitter_oembedder.py
Scanned: 2016-10-12 14:40:07.096535
No vulnerabilities found.


DasIch/Flask-MakeStatic
https://github.com/DasIch/Flask-MakeStatic
Entry file: Flask-MakeStatic/flask_makestatic/__init__.py
Scanned: 2016-10-12 14:40:10.775213
No vulnerabilities found.


insynchq/flask-captain
https://github.com/insynchq/flask-captain
Entry file: flask-captain/example.py
Scanned: 2016-10-12 14:40:16.227170
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fedenusy/flaskr
https://github.com/fedenusy/flaskr
Entry file: flaskr/flaskr.py
Scanned: 2016-10-12 14:40:24.736689
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

scottmiao/Flaskr
https://github.com/scottmiao/Flaskr
Entry file: Flaskr/flaskr.py
Scanned: 2016-10-12 14:40:30.253137
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

rubensayshi/flaskbp
https://github.com/rubensayshi/flaskbp
Entry file: flaskbp/flaskbp/application.py
Scanned: 2016-10-12 14:40:35.589904
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ovet/flaskboard
https://github.com/ovet/flaskboard
Entry file: flaskboard/flaskboard.py
Scanned: 2016-10-12 14:40:42.923190
No vulnerabilities found.


iaserrat/flaskify
https://github.com/iaserrat/flaskify
Entry file: flaskify/flaskify.py
Scanned: 2016-10-12 14:40:48.240801
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

EventMobi/thorium
https://github.com/EventMobi/thorium
Entry file: thorium/thorium/testsuite/test_thoriumflask.py
Scanned: 2016-10-12 14:40:59.010088
No vulnerabilities found.


paraboul/FlaskPress
https://github.com/paraboul/FlaskPress
Entry file: None
Scanned: 2016-10-12 14:41:04.501921
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/paraboul/FlaskPress.

dl33/FlaskBlog
https://github.com/dl33/FlaskBlog
Entry file: FlaskBlog/flask/lib/python2.7/site-packages/flask_sqlalchemy.py
Scanned: 2016-10-12 14:41:13.982204
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flebel/flask-ip-hostname-resolvers
https://github.com/flebel/flask-ip-hostname-resolvers
Entry file: flask-ip-hostname-resolvers/ip.py
Scanned: 2016-10-12 14:41:15.320924
No vulnerabilities found.


newbiemasih/Flask-Course
https://github.com/newbiemasih/Flask-Course
Entry file: None
Scanned: 2016-10-12 14:41:21.020571
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

port-/flask-skeleton
https://github.com/port-/flask-skeleton
Entry file: None
Scanned: 2016-10-12 14:41:25.550779
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/port-/flask-skeleton.

AlexeyMK/gglto_flask
https://github.com/AlexeyMK/gglto_flask
Entry file: gglto_flask/gglto.py
Scanned: 2016-10-12 14:41:36.396231
No vulnerabilities found.


xor-xor/webapp_flask
https://github.com/xor-xor/webapp_flask
Entry file: webapp_flask/app.py
Scanned: 2016-10-12 14:41:43.742528
No vulnerabilities found.


suneel0101/flask-buddy
https://github.com/suneel0101/flask-buddy
Entry file: flask-buddy/server.py
Scanned: 2016-10-12 14:41:49.057019
No vulnerabilities found.


sanoju/GaeFlask
https://github.com/sanoju/GaeFlask
Entry file: GaeFlask/flask/sessions.py
Scanned: 2016-10-12 14:41:57.258634
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kfk/flask-blog
https://github.com/kfk/flask-blog
Entry file: flask-blog/blog.py
Scanned: 2016-10-12 14:42:03.806971
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: flask-blog/venv/lib/python2.7/genericpath.py

irakasleibiltaria/flask-tutorial
https://github.com/irakasleibiltaria/flask-tutorial
Entry file: flask-tutorial/hello.py
Scanned: 2016-10-12 14:42:08.134580
No vulnerabilities found.


wodim/flask-test
https://github.com/wodim/flask-test
Entry file: flask-test/hello.py
Scanned: 2016-10-12 14:42:15.490112
No vulnerabilities found.


sammyrulez/flask-grolla
https://github.com/sammyrulez/flask-grolla
Entry file: flask-grolla/tests.py
Scanned: 2016-10-12 14:42:28.145847
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

maxbucknell/vanilla_flask
https://github.com/maxbucknell/vanilla_flask
Entry file: vanilla_flask/vanilla/__init__.py
Scanned: 2016-10-12 14:42:33.041393
No vulnerabilities found.


DamnedFacts/flask-contact
https://github.com/DamnedFacts/flask-contact
Entry file: flask-contact/main.py
Scanned: 2016-10-12 14:42:35.549753
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marcilioleite/flask-websocket
https://github.com/marcilioleite/flask-websocket
Entry file: flask-websocket/server.py
Scanned: 2016-10-12 14:42:43.869135
No vulnerabilities found.


duffy25/sample_flask
https://github.com/duffy25/sample_flask
Entry file: sample_flask/sample_flask.py
Scanned: 2016-10-12 14:42:56.138022
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

elijahc/hello_flask
https://github.com/elijahc/hello_flask
Entry file: hello_flask/hello.py
Scanned: 2016-10-12 14:43:05.460034
No vulnerabilities found.


tmadsen/flask-scaffold
https://github.com/tmadsen/flask-scaffold
Entry file: flask-scaffold/[appname].py
Scanned: 2016-10-12 14:43:15.491569
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tomashley/flask-template
https://github.com/tomashley/flask-template
Entry file: flask-template/app/urls.py
Scanned: 2016-10-12 14:43:17.947551
No vulnerabilities found.


PromooD/flask-aselect
https://github.com/PromooD/flask-aselect
Entry file: flask-aselect/flask_aselect/core.py
Scanned: 2016-10-12 14:43:29.371071
No vulnerabilities found.


danthemanvsqz/Flask-Demo
https://github.com/danthemanvsqz/Flask-Demo
Entry file: Flask-Demo/contacts.py
Scanned: 2016-10-12 14:43:33.068037
No vulnerabilities found.


nisiotis/flask_app
https://github.com/nisiotis/flask_app
Entry file: None
Scanned: 2016-10-12 14:43:35.567033
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/nisiotis/flask_app.

Joinhack/agent
https://github.com/Joinhack/agent
Entry file: agent/flask_sqlalchemy.py
Scanned: 2016-10-12 14:43:44.544373
Vulnerability 1:
File: agent/agent/views/user.py
 > User input at line 44, trigger word "form[": 
	area = request.form['area']
Reassigned in: 
	File: agent/agent/views/user.py
	 > Line 46: reg = Region(type=3, name=name, parent_id=area)
	File: agent/agent/views/user.py
	 > Line 49: data = 'value''content''selected'reg.idreg.nameTrue
File: agent/agent/views/user.py
 > reaches line 50, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('code''data'0data)

Vulnerability 2:
File: agent/agent/views/user.py
 > User input at line 45, trigger word "form[": 
	name = request.form['section']
Reassigned in: 
	File: agent/agent/views/user.py
	 > Line 46: reg = Region(type=3, name=name, parent_id=area)
	File: agent/agent/views/user.py
	 > Line 49: data = 'value''content''selected'reg.idreg.nameTrue
File: agent/agent/views/user.py
 > reaches line 50, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('code''data'0data)

Vulnerability 3:
File: agent/agent/views/house.py
 > User input at line 12, trigger word "get(": 
	loginid = session.get(LOGINID)
Reassigned in: 
	File: agent/agent/views/house.py
	 > Line 15: user = um.getByLoginId(loginid)
	File: agent/agent/views/house.py
	 > Line 16: company = um.getUserCompany(user)
	File: agent/agent/views/house.py
	 > Line 17: cities = dm.getCitiesOfCompany(company)
File: agent/agent/views/house.py
 > reaches line 18, trigger word "render_template(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('code''content'0render_template('/house/community_add.html',cities=cities))

Vulnerability 4:
File: agent/agent/views/house.py
 > User input at line 12, trigger word "get(": 
	loginid = session.get(LOGINID)
Reassigned in: 
	File: agent/agent/views/house.py
	 > Line 15: user = um.getByLoginId(loginid)
	File: agent/agent/views/house.py
	 > Line 16: company = um.getUserCompany(user)
	File: agent/agent/views/house.py
	 > Line 17: cities = dm.getCitiesOfCompany(company)
File: agent/agent/views/house.py
 > reaches line 18, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('code''content'0render_template('/house/community_add.html',cities=cities))

Vulnerability 5:
File: agent/agent/views/house.py
 > User input at line 34, trigger word "get(": 
	loginid = session.get(LOGINID)
Reassigned in: 
	File: agent/agent/views/house.py
	 > Line 36: user = um.getByLoginId(loginid)
	File: agent/agent/views/house.py
	 > Line 38: data = cmgmt.queryCommunitiesByUserId(user, q)
	File: agent/agent/views/house.py
	 > Line 33: ret_MAYBE_FUNCTION_NAME = jsonify('code''msg'-1'unkown query')
File: agent/agent/views/house.py
 > reaches line 39, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('code''data'0toselect(data))

Vulnerability 6:
File: agent/agent/views/house.py
 > User input at line 45, trigger word "form[": 
	community_name = request.form['community']
Reassigned in: 
	File: agent/agent/views/house.py
	 > Line 55: community = Community(name=community_name, location=location)
File: agent/agent/views/house.py
 > reaches line 67, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('code''data'0'value''content'community.idcommunity.name)

Vulnerability 7:
File: agent/agent/views/house.py
 > User input at line 46, trigger word "form[": 
	location = request.form['location']
Reassigned in: 
	File: agent/agent/views/house.py
	 > Line 55: community = Community(name=community_name, location=location)
File: agent/agent/views/house.py
 > reaches line 67, trigger word "jsonify(": 
	ret_MAYBE_FUNCTION_NAME = jsonify('code''data'0'value''content'community.idcommunity.name)



brianly/flask-mega-tutorial
https://github.com/brianly/flask-mega-tutorial
Entry file: flask-mega-tutorial/app/__init__.py
Scanned: 2016-10-12 14:43:49.059916
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ivosevicmikica/testiranje
https://github.com/ivosevicmikica/testiranje
Entry file: testiranje/index.py
Scanned: 2016-10-12 14:43:56.391643
No vulnerabilities found.


myevan/microblog
https://github.com/myevan/microblog
Entry file: microblog/views.py
Scanned: 2016-10-12 14:44:05.736915
No vulnerabilities found.


Eleonore9/StreetMap_ChallengePy
https://github.com/Eleonore9/StreetMap_ChallengePy
Entry file: StreetMap_ChallengePy/StreetMap.py
Scanned: 2016-10-12 14:44:09.189241
No vulnerabilities found.


eriktaubeneck/flask-s3-assets-example
https://github.com/eriktaubeneck/flask-s3-assets-example
Entry file: flask-s3-assets-example/app/__init__.py
Scanned: 2016-10-12 14:44:18.586349
No vulnerabilities found.


vasnake/mapfeatureserver
https://github.com/vasnake/mapfeatureserver
Entry file: None
Scanned: 2016-10-12 14:44:31.640826
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/vasnake/mapfeatureserver.

EvilDmitri/FlaskProject_FuncExe
https://github.com/EvilDmitri/FlaskProject_FuncExe
Entry file: None
Scanned: 2016-10-12 14:44:40.329096
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

epelz/flask-fb-demo
https://github.com/epelz/flask-fb-demo
Entry file: flask-fb-demo/main.py
Scanned: 2016-10-12 14:44:44.662680
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tonilxm/1stFlask
https://github.com/tonilxm/1stFlask
Entry file: 1stFlask/src/lib/flask/sessions.py
Scanned: 2016-10-12 14:44:52.719233
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cldershem/WebFlask-CleanTemplate
https://github.com/cldershem/WebFlask-CleanTemplate
Entry file: None
Scanned: 2016-10-12 14:45:01.867190
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

brooks/python-flask-sample
https://github.com/brooks/python-flask-sample
Entry file: python-flask-sample/hello.py
Scanned: 2016-10-12 14:45:10.080208
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: python-flask-sample/venv/lib/python2.7/genericpath.py

palei/Just-Another-Flask-App
https://github.com/palei/Just-Another-Flask-App
Entry file: Just-Another-Flask-App/app/__init__.py
Scanned: 2016-10-12 14:45:11.955515
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

noisufnoc/HowToFlask
https://github.com/noisufnoc/HowToFlask
Entry file: HowToFlask/app.py
Scanned: 2016-10-12 14:45:17.313270
No vulnerabilities found.


FriendCode/python-flask-sample
https://github.com/FriendCode/python-flask-sample
Entry file: python-flask-sample/hello.py
Scanned: 2016-10-12 14:45:28.355221
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: python-flask-sample/venv/lib/python2.7/genericpath.py

wavrin/flask-mongo-site
https://github.com/wavrin/flask-mongo-site
Entry file: flask-mongo-site/blog/__init__.py
Scanned: 2016-10-12 14:45:37.173880
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marulkan/nagios-status-flask
https://github.com/marulkan/nagios-status-flask
Entry file: nagios-status-flask/hello.py
Scanned: 2016-10-12 14:45:45.578018
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

thrisp/flarf
https://github.com/thrisp/flarf
Entry file: flarf/examples/example.py
Scanned: 2016-10-12 14:45:51.267171
No vulnerabilities found.


NSkelsey/trance_piano
https://github.com/NSkelsey/trance_piano
Entry file: trance_piano/app.py
Scanned: 2016-10-12 14:46:07.105865
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

lhr530124/nozomiServer
https://github.com/lhr530124/nozomiServer
Entry file: nozomiServer/app.py
Scanned: 2016-10-12 14:46:14.478765
No vulnerabilities found.


skrieder/microblog
https://github.com/skrieder/microblog
Entry file: None
Scanned: 2016-10-12 14:46:23.869391
No vulnerabilities found.
An Error occurred while scanning the repo: Other Error Unknown while cloning :-(

carlosvin/cmsflask
https://github.com/carlosvin/cmsflask
Entry file: cmsflask/cmsflask/__init__.py
Scanned: 2016-10-12 14:46:25.301601
No vulnerabilities found.


Sadhanandh/Fb-page-manager
https://github.com/Sadhanandh/Fb-page-manager
Entry file: Fb-page-manager/flask_app.py
Scanned: 2016-10-12 14:46:29.730270
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

thomas-/pyshorturls
https://github.com/thomas-/pyshorturls
Entry file: pyshorturls/short.py
Scanned: 2016-10-12 14:46:34.425424
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sangallimarco/arduino_raspberry_garden_ui
https://github.com/sangallimarco/arduino_raspberry_garden_ui
Entry file: arduino_raspberry_garden_ui/main.py
Scanned: 2016-10-12 14:46:39.272644
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sigilioso/long_polling_example
https://github.com/sigilioso/long_polling_example
Entry file: long_polling_example/server.py
Scanned: 2016-10-12 14:46:51.079835
No vulnerabilities found.


zxt/quotl
https://github.com/zxt/quotl
Entry file: quotl/quotl/__init__.py
Scanned: 2016-10-12 14:46:58.570392
No vulnerabilities found.


bdeeney/crudite
https://github.com/bdeeney/crudite
Entry file: crudite/examples/hello_flask.py
Scanned: 2016-10-12 14:47:08.010559
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

luhn/address-book
https://github.com/luhn/address-book
Entry file: address-book/app.py
Scanned: 2016-10-12 14:47:12.424179
No vulnerabilities found.


cameronbracken/pitchforksearch
https://github.com/cameronbracken/pitchforksearch
Entry file: pitchforksearch/pitchforksearch/__init__.py
Scanned: 2016-10-12 14:47:18.889167
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

chromy/pithy
https://github.com/chromy/pithy
Entry file: None
Scanned: 2016-10-12 14:47:25.320025
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/chromy/pithy.

adedot/countries_project
https://github.com/adedot/countries_project
Entry file: countries_project/flaskr.py
Scanned: 2016-10-12 14:47:29.668758
No vulnerabilities found.


titainium/PRPHOTO
https://github.com/titainium/PRPHOTO
Entry file: PRPHOTO/prphoto.py
Scanned: 2016-10-12 14:47:39.944944
No vulnerabilities found.


keybits/stripe-experiments
https://github.com/keybits/stripe-experiments
Entry file: stripe-experiments/app.py
Scanned: 2016-10-12 14:47:41.296193
No vulnerabilities found.


izaac/twitty
https://github.com/izaac/twitty
Entry file: twitty/twitty.py
Scanned: 2016-10-12 14:47:45.749140
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

fc-thrisp-hurrata-dlm-graveyard/flack
https://github.com/fc-thrisp-hurrata-dlm-graveyard/flack
Entry file: flack/tests/test_app/__init__.py
Scanned: 2016-10-12 14:47:52.190188
No vulnerabilities found.


cenk/github-flask
https://github.com/cenk/github-flask
Entry file: github-flask/test_flask_github.py
Scanned: 2016-10-12 14:48:08.630803
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

davidism/basic_flask
https://github.com/davidism/basic_flask
Entry file: basic_flask/basic_app/__init__.py
Scanned: 2016-10-12 14:48:25.923391
No vulnerabilities found.


quokkaproject/quokka
https://github.com/quokkaproject/quokka
Entry file: quokka/quokka/tests/flask_csrf_test_client.py
Scanned: 2016-10-12 14:48:34.458288
No vulnerabilities found.


akprasad/flask-forum
https://github.com/akprasad/flask-forum
Entry file: flask-forum/application/__init__.py
Scanned: 2016-10-12 14:48:41.462998
No vulnerabilities found.


miguelgrinberg/Flask-Runner
https://github.com/miguelgrinberg/Flask-Runner
Entry file: Flask-Runner/examples/runner.py
Scanned: 2016-10-12 14:48:45.995883
No vulnerabilities found.


pallets/flask
https://github.com/pallets/flask
Entry file: flask/setup.py
Scanned: 2016-10-18 08:11:24.915779
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

gigq/flasktodo
https://github.com/gigq/flasktodo
Entry file: flasktodo/application.py
Scanned: 2016-10-18 08:11:26.246544
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flosch/simpleapi
https://github.com/flosch/simpleapi
Entry file: simpleapi/example_project/server/flask1/app.py
Scanned: 2016-10-18 08:11:27.963021
No vulnerabilities found.


codebykat/robotkitten
https://github.com/codebykat/robotkitten
Entry file: None
Scanned: 2016-10-18 08:11:28.473730
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/codebykat/robotkitten.

mitsuhiko/flask-oauth
https://github.com/mitsuhiko/flask-oauth
Entry file: flask-oauth/example/facebook.py
Scanned: 2016-10-18 08:11:29.515950
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-openid
https://github.com/mitsuhiko/flask-openid
Entry file: flask-openid/flask_openid.py
Scanned: 2016-10-18 08:11:30.535521
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.BoolOp'>)

artisonian/flaskengine
https://github.com/artisonian/flaskengine
Entry file: flaskengine/flaskengine/__init__.py
Scanned: 2016-10-18 08:11:33.880936
No vulnerabilities found.


toomoresuch/template-gae-with-flask
https://github.com/toomoresuch/template-gae-with-flask
Entry file: template-gae-with-flask/application.py
Scanned: 2016-10-18 08:11:34.403575
No vulnerabilities found.
An Error occurred while scanning the repo: Input needs to be a file. Path: template-gae-with-flask/flask.py

aljoscha/shot-o-matic
https://github.com/aljoscha/shot-o-matic
Entry file: shot-o-matic/shotomatic.py
Scanned: 2016-10-18 08:11:35.417208
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-sqlalchemy
https://github.com/mitsuhiko/flask-sqlalchemy
Entry file: flask-sqlalchemy/run.py
Scanned: 2016-10-18 08:11:36.440531
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-fungiform
https://github.com/mitsuhiko/flask-fungiform
Entry file: flask-fungiform/examples/example.py
Scanned: 2016-10-18 08:11:38.682909
No vulnerabilities found.


fsouza/talks
https://github.com/fsouza/talks
Entry file: talks/flask/app.py
Scanned: 2016-10-18 08:11:39.681068
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

unbracketed/flapp
https://github.com/unbracketed/flapp
Entry file: flapp/flapp/project_template/application.py
Scanned: 2016-10-18 08:11:40.249110
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

dcolish/flask-markdown
https://github.com/dcolish/flask-markdown
Entry file: flask-markdown/tests/test_markdown.py
Scanned: 2016-10-18 08:12:23.420588
No vulnerabilities found.


blossom/flask-gae-skeleton
https://github.com/blossom/flask-gae-skeleton
Entry file: flask-gae-skeleton/gae/main.py
Scanned: 2016-10-18 08:12:23.922133
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

kijun/flask-methodhack
https://github.com/kijun/flask-methodhack
Entry file: flask-methodhack/flaskext/methodhack.py
Scanned: 2016-10-18 08:12:26.173178
No vulnerabilities found.


viniciusfs/pasted-flask
https://github.com/viniciusfs/pasted-flask
Entry file: pasted-flask/pasted.py
Scanned: 2016-10-18 08:12:27.400028
Vulnerability 1:
File: pasted-flask/pasted.py
 > User input at line 219, trigger word "form[": 
	hexdigest = calc_md5(request.form['code'])
Reassigned in: 
	File: pasted-flask/pasted.py
	 > Line 221: paste = query_db('select * from pasted where md5 = ?', [hexdigest],one=True)
	File: pasted-flask/pasted.py
	 > Line 225: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 231: paste_id = cur.lastrowid
	File: pasted-flask/pasted.py
	 > Line 232: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 234: ret_MAYBE_FUNCTION_NAME = render_template('view.html',paste=paste)
	File: pasted-flask/pasted.py
	 > Line 203: paste = query_db('select * from pasted where id = ?', [paste_id],one=True)
	File: pasted-flask/pasted.py
	 > Line 207: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 209: ret_MAYBE_FUNCTION_NAME = render_template('form.html',original=paste)
	File: pasted-flask/pasted.py
	 > Line 213: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
	File: pasted-flask/pasted.py
	 > Line 217: ret_MAYBE_FUNCTION_NAME = redirect(url_for('index'))
File: pasted-flask/pasted.py
 > reaches line 229, trigger word "execute(": 
	cur = g.db.execute('insert into pasted (code, md5, viewed_at, parent) values (?, ?, ?, ?)', [request.form['code'], hexdigest, viewed_at, request.form['parent']])



Cornu/Brain
https://github.com/Cornu/Brain
Entry file: Brain/brain/__init__.py
Scanned: 2016-10-18 08:12:30.023063
Vulnerability 1:
File: Brain/brain/controllers/text.py
 > User input at line 43, trigger word "get(": 
	key = request.form.get('search')
File: Brain/brain/controllers/text.py
 > reaches line 44, trigger word "redirect(": 
	ret_MAYBE_FUNCTION_NAME = redirect('/' + key)



jbochi/scrum-you
https://github.com/jbochi/scrum-you
Entry file: scrum-you/application.py
Scanned: 2016-10-18 08:12:30.555396
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

miracle2k/flask-assets
https://github.com/miracle2k/flask-assets
Entry file: flask-assets/tests/test_config.py
Scanned: 2016-10-18 08:12:33.235919
No vulnerabilities found.


jgumbley/flask-payment
https://github.com/jgumbley/flask-payment
Entry file: flask-payment/tests.py
Scanned: 2016-10-18 08:12:34.691829
No vulnerabilities found.


eugenkiss/Simblin
https://github.com/eugenkiss/Simblin
Entry file: Simblin/simblin/__init__.py
Scanned: 2016-10-18 08:12:35.208274
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

jugyo/flask-gae-template
https://github.com/jugyo/flask-gae-template
Entry file: flask-gae-template/app.py
Scanned: 2016-10-18 08:12:37.008561
No vulnerabilities found.


swanson/flask-embedly
https://github.com/swanson/flask-embedly
Entry file: flask-embedly/example/app.py
Scanned: 2016-10-18 08:12:38.326310
No vulnerabilities found.


LightStyle/Python-Board
https://github.com/LightStyle/Python-Board
Entry file: Python-Board/src/index.py
Scanned: 2016-10-18 08:12:39.568423
No vulnerabilities found.


miku/flask-gae-stub
https://github.com/miku/flask-gae-stub
Entry file: flask-gae-stub/flask/app.py
Scanned: 2016-10-18 08:12:40.068455
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

derwiki/wordisms_flask
https://github.com/derwiki/wordisms_flask
Entry file: wordisms_flask/www/main.py
Scanned: 2016-10-18 08:12:40.570711
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

flebel/cisco79xx_phone_directory
https://github.com/flebel/cisco79xx_phone_directory
Entry file: cisco79xx_phone_directory/cisco79xx_phone_directory.py
Scanned: 2016-10-18 08:12:41.776165
No vulnerabilities found.


jkossen/imposter
https://github.com/jkossen/imposter
Entry file: None
Scanned: 2016-10-18 08:12:42.315914
No vulnerabilities found.
An Error occurred while scanning the repo: No entry path found in repo https://github.com/jkossen/imposter.

sublee/subleekr
https://github.com/sublee/subleekr
Entry file: subleekr/subleekr/app.py
Scanned: 2016-10-18 08:12:44.780121
No vulnerabilities found.


akhodakivskiy/flask
https://github.com/akhodakivskiy/flask
Entry file: flask/setup.py
Scanned: 2016-10-18 08:12:46.910307
No vulnerabilities found.
An Error occurred while scanning the repo: ('Unexpected node type:', <class '_ast.Assert'>)

thadeusb/flask-cache
https://github.com/thadeusb/flask-cache
Entry file: flask-cache/examples/hello.py
Scanned: 2016-10-18 08:12:48.690731
No vulnerabilities found.


kamalgill/flask-appengine-template
https://github.com/kamalgill/flask-appengine-template
Entry file: flask-appengine-template/src/lib/flask/sessions.py
Scanned: 2016-10-18 08:12:51.676943
No vulnerabilities found.


sublee/flask-autoindex
https://github.com/sublee/flask-autoindex
Entry file: flask-autoindex/flask_autoindex/__init__.py
Scanned: 2016-10-18 08:12:54.177473
No vulnerabilities found.


ericmoritz/flaskcma
https://github.com/ericmoritz/flaskcma
Entry file: flaskcma/flaskcma/app.py
Scanned: 2016-10-18 08:13:23.567117
No vulnerabilities found.


indexofire/flasky
https://github.com/indexofire/flasky
Entry file: flasky/flasky/flask/app.py
Scanned: 2016-10-18 08:13:24.079266
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

ericmoritz/flask-auth
https://github.com/ericmoritz/flask-auth
Entry file: flask-auth/flaskext/auth/tests/workflow.py
Scanned: 2016-10-18 08:13:25.417470
No vulnerabilities found.


sublee/flask-silk
https://github.com/sublee/flask-silk
Entry file: flask-silk/test.py
Scanned: 2016-10-18 08:13:27.829119
No vulnerabilities found.


proudlygeek/proudlygeek-blog
https://github.com/proudlygeek/proudlygeek-blog
Entry file: proudlygeek-blog/flask/app.py
Scanned: 2016-10-18 08:13:28.363532
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

JunKikuchi/flask-gae
https://github.com/JunKikuchi/flask-gae
Entry file: flask-gae/lib/flask/app.py
Scanned: 2016-10-18 08:13:28.864068
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

glenbot/flask-tweetfeed
https://github.com/glenbot/flask-tweetfeed
Entry file: flask-tweetfeed/tweetfeedapp.py
Scanned: 2016-10-18 08:13:30.172271
No vulnerabilities found.


fsouza/palestra-flask-2010-giran
https://github.com/fsouza/palestra-flask-2010-giran
Entry file: palestra-flask-2010-giran/projetos/projetos.py
Scanned: 2016-10-18 08:13:32.381019
No vulnerabilities found.


shiloa/flask-clean
https://github.com/shiloa/flask-clean
Entry file: flask-clean/app.py
Scanned: 2016-10-18 08:13:34.162825
No vulnerabilities found.


dag/flask-genshi
https://github.com/dag/flask-genshi
Entry file: flask-genshi/examples/flaskr/flaskr.py
Scanned: 2016-10-18 08:13:36.849191
No vulnerabilities found.


raliste/Flaskito
https://github.com/raliste/Flaskito
Entry file: Flaskito/flaskito/__init__.py
Scanned: 2016-10-18 08:13:38.636915
No vulnerabilities found.


mikewest/flask-pyplaceholder
https://github.com/mikewest/flask-pyplaceholder
Entry file: flask-pyplaceholder/generator.py
Scanned: 2016-10-18 08:13:40.938118
No vulnerabilities found.


whalesalad/arbesko-files
https://github.com/whalesalad/arbesko-files
Entry file: arbesko-files/files/__init__.py
Scanned: 2016-10-18 08:13:42.549817
No vulnerabilities found.


danjac/Flask-Script
https://github.com/danjac/Flask-Script
Entry file: Flask-Script/tests.py
Scanned: 2016-10-18 08:13:43.603072
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

danjac/Flask-WTF
https://github.com/danjac/Flask-WTF
Entry file: Flask-WTF/examples/recaptcha/app.py
Scanned: 2016-10-18 08:13:46.041250
No vulnerabilities found.


danjac/Flask-Mail
https://github.com/danjac/Flask-Mail
Entry file: Flask-Mail/tests.py
Scanned: 2016-10-18 08:13:47.034308
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

cropd/crashkurs-flask
https://github.com/cropd/crashkurs-flask
Entry file: crashkurs-flask/flask/app.py
Scanned: 2016-10-18 08:13:48.014451
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

hasgeek/github-hook
https://github.com/hasgeek/github-hook
Entry file: github-hook/github-hook.py
Scanned: 2016-10-18 08:13:49.208534
No vulnerabilities found.


pygloo/bewype-flask-controllers
https://github.com/pygloo/bewype-flask-controllers
Entry file: bewype-flask-controllers/bewype/flask/_app.py
Scanned: 2016-10-18 08:13:50.540502
No vulnerabilities found.


sontek-archive/redditor-stats
https://github.com/sontek-archive/redditor-stats
Entry file: redditor-stats/web.py
Scanned: 2016-10-18 08:13:53.887725
No vulnerabilities found.


Frozen-Flask/Frozen-Flask
https://github.com/Frozen-Flask/Frozen-Flask
Entry file: Frozen-Flask/flask_frozen/__init__.py
Scanned: 2016-10-18 08:14:23.122241
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

cobrateam/flask-mongoalchemy
https://github.com/cobrateam/flask-mongoalchemy
Entry file: flask-mongoalchemy/flask_mongoalchemy/__init__.py
Scanned: 2016-10-18 08:14:25.705746
No vulnerabilities found.


Flask-FlatPages/Flask-FlatPages
https://github.com/Flask-FlatPages/Flask-FlatPages
Entry file: Flask-FlatPages/tests/test_flask_flatpages.py
Scanned: 2016-10-18 08:14:26.232298
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

fsouza/flask-rest-example
https://github.com/fsouza/flask-rest-example
Entry file: flask-rest-example/library.py
Scanned: 2016-10-18 08:14:27.444377
Vulnerability 1:
File: flask-rest-example/library.py
 > User input at line 63, trigger word "form[": 
	name = request.form['name']
Reassigned in: 
	File: flask-rest-example/library.py
	 > Line 64: book = Book(id=2, name=name)
File: flask-rest-example/library.py
 > reaches line 65, trigger word "flash(": 
	flash('Book %s sucessful saved!' % book.name)



pilt/flask-versioned
https://github.com/pilt/flask-versioned
Entry file: flask-versioned/test_versioned.py
Scanned: 2016-10-18 08:14:28.776840
No vulnerabilities found.


tokibito/flask-hgwebcommit
https://github.com/tokibito/flask-hgwebcommit
Entry file: flask-hgwebcommit/hgwebcommit/__init__.py
Scanned: 2016-10-18 08:14:31.747795
Vulnerability 1:
File: flask-hgwebcommit/hgwebcommit/views.py
 > User input at line 97, trigger word ".data": 
	message = operation_repo(repo, form.data['operation'], form.data['files'], form.data['commit_message'])
File: flask-hgwebcommit/hgwebcommit/views.py
 > reaches line 98, trigger word "flash(": 
	flash(message)



Nassty/flask-gae
https://github.com/Nassty/flask-gae
Entry file: flask-gae/lib/flask/app.py
Scanned: 2016-10-18 08:14:32.252219
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sgk/BulkDM
https://github.com/sgk/BulkDM
Entry file: BulkDM/application.py
Scanned: 2016-10-18 08:14:33.773355
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

sontek-archive/redditor-stats
https://github.com/sontek-archive/redditor-stats
Entry file: redditor-stats/web.py
Scanned: 2016-10-18 08:14:36.564019
No vulnerabilities found.


zzzsochi/Flask-Gravatar
https://github.com/zzzsochi/Flask-Gravatar
Entry file: Flask-Gravatar/tests/test_core.py
Scanned: 2016-10-18 08:14:38.562460
No vulnerabilities found.


dag/flask-zodb
https://github.com/dag/flask-zodb
Entry file: flask-zodb/flask_zodb.py
Scanned: 2016-10-18 08:14:39.085435
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

zen4ever/route53manager
https://github.com/zen4ever/route53manager
Entry file: route53manager/route53/__init__.py
Scanned: 2016-10-18 08:14:39.589132
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-kitchensink
https://github.com/mitsuhiko/flask-kitchensink
Entry file: flask-kitchensink/example-code/hello.py
Scanned: 2016-10-18 08:14:40.094300
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

eyeseast/flask-docviewer
https://github.com/eyeseast/flask-docviewer
Entry file: flask-docviewer/docviewer/app.py
Scanned: 2016-10-18 08:14:41.325448
No vulnerabilities found.


dag/flask-attest
https://github.com/dag/flask-attest
Entry file: flask-attest/tests.py
Scanned: 2016-10-18 08:14:41.865295
No vulnerabilities found.
An Error occurred while scanning the repo: 'Node' object has no attribute 'first_statement'

ekalinin/flask-noextref
https://github.com/ekalinin/flask-noextref
Entry file: flask-noextref/test_noextref.py
Scanned: 2016-10-18 08:14:44.192667
No vulnerabilities found.


teohm/flitter
https://github.com/teohm/flitter
Entry file: flitter/flitter/__init__.py
Scanned: 2016-10-18 08:14:47.783476
Vulnerability 1:
File: flitter/flitter/controllers/user.py
 > User input at line 19, trigger word "form[": 
	username = request.form['username']
Reassigned in: 
	File: flitter/flitter/controllers/user.py
	 > Line 24: session['user'] = username
	File: flitter/flitter/controllers/user.py
	 > Line 26: ret_MAYBE_FUNCTION_NAME = redirect(url_for('entry.entries',username=username))
	File: flitter/flitter/controllers/user.py
	 > Line 30: ret_MAYBE_FUNCTION_NAME = render_template('signup.html',error=error)
	File: flitter/flitter/controllers/user.py
	 > Line 15: ret_MAYBE_FUNCTION_NAME = redirect_to_user_page()
File: flitter/flitter/controllers/user.py
 > reaches line 25, trigger word "flash(": 
	flash('Welcome, {0}.'.format(username))



aaront/calcmymarks2
https://github.com/aaront/calcmymarks2
Entry file: calcmymarks2/main.py
Scanned: 2016-10-18 08:14:48.304704
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

mitsuhiko/flask-feedback
https://github.com/mitsuhiko/flask-feedback
Entry file: flask-feedback/feedback.py
Scanned: 2016-10-18 08:14:49.383943
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

wilsaj/flask-admin-old
https://github.com/wilsaj/flask-admin-old
Entry file: flask-admin-old/test_admin.py
Scanned: 2016-10-18 08:14:58.221312
No vulnerabilities found.


leandrosilva/flaskito
https://github.com/leandrosilva/flaskito
Entry file: flaskito/src/flaskito.py
Scanned: 2016-10-18 08:14:58.774707
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

marchon/Flask-API-Server
https://github.com/marchon/Flask-API-Server
Entry file: Flask-API-Server/apiserver/tests/app.py
Scanned: 2016-10-18 08:15:00.118659
No vulnerabilities found.


kapilreddy/Shabda-Sangraha
https://github.com/kapilreddy/Shabda-Sangraha
Entry file: Shabda-Sangraha/dict.py
Scanned: 2016-10-18 08:15:23.150239
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

tooxie/flask-syrinx
https://github.com/tooxie/flask-syrinx
Entry file: flask-syrinx/syrinx/__init__.py
Scanned: 2016-10-18 08:15:24.667221
No vulnerabilities found.
An Error occurred while scanning the repo: The ast module can not parse the file and the python 2 to 3 conversion also failed.

joshourisman/flask-shortly
https://github.com/joshourisman/flask-shortly
Entry file: flask-shortly/shortly/__init__.py
Scanned: 2016-10-18 08:15:28.505207
No vulnerabilities found.


