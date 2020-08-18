#!/usr/bin/python

"""Returns triggersID and triggers description of the given host_name"""

from zabbix_methods import ZabbixConnection
from helper import load_config, config

class ZabbixConnectionTrigger(ZabbixConnection):
   
    def get_triggers_description(self, host_name, priority = 3):
        """Get dictionary of trigger ID and descriotion for triggers with priority >= 3"""

        results = self.session.do_request(
            "trigger.get", {
                "filter":
                {"host": [host_name]}
                ,"only_true": True
            })["result"]
        if results == []:
            return None

        trigger_dict = {}
        for item in results:
           # if int(item['priority']) >= priority and item['prop_name']) = priority  :
           if int(item['priority']) >= priority:
                trigger_dict[item['triggerid']] = item['comments']
        return trigger_dict


def get_triggers():
    """ Filtering trigger info to get desired output"""

    load_config()
    USER = config['general']['USER']
    PASSWORD = config['general']['PASSWORD']
    ZABBIX_SERVER = config['general']['ZABBIX_SERVER']

    with ZabbixConnectionTrigger(USER, "https://" + ZABBIX_SERVER , PASSWORD) as conn:
        conn.login(USER, "https://" + ZABBIX_SERVER , PASSWORD)
         
        host_name = 'openstack-monitoring'
        trigger_dict = conn.get_triggers_description(host_name)
        #print(trigger_dict)
        return trigger_dict

if __name__ == "__main__":
    get_triggers()
