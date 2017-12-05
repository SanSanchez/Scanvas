from canvasapi import Canvas
from canvasapi import user

"""
Access Token: Do Not Lose
10284~KYMyTLPkhLQt9vWzRpgh4copUye0XbBJTLUBcF5qbYGdqhkMTUcWE4WpqwquUh4V
"""

API_URL = "https://fsu.instructure.com/api/v1"

#TODO
API_KEY = "10284~KYMyTLPkhLQt9vWzRpgh4copUye0XbBJTLUBcF5qbYGdqhkMTUcWE4WpqwquUh4V"

canvas = Canvas(API_URL, API_KEY)

canvas.get_user()