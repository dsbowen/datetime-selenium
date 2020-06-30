<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

<link rel="stylesheet" href="https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css" type="text/css" />

<style>
    a.src-href {
        float: right;
    }
    p.attr {
        margin-top: 0.5em;
        margin-left: 1em;
    }
    p.func-header {
        background-color: gainsboro;
        border-radius: 0.1em;
        padding: 0.5em;
        padding-left: 1em;
    }
    table.field-table {
        border-radius: 0.1em
    }
</style># API

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##selenium_tools.**drag_range**

<p class="func-header">
    <i>def</i> selenium_tools.<b>drag_range</b>(<i>driver, range_, target, horizontal=True, tol=0, max_iter=10</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/selenium-tools/blob/master/selenium_tools/__init__.py#L8">[source]</a>
</p>

Drag a range slider to a desired target value.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>driver : <i>selenium.webdriver.chrome.webdriver.WebDriver or other webdriver</i></b>
<p class="attr">
    Webdriver in which the form is open.
</p>
<b>range_ : <i>selenium.webdriver.remote.webelement.WebElement</i></b>
<p class="attr">
    The range slider to be dragged.
</p>
<b>target : <i>float</i></b>
<p class="attr">
    Target value to which the sider should be dragged.
</p>
<b>horizontal : <i>bool, default=True</i></b>
<p class="attr">
    Indicates the slider is oriented horizontally, as opposed to vertically.
</p>
<b>tol : <i>float, default=0</i></b>
<p class="attr">
    Tolerance for error if the slider cannot be dragged to the exact target.
</p>
<b>max_iter : <i>int, default=10</i></b>
<p class="attr">
    Maximum number of iterations for the slider to reach the target.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>delta : <i>float</i></b>
<p class="attr">
    Remaining difference between the target and actual value.
</p></td>
</tr>
    </tbody>
</table>

####Examples

```python
from selenium_tools import drag_range

from selenium.webdriver import Chrome

driver = Chrome()
driver.get('data:text/html,<input type="range">')
range_ = driver.find_element_by_css_selector('input[type=range]')
drag_range(driver, range_, 80)
range_.get_property('value')
```

Out:

```
'80'
```

##selenium_tools.**send_datetime**

<p class="func-header">
    <i>def</i> selenium_tools.<b>send_datetime</b>(<i>input_, datetime_</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/selenium-tools/blob/master/selenium_tools/__init__.py#L74">[source]</a>
</p>

Send a datetime object to a form input.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>input_ : <i>selenium.webdriver.remote.webelement.WebElement</i></b>
<p class="attr">
    The form input to which the datetime object will be sent.
</p>
<b>datetime_ : <i>datetime.datetime</i></b>
<p class="attr">
    The datetime object to be sent.
</p></td>
</tr>
    </tbody>
</table>

####Examples

```python
from selenium_tools import send_datetime

from selenium.webdriver import Chrome

from datetime import datetime

driver = Chrome()
driver.get('data:text/html,<input type="date">')
input_ = driver.find_element_by_css_selector('input[type=date]')
send_datetime(input_, datetime.utcnow())
```

You should see the current date entered in the date input field in your
browser.

##selenium_tools.**get_datetime**

<p class="func-header">
    <i>def</i> selenium_tools.<b>get_datetime</b>(<i>input_type, response</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/selenium-tools/blob/master/selenium_tools/__init__.py#L133">[source]</a>
</p>

Get a datetime object from a form response after a POST request.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>input_type : <i>str</i></b>
<p class="attr">
    Type of the input tag.
</p>
<b>response : <i>str</i></b>
<p class="attr">
    Response to the input tag.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>datetime : <i>datetime.datetime</i></b>
<p class="attr">
    The response converted to a datetime object if possible, otherwise the raw response. This method will fail to convert the response if the input type is invalid or if the client did not enter a response in this input tag.
</p></td>
</tr>
    </tbody>
</table>

####Examples

```python
from selenium_tools import get_datetime, send_datetime

from selenium.webdriver import Chrome

from datetime import datetime

driver = Chrome()
driver.get('data:text/html,<input type="date">')
input_ = driver.find_element_by_css_selector('input[type=date]')
send_datetime(input_, datetime.utcnow())
get_datetime(input_.get_attribute('type'), input_.get_property('value'))
```

Out:

```
datetime.datetime(2020, 6, 30, 0, 0)
```