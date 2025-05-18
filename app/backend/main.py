import flask
from flask import Flask,send_file,render_template
import os 

ROOT_DIR=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
APP_PATH=os.path.join(ROOT_DIR,'app/')

ui_path=os.path.join(APP_PATH,'frontend/')
model_path=os.path.join(ROOT_DIR,'models/')















app=Flask(__name__,static_folder=ui_path)

app.run()
