# -*- coding: utf-8 -*-
import os
from tmeizu_article import article_check
from flask import Flask, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class, TEXT
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOADED_MARKDOWNS_DEST'] = os.getcwd()

markdowns = UploadSet('markdowns', TEXT)
configure_uploads(app, markdowns)
patch_request_class(app)  # set maximum file size, default is 16MB
test2 = ["example1","example2"]
class UploadForm(FlaskForm):
    markdown = FileField(validators=[FileAllowed(markdowns, 'markdown only!'), FileRequired('File was empty!')])
    submit = SubmitField(u'分析')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    test1 = {}
    form = UploadForm()
    if form.validate_on_submit():
        filename = markdowns.save(form.markdown.data)
        test1 = article_check(filename)
        #test1 = ", ".join(test1)
        os.remove(filename)
        file_url = markdowns.url(filename)
    else:
        file_url = None
#    return render_template('index.html', form=form, file_url=file_url,test=test1)
    return render_template('index.html', form=form,my_dict=test1)

if __name__ == '__main__':
    app.run()
