from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, UnexpectedAlertPresentException, NoSuchFrameException, NoAlertPresentException, ElementNotVisibleException, InvalidElementStateException
from selenium.webdriver.common.by import By
from urllib.parse import urlparse, urljoin
import json
import pprint
import datetime
import tldextract
import math
import os
import traceback
import random
import re
import logging
import copy
import time

import Classes

# Search for tags with contents equal to some text
def extract_ssitext(driver):
    elem = driver.find_elements(By.XPATH, "//*[contains(., 'VirtualBox')]")

    ssitexts = set()
    for el in elem:
        ssitexts.add(el)

    if ssitexts:
        ssitexts.add(driver.current_url)
    return ssitexts
