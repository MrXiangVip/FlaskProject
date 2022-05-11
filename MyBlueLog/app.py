import os

from flask import Flask

from bluelog import create_app




app = create_app('development')
if __name__ == '__main__':
    app.run()
