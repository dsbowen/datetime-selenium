from docstr_md.python import PySoup, compile_md
from docstr_md.src_href import Github

src_href = Github('https://github.com/dsbowen/datetime-selenium/blob/master')

path = 'datetime_selenium/__init__.py'
soup = PySoup(path=path, src_href=src_href)
compile_md(soup, outfile='docs_md/api.md')