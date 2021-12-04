from jinja2 import Template
import yaml

# if

template = """hostname {{ hostname }}
ip routing

{% for intf, idata in interfaces.items() -%}
interface {{ intf }}
  ip address {{ idata.ip }}/{{ idata.mask }}
{%- endfor %}

{% if routing_protocol == 'bgp' -%}
router bgp {{ bgp.as }}
  router-id {{ interfaces.Loopback0.ip }}
  network {{ interfaces.Loopback0.ip }}/{{ interfaces.Loopback0.mask }}
{%- elif routing_protocol == 'ospf' -%}
router ospf {{ ospf.pid }}
  router-id {{ interfaces.Loopback0.ip }}
  network {{ interfaces.Loopback0.ip }}/{{ interfaces.Loopback0.mask }} area 0
{%- else -%}
  ip route 0.0.0.0/0 {{ default_nh }}
{%- endif %}"""

data_BGP = yaml.safe_load("""
hostname: router-w-bgp
routing_protocol: bgp

interfaces:
  Loopback0: 
    ip: 10.0.0.1
    mask: 32

bgp:
  as: 65001
""")

data_OSPF = yaml.safe_load("""
hostname: router-w-ospf
routing_protocol: ospf

interfaces:
  Loopback0:
    ip: 10.0.0.2
    mask: 32

ospf:
  pid: 1
""")

data_default = yaml.safe_load("""
hostname: router-w-ospf
routing_protocol: ospf

interfaces:
  Loopback0:
    ip: 10.0.0.2
    mask: 32

ospf:
  pid: 1
""")

j2_template = Template(template)

print(j2_template.render(data_BGP))
print(j2_template.render(data_OSPF))
print(j2_template.render(data_default))


# conditionals


template = """{% if x and y -%}
Both x and y are True. x: {{ x }}, y: {{ y }}
{%- endif %}

{% if x or z -%}
At least one of x and z is True. x: {{ x }}, z: {{ z }}
{%- endif %}

{% if not z -%}
We see that z is not True. z: {{ z }}
{%- endif %}"""

data = yaml.safe_load("""
x: true
y: true
z: false
""")


j2_template = Template(template)

print(j2_template.render(data))


# Truthiness

template = """{% macro bool_eval(value) -%}
{% if value -%}
True
{%- else -%}
False
{%- endif %}
{%- endmacro -%}

My one element list has bool value of: {{ bool_eval(my_list) }}
My one key dict has bool value of: {{ bool_eval(my_dict) }}
My short string has bool value of: {{ bool_eval(my_string) }}

My empty list has bool value of: {{ bool_eval(my_list_empty) }}
My empty dict has bool value of: {{ bool_eval(my_dict_empty) }}
My empty string has bool value of: {{ bool_eval(my_string_empty) }}"""

data = {
    "my_list": [
        "list-element"
    ],
    "my_dict": {
        "my_key": "my_value"
    },
    "my_string": "example string",
    "my_list_empty": [],
    "my_dict_empty": {},
    "my_string_empty": ""
}


j2_template = Template(template)

print(j2_template.render(data))


# Tests

template = """{{ hostname }} is an iterable: {{ hostname is iterable }}
{{ hostname }} is a sequence: {{ hostname is sequence }}
{{ hostname }} is a string: {{ hostname is string }}

{{ eos_ver }} is a number: {{ eos_ver is number }}
{{ eos_ver }} is an integer: {{ eos_ver is integer }}
{{ eos_ver }} is a float: {{ eos_ver is float }}

{{ bgp_as }} is a number: {{ bgp_as is number }}
{{ bgp_as }} is an integer: {{ bgp_as is integer }}
{{ bgp_as }} is a float: {{ bgp_as is float }}

{{ interfaces }} is an iterable: {{ interfaces is iterable }}
{{ interfaces }} is a sequence: {{ interfaces is sequence }}
{{ interfaces }} is a mapping: {{ interfaces is mapping }}

{{ dns_servers }} is an iterable: {{ dns_servers is iterable }}
{{ dns_servers }} is a sequence: {{ dns_servers is sequence }}
{{ dns_servers }} is a mapping: {{ dns_servers is mapping }}"""

data = {
    "hostname": "sw-office-lon-01",
    "eos_ver": 4.22,
    "bgp_as": 65001,
    "interfaces": {
        "Ethernet1": "Uplink to core"
    },
    "dns_servers": [
        "1.1.1.1",
        "8.8.4.4",
        "8.8.8.8"
    ]
}


j2_template = Template(template)

print(j2_template.render(data))


# In operator

template = """{% if 'Loopback0' in interfaces -%}
sflow source-interface Loopback0
snmp-server source-interface Loopback0
ip radius source-interface Loopback0
{%- else %}
sflow source-interface Management1
snmp-server source-interface Management1
ip radius source-interface Management1
{% endif %}"""

data = {
    "interfaces": {
        "Loopback0": {
            "description": "Management plane traffic",
            "ipv4_address": "10.255.255.34/32"
        },
        "Management1": {
            "description": "Management interface",
            "ipv4_address": "10.10.0.5/24"
        },
        "Ethernet1": {
            "description": "Span port - SPAN1"
        },
        "Ethernet2": {
            "description": "PortChannel50 - port 1"
        },
        "Ethernet51": {
            "description": "leaf01-eth51",
            "ipv4_address": "10.50.0.0/31"
        },
        "Ethernet52": {
            "description": "leaf02-eth51",
            "ipv4_address": "10.50.0.2/31"
        }
    }
}


j2_template = Template(template)

print(j2_template.render(data))