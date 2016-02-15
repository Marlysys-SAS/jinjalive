My variable: {{ foo_variable }}

My list:
{% for item in foolist_variable %}
    - {{ item }}
{% endfor %}

My dictionary:
{% for key, value in foodict_variable.iteritems()|sort %}
    - {{ key }}: {{ value }}
{% endfor %}

{% for item in unknown_variable %}
{{ item }}
{% endfor %}
