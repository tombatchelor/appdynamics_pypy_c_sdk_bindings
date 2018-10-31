#Python/PyPy Bindings for the AppDynamics C SDK

AppDynamics provides a SDK to instrument C/C++ applications through code decoration. This Python script creates a module with bindings from Python into this SDK. The primary use case this address is insturmenting PyPy code.

##Prereqs

This uses [CFFI](https://cffi.readthedocs.io/en/latest/goals.html) to create the bindings. This can be installed using pip.

`pip install cffi`

This code has currently been tested using PyPy 5.0.1 (Python 2.7.10) on CentOS 7.

[AppDynamics C SDK](https://docs.appdynamics.com/pages/viewpage.action?pageId=45486535) 4.5.1 is also required on the Library Path.

##Module Creation

To create the module with the bindings, run the `appd_sdk.py` script e.g.

'pypy appd_sdk.py'

This will produce complied Python code and binary libary for the bindings.

##Usage

The 'example.py' script shows a basic usage of the module, to import into a Python script:

`from _appd_cffi import ffi,lib`

Then the C SDK functions are available, for example the following code sets up the SDK for usage:

```    appdConf = lib.appd_config_init()
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
```

The C example of this is covered in the [Initialize the Controller Configuration](https://docs.appdynamics.com/pages/viewpage.action?pageId=45486535#UsingtheC/C++AgentSDK-InitializetheControllerConfiguration) section of the AppDynamics C SDK documenation.

Usage follows the same patern as using the C SDK, with all functions avialble on the `lib` object.



