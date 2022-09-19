"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length
from flaskdb.widgets import ButtonField

class LoginForm(FlaskForm):
    username = StringField(
        "User Name",
        validators = [
            DataRequired(message="User Name is required."),
            length(max=64, message="User Name should be input within 64 characters."),
        ],
    )
    password = PasswordField(
        "Password",
        validators = [
            DataRequired(message="Password is required."),
        ],
    )


    cancel = ButtonField("Cancel")
    submit = SubmitField("Login")

    def copy_from(self, user):
        self.username.data = user.username
        self.password.data = user.password

    def copy_to(self, user):
        user.username = self.username.data
        user.password = self.password.data

class AddReviewForm(FlaskForm):
    companyname = StringField(
        "Company Name",
        validators = [
            DataRequired(message="Comapany Name is required."),
        ],
    )
    grade = IntegerField(
        "Grade (1~5)",
        validators = [
            DataRequired(message="Grade is required."),
        ],
    )
    cancel = ButtonField("Cancel")
    submit = SubmitField("Submit")

    def copy_from(self, item):
        self.companyname.data = item.companyname
        self.grade.data = item.grade

    def copy_to(self, item):
        item.itemname = self.companyname.data
        item.grade = self.grade.data

class SearchItemForm(FlaskForm):
    itemname = StringField(
        "Item Name",
        validators = [
            DataRequired(message="Item Name is required."),
        ],
    )
    cancel = ButtonField("Cancel")
    submit = SubmitField("Submit")

    def copy_from(self, item):
        self.itemname.data = item.itemname

    def copy_to(self, item):
        item.itemname = self.itemname.data

class CheckOutForm(FlaskForm):
    cancel = ButtonField("Cancel")
    submit = SubmitField("Checkout")
