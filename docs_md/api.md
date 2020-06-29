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



##datetime_selenium.**send_datetime**

<p class="func-header">
    <i>def</i> datetime_selenium.<b>send_datetime</b>(<i>input_, datetime_</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/datetime-selenium/blob/master/datetime_selenium/__init__.py#L7">[source]</a>
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



##datetime_selenium.**get_datetime**

<p class="func-header">
    <i>def</i> datetime_selenium.<b>get_datetime</b>(<i>input_type, response</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/datetime-selenium/blob/master/datetime_selenium/__init__.py#L48">[source]</a>
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

