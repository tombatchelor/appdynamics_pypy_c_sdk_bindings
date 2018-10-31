#   THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
#   FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY APPDYNAMICS.

################################################################################
# 2018-10-131 - 1 - Tom Batchelor - Initial release, basic PyPy Bindings using CFFI
#
#
################################################################################

from _pi_cffi import ffi,lib
import time
import random
import requests

# This function connects the SDK to the AppD controller. App/tier/node name and the
# controller connection details need to be set here
def connect_to_appd():
    lib.appd_config_init()
    appdConf = lib.appd_config_init()
    lib.appd_config_set_app_name(appdConf,"")
    lib.appd_config_set_tier_name(appdConf,"")
    lib.appd_config_set_node_name(appdConf,"")
    lib.appd_config_set_controller_host(appdConf,"")
    lib.appd_config_set_controller_port(appdConf,8090)
    lib.appd_config_set_controller_account(appdConf,"")
    lib.appd_config_set_controller_use_ssl(appdConf,0)
    lib.appd_config_set_controller_access_key(appdConf,"")
    lib.appd_config_set_logging_log_dir(appdConf,"/tmp/appd/logs")
    lib.appd_config_set_logging_min_level(appdConf,lib.APPD_LOG_LEVEL_TRACE)
    appDConn = lib.appd_sdk_init(appdConf)

# This defines a downstream HTTP backend
def define_cars_backend():
    lib.appd_backend_declare("HTTP", "Cars")
    lib.appd_backend_set_identifying_property("Cars", "HOST", "192.168.56.1")
    lib.appd_backend_set_identifying_property("Cars", "PORT", "8080")
    lib.appd_backend_add("Cars")

# Script Start

connect_to_appd()
define_cars_backend()

# This endless loop starts a new BT, calls a downstream Java tier on HTTP and then ends
while True:
    btHandle = lib.appd_bt_begin("PyPyTest","")
    time.sleep(random.randint(1,4))
    exitHandle = lib.appd_exitcall_begin(btHandle, "Cars")
    lib.appd_exitcall_set_details(exitHandle, "/Cars_Sample_App/home.do")
    correlationHeader = lib.appd_exitcall_get_correlation_header(exitHandle)
    headers = {"singularityheader" : ffi.string(correlationHeader)}
    print(ffi.string(correlationHeader))
    requests.get('http://192.168.56.1:8080/Cars_Sample_App/home.do', headers=headers)
    lib.appd_exitcall_end(exitHandle)
    time.sleep(random.randint(1,2))
    lib.appd_bt_end(btHandle)

time.sleep(60)
lib.appd_sdk_term()
