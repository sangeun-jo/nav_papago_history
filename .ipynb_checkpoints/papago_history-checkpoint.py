{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "coordinated-timeline",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "negative-bishop",
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = webdriver.Chrome('D:\\chromedriver.exe')\n",
    "driver.get('https://papago.naver.com/')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "rental-notion",
   "metadata": {},
   "outputs": [
    {
     "ename": "ElementNotInteractableException",
     "evalue": "Message: element not interactable\n  (Session info: chrome=91.0.4472.114)\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mElementNotInteractableException\u001b[0m           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-21-bd60d5022107>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_element_by_xpath\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'/html/body/div/div/div[2]/button'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mhistory\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_element_by_class_name\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'history_box___2KIvN'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_all\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'div'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhistory\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webelement.py\u001b[0m in \u001b[0;36mclick\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     78\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mclick\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     79\u001b[0m         \u001b[1;34m\"\"\"Clicks the element.\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 80\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_execute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mCLICK_ELEMENT\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     81\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     82\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0msubmit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webelement.py\u001b[0m in \u001b[0;36m_execute\u001b[1;34m(self, command, params)\u001b[0m\n\u001b[0;32m    631\u001b[0m             \u001b[0mparams\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    632\u001b[0m         \u001b[0mparams\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'id'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_id\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 633\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcommand\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    634\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    635\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mfind_element\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mby\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mBy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mID\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    319\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    320\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 321\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    322\u001b[0m             response['value'] = self._unwrap_value(\n\u001b[0;32m    323\u001b[0m                 response.get('value', None))\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[1;34m(self, response)\u001b[0m\n\u001b[0;32m    240\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'alert'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'text'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    241\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 242\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    243\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    244\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_value_or_default\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdefault\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mElementNotInteractableException\u001b[0m: Message: element not interactable\n  (Session info: chrome=91.0.4472.114)\n"
     ]
    }
   ],
   "source": [
    "driver.find_element_by_xpath('/html/body/div/div/div[2]/button').click()\n",
    "history = driver.find_element_by_class_name('history_box___2KIvN').find_all('div')\n",
    "print(history)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "specified-specialist",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<selenium.webdriver.remote.webelement.WebElement (session=\"127fd67a7691f90b5ac6d39b83fb064c\", element=\"b734ca24-c16b-4d4a-a6d0-f94b8698aea1\")>\n"
     ]
    }
   ],
   "source": [
    "print(history)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "distant-relief",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
