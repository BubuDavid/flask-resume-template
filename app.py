# -*- coding: utf-8 -*-
import oyaml as yaml
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    website_data = yaml.load(open('_config.yaml', encoding='UTF-8'))

    print(website_data['profile'])
    return render_template('index.html', data=website_data, allow_unicode=True)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
