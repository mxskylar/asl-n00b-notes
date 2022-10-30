---
cards-deck: {{ deck }}
tags: {% for tag in tags  %}{{ tag }}{%- if loop.first %}, {% endif %}{% endfor %}
---

#card/reverse
![[{{ gif }}]]
