
from jinja2 import Template

template = """
{% include 't.j2' ignore missing %}

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