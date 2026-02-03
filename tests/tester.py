import pytest
from pages.sait import LoginPage

def test_successful_login(page):
    sait = LoginPage(page)
    sait.navigate()
    sait.login("standard_user", "secret_sauce")
    assert "inventory.html" in page.url

def test_wrong_password(page):
    sait = LoginPage(page)
    sait.navigate()
    sait.login("standard_user", "wrong_password")
    assert sait.error_message.is_visible()
    assert "Username and password do not match" in sait.error_message.text_content()

def test_locked_user(page):
    sait = LoginPage(page)
    sait.navigate()
    sait.login("locked_out_user", "secret_sauce")
    assert "Sorry, this user has been locked out" in sait.error_message.text_content()

def test_empty_fields(page):
    sait = LoginPage(page)
    sait.navigate()
    sait.login("", "")
    assert "Username is required" in sait.error_message.text_content()

def test_glitch_user(page):
    sait = LoginPage(page)
    sait.navigate()
    sait.login("performance_glitch_user", "secret_sauce")
    assert "inventory.html" in page.url