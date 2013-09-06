Flask-AYAH
==========
    
Are You A Human (AYAH) integration on Flask

About
-----

Are you A Human (AYAH) is an alternative to CAPTCHA tests by providing a minigame to resolve instead of a word guessing test. This Flask extension tries to ease the implementation of this service by providing a helper to integrate the code on your forms and automatically processing the additional form data generated.

How to Use
----------
1. You must have an [Are you a Human account](http://portal.areyouahuman.com/signup/basic) to obtain the API keys needed to implement AYAH in your website.

2. Install Flask-AYAH using an package manager, like pip:

        pip install Flask-AYAH
        
    This will also install the Flask and are-you-a-human packages from PyPI if they are not installed.
    
3. Import the AreYouAHuman class from the `flask.ext.ayah` package:

        from flask.ext.ayah import AreYouAHuman

4. Add your AYAH API Keys to your app configuration parameters:

        app.config['AYAH_PUBLISHER'] = 'your publisher api key'
        app.config['AYAH_SCORING'] = 'your scoring api key'
        
5. Initialize an AreYouAHuman object, passing the Flask app object.
        
        ayah = AreYouAHuman(app)

6. On your templates, you can use the `ayah_get_publisher_html()` helper to integrate AYAH on your forms.
    
        <form>
            {{ ayah_get_publisher_html()}}
        </form>

7. To check if a test was passed, you must use the `score_result` method of the AreYouAHuman object.

        if ayah.score_result():
            process_the_form()

    Unlike the `score_result` function of the original are-you-a-human library, you don't need to pass the
    `session_secret` form parameter, this data is automatically passed when you call the `score_result` method.

Improving this extension
------------------------

This is my first Flask extension. So errors will probably appear.
To improve this extension, you can clone this repository, add your improvements and create a new pull request.

TO-DO
-----
(If you want something to be added or fixed, you can create a new issue).

* Making this an approved Flask extension.
