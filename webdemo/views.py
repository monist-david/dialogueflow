import time

from django.shortcuts import render
from django.views.generic import TemplateView
from selenium import webdriver
import selenium


#
class HomeView(TemplateView):
    template_name = "webdemo/webdemo.html"

    def get(self, request):
        driver = webdriver.Chrome("C:/Users/david/Desktop/ChineseTutor/wordpress/dialogueflow/webdemo/chromedriver.exe")
        driver.get("https://console.dialogflow.com/api-client/demo/embedded/ad7e3869-10aa-43b1-b10e-d132a8bc7c75")
        while True:
            try:
                last_element = driver.find_elements_by_xpath("//i[@class='fa fa-volume-up']")[-1]
                last_element.click()
                while driver.find_elements_by_xpath("//i[@class='fa fa-volume-up']")[-1] == last_element:
                    continue
            except:
                pass

    def post(self, request):
        return render(request, "webdemo/webdemo.html")
