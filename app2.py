import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.varzesh3.com/")
    page.get_by_role("link", name="تارتار در اتوبان غافلگیر شد اختصاصی: سرقت بزرگ از سرمربی پرسپولیس! سرمربی تیم پر").first.click()
    page.goto("https://www.varzesh3.com/news/2434104/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%DB%8C-%D8%B3%D8%B1%D9%82%D8%AA-%D8%A8%D8%B2%D8%B1%DA%AF-%D8%A7%D8%B2-%D8%B3%D8%B1%D9%85%D8%B1%D8%A8%DB%8C-%D9%BE%D8%B1%D8%B3%D9%BE%D9%88%D9%84%DB%8C%D8%B3")
    page.goto("https://www.varzesh3.com/")
    page.get_by_role("link", name="صفحه‌اصلی").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="ویدیو", description="ویدیو").click()
    page1 = page1_info.value
    page1.get_by_role("link", name="گزارش تصویری").click()
    page1.close()
    page2 = context.new_page()
    page2.goto("https://www.varzesh3.com/album")
    page2.goto("https://www.varzesh3.com/album")
    page2.get_by_role("link", name="+19").click()
    page2.goto("https://www.varzesh3.com/album/12000/%D8%B4%D8%B1%D9%88%D8%B9-%D8%B7%D9%88%D9%81%D8%A7%D9%86%DB%8C-%D9%BE%D8%AF%DB%8C%D8%AF%D9%87-%D8%AF%D8%B1-%D8%B4%DB%8C%D8%B1%D8%A7%D8%B2")

    # ---------------------
    # context.close()
    # browser.close()

    page.pause()
    
with sync_playwright() as playwright:
    run(playwright)
