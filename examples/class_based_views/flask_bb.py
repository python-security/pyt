class Login(MethodView):
    decorators = [anonymous_required]

    def __init__(self, authentication_manager_factory):
        self.authentication_manager_factory = authentication_manager_factory

    def form(self):
        if enforce_recaptcha(limiter):
            return LoginRecaptchaForm()
        return LoginForm()

    def get(self):
        return render_template("auth/login.html", form=self.form())

    def post(self):
        foo = request.args.get('next')
        # return redirect(foo)
        return redirect(request.args.get('next'))
        # form = self.form()
        # if form.validate_on_submit():
        #     auth_manager = self.authentication_manager_factory()
        #     try:
        #         user = auth_manager.authenticate(
        #             identifier=form.login.data, secret=form.password.data
        #         )
        #         login_user(user, remember=form.remember_me.data)
        #         return redirect_or_next(url_for("forum.index"))
        #     except StopAuthentication as e:
        #         flash(e.reason, "danger")
        #     except Exception:
        #         flash(_("Unrecoverable error while handling login"))

        # return render_template("auth/login.html", form=form)


def redirect_or_next(endpoint, **kwargs):
    """Redirects the user back to the page they were viewing or to a specified
    endpoint. Wraps Flasks :func:`Flask.redirect` function.
    :param endpoint: The fallback endpoint.
    """
    return redirect(request.args.get('next'))
    # return redirect(
    #      request.args.get('next') or endpoint, **kwargs
    # )



