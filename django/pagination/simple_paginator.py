{% load extra_tags %}

{% if is_paginated %}
  <hr/>
  <ul class="pagination">
    {% if page_obj.has_previous %}
      <li class="page-item">
        <a class="page-link" href="?{% url_replace request 'page' page_obj.previous_page_number %}">&laquo;</a>
      </li>
    {% endif %}

    {% for page_num in paginator.page_range %}
        <li class="page-item {% if page_obj.number == page_num %}active{% endif %}">
          <a class="page-link active" href="?{% url_replace request 'page' page_num %}">{{ page_num }}</a>
        </li>
    {% endfor %}

    {% if page_obj.has_next %}
      <li class="page-item">
        <a class="page-link" href="?{% url_replace request 'page' page_obj.next_page_number %}">&raquo;</a>
      </li>
    {% endif %}
  </ul>
{% endif %}

