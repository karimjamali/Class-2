#!/usr/bin/env python
from snmp_helper import snmp_get_oid,snmp_extract

COMMUNITY_STRING='galileo'
SNMP_PORT=[7961,8061]
IP_ADDR='50.76.53.27'
OIDs=['1.3.6.1.2.1.1.5.0','1.3.6.1.2.1.1.1.0']


for RTR in SNMP_PORT:
 for oid in OIDs:
  a_device = (IP_ADDR,COMMUNITY_STRING,RTR)
  snmp_data=snmp_get_oid(a_device,oid)
  output=snmp_extract(snmp_data)
  print output + '\n'
 print '\n\n\n'

