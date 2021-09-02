markdown.highlight
==================

Adds the possibility to use ```??? something ???``` or ```___ something ___``` to create a span that looks like <mark>something</mark>

Install through pip:

```$ pip install MarkdownHighlight```

To enable the MarkdownHighlight package and use it in your markdown generation just add it like so:

```
import markdown
from MarkdownHighlight.highlight import HighlightExtension

result = markdown.markdown(textToRender, output_format="html5", extensions=[HighlightExtension,]) )
```

## Changelog
 - 2021.9.1 - updated readme from .txt to .md
