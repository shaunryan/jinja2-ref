# https://ttl255.com/jinja2-tutorial-part-1-introduction-and-variable-substitution/
from jinja2 import Template, StrictUndefined
from jinja2.exceptions import UndefinedError

template = """hostname {{ hostname }}

no ip domain lookup
ip domain name local.lab
ip name-server {{ name_server_pri }}
ip name-server {{ name_server_sec }}

ntp server {{ ntp_server_pri }} prefer
ntp server {{ ntp_server_sec }}"""


data = {
    "hostname": "core-sw-waw-01",
    "name_server_pri": "1.1.1.1",
    "name_server_sec": "8.8.8.8",
    "ntp_server_pri": "0.pool.ntp.org",
    "ntp_server_sec": "1.pool.ntp.org",
}

j2_template = Template(template)

print(j2_template.render(data))

# dictionaries as variables with dot

template = """interface {{ interface.name }}
 description {{ interface.description }}
 ip address {{ interface.ip_address }}
 speed {{ interface.speed }}
 duplex {{ interface.duplex }}
 mtu {{ interface.mtu }}"""


data = {
  "interface": {
    "name": "GigabitEthernet1/1",
    "ip_address": "10.0.0.1/31",
    "description": "Uplink to core",
    "speed": "1000",
    "duplex": "full",
    "mtu": "9124"
  }
}

j2_template = Template(template)

print(j2_template.render(data))

# dictionaries as variables with []

template = """Details for 10.0.0.0/24 prefix:
 Description: {{ prefixes['10.0.0.0/24'].description }}
 Region: {{ prefixes['10.0.0.0/24'].region }}
 Site: {{ prefixes['10.0.0.0/24'].site }}"""


data = {
  "prefixes": {
     "10.0.0.0/24": {
        "description":"Corporate NAS",
        "region": "Europe",
        "site": "Telehouse-West"
     }
  }
}

j2_template = Template(template)

print(j2_template.render(data))

# raising errors for missing variables


template = "Device {{ name }} is a {{ type }} located in the {{ site }} datacenter."

data = {
    "name": "waw-rtr-core-01",
    "site": "warsaw-01",
}

j2_template = Template(template)

print(j2_template.render(data))

try:
    template = "Device {{ name }} is a {{ type }} located in the {{ site }} datacenter."

    data = {
        "name": "waw-rtr-core-01",
        "site": "warsaw-01",
    }

    j2_template = Template(template, undefined=StrictUndefined)

    print(j2_template.render(data))
except UndefinedError as e:
    print(e)

# Using comments

template = """hostname {{ hostname }}

{# DNS configuration -#}
no ip domain lookup
ip domain name local.lab
ip name-server {{ name_server_pri }}
ip name-server {{ name_server_sec }}

{# Time servers config, we should use pool.ntp.org -#}
ntp server {{ ntp_server_pri }} prefer
ntp server {{ ntp_server_sec }}
ntp server {{ ntp_server_trd }}"""

data = {
    "hostname": "core-sw-waw-01",
    "name_server_pri": "1.1.1.1",
    "name_server_sec": "8.8.8.8",
    "ntp_server_pri": "0.pool.ntp.org",
    "ntp_server_sec": "1.pool.ntp.org",
}

j2_template = Template(template)

print(j2_template.render(data))
