from jinja2 import Template

# looping over a list
template = """# Configuring Prefix List
ip prefix-list PL_AS_65003_IN
{%- for line in PL_AS_65003_IN %}
 {{ line -}}
{% endfor %}"""

data = {
    "PL_AS_65003_IN": [
        "permit 10.96.0.0/24",
        "permit 10.97.11.0/24",
        "permit 10.99.15.0/24",
        "permit 10.100.5.0/25",
        "permit 10.100.6.128/25",
    ]
}

j2_template = Template(template)

print(j2_template.render(data))

# looping over a dictionary
template = """{% for intf in interfaces -%}
interface {{ intf }}
 description {{ interfaces[intf].description }}
 ip address {{ interfaces[intf].ipv4_address }}
{% endfor %}"""

data = {
    "interfaces": {
        "Ethernet1":
        {
            "description": "leaf01-eth51",
            "ipv4_address": "10.50.0.0/31"
        },
        "Ethernet2":
        {   
            "description": "leaf02-eth51",
            "ipv4_address": "10.50.0.2/31"
        }
    }
}

j2_template = Template(template)

print(j2_template.render(data))

# looping over a dictionary - key value
template = """{% for iname, idata in interfaces.items() -%}
interface {{ iname }}
 description {{ idata.description }}
 ip address {{ idata.ipv4_address }}
{% endfor %}"""

data = {
    "interfaces": {
        "Ethernet1":
        {
            "description": "leaf01-eth51",
            "ipv4_address": "10.50.0.0/31"
        },
        "Ethernet2":
        {   
            "description": "leaf02-eth51",
            "ipv4_address": "10.50.0.2/31"
        }
    }
}

j2_template = Template(template)

print(j2_template.render(data))

# Ordering dictionaries
# Ordering by key {% for k, v in my_dict | dictsort -%}
# Ordering by value {% for k, v in my_dict | dictsort(by='value')

# loop filtering

template = """{% 
    for iname, idata in interfaces.items() if idata.ipv4_address is defined
-%}
interface {{ iname }}
 description {{ idata.description }}
 ip address {{ idata.ipv4_address }}
{% endfor %}"""

data = {
    "interfaces": {
        "Ethernet1":
        {
            "description": "leaf01-eth51",
            "ipv4_address": "10.50.0.0/31"
        },
        "Ethernet2":
        {   
            "description": "leaf02-eth51",
            "ipv4_address": "10.50.0.2/31"
        },
        "Ethernet3":
        {   
            "description": "leaf02-eth51"
        }
    }
}

j2_template = Template(template)

print(j2_template.render(data))
