from jinja2 import Template
import yaml

# In operator


template = """{% for acl, acl_lines in access_lists.items() %}
ip access-list extended {{ acl }}
  {% for line in acl_lines %}
    {% if line.action == "remark" %}
    remark {{ line.text }}
    {% elif line.action == "permit" %}
    permit {{ line.src }} {{ line.dst }}
    {% endif %}
  {% endfor %}
{% endfor %}

# All ACLs have been generated"""

data = yaml.safe_load("""
access_lists:
  al-hq-in:
    - action: remark
      text: Allow traffic from hq to local office
    - action: permit
      src: 10.0.0.0/22
      dst: 10.100.0.0/24
""")


j2_template = Template(template)

print(j2_template.render(data))

j2_template = Template(template, trim_blocks=True, lstrip_blocks=True)
print(j2_template.render(data))